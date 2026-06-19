---
type: concept
title: Open Knowledge Format
description: A Markdown and YAML-frontmatter format for portable knowledge packages.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags:
  - okf
  - markdown
  - frontmatter
timestamp: 2026-06-19T00:00:00+08:00
status: curated
confidence: medium
created: 2026-06-19
last_reviewed: 2026-06-19
review_after: 2026-09-19
curator: codex
sensitivity: public
provenance: mixed
related:
  - ../sources/google-okf.md
  - llm-wiki.md
---

# Open Knowledge Format

Open Knowledge Format standardizes the idea of a portable knowledge package using a directory of Markdown files with structured frontmatter.

## Local Interpretation

This project uses a compact OKF-compatible subset:

- `type`
- `title`
- `description`
- `resource`
- `tags`
- `timestamp`
- optional `related`

The local profile is intentionally stricter than OKF's minimal extensibility rule so the viewer and agent team have enough metadata to manage quality.

## Related

- [Google OKF Source](../sources/google-okf.md)
- [LLM Wiki](llm-wiki.md)
