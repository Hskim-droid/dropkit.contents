import importlib.util
from pathlib import Path
import tempfile
import unittest
import json

spec = importlib.util.spec_from_file_location('metadata_check', Path(__file__).with_name('check-article-metadata.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MetadataTests(unittest.TestCase):
    def fixture(self, description=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        posts = root / 'src/content/posts'; posts.mkdir(parents=True)
        text = '---\ntitle: "Synthetic article"\npubDate: 2026-10-08\ndraft: false\napproved: true\n'
        if description is not None:
            text += 'description: ' + json.dumps(description) + '\n'
        (posts / 'example.md').write_text(text + '---\n\nSynthetic content.\n')
        return root, posts

    def test_missing_description_fails_before_build(self):
        root, _ = self.fixture()
        with self.assertRaisesRegex(ValueError, 'missing_or_duplicate_description'):
            m.check(root)

    def test_duplicate_article_descriptions_fail(self):
        root, posts = self.fixture('A synthetic review of automation evidence with clearly stated limitations.')
        (posts / 'other.md').write_text((posts / 'example.md').read_text().replace('Synthetic article','Another article'))
        with self.assertRaisesRegex(ValueError, 'duplicate_article_description'):
            m.check(root)

    def test_metadata_injection_and_language_residue_fail(self):
        for description in ('A description containing <script>active metadata</script> and claims.',
                            'An English description with 한국어 language residue and limitations.'):
            with self.subTest(description=description):
                root, _ = self.fixture(description)
                with self.assertRaisesRegex(ValueError, 'unsafe_or_non_english'):
                    m.check(root)

    def test_local_description_convention_is_not_fixed_160(self):
        root, _ = self.fixture(('A synthetic review with clear evidence and limitations. ' * 4).strip())
        self.assertEqual(m.check(root), 1)


if __name__ == '__main__':
    unittest.main()
