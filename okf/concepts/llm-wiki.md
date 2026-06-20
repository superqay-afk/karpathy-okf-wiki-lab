---
type: concept
title: LLM Wiki 模式
description: 一种基于文件的知识工作区，让 Agent 能长期维护、检索和引用上下文。
resource: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags:
  - LLM Wiki
  - 智能体
  - Markdown
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

# LLM Wiki 模式

LLM Wiki 模式把知识放在人类可读的文件中，让 Agent 可以搜索、编辑、链接和引用稳定上下文，而不是只依赖一次对话里的短期记忆。

## 本地理解

在这个项目里，Wiki 是一个 Markdown 文件夹：每个条目都有明确元数据、内部链接和可生成的图谱数据。Markdown 是知识源，HTML 页面只是查看和管理入口。

## 来源边界

本页是对公开 gist 的本地化理解，不代表官方标准。

## 相关

- [Karpathy LLM Wiki 来源](../sources/karpathy-llm-wiki.md)
- [开放知识格式 OKF](open-knowledge-format.md)
