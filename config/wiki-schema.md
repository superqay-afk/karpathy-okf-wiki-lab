# Local OKF Profile

This project follows a local-first OKF profile: Markdown files are the durable source of truth, and `app/data.json` is generated output.

## Required Frontmatter

- `type`
- `title`
- `description`
- `resource`
- `tags`
- `timestamp`

## Managed Extensions

- `status`: `draft`, `curated`, or `deprecated`
- `confidence`: `low`, `medium`, or `high`
- `created`
- `last_reviewed`
- `review_after`
- `curator`
- `sensitivity`: `public`, `local`, or `private`
- `provenance`: `source`, `human`, `llm`, `import`, or `mixed`
- `related`

## Hygiene Rules

- Preserve source URLs in `resource` or source pages.
- Use relative Markdown links for internal references.
- Keep unknown fields when editing by hand or through agent workflows.
- Treat unknown `type` values as warnings, not fatal errors.
- Record notable schema or source changes in `okf/log.md`.
