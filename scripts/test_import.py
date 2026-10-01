import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "scripts").mkdir()
        (self.root / "src/content/posts").mkdir(parents=True)
        self.script = self.root / "scripts/import-from-hub.sh"
        shutil.copyfile(Path(__file__).with_name("import-from-hub.sh"), self.script)
        self.source = self.root / "source.md"
        self.source.write_text('# A: "quoted" title\n정제된 신호: "sample"\n\nBody\n')

    def run_import(self, slug="fixture"):
        return subprocess.run(["bash", str(self.script), slug, str(self.source)],
                              env={**os.environ, "CT_CONTENT_HUB": str(self.root)},
                              capture_output=True, text=True)

    def test_import_is_draft_and_quotes_frontmatter(self):
        self.assertEqual(self.run_import().returncode, 0)
        text = (self.root / "src/content/posts/fixture.md").read_text()
        self.assertIn("draft: true", text)
        title = next(line[7:] for line in text.splitlines() if line.startswith("title: "))
        self.assertEqual(json.loads(title), 'A: "quoted" title')
        self.assertNotIn('# A:', text)
        self.assertIn("Body", text)

    def test_existing_post_is_preserved(self):
        target = self.root / "src/content/posts/fixture.md"
        target.write_text("Original")
        self.assertNotEqual(self.run_import().returncode, 0)
        self.assertEqual(target.read_text(), "Original")

    def test_path_traversal_is_rejected(self):
        self.assertEqual(self.run_import("../escape").returncode, 2)
        self.assertFalse((self.root / "src/content/escape.md").exists())


if __name__ == "__main__":
    unittest.main()
