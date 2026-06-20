from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AppContractTests(unittest.TestCase):
    def test_html_contains_required_surfaces(self) -> None:
        html = (ROOT / "app" / "index.html").read_text(encoding="utf-8")
        for token in ["data.json", "graphCanvas", "searchInput", "entryList", "draftOutput"]:
            self.assertIn(token, html)

    def test_html_uses_chinese_user_facing_copy(self) -> None:
        html = (ROOT / "app" / "index.html").read_text(encoding="utf-8")
        for token in ["Karpathy LLM Wiki 中文知识库", "条目", "图谱", "质量检查", "新条目草稿"]:
            self.assertIn(token, html)

    def test_generated_data_file_contract_when_present(self) -> None:
        data_path = ROOT / "app" / "data.json"
        if not data_path.exists():
            self.skipTest("app/data.json has not been generated yet")
        data = json.loads(data_path.read_text(encoding="utf-8"))
        self.assertIn("nodes", data)
        self.assertIn("links", data)
        self.assertIn("stats", data)
        self.assertGreaterEqual(data["stats"]["node_count"], len(data["nodes"]))


if __name__ == "__main__":
    unittest.main()
