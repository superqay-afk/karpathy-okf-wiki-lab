# Karpathy OKF Wiki Lab Delivery Plan

## 拆解

| Slice | Owner Role | Output |
| --- | --- | --- |
| PDOS hardening | Orchestrator + Self-Improvement Reviewer | command consistency, team validation, doc contract selftest |
| Source/schema design | Researcher + Knowledge Curator | OKF local profile, curated source pages, curation log |
| Tooling | Builder | parser, lint, ingest, graph build scripts |
| UI | Builder + Visual QA | local HTML viewer and management surface |
| Quality | QA Engineer | unit, integration, E2E, visual baseline |
| Release readiness | Release Manager | ready validation and preflight |

## 依赖

- Python 3 standard library.
- Existing PDOS skill under `/Users/yikuaiqian/.codex/skills/product-delivery-os`.
- Playwright runtime already available through the PDOS visual harness.
- Local HTTP server for browser screenshot capture.

## 开发顺序

1. Harden PDOS before project execution.
2. Create project structure and OKF seed documents.
3. Implement parser/lint/graph scripts.
4. Build HTML app.
5. Add unit and contract tests.
6. Generate data and run configured test suite.
7. Capture screenshot baseline and compare.
8. Mark quality gates and run preflight.

## 回滚方案

- Knowledge entries are plain Markdown and can be reverted with Git.
- Generated `app/data.json` and screenshot artifacts can be regenerated.
- Release policy has push, PR creation, and merge disabled.
- If OKF spec changes, update `config/wiki-schema.md` and parser warnings without breaking existing fields.

## 交接

- Main project path: `/Users/yikuaiqian/Documents/工作台/karpathy-okf-wiki-lab`.
- Local URL: `http://127.0.0.1:8765/app/`.
- Test logs: `/Users/yikuaiqian/Documents/工作台/karpathy-okf-wiki-lab/docs/product-delivery-artifacts/test-runs/manifest.json`.
- Visual manifest: `/Users/yikuaiqian/Documents/工作台/karpathy-okf-wiki-lab/docs/product-delivery-artifacts/visual/manifest.json`.
