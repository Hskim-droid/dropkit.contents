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
        self.private = self.root.parent / (self.root.name + '-private')
        self.private.mkdir(mode=0o700)
        self.addCleanup(shutil.rmtree, self.private)

    def run_import(self, slug="fixture", staging=None):
        return subprocess.run(["bash", str(self.script), slug, str(self.source)],
                              env={**os.environ, "CT_CONTENT_HUB": str(self.root),
                                   "CT_PRIVATE_STAGING": str(staging or self.private)},
                              capture_output=True, text=True)

    def test_import_is_draft_and_quotes_frontmatter(self):
        self.assertEqual(self.run_import().returncode, 0)
        text = (self.private / "fixture.md").read_text()
        self.assertIn("draft: true", text)
        self.assertIn("approved: false", text)
        self.assertFalse(list((self.root / "src/content/posts").iterdir()))
        self.assertEqual((self.private / 'fixture.md').stat().st_mode & 0o777, 0o600)
        title = next(line[7:] for line in text.splitlines() if line.startswith("title: "))
        self.assertEqual(json.loads(title), 'A: "quoted" title')
        self.assertNotIn('# A:', text)
        self.assertIn("Body", text)

    def test_existing_post_is_preserved(self):
        target = self.private / "fixture.md"
        target.write_text("Original")
        self.assertNotEqual(self.run_import().returncode, 0)
        self.assertEqual(target.read_text(), "Original")

    def test_path_traversal_is_rejected(self):
        self.assertEqual(self.run_import("../escape").returncode, 2)
        self.assertFalse((self.root / "src/content/escape.md").exists())

    def test_public_checkout_staging_is_rejected(self):
        self.assertNotEqual(self.run_import(staging=self.root / 'drafts').returncode, 0)
        self.assertFalse((self.root / 'drafts').exists())

    def test_symlink_into_public_checkout_is_rejected(self):
        link = self.private / 'public-link'
        link.symlink_to(self.root / 'src/content/posts')
        self.assertNotEqual(self.run_import(staging=link).returncode, 0)
        self.assertFalse(list((self.root / 'src/content/posts').iterdir()))


if __name__ == "__main__":
    unittest.main()
