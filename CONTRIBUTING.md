# Contributing

Agent Prime is designed for individual use, but contributions that improve the system for everyone are welcome.

## Good Contributions

- **New skills** — Domain methodologies in `shared/toolkits/skills/`. Follow the spec in `shared/toolkits/skill_file_spec.md` and validate with `python meta/scripts/check_skill_compliance.py`.
- **Agent improvements** — Better methodologies, clearer output formats, stronger quality checks in any `agents/*/prompt.md`.
- **Documentation** — Fixes, clarifications, better examples.
- **Scripts** — Bug fixes or improvements to the Python scripts in `meta/scripts/`.
- **Example domains** — New worked examples in `examples/` showing Agent Prime configured for different roles.

## Submitting Changes

1. Fork the repo and create a branch.
2. Keep PRs focused — one skill, one agent fix, or one documentation improvement per PR.
3. If modifying an agent prompt, verify the Context Verification Gate still works.
4. If adding a skill, include the full SKILL.md structure (metadata, method, output format, quality markers).
5. Do not include personal data (names, employer details, NDA-covered information) — keep contributions generic.

## What Not to Submit

- Your personal `shared/context.md`, `registry.json`, or `learnings.md` — these are private to each user.
- Changes to `.github/copilot-instructions.md` system rules without discussion — these are structural load-bearing walls.
- Benchmark outputs or evaluation results from your own usage.
