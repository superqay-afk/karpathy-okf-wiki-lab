#!/usr/bin/env python3
"""Build graph/search data from OKF Markdown files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from okf_core import extract_links, load_entries, normalize_list


def excerpt(body: str, max_len: int = 240) -> str:
    text = re.sub(r"\s+", " ", re.sub(r"#+\s*", "", body)).strip()
    return text[:max_len] + ("..." if len(text) > max_len else "")


def build_graph(root: Path) -> dict:
    entries = load_entries(root)
    nodes = []
    links = []
    all_paths = {entry["path"] for entry in entries}
    tag_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}

    for entry in entries:
        metadata = entry["metadata"]
        tags = normalize_list(metadata.get("tags"))
        for tag in tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        type_counts[entry["type"]] = type_counts.get(entry["type"], 0) + 1
        nodes.append(
            {
                "id": entry["path"],
                "path": entry["path"],
                "title": entry["title"],
                "type": entry["type"],
                "description": metadata.get("description", ""),
                "resource": metadata.get("resource", ""),
                "tags": tags,
                "timestamp": metadata.get("timestamp", ""),
                "excerpt": excerpt(entry["body"]),
            }
        )
        for target in extract_links(entry):
            if target in all_paths:
                links.append({"source": entry["path"], "target": target})

    return {
        "nodes": nodes,
        "links": links,
        "stats": {
            "node_count": len(nodes),
            "link_count": len(links),
            "tag_counts": dict(sorted(tag_counts.items())),
            "type_counts": dict(sorted(type_counts.items())),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build OKF graph data")
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    graph = build_graph(root)
    output.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "stats": graph["stats"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
