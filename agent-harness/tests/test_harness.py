import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import harness  # noqa: E402


class HarnessTests(unittest.TestCase):
    def test_enqueue_and_dry_run_preserve_queued_state(self):
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
                        "executor": {"extract": None, "render": None, "send": None},
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
                        "daily report",
                        "--output-format",
                        "docx",
                    ]
                ),
                0,
            )
            self.assertEqual(
                harness.main(["--config", str(config_path), "run-once", "--dry-run"]),
                0,
            )
            config = harness.load_config(config_path)
            with harness.connect(config) as connection:
                row = connection.execute("SELECT status FROM jobs").fetchone()
            self.assertEqual(row["status"], "queued")

    def test_invalid_output_format_is_rejected(self):
        with self.assertRaises(SystemExit):
            harness.build_parser().parse_args(
                [
                    "enqueue",
                    "--source-system",
                    "QMS",
                    "--request",
                    "x",
                    "--output-format",
                    "pdf",
                ]
            )


if __name__ == "__main__":
    unittest.main()
