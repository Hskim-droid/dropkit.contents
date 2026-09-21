import json
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import browser_probe  # noqa: E402


@unittest.skipUnless(browser_probe.IMPORT_ERROR is None, "browser probe dependencies are not installed")
class BrowserProbeTests(unittest.TestCase):
    def test_one_task_contract_handles_three_menu_and_table_variants(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        expected_ids = ["QMS-1001", "QMS-1002", "QMS-1003"]
        for number in (1, 2, 3):
            with self.subTest(variant=number):
                result = browser_probe.run_task(ROOT / "fixtures" / f"qms_variant_{number}.html", task)
                self.assertEqual([record["issue_id"] for record in result["records"]], expected_ids)
                self.assertEqual(result["field_mapping"]["issue_id"], 0 if number != 2 else 1)
                self.assertTrue(all(check["passed"] for check in result["checks"]))
                self.assertGreaterEqual(len(result["actions"]), 2 if number < 3 else 4)
                self.assertIn("read_table", result["observation_after"]["capabilities"])

    def test_ambiguous_navigation_stops_without_clicking(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        html = (ROOT / "fixtures" / "qms_variant_1.html").read_text(encoding="utf-8")
        html = html.replace(
            "<button role=\"menuitem\" onclick=\"showIssues()\">Quality open issues</button>",
            "<button role=\"menuitem\" onclick=\"showIssues()\">Quality open issues</button>"
            "<button role=\"menuitem\" onclick=\"showIssues()\">Quality open issues</button>",
        )
        path = ROOT / "fixtures" / ".tmp-ambiguous-qms.html"
        path.write_text(html, encoding="utf-8")
        try:
            with self.assertRaises(browser_probe.ProbeError):
                browser_probe.run_task(path, task)
        finally:
            path.unlink()

    def test_unpublished_menu_label_variant_uses_the_same_contract(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        html = (ROOT / "fixtures" / "qms_variant_1.html").read_text(encoding="utf-8")
        html = html.replace("Quality open issues", "Quality exceptions — open issues")
        path = ROOT / "fixtures" / ".tmp-unpublished-qms.html"
        path.write_text(html, encoding="utf-8")
        try:
            result = browser_probe.run_task(path, task)
            self.assertEqual([record["issue_id"] for record in result["records"]], ["QMS-1001", "QMS-1002", "QMS-1003"])
        finally:
            path.unlink()

    def test_matching_column_aliases_must_be_one_to_one(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        html = (ROOT / "fixtures" / "qms_variant_1.html").read_text(encoding="utf-8")
        html = html.replace("<th>Title</th>", "").replace("<td>Incoming inspection hold</td>", "")
        html = html.replace("<td>Calibration evidence missing</td>", "").replace("<td>Supplier corrective action overdue</td>", "")
        path = ROOT / "fixtures" / ".tmp-colliding-columns.html"
        path.write_text(html, encoding="utf-8")
        try:
            with self.assertRaises(browser_probe.ProbeError):
                browser_probe.run_task(path, task)
        finally:
            path.unlink()

    def test_forbidden_menu_item_is_rejected_before_click(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        html = (ROOT / "fixtures" / "qms_variant_1.html").read_text(encoding="utf-8")
        html = html.replace(
            "<button role=\"menuitem\" onclick=\"showIssues()\">Quality open issues</button>",
            "<button role=\"menuitem\" onclick=\"document.body.dataset.mutated='yes'\">Delete quality issue</button>",
        )
        path = ROOT / "fixtures" / ".tmp-forbidden-qms.html"
        path.write_text(html, encoding="utf-8")
        try:
            with self.assertRaises(browser_probe.ProbeError):
                browser_probe.run_task(path, task)
        finally:
            path.unlink()

    def test_table_identity_prevents_selecting_a_completed_same_schema_table(self):
        task = json.loads((ROOT / "fixtures" / "qms_task.json").read_text(encoding="utf-8"))
        html = (ROOT / "fixtures" / "qms_variant_1.html").read_text(encoding="utf-8")
        completed = """
        <table aria-label="Completed quality issues">
          <thead><tr><th>Issue ID</th><th>Title</th><th>Status</th><th>Owner</th><th>Updated</th></tr></thead>
          <tbody><tr><td>QMS-9999</td><td>Closed issue</td><td>Closed</td><td>J. Kim</td><td>2026-01-01</td></tr></tbody>
        </table>
        """
        html = html.replace("<main id=\"issues\" hidden>", completed + "<main id=\"issues\" hidden>")
        path = ROOT / "fixtures" / ".tmp-completed-qms.html"
        path.write_text(html, encoding="utf-8")
        try:
            result = browser_probe.run_task(path, task)
            self.assertNotIn("QMS-9999", [record["issue_id"] for record in result["records"]])
        finally:
            path.unlink()


if __name__ == "__main__":
    unittest.main()
