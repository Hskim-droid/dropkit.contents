import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('builder', Path(__file__).with_name('build-skills.py'))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class CatalogTests(unittest.TestCase):
    def fixture(self, root):
        (root / 'skills/sample').mkdir(parents=True)
        (root / 'services').mkdir()
        (root / 'skills/sample/SKILL.md').write_text('Use a synthetic input and verify the result.')
        (root / 'skills/sample/LICENSE').write_text('MIT synthetic test fixture')
        entry = dict(id='sample', title='Sample', description='Synthetic fixture', license='MIT',
                     provenance='Synthetic test fixture only', files=['SKILL.md', 'LICENSE'],
                     ownershipConfirmed=True, generalizationReviewed=True, syntheticExamplesOnly=True,
                     publicationApproved=True, companyDerived=False)
        (root / 'services/catalog.json').write_text('{"services": []}')
        return entry

    def run_fixture(self, change=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entry = self.fixture(root)
            if change:
                change(root, entry)
            (root / 'skills/catalog.json').write_text(json.dumps({'skills': [entry]}))
            result = builder.build(root)
            with zipfile.ZipFile(root / 'public/skills/sample.zip') as archive:
                self.assertEqual(set(archive.namelist()), {'sample/SKILL.md', 'sample/LICENSE'})
            return result

    def test_only_reviewed_files_are_packaged(self):
        self.assertEqual(self.run_fixture(), (1, 0))

    def test_missing_publication_approval_is_blocked(self):
        with self.assertRaises(ValueError):
            self.run_fixture(lambda _, e: e.update(publicationApproved=False))

    def test_undeclared_sensitive_file_is_blocked(self):
        with self.assertRaises(ValueError):
            self.run_fixture(lambda r, _: (r / 'skills/sample/extra.txt').write_text('unreviewed'))

    def test_path_traversal_is_blocked(self):
        with self.assertRaises(ValueError):
            self.run_fixture(lambda _, e: e['files'].append('../private.txt'))

    def test_symlink_to_external_file_is_blocked(self):
        def inject(root, entry):
            (root / 'external.txt').write_text('not reviewed')
            (root / 'skills/sample/external.txt').symlink_to(root / 'external.txt')
            entry['files'].append('external.txt')
        with self.assertRaises(ValueError):
            self.run_fixture(inject)

    def test_company_text_is_blocked(self):
        with self.assertRaises(ValueError):
            self.run_fixture(lambda r, _: (r / 'skills/sample/SKILL.md').write_text('Hanlim-specific procedure'))

    def test_unlaunched_service_is_blocked(self):
        def inject(root, _):
            (root / 'services/catalog.json').write_text(json.dumps({'services': [dict(
                id='example', title='Example', description='Fixture', url='https://example.com',
                launched=False, publicationApproved=True)]}))
        with self.assertRaises(ValueError):
            self.run_fixture(inject)


if __name__ == '__main__':
    unittest.main()
