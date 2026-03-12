# Change Propagation Registry

> Maps which files depend on which. After modifying ANY source file, check this map and update all dependent files.

<!-- 
Format: Source → Dependent files
When you modify a Source file, update every Dependent listed.
Add new dependencies as the system grows.
-->

## Dependencies

| Source | Dependents | Notes |
|--------|-----------|-------|
| `shared/registry.json` | `prime/dashboard.md`, `projects/README.md` | Run `python meta/scripts/generate_dashboard.py` after changes |
| `shared/context.md` | All agent prompts | Voice, identity, goals flow into every agent |
| `shared/learnings.md` | All agent prompts | Hard constraints — agents read at session start |
| `.github/copilot-instructions.md` | All sessions | System rules — auto-injected |
| `prime/config.json` | `prime/dashboard.md` | Cadences, cycle state |
| `shared/theses.json` | Writer, Synthesizer outputs | Thesis data flows to content |
