#!/usr/bin/env python3
"""Create an OKF draft from a raw Markdown/text file."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", value.strip()).strip("-").lower()
    return slug[:80] or "untitled"


def yaml_scalar(value: str) -> str:
    if not value:
        return '""'
    if re.search(r"[:#\\[\\]{}]|^\\s|\\s$", value):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def create_draft(source: Path, output_dir: Path, title: str, entry_type: str, tags: list[str], resource: str) -> Path:
    body = source.read_text(encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{slugify(title)}.md"
    today = dt.date.today()
    frontmatter = "\n".join(
        [
            "---",
            f"type: {yaml_scalar(entry_type)}",
            f"title: {yaml_scalar(title)}",
            f"description: {yaml_scalar('Draft created from ' + source.name)}",
            f"resource: {yaml_scalar(resource)}",
            "tags:",
            *[f"  - {tag}" for tag in tags],
            f"timestamp: {dt.datetime.now(dt.timezone.utc).isoformat()}",
            "status: draft",
            "confidence: low",
            f"created: {today.isoformat()}",
            f"last_reviewed: {today.isoformat()}",
            f"review_after: {(today + dt.timedelta(days=90)).isoformat()}",
            "curator: TODO",
            "sensitivity: local",
            "provenance: import",
            "---",
            "",
        ]
    )
    path.write_text(frontmatter + body.strip() + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create OKF draft from raw file")
    parser.add_argument("--source", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--type", default="note")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--resource", default="local")
    args = parser.parse_args()

    tags = args.tag or ["draft"]
    path = create_draft(Path(args.source).resolve(), Path(args.output_dir).resolve(), args.title, args.type, tags, args.resource)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
