#!/usr/bin/env python3
"""Shared OKF parsing helpers."""

from __future__ import annotations

import datetime as dt
import json
import posixpath
import re
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = ["type", "title", "description", "resource", "tags", "timestamp"]
VALID_TYPES = {"index", "concept", "source", "question", "project", "person", "pattern", "note"}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")
WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]]+\.md)\]\]")


def parse_scalar(value: str) -> Any:
    text = value.strip()
    if text.startswith("[") and text.endswith("]"):
        try:
            return json.loads(text.replace("'", '"'))
        except json.JSONDecodeError:
            return [item.strip() for item in text.strip("[]").split(",") if item.strip()]
    return text.strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw = text[4:end].strip().splitlines()
    body = text[end + 4 :].lstrip("\n")
    metadata: dict[str, Any] = {}
    current_key = ""

    for line in raw:
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            metadata.setdefault(current_key, []).append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        if value.strip():
            metadata[current_key] = parse_scalar(value)
        else:
            metadata[current_key] = []
    return metadata, body


def read_okf_file(path: Path, root: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(text)
    rel_path = path.relative_to(root).as_posix()
    return {
        "path": rel_path,
        "metadata": metadata,
        "body": body,
        "title": metadata.get("title", path.stem),
        "type": metadata.get("type", "note"),
        "tags": metadata.get("tags", []),
    }


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        if path.is_file():
            yield path


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


def is_iso_date(value: Any) -> bool:
    text = str(value).strip()
    try:
        dt.date.fromisoformat(text)
        return True
    except ValueError:
        pass
    try:
        dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def contains_todo(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip() == "TODO" or "TODO" in value
    if isinstance(value, list):
        return any(contains_todo(item) for item in value)
    if isinstance(value, dict):
        return any(contains_todo(item) for item in value.values())
    return False


def resolve_link(source_path: str, target: str) -> str:
    if target.startswith(("http://", "https://", "mailto:")):
        return target
    if target.startswith("/"):
        return posixpath.normpath(target.lstrip("/"))
    base = posixpath.dirname(source_path)
    return posixpath.normpath(posixpath.join(base, target))


def extract_links(entry: dict[str, Any]) -> list[str]:
    body = entry["body"]
    source_path = entry["path"]
    links = []
    for match in LINK_PATTERN.findall(body):
        links.append(resolve_link(source_path, match))
    for match in WIKI_LINK_PATTERN.findall(body):
        links.append(resolve_link(source_path, match))
    for related in normalize_list(entry["metadata"].get("related")):
        links.append(resolve_link(source_path, related))
    return sorted(set(links))


def validate_entry(entry: dict[str, Any], all_paths: set[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    metadata = entry["metadata"]
    path = entry["path"]

    if not metadata:
        errors.append(f"{path}: missing frontmatter")
        return errors, warnings

    for field in REQUIRED_FIELDS:
        if field not in metadata or metadata[field] in ("", [], None):
            errors.append(f"{path}: missing required field {field}")

    entry_type = metadata.get("type")
    if entry_type and str(entry_type).lower() not in VALID_TYPES:
        warnings.append(f"{path}: unknown local type {entry_type}")

    tags = metadata.get("tags")
    if not isinstance(tags, list) or not normalize_list(tags):
        errors.append(f"{path}: tags must be a non-empty list")

    if "timestamp" in metadata and not is_iso_date(metadata["timestamp"]):
        errors.append(f"{path}: timestamp must be ISO 8601 date or datetime")

    if "TODO" in entry["body"] or contains_todo(metadata):
        warnings.append(f"{path}: contains TODO")

    for link in extract_links(entry):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        if link not in all_paths:
            errors.append(f"{path}: broken internal link {link}")

    return errors, warnings


def load_entries(root: Path) -> list[dict[str, Any]]:
    return [read_okf_file(path, root) for path in iter_markdown(root)]
