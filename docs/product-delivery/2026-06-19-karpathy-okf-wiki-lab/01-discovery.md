# Karpathy OKF Wiki Lab Discovery

## 决策问题

应如何把 Codex 的“从需求到上线”能力做成全局可用、可复用、不过度复杂的体系，并用一个 Karpathy LLM Wiki + Google OKF 本地知识库项目验证它。

## 证据地图

| 证据 | 来源 | 链接/路径 | 可信度 | 说明 |
| --- | --- | --- | --- | --- |
| LLM Wiki pattern | Karpathy public gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | Medium | 作为本地文件化知识库思路来源 |
| Open Knowledge Format | Google Cloud announcement | https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing | High | 说明 OKF 作为 agent knowledge exchange 格式 |
| OKF v0.1 spec | GoogleCloudPlatform knowledge-catalog | https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md | High | 约束 Markdown bundle、frontmatter、extensibility |
| PDOS skill self-audit | Local harness output | /Users/yikuaiqian/.codex/skills/product-delivery-os/scripts/pdos_tests.py | High | 自测覆盖 harness、team、visual、release、doc contract |
| Project verification | Local test artifacts | /Users/yikuaiqian/Documents/工作台/karpathy-okf-wiki-lab/docs/product-delivery-artifacts/test-runs/manifest.json | High | 记录 lint、typecheck、unit、integration、e2e、build |

## 用户/场景

用户希望 Codex 不只是临时写代码，而是拥有可沉淀、可复制的工作系统。该系统要能先判断需求和证据，再组织 agent team、产出方案、开发、测试、截图、上线验收和复盘。

## 机会判断

推荐构建“一个主技能 + 少量 harness + 文件化 agent team”的 OS，而不是堆很多独立 skill 或常驻智能体。这样既能全局触发，又能把确定性检查交给脚本，降低多智能体协作漂移。

## 不做什么

- 不创建无法被当前 Codex runtime 直接调用的伪常驻 agent。
- 不为每个职能创建重复 skill。
- 不把 OKF 数据塞进数据库作为第一版。
- 不自动发布到 GitHub 或线上环境，除非后续显式开启 release policy。
