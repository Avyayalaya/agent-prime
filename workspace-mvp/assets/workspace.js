/* ==========================================================================
   Agent Prime Workspace MVP
   Static, localStorage-backed product shell for guided onboarding and runs.
   ========================================================================== */

(function () {
  'use strict';

  var STORAGE_KEY = 'agent-prime-workspace-v1';
  var uiState = {
    editProfile: false,
    showRevisionForm: false,
    showRuleForm: false,
    message: null
  };
  var e2eDownloads = [];

  var WORKFLOWS = [
    {
      id: 'research-insight',
      name: 'Research → Insight',
      shortName: 'Insight memo',
      description: 'Turn a topic into a structured insight memo with signals, synthesis, implications, and next moves.',
      bestFor: 'Design leaders or strategists exploring an emerging theme or industry shift.',
      steps: ['Clarify the question', 'Scan signals', 'Synthesize the pattern', 'Draft the memo'],
      outputLabel: 'Insight memo'
    },
    {
      id: 'strategy-narrative',
      name: 'Strategy → Narrative',
      shortName: 'Narrative brief',
      description: 'Shape an initiative into a concise narrative with positioning, stakes, principles, and talking points.',
      bestFor: 'Leaders aligning a team, pitching a direction, or articulating a point of view.',
      steps: ['Frame the opportunity', 'Stress-test the angle', 'Build the message architecture', 'Draft the narrative'],
      outputLabel: 'Narrative brief'
    },
    {
      id: 'plan-build-spec',
      name: 'Plan → Build Spec',
      shortName: 'Build spec',
      description: 'Translate a project into phases, deliverables, risks, and a build-ready execution spec.',
      bestFor: 'Shipping a site, system, process, or internal product with less ambiguity.',
      steps: ['Excavate the real goal', 'Map phases and dependencies', 'Define quality bars', 'Write the build spec'],
      outputLabel: 'Build specification'
    }
  ];

  var state = loadState();
  reconcileRunningRuns();
  renderAll();
  bindEvents();
  runE2EIfRequested();

  function bindEvents() {
    document.addEventListener('click', handleClick);
    document.addEventListener('submit', handleSubmit);
    document.addEventListener('input', handleInput);
  }

  function runE2EIfRequested() {
    if (!shouldRunE2E()) return;

    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {}

    state = createDefaultState();
    renderAll();

    window.setTimeout(function () {
      runE2ESequence().catch(function (error) {
        writeE2EResult({
          pass: false,
          error: String(error && error.stack ? error.stack : error)
        });
      });
    }, 50);
  }

  async function runE2ESequence() {
    fillBoundInput('profile.name', 'Maya Chen');
    fillBoundInput('profile.role', 'Design leader exploring personal AI infrastructure');
    state.profile.currentStep = 1;
    renderOnboarding();

    fillBoundInput('profile.goal', 'Build a plug-and-play personal AI workspace for design leaders.');
    state.profile.currentStep = 2;
    renderOnboarding();

    fillBoundInput('profile.voice', 'Sharp, concise, editorial, and grounded.');
    state.profile.currentStep = 3;
    renderOnboarding();

    fillBoundInput('profile.constraints', 'Avoid generic jargon. Keep the next action obvious.');
    state.profile.onboardingComplete = true;
    state.profile.completedAt = nowIso();
    state.activeWorkflowId = recommendedWorkflowId();
    state.profile.currentStep = 3;
    ensureRunDraft();
    saveState();
    renderAll();

    state.activeWorkflowId = recommendedWorkflowId();
    state.runDraft = createRunDraft(state.activeWorkflowId);
    fillBoundInput('runDraft.title', 'Agent Prime workspace for design leaders');
    fillBoundInput('runDraft.context', 'We want a personal system that feels like a product, not a repo ritual. It should help a design leader go from scattered notes to a structured artifact fast.');
    fillBoundInput('runDraft.audience', 'A design leader evaluating whether to adopt the system personally');
    fillBoundInput('runDraft.successSignal', 'The output feels strong enough to share and specific enough to build from.');
    startRun();

    await waitForCondition(function () {
      var run = getOpenRun();
      return !!run && run.status === 'waiting_review';
    }, 6000);

    state.rules.unshift({
      id: makeId('rule'),
      type: 'voice',
      text: 'Keep the recommendation explicit in the first screenful.',
      active: true,
      createdAt: nowIso(),
      sourceArtifactId: getLatestArtifact() ? getLatestArtifact().id : '',
      sourceArtifactTitle: getLatestArtifact() ? getLatestArtifact().title : ''
    });
    saveState();
    renderAll();

    approveLatestArtifact();
    exportWorkspaceJson();
    exportLatestArtifactMarkdown();

    var latestRun = state.runs.slice().sort(function (a, b) {
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    })[0];
    var latestArtifact = state.artifacts.slice().sort(function (a, b) {
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    })[0];

    writeE2EResult({
      pass: !!(
        state.profile &&
        state.profile.onboardingComplete &&
        latestRun &&
        latestRun.status === 'done' &&
        latestArtifact &&
        latestArtifact.status === 'approved' &&
        state.rules.length >= 1 &&
        e2eDownloads.length >= 2
      ),
      checks: {
        onboardingComplete: !!(state.profile && state.profile.onboardingComplete),
        runCount: state.runs.length,
        latestRunStatus: latestRun ? latestRun.status : null,
        artifactCount: state.artifacts.length,
        latestArtifactStatus: latestArtifact ? latestArtifact.status : null,
        ruleCount: state.rules.length,
        downloadsTriggered: e2eDownloads.slice()
      }
    });
  }

  function handleInput(event) {
    var target = event.target;
    var path = target.getAttribute('data-bind');
    if (!path) return;

    setPathValue(state, path, target.value);
    saveState();
  }

  function handleClick(event) {
    var actionEl = event.target.closest('[data-action]');
    if (!actionEl) return;

    var action = actionEl.getAttribute('data-action');
    persistBoundInputs();

    if (action === 'onboarding-prev') {
      event.preventDefault();
      state.profile.currentStep = Math.max(0, state.profile.currentStep - 1);
      saveState();
      renderOnboarding();
      return;
    }

    if (action === 'onboarding-next') {
      event.preventDefault();
      if (!validateOnboardingStep(state.profile.currentStep)) return;
      state.profile.currentStep = Math.min(3, state.profile.currentStep + 1);
      saveState();
      renderOnboarding();
      renderDashboard();
      return;
    }

    if (action === 'onboarding-complete') {
      event.preventDefault();
      if (!validateOnboardingStep(state.profile.currentStep)) return;
      state.profile.onboardingComplete = true;
      state.profile.completedAt = nowIso();
      uiState.editProfile = false;
      state.activeWorkflowId = recommendedWorkflowId();
      ensureRunDraft();
      setMessage('Workspace ready. Pick a workflow and generate your first artifact.', 'success');
      saveState();
      renderAll();
      scrollToId('workflows');
      return;
    }

    if (action === 'edit-profile') {
      event.preventDefault();
      uiState.editProfile = true;
      renderOnboarding();
      scrollToId('onboarding');
      return;
    }

    if (action === 'use-recommended-workflow') {
      event.preventDefault();
      state.activeWorkflowId = recommendedWorkflowId();
      ensureRunDraft();
      saveState();
      renderWorkflows();
      renderStudio();
      scrollToId('studio');
      return;
    }

    if (action === 'start-workflow') {
      event.preventDefault();
      if (!state.profile.onboardingComplete) {
        setMessage('Finish onboarding first so the workspace has your context and style.', 'warning');
        renderDashboard();
        scrollToId('onboarding');
        return;
      }
      state.activeWorkflowId = actionEl.getAttribute('data-workflow-id');
      state.runDraft = createRunDraft(state.activeWorkflowId);
      saveState();
      renderWorkflows();
      renderStudio();
      scrollToId('studio');
      return;
    }

    if (action === 'approve-artifact') {
      event.preventDefault();
      approveLatestArtifact();
      return;
    }

    if (action === 'toggle-revision-form') {
      event.preventDefault();
      uiState.showRevisionForm = !uiState.showRevisionForm;
      uiState.showRuleForm = false;
      renderArtifacts();
      return;
    }

    if (action === 'toggle-rule-form') {
      event.preventDefault();
      uiState.showRuleForm = !uiState.showRuleForm;
      uiState.showRevisionForm = false;
      renderArtifacts();
      return;
    }

    if (action === 'remove-rule') {
      event.preventDefault();
      removeRule(actionEl.getAttribute('data-rule-id'));
      return;
    }

    if (action === 'export-json') {
      event.preventDefault();
      exportWorkspaceJson();
      return;
    }

    if (action === 'export-markdown') {
      event.preventDefault();
      exportLatestArtifactMarkdown();
      return;
    }

    if (action === 'reset-workspace') {
      event.preventDefault();
      resetWorkspace();
      return;
    }
  }

  function handleSubmit(event) {
    var form = event.target;

    if (form.id === 'runComposerForm') {
      event.preventDefault();
      persistBoundInputs(form);
      startRun();
      return;
    }

    if (form.id === 'revisionForm') {
      event.preventDefault();
      submitRevision(form);
      return;
    }

    if (form.id === 'ruleForm') {
      event.preventDefault();
      submitRule(form);
    }
  }

  function renderAll() {
    ensureRunDraft();
    renderDashboard();
    renderOnboarding();
    renderWorkflows();
    renderStudio();
    renderArtifacts();
    renderRules();
    renderSettings();
  }

  function renderDashboard() {
    var root = document.getElementById('workspaceDashboard');
    if (!root) return;

    var activeRun = getOpenRun();
    var latestArtifact = getLatestArtifact();
    var recommended = getWorkflow(recommendedWorkflowId());
    var ruleCount = getActiveRules().length;
    var artifactCount = state.artifacts.length;
    var completedRuns = state.runs.filter(function (run) {
      return run.status === 'done';
    }).length;

    root.innerHTML =
      '<div class="workspace-grid">' +
        '<div class="workspace-stack">' +
          renderMessage() +
          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Workspace profile</p>' +
                '<h3>' + escapeHtml(state.profile.name || 'Your personal Agent Prime workspace') + '</h3>' +
              '</div>' +
              renderStatusChip(state.profile.onboardingComplete ? 'ready' : 'needs-setup', state.profile.onboardingComplete ? 'Ready' : 'Needs setup') +
            '</div>' +
            '<p class="workspace-lead">' + escapeHtml(getProfileSummary()) + '</p>' +
            '<div class="workspace-metric-grid">' +
              renderMetricCard(state.profile.onboardingComplete ? 'Complete' : 'In progress', 'Onboarding') +
              renderMetricCard(String(completedRuns), 'Completed runs') +
              renderMetricCard(String(ruleCount), 'Saved rules') +
              renderMetricCard(String(artifactCount), 'Artifacts') +
            '</div>' +
          '</div>' +

          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Current momentum</p>' +
                '<h3>' + escapeHtml(activeRun ? activeRun.title : 'No workflow running') + '</h3>' +
              '</div>' +
              renderStatusChip(activeRun ? activeRun.status : 'idle', activeRun ? humanizeStatus(activeRun.status) : 'Idle') +
            '</div>' +
            '<div class="workspace-split">' +
              '<div>' +
                '<p class="workspace-meta-label">Recommended next move</p>' +
                '<p>' + escapeHtml(getNextMoveCopy(activeRun, latestArtifact, recommended)) + '</p>' +
              '</div>' +
              '<div>' +
                '<p class="workspace-meta-label">Latest artifact</p>' +
                '<p>' + escapeHtml(latestArtifact ? latestArtifact.title : 'Nothing generated yet') + '</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +

        '<aside class="workspace-sidebar-stack">' +
          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">Quick actions</p>' +
            '<div class="workspace-action-stack">' +
              '<button class="btn btn--primary workspace-button" type="button" data-action="use-recommended-workflow">Open recommended workflow</button>' +
              '<a class="btn btn--secondary workspace-button" href="#onboarding">Refine onboarding</a>' +
              '<button class="btn btn--secondary workspace-button" type="button" data-action="export-json">Export workspace</button>' +
            '</div>' +
          '</div>' +

          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">What this prototype proves</p>' +
            '<ul class="workspace-bullet-list">' +
              '<li>No files or prompt syntax in the core flow</li>' +
              '<li>Workflow state stays visible and reviewable</li>' +
              '<li>Feedback becomes reusable rules</li>' +
              '<li>Workspace state persists across sessions</li>' +
            '</ul>' +
          '</div>' +

          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">Recommended wedge</p>' +
            '<h4>' + escapeHtml(recommended.name) + '</h4>' +
            '<p>' + escapeHtml(recommended.bestFor) + '</p>' +
          '</div>' +
        '</aside>' +
      '</div>';
  }

  function renderOnboarding() {
    var root = document.getElementById('workspaceOnboarding');
    if (!root) return;

    var shouldShowForm = !state.profile.onboardingComplete || uiState.editProfile;
    var steps = ['Identity', 'Goal', 'Voice', 'Constraints'];

    if (!shouldShowForm) {
      root.innerHTML =
        '<div class="card workspace-panel">' +
          '<div class="workspace-panel__header">' +
            '<div>' +
              '<p class="workspace-eyebrow">Onboarding complete</p>' +
              '<h3>Profile captured</h3>' +
            '</div>' +
            renderStatusChip('ready', 'Complete') +
          '</div>' +
          '<div class="workspace-definition-grid">' +
            renderDefinition('Name', state.profile.name) +
            renderDefinition('Role', state.profile.role) +
            renderDefinition('Primary goal', state.profile.goal) +
            renderDefinition('Preferred voice', state.profile.voice) +
            renderDefinition('Constraints', state.profile.constraints) +
            renderDefinition('Recommended workflow', getWorkflow(recommendedWorkflowId()).name) +
          '</div>' +
          '<div class="workspace-action-row">' +
            '<button class="btn btn--secondary" type="button" data-action="edit-profile">Edit answers</button>' +
            '<a class="btn btn--primary" href="#workflows">Go to workflows</a>' +
          '</div>' +
        '</div>';
      return;
    }

    root.innerHTML =
      '<div class="card workspace-panel">' +
        '<div class="workspace-panel__header">' +
          '<div>' +
            '<p class="workspace-eyebrow">Onboarding wizard</p>' +
            '<h3>Make the workspace personal in four short steps</h3>' +
          '</div>' +
          renderStatusChip('progress', 'Step ' + String(state.profile.currentStep + 1) + ' of 4') +
        '</div>' +
        '<div class="workspace-stepper">' +
          steps.map(function (step, index) {
            var stepClass = 'workspace-step';
            if (index === state.profile.currentStep) stepClass += ' is-active';
            if (index < state.profile.currentStep) stepClass += ' is-complete';
            return '<div class="' + stepClass + '"><span>' + String(index + 1) + '</span><strong>' + step + '</strong></div>';
          }).join('') +
        '</div>' +

        '<form class="workspace-form-grid" id="onboardingForm">' +
          renderStepPanel(0,
            renderField('Your name', 'Tell the workspace who it is supporting.', '<input type="text" data-bind="profile.name" value="' + escapeAttribute(state.profile.name) + '" placeholder="e.g. Maya Chen" required>') +
            renderField('Role or lens', 'What kind of work do you do or own?', '<input type="text" data-bind="profile.role" value="' + escapeAttribute(state.profile.role) + '" placeholder="e.g. Design leader building a personal operating system" required>')
          ) +
          renderStepPanel(1,
            renderField('Primary goal', 'What should this workspace help you accomplish over the next few weeks?', '<textarea rows="4" data-bind="profile.goal" placeholder="e.g. Turn scattered product and design thinking into a repeatable strategic output system." required>' + escapeHtml(state.profile.goal) + '</textarea>')
          ) +
          renderStepPanel(2,
            renderField('Preferred voice and style', 'Describe how you want outputs to feel.', '<textarea rows="4" data-bind="profile.voice" placeholder="e.g. Sharp, concise, grounded, and slightly editorial. Fewer platitudes. Strong structure." required>' + escapeHtml(state.profile.voice) + '</textarea>')
          ) +
          renderStepPanel(3,
            renderField('Constraints or boundaries', 'What should the workspace avoid or respect?', '<textarea rows="4" data-bind="profile.constraints" placeholder="e.g. Keep outputs practical, avoid generic jargon, do not overclaim evidence." required>' + escapeHtml(state.profile.constraints) + '</textarea>') +
            '<div class="workspace-note">' +
              '<strong>Recommended workflow after setup:</strong> ' + escapeHtml(getWorkflow(recommendedWorkflowId()).name) +
            '</div>'
          ) +
        '</form>' +

        '<div class="workspace-action-row">' +
          '<button class="btn btn--secondary" type="button" data-action="onboarding-prev"' + (state.profile.currentStep === 0 ? ' disabled' : '') + '>Back</button>' +
          (state.profile.currentStep === 3
            ? '<button class="btn btn--primary" type="button" data-action="onboarding-complete">Complete onboarding</button>'
            : '<button class="btn btn--primary" type="button" data-action="onboarding-next">Next step</button>') +
        '</div>' +
      '</div>';
  }

  function renderWorkflows() {
    var root = document.getElementById('workspaceWorkflows');
    if (!root) return;

    var recommendedId = recommendedWorkflowId();

    root.innerHTML =
      '<div class="workspace-card-grid">' +
        WORKFLOWS.map(function (workflow) {
          var isActive = workflow.id === state.activeWorkflowId;
          var isRecommended = workflow.id === recommendedId;
          return (
            '<div class="card workspace-panel workflow-card' + (isActive ? ' workflow-card--active' : '') + '">' +
              '<div class="workspace-panel__header">' +
                '<div>' +
                  '<p class="workspace-eyebrow">' + escapeHtml(workflow.shortName) + '</p>' +
                  '<h3>' + escapeHtml(workflow.name) + '</h3>' +
                '</div>' +
                '<div class="workspace-chip-row">' +
                  (isRecommended ? renderStatusChip('recommended', 'Recommended') : '') +
                  (isActive ? renderStatusChip('active', 'Selected') : '') +
                '</div>' +
              '</div>' +
              '<p class="workspace-lead">' + escapeHtml(workflow.description) + '</p>' +
              '<p class="workspace-meta-label">Best for</p>' +
              '<p>' + escapeHtml(workflow.bestFor) + '</p>' +
              '<ol class="workspace-numbered-list">' +
                workflow.steps.map(function (step) {
                  return '<li>' + escapeHtml(step) + '</li>';
                }).join('') +
              '</ol>' +
              '<div class="workspace-action-row">' +
                '<button class="btn btn--primary" type="button" data-action="start-workflow" data-workflow-id="' + workflow.id + '">Start this workflow</button>' +
              '</div>' +
            '</div>'
          );
        }).join('') +
      '</div>';
  }

  function renderStudio() {
    var root = document.getElementById('workspaceStudio');
    if (!root) return;

    var activeWorkflow = getWorkflow(state.activeWorkflowId || recommendedWorkflowId());
    var openRun = getOpenRun();

    if (!state.profile.onboardingComplete) {
      root.innerHTML =
        '<div class="card workspace-panel">' +
          '<div class="workspace-empty-state">' +
            '<h3>Onboarding comes first</h3>' +
            '<p>Agent Prime only becomes meaningfully personal once it knows who you are, what you want, and how you like outputs to sound.</p>' +
            '<a href="#onboarding" class="btn btn--primary">Go to onboarding</a>' +
          '</div>' +
        '</div>';
      return;
    }

    root.innerHTML =
      '<div class="workspace-grid">' +
        '<div class="workspace-stack">' +
          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Selected workflow</p>' +
                '<h3>' + escapeHtml(activeWorkflow.name) + '</h3>' +
              '</div>' +
              renderStatusChip(openRun ? openRun.status : 'ready', openRun ? humanizeStatus(openRun.status) : 'Ready to run') +
            '</div>' +
            '<p class="workspace-lead">' + escapeHtml(activeWorkflow.description) + '</p>' +
            '<p class="workspace-meta-label">Output</p>' +
            '<p>' + escapeHtml(activeWorkflow.outputLabel) + '</p>' +
          '</div>' +
          renderComposer(activeWorkflow, openRun) +
        '</div>' +
        '<aside class="workspace-sidebar-stack">' +
          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">Workflow steps</p>' +
            '<div class="workspace-timeline">' +
              activeWorkflow.steps.map(function (step, index) {
                var status = 'queued';
                if (openRun && openRun.steps[index]) {
                  status = openRun.steps[index].status;
                }
                return renderTimelineStep(step, status);
              }).join('') +
            '</div>' +
          '</div>' +
        '</aside>' +
      '</div>';
  }

  function renderArtifacts() {
    var root = document.getElementById('workspaceArtifacts');
    if (!root) return;

    var artifact = getLatestArtifact();
    if (!artifact) {
      root.innerHTML =
        '<div class="card workspace-panel">' +
          '<div class="workspace-empty-state">' +
            '<h3>No artifacts yet</h3>' +
            '<p>Complete onboarding and run one of the starter workflows to generate the first artifact.</p>' +
            '<a href="#workflows" class="btn btn--primary">Go to workflows</a>' +
          '</div>' +
        '</div>';
      return;
    }

    var versions = getArtifactsForRun(artifact.runId);
    root.innerHTML =
      '<div class="workspace-grid">' +
        '<div class="workspace-stack">' +
          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">' + escapeHtml(artifact.type) + '</p>' +
                '<h3>' + escapeHtml(artifact.title) + '</h3>' +
              '</div>' +
              renderStatusChip(artifact.status, humanizeArtifactStatus(artifact.status)) +
            '</div>' +
            '<div class="workspace-chip-row">' +
              renderInfoChip('Version ' + String(artifact.version)) +
              renderInfoChip(formatDate(artifact.createdAt)) +
              renderInfoChip(String(artifact.appliedRuleIds.length) + ' rules applied') +
            '</div>' +
            '<div class="workspace-artifact-render">' + artifact.html + '</div>' +
          '</div>' +

          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Review actions</p>' +
                '<h3>What should happen next?</h3>' +
              '</div>' +
            '</div>' +
            '<div class="workspace-action-row workspace-action-row--wrap">' +
              '<button class="btn btn--primary" type="button" data-action="approve-artifact"' + (artifact.status === 'approved' ? ' disabled' : '') + '>Approve</button>' +
              '<button class="btn btn--secondary" type="button" data-action="toggle-revision-form">Request revision</button>' +
              '<button class="btn btn--secondary" type="button" data-action="toggle-rule-form">Save as rule</button>' +
            '</div>' +
            (uiState.showRevisionForm ? renderRevisionForm() : '') +
            (uiState.showRuleForm ? renderRuleForm() : '') +
          '</div>' +
        '</div>' +
        '<aside class="workspace-sidebar-stack">' +
          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">Artifact history</p>' +
            '<div class="workspace-history-list">' +
              versions.map(function (version) {
                return (
                  '<div class="workspace-history-item">' +
                    '<strong>v' + String(version.version) + '</strong>' +
                    '<span>' + escapeHtml(humanizeArtifactStatus(version.status)) + '</span>' +
                    '<time>' + escapeHtml(formatDate(version.createdAt)) + '</time>' +
                  '</div>'
                );
              }).join('') +
            '</div>' +
          '</div>' +
        '</aside>' +
      '</div>';
  }

  function renderRules() {
    var root = document.getElementById('workspaceRules');
    if (!root) return;

    var rules = getActiveRules();
    if (!rules.length) {
      root.innerHTML =
        '<div class="card workspace-panel">' +
          '<div class="workspace-empty-state">' +
            '<h3>No saved rules yet</h3>' +
            '<p>When an artifact needs a repeatable preference, capture it as a rule instead of making the same edit next time.</p>' +
          '</div>' +
        '</div>';
      return;
    }

    root.innerHTML =
      '<div class="workspace-card-grid">' +
        rules.map(function (rule) {
          return (
            '<div class="card workspace-panel workspace-rule-card">' +
              '<div class="workspace-panel__header">' +
                '<div>' +
                  '<p class="workspace-eyebrow">Saved from ' + escapeHtml(rule.sourceArtifactTitle || 'artifact') + '</p>' +
                  '<h3>' + escapeHtml(humanizeRuleType(rule.type)) + ' rule</h3>' +
                '</div>' +
                renderStatusChip('active', 'Active') +
              '</div>' +
              '<p class="workspace-lead">' + escapeHtml(rule.text) + '</p>' +
              '<div class="workspace-action-row">' +
                '<button class="btn btn--secondary" type="button" data-action="remove-rule" data-rule-id="' + rule.id + '">Remove rule</button>' +
              '</div>' +
            '</div>'
          );
        }).join('') +
      '</div>';
  }

  function renderSettings() {
    var root = document.getElementById('workspaceSettings');
    if (!root) return;

    root.innerHTML =
      '<div class="workspace-grid">' +
        '<div class="workspace-stack">' +
          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Exportability</p>' +
                '<h3>Take the workspace with you</h3>' +
              '</div>' +
              renderStatusChip('portable', 'Portable') +
            '</div>' +
            '<p class="workspace-lead">Export profile data, saved rules, run metadata, and generated artifacts without exposing the underlying file-backed engine.</p>' +
            '<div class="workspace-action-row workspace-action-row--wrap">' +
              '<button class="btn btn--primary" type="button" data-action="export-json">Export workspace (.json)</button>' +
              '<button class="btn btn--secondary" type="button" data-action="export-markdown">Download latest artifact (.md)</button>' +
            '</div>' +
          '</div>' +

          '<div class="card workspace-panel">' +
            '<div class="workspace-panel__header">' +
              '<div>' +
                '<p class="workspace-eyebrow">Persistence model</p>' +
                '<h3>What this prototype is doing</h3>' +
              '</div>' +
            '</div>' +
            '<ul class="workspace-bullet-list">' +
              '<li>Workspace state is stored in browser localStorage.</li>' +
              '<li>Runs, artifacts, and rules persist across reloads on the same browser.</li>' +
              '<li>Reset clears everything and takes you back to a fresh workspace.</li>' +
            '</ul>' +
          '</div>' +
        '</div>' +

        '<aside class="workspace-sidebar-stack">' +
          '<div class="card workspace-panel">' +
            '<p class="workspace-eyebrow">Reset</p>' +
            '<h3>Start from a clean workspace</h3>' +
            '<p>This is useful for testing the first-run experience again.</p>' +
            '<div class="workspace-action-row">' +
              '<button class="btn btn--danger" type="button" data-action="reset-workspace">Reset workspace</button>' +
            '</div>' +
          '</div>' +
        '</aside>' +
      '</div>';
  }

  function renderComposer(workflow, openRun) {
    var runDraft = state.runDraft || createRunDraft(workflow.id);
    var disableComposer = openRun && openRun.status === 'running';
    var waitingReview = openRun && openRun.status === 'waiting_review';

    return (
      '<div class="card workspace-panel">' +
        '<div class="workspace-panel__header">' +
          '<div>' +
            '<p class="workspace-eyebrow">Run composer</p>' +
            '<h3>' + (disableComposer ? 'Workflow is currently running' : waitingReview ? 'Artifact waiting for review' : 'Describe what this run should produce') + '</h3>' +
          '</div>' +
        '</div>' +
        (disableComposer
          ? '<p class="workspace-lead">The workflow is stepping through the pipeline now. Watch the timeline update, then review the artifact once it lands.</p>'
          : waitingReview
            ? '<p class="workspace-lead">Review the latest artifact before starting another run. This keeps the loop human-in-the-middle.</p><a href="#artifacts" class="btn btn--primary">Go to artifact review</a>'
            : '<form id="runComposerForm" class="workspace-form-grid">' +
                renderField('Project or topic title', 'Name the thing you want this run to tackle.', '<input type="text" data-bind="runDraft.title" value="' + escapeAttribute(runDraft.title) + '" placeholder="e.g. Personal AI system for design leaders" required>') +
                renderField('Context', 'Give the workflow the background or problem framing.', '<textarea rows="4" data-bind="runDraft.context" placeholder="What is happening, what matters, or what is stuck?" required>' + escapeHtml(runDraft.context) + '</textarea>') +
                renderField('Audience or outcome', 'Who is this for, or what should it help you decide?', '<input type="text" data-bind="runDraft.audience" value="' + escapeAttribute(runDraft.audience) + '" placeholder="e.g. Myself, a design leader peer, my team, a board audience" required>') +
                renderField('Success signal', 'What would make this run feel genuinely useful?', '<input type="text" data-bind="runDraft.successSignal" value="' + escapeAttribute(runDraft.successSignal) + '" placeholder="e.g. I can share it immediately or build from it without more clarification." required>') +
                '<div class="workspace-action-row">' +
                  '<button class="btn btn--primary" type="submit">Run workflow</button>' +
                '</div>' +
              '</form>') +
      '</div>'
    );
  }

  function renderRevisionForm() {
    return (
      '<form id="revisionForm" class="workspace-inline-form">' +
        '<label for="revisionNote">Revision note</label>' +
        '<textarea id="revisionNote" name="revisionNote" rows="4" placeholder="Describe what should change next time." required></textarea>' +
        '<div class="workspace-action-row">' +
          '<button class="btn btn--primary" type="submit">Generate revision</button>' +
        '</div>' +
      '</form>'
    );
  }

  function renderRuleForm() {
    return (
      '<form id="ruleForm" class="workspace-inline-form">' +
        '<label for="ruleType">Rule type</label>' +
        '<select id="ruleType" name="ruleType">' +
          '<option value="voice">Voice</option>' +
          '<option value="process">Process</option>' +
          '<option value="content">Content</option>' +
        '</select>' +
        '<label for="ruleText">Rule text</label>' +
        '<textarea id="ruleText" name="ruleText" rows="4" placeholder="e.g. Keep headings short and make the recommendation explicit in the first screenful." required></textarea>' +
        '<div class="workspace-action-row">' +
          '<button class="btn btn--primary" type="submit">Save rule</button>' +
        '</div>' +
      '</form>'
    );
  }

  function renderStepPanel(index, innerHtml) {
    return '<div class="workspace-step-panel"' + (state.profile.currentStep !== index ? ' hidden' : '') + '>' + innerHtml + '</div>';
  }

  function renderField(label, helper, controlHtml) {
    return (
      '<div class="workspace-field">' +
        '<label><strong>' + escapeHtml(label) + '</strong></label>' +
        '<p class="workspace-field__helper">' + escapeHtml(helper) + '</p>' +
        controlHtml +
      '</div>'
    );
  }

  function renderMetricCard(value, label) {
    return (
      '<div class="workspace-metric-card">' +
        '<strong>' + escapeHtml(value) + '</strong>' +
        '<span>' + escapeHtml(label) + '</span>' +
      '</div>'
    );
  }

  function renderTimelineStep(label, status) {
    return (
      '<div class="workspace-timeline__step workspace-timeline__step--' + escapeAttribute(status) + '">' +
        '<span class="workspace-timeline__dot" aria-hidden="true"></span>' +
        '<div>' +
          '<strong>' + escapeHtml(label) + '</strong>' +
          '<p>' + escapeHtml(humanizeStatus(status)) + '</p>' +
        '</div>' +
      '</div>'
    );
  }

  function renderDefinition(label, value) {
    return (
      '<div class="workspace-definition">' +
        '<span>' + escapeHtml(label) + '</span>' +
        '<strong>' + escapeHtml(value || '—') + '</strong>' +
      '</div>'
    );
  }

  function renderMessage() {
    if (!uiState.message) return '';
    return '<div class="workspace-message workspace-message--' + escapeAttribute(uiState.message.tone) + '">' + escapeHtml(uiState.message.text) + '</div>';
  }

  function renderStatusChip(kind, label) {
    return '<span class="workspace-status workspace-status--' + escapeAttribute(kind) + '">' + escapeHtml(label) + '</span>';
  }

  function renderInfoChip(label) {
    return '<span class="workspace-info-chip">' + escapeHtml(label) + '</span>';
  }

  function startRun() {
    if (!state.profile.onboardingComplete) {
      setMessage('Finish onboarding before starting a workflow.', 'warning');
      renderDashboard();
      scrollToId('onboarding');
      return;
    }

    ensureRunDraft();
    if (!state.runDraft.title || !state.runDraft.context || !state.runDraft.audience || !state.runDraft.successSignal) {
      setMessage('Fill in all run details so the workflow has enough context to work with.', 'warning');
      renderDashboard();
      return;
    }

    var workflow = getWorkflow(state.runDraft.templateId || state.activeWorkflowId || recommendedWorkflowId());
    var run = {
      id: makeId('run'),
      templateId: workflow.id,
      title: state.runDraft.title,
      input: cloneObject(state.runDraft),
      status: 'running',
      createdAt: nowIso(),
      updatedAt: nowIso(),
      steps: workflow.steps.map(function (step) {
        return { label: step, status: 'queued' };
      })
    };

    state.runs.push(run);
    state.activeWorkflowId = workflow.id;
    state.runDraft = createRunDraft(workflow.id);
    saveState();
    renderDashboard();
    renderStudio();
    setMessage('Workflow started. The run will move through its steps and land in artifact review.', 'progress');
    renderDashboard();
    simulateRun(run.id);
  }

  function simulateRun(runId) {
    var run = findRun(runId);
    if (!run) return;

    advanceRunStep(run, 0);
  }

  function advanceRunStep(run, index) {
    if (index >= run.steps.length) {
      finalizeRun(run.id, null);
      return;
    }

    run.steps[index].status = 'running';
    run.updatedAt = nowIso();
    saveState();
    renderDashboard();
    renderStudio();

    window.setTimeout(function () {
      var freshRun = findRun(run.id);
      if (!freshRun) return;
      if (freshRun.steps[index]) {
        freshRun.steps[index].status = 'done';
      }
      freshRun.updatedAt = nowIso();
      saveState();
      renderDashboard();
      renderStudio();
      advanceRunStep(freshRun, index + 1);
    }, 600 + index * 200);
  }

  function finalizeRun(runId, revisionNote) {
    var run = findRun(runId);
    if (!run) return;

    var workflow = getWorkflow(run.templateId);
    run.status = 'waiting_review';
    run.updatedAt = nowIso();
    for (var i = 0; i < run.steps.length; i += 1) {
      run.steps[i].status = 'done';
    }

    var artifact = buildArtifact(workflow, run, revisionNote);
    state.artifacts.push(artifact);
    saveState();
    uiState.showRevisionForm = false;
    setMessage('Artifact ready. Review it, approve it, or turn feedback into a reusable rule.', 'success');
    renderAll();
    scrollToId('artifacts');
  }

  function buildArtifact(workflow, run, revisionNote) {
    var activeRules = getActiveRules();
    var version = getArtifactsForRun(run.id).length + 1;
    var generated = generateArtifactContent(workflow, run, activeRules, revisionNote);

    return {
      id: makeId('artifact'),
      runId: run.id,
      title: generated.title,
      type: workflow.outputLabel,
      status: 'needs_review',
      version: version,
      createdAt: nowIso(),
      markdown: generated.markdown,
      html: generated.html,
      appliedRuleIds: activeRules.map(function (rule) { return rule.id; })
    };
  }

  function generateArtifactContent(workflow, run, rules, revisionNote) {
    var profile = state.profile;
    var keywords = extractKeywords(run.input.context + ' ' + run.input.title + ' ' + run.input.audience);
    var topKeywords = keywords.slice(0, 4);
    var appliedRulesText = rules.length
      ? rules.map(function (rule) { return '- [' + humanizeRuleType(rule.type) + '] ' + rule.text; }).join('\n')
      : '- No saved rules yet.';

    if (workflow.id === 'research-insight') {
      return {
        title: run.title + ' — Insight memo',
        markdown:
          '# ' + run.title + ' — Insight memo\n\n' +
          'Prepared for: ' + profile.name + ' (' + profile.role + ')\n\n' +
          '## Framing\n' +
          shortLead(profile.voice, 'This memo turns a fuzzy topic into a sharper point of view.') + '\n\n' +
          'Context: ' + run.input.context + '\n\n' +
          '## Signals worth following\n' +
          topKeywords.map(function (keyword, index) {
            return (index + 1) + '. ' + capitalize(keyword) + ' is showing up as a meaningful thread inside the brief.';
          }).join('\n') + '\n\n' +
          '## Working insight\n' +
          'The opportunity is less about collecting more information and more about deciding what pattern deserves action now.\n\n' +
          '## Implications\n' +
          '- Shape the next conversation around a clear question.\n' +
          '- Turn the strongest pattern into one artifact you can share quickly.\n' +
          '- Treat ambiguity as something to structure, not something to wait out.\n\n' +
          '## Success signal\n' +
          run.input.successSignal + '\n\n' +
          '## Saved rules applied\n' +
          appliedRulesText + '\n' +
          (revisionNote ? '\n## Revision note\n' + revisionNote + '\n' : ''),
        html:
          '<article class="workspace-artifact">' +
            '<p class="workspace-artifact__kicker">Prepared for ' + escapeHtml(profile.name) + ' &middot; ' + escapeHtml(profile.role) + '</p>' +
            '<h3>' + escapeHtml(run.title + ' — Insight memo') + '</h3>' +
            '<p>' + escapeHtml(shortLead(profile.voice, 'This memo turns a fuzzy topic into a sharper point of view.')) + '</p>' +
            '<section><h4>Framing</h4><p>' + escapeHtml(run.input.context) + '</p></section>' +
            '<section><h4>Signals worth following</h4><ul>' +
              topKeywords.map(function (keyword) {
                return '<li>' + escapeHtml(capitalize(keyword) + ' is surfacing as a meaningful thread in the brief.') + '</li>';
              }).join('') +
            '</ul></section>' +
            '<section><h4>Working insight</h4><p>The leverage comes from deciding what pattern deserves action now, not from collecting endless extra context.</p></section>' +
            '<section><h4>Implications</h4><ul><li>Choose one sharp question to drive the next conversation.</li><li>Turn the strongest pattern into a shareable artifact.</li><li>Use structure to reduce ambiguity instead of postponing judgment.</li></ul></section>' +
            '<section><h4>Success signal</h4><p>' + escapeHtml(run.input.successSignal) + '</p></section>' +
            renderAppliedRulesHtml(rules) +
            (revisionNote ? '<section><h4>Revision note</h4><p>' + escapeHtml(revisionNote) + '</p></section>' : '') +
          '</article>'
      };
    }

    if (workflow.id === 'strategy-narrative') {
      return {
        title: run.title + ' — Narrative brief',
        markdown:
          '# ' + run.title + ' — Narrative brief\n\n' +
          'Prepared for: ' + profile.name + ' (' + profile.role + ')\n\n' +
          '## Strategic frame\n' +
          'This narrative is designed for ' + run.input.audience + '.\n\n' +
          '## Why now\n' +
          'The window matters because the team needs a coherent way to talk about the work before momentum fragments.\n\n' +
          '## Core positioning\n' +
          'Position this as a disciplined response to ' + (topKeywords[0] ? capitalize(topKeywords[0]) : 'a shifting context') + ', not as another generic initiative.\n\n' +
          '## Message architecture\n' +
          '- Problem: what is broken or under-structured.\n' +
          '- Bet: the specific move worth making now.\n' +
          '- Proof: the evidence or patterns that make the bet credible.\n' +
          '- Ask: the decision or alignment needed next.\n\n' +
          '## Talking points\n' +
          '- Make the stakes concrete.\n' +
          '- Make the choice legible.\n' +
          '- Make the next step easy to say yes to.\n\n' +
          '## Success signal\n' +
          run.input.successSignal + '\n\n' +
          '## Saved rules applied\n' +
          appliedRulesText + '\n' +
          (revisionNote ? '\n## Revision note\n' + revisionNote + '\n' : ''),
        html:
          '<article class="workspace-artifact">' +
            '<p class="workspace-artifact__kicker">Prepared for ' + escapeHtml(profile.name) + ' &middot; ' + escapeHtml(profile.role) + '</p>' +
            '<h3>' + escapeHtml(run.title + ' — Narrative brief') + '</h3>' +
            '<section><h4>Strategic frame</h4><p>This narrative is written for ' + escapeHtml(run.input.audience) + ' and shaped to make the bet legible quickly.</p></section>' +
            '<section><h4>Why now</h4><p>The moment matters because the team needs a coherent story before momentum fragments into isolated decisions.</p></section>' +
            '<section><h4>Core positioning</h4><p>Frame this as a disciplined response to ' + escapeHtml(topKeywords[0] ? capitalize(topKeywords[0]) : 'a shifting context') + ', not as another generic initiative.</p></section>' +
            '<section><h4>Message architecture</h4><ul><li><strong>Problem:</strong> what is broken or under-structured.</li><li><strong>Bet:</strong> the move worth making now.</li><li><strong>Proof:</strong> what makes the bet credible.</li><li><strong>Ask:</strong> the alignment or decision needed next.</li></ul></section>' +
            '<section><h4>Talking points</h4><ul><li>Make the stakes concrete.</li><li>Make the choice legible.</li><li>Make the next step easy to say yes to.</li></ul></section>' +
            '<section><h4>Success signal</h4><p>' + escapeHtml(run.input.successSignal) + '</p></section>' +
            renderAppliedRulesHtml(rules) +
            (revisionNote ? '<section><h4>Revision note</h4><p>' + escapeHtml(revisionNote) + '</p></section>' : '') +
          '</article>'
      };
    }

    return {
      title: run.title + ' — Build specification',
      markdown:
        '# ' + run.title + ' — Build specification\n\n' +
        'Prepared for: ' + profile.name + ' (' + profile.role + ')\n\n' +
        '## Outcome\n' +
        'Ship a version of this work that is clear enough to execute and small enough to finish.\n\n' +
        '## Input context\n' +
        run.input.context + '\n\n' +
        '## Phases\n' +
        '1. Clarify scope and success.\n' +
        '2. Build the thinnest slice that proves value.\n' +
        '3. Review, refine, and harden.\n\n' +
        '## Deliverables\n' +
        '- One clear artifact for the end user.\n' +
        '- A visible review loop.\n' +
        '- An exportable output.\n\n' +
        '## Risks\n' +
        '- The scope drifts into architecture theater.\n' +
        '- The build hides important decisions.\n' +
        '- The output is impressive but not usable.\n\n' +
        '## Acceptance checks\n' +
        '- A new user can understand the flow.\n' +
        '- The artifact can be reviewed without extra explanation.\n' +
        '- The next action is obvious.\n\n' +
        '## Success signal\n' +
        run.input.successSignal + '\n\n' +
        '## Saved rules applied\n' +
        appliedRulesText + '\n' +
        (revisionNote ? '\n## Revision note\n' + revisionNote + '\n' : ''),
      html:
        '<article class="workspace-artifact">' +
          '<p class="workspace-artifact__kicker">Prepared for ' + escapeHtml(profile.name) + ' &middot; ' + escapeHtml(profile.role) + '</p>' +
          '<h3>' + escapeHtml(run.title + ' — Build specification') + '</h3>' +
          '<section><h4>Outcome</h4><p>Ship a version of this work that is clear enough to execute and small enough to finish.</p></section>' +
          '<section><h4>Input context</h4><p>' + escapeHtml(run.input.context) + '</p></section>' +
          '<section><h4>Phases</h4><ol><li>Clarify scope and success.</li><li>Build the thinnest slice that proves value.</li><li>Review, refine, and harden.</li></ol></section>' +
          '<section><h4>Deliverables</h4><ul><li>One clear artifact for the end user.</li><li>A visible review loop.</li><li>An exportable output.</li></ul></section>' +
          '<section><h4>Risks</h4><ul><li>Scope drifts into architecture theater.</li><li>The build hides important decisions.</li><li>The output is impressive but not usable.</li></ul></section>' +
          '<section><h4>Acceptance checks</h4><ul><li>A new user can understand the flow.</li><li>The artifact can be reviewed without extra explanation.</li><li>The next action is obvious.</li></ul></section>' +
          '<section><h4>Success signal</h4><p>' + escapeHtml(run.input.successSignal) + '</p></section>' +
          renderAppliedRulesHtml(rules) +
          (revisionNote ? '<section><h4>Revision note</h4><p>' + escapeHtml(revisionNote) + '</p></section>' : '') +
        '</article>'
    };
  }

  function renderAppliedRulesHtml(rules) {
    return (
      '<section><h4>Saved rules applied</h4>' +
      (rules.length
        ? '<ul>' + rules.map(function (rule) {
            return '<li><strong>' + escapeHtml(humanizeRuleType(rule.type)) + ':</strong> ' + escapeHtml(rule.text) + '</li>';
          }).join('') + '</ul>'
        : '<p>No saved rules yet.</p>') +
      '</section>'
    );
  }

  function approveLatestArtifact() {
    var artifact = getLatestArtifact();
    if (!artifact) return;
    artifact.status = 'approved';

    var run = findRun(artifact.runId);
    if (run) {
      run.status = 'done';
      run.updatedAt = nowIso();
    }

    saveState();
    setMessage('Artifact approved. The workspace now treats this run as complete.', 'success');
    renderAll();
  }

  function submitRevision(form) {
    var artifact = getLatestArtifact();
    if (!artifact) return;

    var revisionNoteField = form.querySelector('#revisionNote');
    var revisionNote = revisionNoteField ? revisionNoteField.value.trim() : '';
    if (!revisionNote) {
      setMessage('Add a revision note so the next version knows what to change.', 'warning');
      renderDashboard();
      return;
    }

    artifact.status = 'superseded';
    finalizeRun(artifact.runId, revisionNote);
  }

  function submitRule(form) {
    var artifact = getLatestArtifact();
    if (!artifact) return;

    var typeField = form.querySelector('#ruleType');
    var textField = form.querySelector('#ruleText');
    var type = typeField ? typeField.value : 'voice';
    var text = textField ? textField.value.trim() : '';

    if (!text) {
      setMessage('Write the rule in plain language so it can apply on the next run.', 'warning');
      renderDashboard();
      return;
    }

    state.rules.unshift({
      id: makeId('rule'),
      type: type,
      text: text,
      active: true,
      createdAt: nowIso(),
      sourceArtifactId: artifact.id,
      sourceArtifactTitle: artifact.title
    });

    uiState.showRuleForm = false;
    saveState();
    setMessage('Rule saved. Future runs will carry this preference forward.', 'success');
    renderAll();
    scrollToId('rules');
  }

  function removeRule(ruleId) {
    state.rules = state.rules.filter(function (rule) {
      return rule.id !== ruleId;
    });
    saveState();
    setMessage('Rule removed from the active workspace memory.', 'success');
    renderAll();
  }

  function exportWorkspaceJson() {
    var payload = {
      exportedAt: nowIso(),
      workspace: {
        profile: state.profile,
        activeWorkflowId: state.activeWorkflowId,
        rules: state.rules,
        runs: state.runs,
        artifacts: state.artifacts
      }
    };

    downloadBlob('agent-prime-workspace.json', JSON.stringify(payload, null, 2), 'application/json');
    setMessage('Workspace exported as JSON.', 'success');
    renderDashboard();
  }

  function exportLatestArtifactMarkdown() {
    var artifact = getLatestArtifact();
    if (!artifact) {
      setMessage('Generate an artifact first, then export the markdown.', 'warning');
      renderDashboard();
      return;
    }

    var filename = slugify(artifact.title) + '.md';
    downloadBlob(filename, artifact.markdown, 'text/markdown');
    setMessage('Latest artifact downloaded as markdown.', 'success');
    renderDashboard();
  }

  function resetWorkspace() {
    var confirmed = window.confirm('Reset the workspace and clear all saved onboarding answers, runs, artifacts, and rules?');
    if (!confirmed) return;

    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {}

    state = createDefaultState();
    uiState.editProfile = false;
    uiState.showRevisionForm = false;
    uiState.showRuleForm = false;
    setMessage('Workspace reset. You are back at a clean first-run state.', 'success');
    renderAll();
    scrollToId('onboarding');
  }

  function validateOnboardingStep(step) {
    if (step === 0 && (!state.profile.name || !state.profile.role)) {
      setMessage('Add both your name and role to continue.', 'warning');
      renderDashboard();
      return false;
    }

    if (step === 1 && !state.profile.goal) {
      setMessage('Describe the goal this workspace should help with.', 'warning');
      renderDashboard();
      return false;
    }

    if (step === 2 && !state.profile.voice) {
      setMessage('Describe the tone or style you want the workspace to use.', 'warning');
      renderDashboard();
      return false;
    }

    if (step === 3 && !state.profile.constraints) {
      setMessage('Capture at least one boundary or constraint before finishing onboarding.', 'warning');
      renderDashboard();
      return false;
    }

    return true;
  }

  function reconcileRunningRuns() {
    var hadRunning = false;
    state.runs.forEach(function (run) {
      if (run.status === 'running') {
        hadRunning = true;
        for (var i = 0; i < run.steps.length; i += 1) {
          run.steps[i].status = 'done';
        }
        run.status = 'waiting_review';
        if (!getArtifactsForRun(run.id).length) {
          state.artifacts.push(buildArtifact(getWorkflow(run.templateId), run, null));
        }
      }
    });
    if (hadRunning) saveState();
  }

  function loadState() {
    var nextState = createDefaultState();
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return nextState;
      var parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== 'object') return nextState;

      nextState.profile = mergeObjects(nextState.profile, parsed.profile || {});
      nextState.runs = Array.isArray(parsed.runs) ? parsed.runs : [];
      nextState.artifacts = Array.isArray(parsed.artifacts) ? parsed.artifacts : [];
      nextState.rules = Array.isArray(parsed.rules) ? parsed.rules : [];
      nextState.activeWorkflowId = parsed.activeWorkflowId || nextState.activeWorkflowId;
      nextState.runDraft = mergeObjects(nextState.runDraft, parsed.runDraft || {});
      return nextState;
    } catch (error) {
      return nextState;
    }
  }

  function saveState() {
    state.updatedAt = nowIso();
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {}
  }

  function createDefaultState() {
    return {
      version: 1,
      updatedAt: nowIso(),
      profile: {
        onboardingComplete: false,
        currentStep: 0,
        name: '',
        role: '',
        goal: '',
        voice: '',
        constraints: ''
      },
      activeWorkflowId: 'research-insight',
      runDraft: createRunDraft('research-insight'),
      runs: [],
      artifacts: [],
      rules: []
    };
  }

  function createRunDraft(templateId) {
    return {
      templateId: templateId,
      title: '',
      context: '',
      audience: '',
      successSignal: ''
    };
  }

  function ensureRunDraft() {
    if (!state.runDraft) {
      state.runDraft = createRunDraft(state.activeWorkflowId || recommendedWorkflowId());
      return;
    }
    if (!state.runDraft.templateId) {
      state.runDraft.templateId = state.activeWorkflowId || recommendedWorkflowId();
    }
  }

  function recommendedWorkflowId() {
    var goal = (state.profile.goal || '').toLowerCase();
    if (goal.indexOf('build') > -1 || goal.indexOf('ship') > -1 || goal.indexOf('system') > -1 || goal.indexOf('site') > -1) {
      return 'plan-build-spec';
    }
    if (goal.indexOf('story') > -1 || goal.indexOf('narrative') > -1 || goal.indexOf('position') > -1 || goal.indexOf('align') > -1) {
      return 'strategy-narrative';
    }
    return 'research-insight';
  }

  function getWorkflow(id) {
    for (var i = 0; i < WORKFLOWS.length; i += 1) {
      if (WORKFLOWS[i].id === id) return WORKFLOWS[i];
    }
    return WORKFLOWS[0];
  }

  function getLatestArtifact() {
    if (!state.artifacts.length) return null;
    return state.artifacts.slice().sort(function (a, b) {
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    })[0];
  }

  function getArtifactsForRun(runId) {
    return state.artifacts.filter(function (artifact) {
      return artifact.runId === runId;
    }).sort(function (a, b) {
      return b.version - a.version;
    });
  }

  function getOpenRun() {
    var runs = state.runs.slice().sort(function (a, b) {
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    });
    for (var i = 0; i < runs.length; i += 1) {
      if (runs[i].status !== 'done' && runs[i].status !== 'failed') {
        return runs[i];
      }
    }
    return null;
  }

  function getActiveRules() {
    return state.rules.filter(function (rule) {
      return rule.active !== false;
    });
  }

  function getProfileSummary() {
    if (!state.profile.onboardingComplete) {
      return 'Capture identity, goals, style, and constraints once. The workspace uses that context on every future run.';
    }
    return state.profile.role + ' focused on ' + state.profile.goal;
  }

  function getNextMoveCopy(activeRun, latestArtifact, recommended) {
    if (!state.profile.onboardingComplete) {
      return 'Complete onboarding so the workspace knows your context before it generates anything.';
    }
    if (activeRun && activeRun.status === 'running') {
      return 'Let the current run finish, then review the artifact and decide whether the feedback should become a permanent rule.';
    }
    if (activeRun && activeRun.status === 'waiting_review') {
      return 'Review the latest artifact. Approve it if it is good enough, revise it if it needs work, or save the pattern as a reusable rule.';
    }
    if (latestArtifact) {
      return 'Start another run using ' + recommended.name + ' so the next artifact benefits from everything learned so far.';
    }
    return 'Launch ' + recommended.name + ' and get to a first useful artifact in one session.';
  }

  function humanizeStatus(status) {
    if (status === 'needs-setup') return 'Needs setup';
    if (status === 'waiting_review') return 'Waiting for review';
    if (status === 'running') return 'Running';
    if (status === 'done') return 'Done';
    if (status === 'progress') return 'In progress';
    if (status === 'recommended') return 'Recommended';
    if (status === 'active') return 'Active';
    if (status === 'portable') return 'Portable';
    if (status === 'ready') return 'Ready';
    if (status === 'idle') return 'Idle';
    return capitalize(status.replace(/_/g, ' '));
  }

  function humanizeArtifactStatus(status) {
    if (status === 'needs_review') return 'Needs review';
    if (status === 'approved') return 'Approved';
    if (status === 'superseded') return 'Superseded';
    return humanizeStatus(status);
  }

  function humanizeRuleType(type) {
    if (type === 'voice') return 'Voice';
    if (type === 'process') return 'Process';
    if (type === 'content') return 'Content';
    return capitalize(type);
  }

  function persistBoundInputs(scope) {
    var root = scope || document;
    var bound = root.querySelectorAll('[data-bind]');
    for (var i = 0; i < bound.length; i += 1) {
      setPathValue(state, bound[i].getAttribute('data-bind'), bound[i].value);
    }
    saveState();
  }

  function fillBoundInput(path, value) {
    setPathValue(state, path, value);
    saveState();
    renderAll();
  }

  function waitForCondition(check, timeoutMs) {
    return new Promise(function (resolve, reject) {
      var start = Date.now();
      (function poll() {
        if (check()) {
          resolve();
          return;
        }
        if (Date.now() - start > timeoutMs) {
          reject(new Error('Timed out waiting for condition'));
          return;
        }
        window.setTimeout(poll, 100);
      })();
    });
  }

  function shouldRunE2E() {
    try {
      return new URLSearchParams(window.location.search).get('e2e') === '1';
    } catch (error) {
      return false;
    }
  }

  function writeE2EResult(result) {
    var node = document.getElementById('workspace-e2e-result');
    if (!node) {
      node = document.createElement('pre');
      node.id = 'workspace-e2e-result';
      node.hidden = true;
      document.body.appendChild(node);
    }
    node.textContent = JSON.stringify(result, null, 2);
  }

  function findRun(runId) {
    for (var i = 0; i < state.runs.length; i += 1) {
      if (state.runs[i].id === runId) return state.runs[i];
    }
    return null;
  }

  function setMessage(text, tone) {
    uiState.message = {
      text: text,
      tone: tone || 'info'
    };
  }

  function extractKeywords(text) {
    var words = (text || '').toLowerCase().match(/[a-z][a-z\-]{3,}/g) || [];
    var stop = {
      this: true, that: true, with: true, from: true, into: true, have: true, your: true,
      there: true, their: true, about: true, where: true, which: true, using: true,
      should: true, would: true, could: true, after: true, before: true, while: true,
      wants: true, need: true, needs: true, work: true, works: true, through: true
    };
    var seen = {};
    var picked = [];
    for (var i = 0; i < words.length; i += 1) {
      var word = words[i];
      if (stop[word] || seen[word]) continue;
      seen[word] = true;
      picked.push(word);
      if (picked.length === 6) break;
    }
    if (!picked.length) return ['clarity', 'momentum', 'signal'];
    return picked;
  }

  function shortLead(voice, fallback) {
    if (!voice) return fallback;
    var style = voice.toLowerCase();
    if (style.indexOf('concise') > -1 || style.indexOf('short') > -1) {
      return 'Tight framing. Clear stakes. Actionable next step.';
    }
    if (style.indexOf('editorial') > -1) {
      return 'This is a crisp read on the moment, the tension, and the move worth making.';
    }
    return fallback;
  }

  function scrollToId(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function mergeObjects(base, extra) {
    var output = cloneObject(base);
    for (var key in extra) {
      if (Object.prototype.hasOwnProperty.call(extra, key)) {
        output[key] = extra[key];
      }
    }
    return output;
  }

  function cloneObject(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function setPathValue(target, path, value) {
    var parts = path.split('.');
    var node = target;
    for (var i = 0; i < parts.length - 1; i += 1) {
      var key = parts[i];
      if (!node[key] || typeof node[key] !== 'object') {
        node[key] = {};
      }
      node = node[key];
    }
    node[parts[parts.length - 1]] = value;
  }

  function makeId(prefix) {
    return prefix + '-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 7);
  }

  function nowIso() {
    return new Date().toISOString();
  }

  function formatDate(iso) {
    try {
      return new Date(iso).toLocaleString(undefined, {
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: '2-digit'
      });
    } catch (error) {
      return iso;
    }
  }

  function downloadBlob(filename, text, mimeType) {
    e2eDownloads.push(filename);
    var blob = new Blob([text], { type: mimeType });
    var url = URL.createObjectURL(blob);
    var link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  function slugify(text) {
    return (text || 'artifact')
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')
      .slice(0, 80) || 'artifact';
  }

  function capitalize(value) {
    if (!value) return '';
    return value.charAt(0).toUpperCase() + value.slice(1);
  }

  function escapeHtml(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function escapeAttribute(value) {
    return escapeHtml(value).replace(/`/g, '&#96;');
  }
})();
