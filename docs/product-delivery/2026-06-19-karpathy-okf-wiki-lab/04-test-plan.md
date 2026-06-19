# Karpathy OKF Wiki Lab Test Plan

## 风险识别

- Parser risk：frontmatter、inline list、relative links、ISO datetime 解析错误。
- Knowledge risk：坏链接、孤儿页、缺 metadata、未知类型误判。
- UI risk：数据未加载、列表筛选失效、图谱空白、移动端文字重叠。
- Process risk：OS 文档和脚本口径漂移，多智能体任务没有依赖/产物校验。

## 用例矩阵

| 类型 | 用例 | 预期 | 证据 |
| --- | --- | --- | --- |
| Happy Path | lint + graph on seeded OKF | 0 errors and valid node/link stats | `lint.log`, `integration.log` |
| Boundary | inline tags list | parser returns list values | `tests/test_okf_tools.py` |
| Boundary | ISO date and ISO datetime | accepted without timestamp error | `tests/test_okf_tools.py` |
| Boundary | parent relative link | normalized to bundle path | `tests/test_okf_tools.py` |
| Failure | missing frontmatter | validation error | `tests/test_okf_tools.py` |
| Failure | broken internal link | lint error | `tests/test_okf_tools.py` |
| Regression | unknown type | warning, not fatal error | `tests/test_okf_tools.py` |
| Regression | visual overlap found in screenshot | row height and mobile label fix verified | visual manifest and screenshots |

## 执行命令

- `python3 -m py_compile scripts/okf_core.py scripts/okf_lint.py scripts/build_graph.py scripts/ingest.py`
- `python3 scripts/okf_lint.py --root okf --json`
- `python3 -m unittest discover -s tests`
- `python3 scripts/build_graph.py --root okf --output app/data.json`
- `python3 /Users/yikuaiqian/.codex/skills/product-delivery-os/scripts/pdos_release.py run-tests --root .`
- `python3 /Users/yikuaiqian/.codex/skills/product-delivery-os/scripts/pdos_visual.py capture --root . --url http://127.0.0.1:8765/app/ --require-baseline`

## 结果记录

- OKF lint: passed, 7 entries, 0 errors, 0 warnings.
- Unit/contract tests: passed, 10 tests.
- Configured PDOS tests: passed for lint, typecheck, unit, integration, e2e, build.
- Visual screenshots: passed for desktop 1280x800 and mobile 375x812; baseline status same.
- Manual screenshot inspection: initial row text overlap and mobile graph label overlap were found and fixed before final baseline.

## 剩余风险

- HTML page is local read-only; direct file write requires a future trusted local app or MCP.
- OKF v0.1 may evolve; current schema should be treated as a local profile.
- Visual baseline uses hash comparison, not semantic layout assertions.
