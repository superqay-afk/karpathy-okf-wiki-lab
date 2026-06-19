---
type: concept
title: LLM Wiki
description: A file-based knowledge workspace that lets agents maintain durable, navigable context over time.
resource: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags:
  - llm-wiki
  - agents
  - markdown
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
  - ../sources/karpathy-llm-wiki.md
  - open-knowledge-format.md
---

# LLM Wiki

The LLM Wiki pattern keeps knowledge in human-readable files so agents can search, edit, and cite durable context instead of relying only on transient chat history.

## Local Interpretation

For this project, the wiki is a folder of Markdown files with explicit metadata, internal links, and generated graph data.

## Source Boundary

This page is a local interpretation of the public gist, not an official standard.

## Related

- [Karpathy LLM Wiki Source](../sources/karpathy-llm-wiki.md)
- [Open Knowledge Format](open-knowledge-format.md)
