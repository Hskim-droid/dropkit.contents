import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import fixture_demo  # noqa: E402
import harness  # noqa: E402


@unittest.skipUnless(fixture_demo.IMPORT_ERROR is None, "fixture dependencies are not installed")
class FixtureDemoTests(unittest.TestCase):
    def test_synthetic_qms_screen_becomes_reopenable_docx(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            config_path = temp_path / "config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "persona_id": "han-gyeol",
                        "persona_name": "한결",
                        "mode": "draft_only",
                        "state_dir": str(temp_path / "state"),
                        "artifact_dir": str(temp_path / "artifacts"),
                        "default_output_format": "docx",
                        "recipient_allowlist": [],
                        "executor": {"extract": "fixture-demo", "render": None, "send": None},
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                harness.main(
                    [
                        "--config",
                        str(config_path),
                        "enqueue",
                        "--source-system",
                        "QMS",
                        "--request",
                        "synthetic daily report 2026-09-21",
                        "--output-format",
                        "docx",
                    ]
                ),
                0,
            )
            config = harness.load_config(config_path)
            with harness.connect(config) as connection:
                job_id = connection.execute("SELECT id FROM jobs").fetchone()[0]
            result = fixture_demo.run_demo(
                config_path,
                job_id,
                ROOT / "fixtures" / "qms_daily.html",
                claim=True,
            )
            self.assertEqual(result["records"], 3)
            self.assertTrue(Path(result["artifact"]).is_file())
            self.assertTrue(Path(result["manifest"]).is_file())
            with harness.connect(config) as connection:
                row = connection.execute("SELECT status FROM jobs WHERE id=?", (job_id,)).fetchone()
            self.assertEqual(row["status"], "drafted")

    def test_duplicate_screen_rows_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            html = Path(temp) / "duplicate.html"
            fixture = (ROOT / "fixtures" / "qms_daily.html").read_text(encoding="utf-8")
            duplicate = fixture.replace(
                '<tr data-record-id="QMS-1003">\n            <td>QMS-1003</td>',
                '<tr data-record-id="QMS-1001">\n            <td>QMS-1001</td>',
            )
            html.write_text(duplicate, encoding="utf-8")
            with self.assertRaises(ValueError):
                fixture_demo.extract_qms_screen(html)

    def test_fixture_rejects_non_docx_without_claiming_it(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            config_path = temp_path / "config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "persona_id": "han-gyeol",
                        "persona_name": "한결",
                        "mode": "draft_only",
                        "state_dir": str(temp_path / "state"),
                        "artifact_dir": str(temp_path / "artifacts"),
                        "default_output_format": "xlsx",
                        "recipient_allowlist": [],
                        "executor": {"extract": "fixture-demo", "render": None, "send": None},
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                harness.main(
                    [
                        "--config",
                        str(config_path),
                        "enqueue",
                        "--source-system",
                        "QMS",
                        "--request",
                        "synthetic xlsx report 2026-09-21",
                        "--output-format",
                        "xlsx",
                    ]
                ),
                0,
            )
            config = harness.load_config(config_path)
            with harness.connect(config) as connection:
                job_id = connection.execute("SELECT id FROM jobs").fetchone()[0]
            with self.assertRaises(ValueError):
                fixture_demo.run_demo(config_path, job_id, ROOT / "fixtures" / "qms_daily.html", claim=True)
            with harness.connect(config) as connection:
                status = connection.execute("SELECT status FROM jobs WHERE id=?", (job_id,)).fetchone()[0]
            self.assertEqual(status, "queued")


if __name__ == "__main__":
    unittest.main()
