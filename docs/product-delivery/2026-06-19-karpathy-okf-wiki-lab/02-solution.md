# Karpathy OKF Wiki Lab Solution

## 推荐方案

采用 Product Delivery OS 作为全局工作层：`product-delivery-os` skill 负责流程和路由，`pdos_team.py` 管理 agent team 任务板，`pdos_harness.py` 管理交付包和质量门，`pdos_release.py`、`pdos_visual.py`、`pdos_doctor.py` 承担测试、截图和 release preflight。

本项目用该 OS 交付一个本地 OKF 知识库：

- `okf/` 保存知识条目。
- `scripts/` 负责 ingest、lint、graph build。
- `app/index.html` 提供可视化和管理界面。
- `docs/product-delivery-artifacts/` 保存测试和截图证据。

## 用户流程

1. 维护者把原始材料放入 `raw/sources/` 或直接新增 OKF Markdown。
2. 运行 lint 检查 frontmatter、链接、标签、孤儿页面。
3. 运行 graph build 生成 `app/data.json`。
4. 打开 `http://127.0.0.1:8765/app/` 浏览、搜索、筛选、查看图谱和 hygiene。
5. 使用 Draft 面板生成新条目的 frontmatter 草稿，再落回 Markdown。

## 规则与边界

- OKF 本地 profile 要求 `type`、`title`、`description`、`resource`、`tags`、`timestamp`。
- 允许未知 `type`，但作为 warning 进入质量反馈。
- 相对链接必须可解析，坏链路作为 error。
- HTML 不直接写文件，避免浏览器安全边界被绕过。
- release policy 禁止 push、建 PR、merge。

## 指标设计

- Knowledge health：lint errors = 0，orphans = 0，hygiene sparse/missing = 0。
- Delivery health：配置化 test commands 全部 returncode = 0。
- Visual health：desktop/mobile screenshot 与 baseline hash 一致。
- Process health：PDOS ready 和 preflight 均通过。

## 验收标准

- `python3 scripts/okf_lint.py --root okf` 返回 0。
- `python3 -m unittest discover -s tests` 返回 0。
- `python3 scripts/build_graph.py --root okf --output app/data.json` 生成有效数据。
- `pdos_visual.py capture --require-baseline` 桌面和移动端均为 same。
- `pdos_harness.py validate --ready` 返回 0。
- `pdos_release.py preflight` 返回 0。
