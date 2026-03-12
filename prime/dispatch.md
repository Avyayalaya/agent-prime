# Dispatch Queue

> Agent tasks queued for execution. Each entry has a priority, assigned agent, and status.

<!-- 
Format:
## Q-NNN: [Task Title]
- **Agent:** [agent name]
- **Priority:** P0 | P1 | P2
- **Status:** queued | in_progress | done | killed
- **Input:** [what the agent needs]
- **Output:** [what the agent produces]

Successor Rules:
| Completing Agent | Successor(s) |
|-----------------|---------------|
| Scout | Synthesizer (if signal is thesis-worthy) |
| Synthesizer | Writer (if thesis is mature) |
| Writer | Connector (if artifact is publishable) |
| Planner | Builder (when spec is complete) |
| Builder | Writer or Connector (when build is done) |
| Any agent | Clerk (if commitments were made) |
-->
