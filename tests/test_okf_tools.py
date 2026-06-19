from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_graph import build_graph  # noqa: E402
from okf_core import parse_frontmatter, read_okf_file, resolve_link, validate_entry  # noqa: E402
from okf_lint import lint  # noqa: E402


def okf_doc(title: str, body: str = "Body", **metadata: object) -> str:
    data = {
        "type": "concept",
        "title": title,
        "description": f"{title} description",
        "resource": "local",
        "tags": ["test", "okf"],
        "timestamp": "2026-06-19T00:00:00+08:00",
        **metadata,
    }
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            lines.append(f"{key}: {value}")
    lines.extend(["---", "", f"# {title}", "", body, ""])
    return "\n".join(lines)


class OkfToolTests(unittest.TestCase):
    def test_happy_path_lint_and_graph(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "concepts").mkdir()
            (root / "index.md").write_text(
                okf_doc("Index", "- [Child](concepts/child.md)", type="index"),
                encoding="utf-8",
            )
            (root / "concepts" / "child.md").write_text(
                okf_doc("Child", "Linked from [Index](../index.md)"),
                encoding="utf-8",
            )

            result = lint(root)
            graph = build_graph(root)

        self.assertEqual(result["errors"], [])
        self.assertEqual(graph["stats"]["node_count"], 2)
        self.assertEqual(graph["stats"]["link_count"], 2)

    def test_inline_tag_list_boundary(self) -> None:
        metadata, _ = parse_frontmatter(
            "---\n"
            "type: concept\n"
            "title: Inline\n"
            "description: Inline list\n"
            "resource: local\n"
            "tags: [alpha, beta]\n"
            "timestamp: 2026-06-19\n"
            "---\n"
            "Body\n"
        )
        self.assertEqual(metadata["tags"], ["alpha", "beta"])

    def test_iso_datetime_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "entry.md"
            path.write_text(okf_doc("Entry", timestamp="2026-06-19T12:01:02+08:00"), encoding="utf-8")
            entry = read_okf_file(path, root)
            errors, _ = validate_entry(entry, {"entry.md"})
        self.assertFalse([error for error in errors if "timestamp" in error])

    def test_parent_relative_link_boundary(self) -> None:
        self.assertEqual(resolve_link("concepts/llm-wiki.md", "../sources/karpathy.md"), "sources/karpathy.md")

    def test_missing_frontmatter_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "bad.md"
            path.write_text("# Bad\n", encoding="utf-8")
            entry = read_okf_file(path, root)
            errors, _ = validate_entry(entry, {"bad.md"})
        self.assertIn("bad.md: missing frontmatter", errors)

    def test_broken_link_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "entry.md"
            path.write_text(okf_doc("Entry", "[Missing](missing.md)"), encoding="utf-8")
            result = lint(root)
        self.assertTrue(any("broken internal link missing.md" in error for error in result["errors"]))

    def test_unknown_type_is_warning_regression(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "entry.md"
            path.write_text(okf_doc("Entry", type="customEntity"), encoding="utf-8")
            entry = read_okf_file(path, root)
            errors, warnings = validate_entry(entry, {"entry.md"})
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown local type customEntity" in warning for warning in warnings))

    def test_todo_metadata_warning_regression(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "entry.md"
            path.write_text(okf_doc("Entry", curator="TODO"), encoding="utf-8")
            entry = read_okf_file(path, root)
            _, warnings = validate_entry(entry, {"entry.md"})
        self.assertTrue(any("contains TODO" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
