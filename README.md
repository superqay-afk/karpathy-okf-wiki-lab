# Karpathy LLM Wiki 中文知识库

这是一个本地优先、文件优先的中文知识库，参考 Andrej Karpathy 的 LLM Wiki 思路和 Google 开放知识格式 OKF。

项目把长期知识保存在 `okf/` 目录下的 Markdown 文件中，再生成图谱数据，并通过 `app/` 下的轻量 HTML 页面进行可视化浏览和管理。

## 快速开始

```bash
python3 scripts/okf_lint.py --root okf
python3 scripts/build_graph.py --root okf --output app/data.json
python3 -m http.server 8000
```

打开 `http://localhost:8000/app/`。

## 项目结构

```text
okf/                  中文 OKF Markdown 知识库
app/index.html        本地可视化管理页面
app/data.json         生成后的图谱和搜索数据
scripts/              导入、校验、图谱构建工具
tests/                单元和集成测试
docs/product-delivery PDOS 交付包
```

## 设计原则

Markdown 是知识源。HTML 页面只是查看和管理入口，不是数据库。
