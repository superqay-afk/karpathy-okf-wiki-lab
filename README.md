# Karpathy OKF Wiki Lab

A local, file-first knowledge base inspired by Andrej Karpathy's LLM Wiki pattern and Google's Open Knowledge Format.

The project keeps durable knowledge as Markdown files under `okf/`, builds a graph data file, and serves a lightweight HTML manager from `app/`.

## Quick Start

```bash
python3 scripts/okf_lint.py --root okf
python3 scripts/build_graph.py --root okf --output app/data.json
python3 -m http.server 8000
```

Open `http://localhost:8000/app/`.

## Project Shape

```text
okf/                  OKF-style Markdown knowledge base
app/index.html        Local visual manager
app/data.json         Generated graph/search data
scripts/              Ingest, lint, graph build tools
tests/                Unit/integration tests
docs/product-delivery PDOS delivery package
```

## Design Rule

Markdown is the source of truth. The HTML app is a viewer and management surface, not the database.
