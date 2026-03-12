# Projects Sync — Shared Tool

> **Purpose:** Keeps the `projects/` portfolio layer in sync with the engine (`agents/`, `shared/planner/`). Runs automatically at the end of every session where artifacts were created or modified.
>
> **Who runs this:** Any agent at session end, or the session-end protocol in `copilot-instructions.md`. This is a shared tool, not an agent — no cadence, no Clerk tracking.

---

## When to Run

| Trigger | Action |
|---------|--------|
| **New project created** (new thesis in `theses.json`, new plan in Planner, new idea promoted from backlog) | Create project folder + README using the template below |
| **Artifact produced** (Writer outputs a draft, Builder completes assets, Scout delivers signals) | Copy to the correct project's `build/`, `references/`, or `media/` folder |
| **State change** (project moves stages, gets published, gets killed) | Update project README metadata + master `projects/README.md` |
| **Session end** (any session where state changed) | Run the full sync checklist below |

---

## Project Folder Creation Protocol

When a new project is identified, create the folder immediately:

### Step 1: Assign Type + ID

| Type | Prefix | When to use |
|------|--------|-------------|
| Thesis | `THS` | Research → write → publish → distribute |
| Event | `EVT` | Sessions, talks, demos |
| Program | `PRG` | Multi-session programs |
| Strategy | `STR` | Career/brand strategic initiatives |
| System | `SYS` | Agent Prime internal improvements |
| Toolkit | `TLK` | Reusable methodologies |
| Exploration | `EXP` | Undefined — could become any type |
| Build | `BLD` | Product/code builds |

**Next available IDs:** Check `projects/README.md` for the latest numbers per type.

### Step 2: Create Folder Structure

```
projects/{TYPE}-{NNN}_{short_name}/
├── README.md          ← REQUIRED (use template below)
├── plan/              ← Strategy, roadmap, decisions
├── build/             ← Deliverables
│   ├── drafts/        ← WIP versions
│   └── final/         ← Published/shipped
├── references/        ← Research inputs, signals, sources
├── media/             ← Images, charts, videos
├── comms/             ← Briefs, emails, outreach
└── backlog/           ← Future ideas scoped to this project
```

Not every project needs every subfolder. Create what's relevant. README is always required.

### Step 3: README Template

```markdown
# {TYPE}-{NNN} — {Title}

> {One-line description}

| Field | Value |
|-------|-------|
| **Type** | {Thesis/Event/Program/Strategy/System/Toolkit/Exploration/Build} |
| **State** | {backlog/planning/building/published/complete/parked} |
| **Engine Source** | {path to engine files this project draws from} |

---

## Artifact Index

| Artifact | Path | Notes |
|----------|------|-------|
| {name} | `{path}` | {notes} |

## Next Actions
1. {next action}

---

*Created: {date}*
```

### Step 4: Update Master Index

Add a row to the appropriate type table in `projects/README.md` and update the counts.

---

## Session-End Sync Checklist

Run this at the end of every session where artifacts were created or state changed:

### 1. Scan for New Artifacts

Check these engine folders for files created/modified this session:

| Engine Folder | Maps To |
|---------------|---------|
| `agents/writer/drafts/` | `projects/THS-{NNN}.../build/drafts/` |
| `agents/synthesizer/theses/` | `projects/THS-{NNN}.../build/thesis/` |
| `agents/scout/signals/` | `projects/THS-{NNN}.../references/` |
| `agents/connector/audience_maps/` | `projects/THS-{NNN}.../references/` |
| `agents/experimenter/experiments/` | `projects/THS-{NNN}.../references/` |
| `shared/planner/plans/PLN-{NNN}_*` | `projects/{mapped project}/plan/` |
| `shared/planner/plans/PLN-{NNN}_assets/*` | `projects/{mapped project}/build/` |
| `shared/toolkits/*` | `projects/TLK-{NNN}.../build/` |

### 2. Copy New/Updated Artifacts

For each new or modified file found:
- Copy to the corresponding project folder
- If no project folder exists for this work, create one (Step 1-4 above)

### 3. Update Project READMEs

For each project that received new artifacts:
- Add the artifact to the Artifact Index table
- Update the State field if it changed
- Update the Next Actions section

### 4. Update Master Index

If any project state changed or a new project was created:
- Update `projects/README.md` state column
- Update counts table

### 5. Report

Output a brief sync summary:
```
📦 Projects Sync:
- {N} artifacts synced to {M} projects
- {K} new project(s) created: {list}
- {J} state changes: {list}
```

---

## Engine → Project ID Mapping

This table maps engine IDs to project IDs. Update when new projects are created.

| Engine ID | Project ID | Project Folder |
|-----------|-----------|----------------|
| *(Add mappings as projects are created)* | | |

---
