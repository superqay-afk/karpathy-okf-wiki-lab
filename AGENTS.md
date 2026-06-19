# AGENTS.md

## Project Rules

- Keep `okf/` Markdown files as the source of truth.
- Use Python standard library for scripts unless a dependency is clearly justified.
- Run `python3 -m unittest discover -s tests` after script changes.
- Run `python3 scripts/okf_lint.py --root okf` after changing knowledge files.
- Run `python3 scripts/build_graph.py --root okf --output app/data.json` after changing knowledge files or graph logic.
- For UI changes, run a local server and capture screenshots through the PDOS visual harness.
- After substantial work, use `$neat-freak` or run `python3 /Users/yikuaiqian/.codex/skills/product-delivery-os/scripts/pdos_capability.py audit --root . --write`.
- Use `$claude-mem` before deciding whether a lesson belongs in project artifacts, `.learnings/`, AGENTS.md, a skill update, or Codex memory.
- Do not write global Codex memory unless the user explicitly asks.
- Keep external actions behind `pdos.project.json` `human_confirmation`.

## OKF Rules

Each knowledge file must start with YAML-style frontmatter containing:

- `type`
- `title`
- `description`
- `resource`
- `tags`
- `timestamp`

Use relative Markdown links for internal references where possible.

## Human Confirmation

Require explicit confirmation before:

- sending external messages;
- publishing social posts;
- deleting or overwriting user-owned files;
- submitting approvals;
- pushing, creating PRs, merging, or deploying;
- spending money or changing billing.

## Learnings

Use `.learnings/` for project-local corrections, errors, and feature requests. Promote only stable project rules to this file.
