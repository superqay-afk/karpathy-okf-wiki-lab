# Karpathy OKF Wiki Lab Launch Acceptance

## 上线检查

- Local preview service runs at `http://127.0.0.1:8765/app/`.
- Release policy disables push, PR creation, and merge.
- Worktree cleanliness is not required for this local package handoff.
- Test, screenshot, and baseline artifacts are recorded under `docs/product-delivery-artifacts/`.

## 验收结论

Accepted for local use. The project can lint and build a local OKF knowledge base, render a browser-based visualization/management page, and pass PDOS quality gates.

## 监控

- Re-run OKF lint after changing `okf/`.
- Re-run graph build after changing knowledge files or graph logic.
- Re-run visual capture after UI changes.
- Watch OKF spec changes before expanding the schema.

## 复盘

- The agent team design is reasonable when roles stay as responsibilities plus task-board state, not permanent fake workers.
- The harness layer is the key reliability improvement: it catches drift in commands, missing task dependencies, missing artifacts, lint failures, and visual regressions.
- The OS was improved once during this project by adding dependency/artifact checks and document contract selftests.
- Current system is intentionally compact: one orchestrating skill, one team board, five focused harness scripts, and optional MCP usage only when live/private context is needed.
