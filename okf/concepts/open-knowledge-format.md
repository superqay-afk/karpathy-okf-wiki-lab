---
type: concept
title: 开放知识格式 OKF
description: 一种基于 Markdown 和 YAML frontmatter 的可迁移知识包格式。
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags:
  - OKF
  - Markdown
  - 元数据
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

# 开放知识格式 OKF

开放知识格式 OKF 将“可迁移知识包”标准化：用一组 Markdown 文件保存知识正文，并用结构化 frontmatter 描述类型、来源、标签和时间等信息。

## 本地理解

这个项目使用一个紧凑的 OKF 兼容子集：

- `type`
- `title`
- `description`
- `resource`
- `tags`
- `timestamp`
- 可选 `related`

本地配置比 OKF 的最低扩展规则更严格，目的是让可视化页面和 Agent 团队有足够元数据来做质量管理。

## 相关

- [Google OKF 来源](../sources/google-okf.md)
- [LLM Wiki 模式](llm-wiki.md)
