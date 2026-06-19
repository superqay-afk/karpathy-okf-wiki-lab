#!/usr/bin/env python3
"""Validate OKF Markdown files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from okf_core import extract_links, load_entries, validate_entry


def lint(root: Path) -> dict:
    entries = load_entries(root)
    all_paths = {entry["path"] for entry in entries}
    errors: list[str] = []
    warnings: list[str] = []
    inbound = {path: 0 for path in all_paths}

    for entry in entries:
        entry_errors, entry_warnings = validate_entry(entry, all_paths)
        errors.extend(entry_errors)
        warnings.extend(entry_warnings)
        for link in extract_links(entry):
            if link in inbound:
                inbound[link] += 1

    orphans = sorted(path for path, count in inbound.items() if count == 0 and path != "index.md")
    for path in orphans:
        warnings.append(f"{path}: orphan page")

    return {
        "root": str(root),
        "entry_count": len(entries),
        "errors": errors,
        "warnings": warnings,
        "orphans": orphans,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint OKF Markdown files")
    parser.add_argument("--root", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = lint(Path(args.root).resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"OKF entries: {result['entry_count']}")
        print(f"Errors: {len(result['errors'])}")
        for item in result["errors"]:
            print(f"  - {item}")
        print(f"Warnings: {len(result['warnings'])}")
        for item in result["warnings"]:
            print(f"  - {item}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
