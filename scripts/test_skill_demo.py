import importlib.util
from pathlib import Path
import tempfile
import unittest
import sys

sys.dont_write_bytecode = True

spec = importlib.util.spec_from_file_location('demo', Path(__file__).resolve().parents[1] / 'skills/nightly-rpa/scripts/demo.py')
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)


class DemoTests(unittest.TestCase):
    def test_dry_run_creates_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'out'
            self.assertTrue(demo.run(output, True)['dry_run'])
            self.assertFalse(output.exists())

    def test_repeat_verifies_existing_outputs_and_preserves_receipts(self):
        with tempfile.TemporaryDirectory() as folder:
            first = demo.run(folder)
            second = demo.run(folder)
            self.assertEqual((first['completed'], first['failed']), (2, 1))
            self.assertEqual((second['skipped'], second['failed']), (2, 1))
            self.assertEqual(len(list(Path(folder).glob('summary-*.json'))), 2)

    def test_conflict_is_reported_without_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'sample-a.txt'
            target.write_text('Existing original')
            result = demo.run(folder)
            self.assertEqual(result['failed'], 2)
            self.assertEqual(target.read_text(), 'Existing original')

    def test_symlink_destination_is_not_followed(self):
        with tempfile.TemporaryDirectory() as folder:
            outside = Path(folder) / 'original'
            outside.write_text('Existing original')
            (Path(folder) / 'sample-a.txt').symlink_to(outside)
            self.assertEqual(demo.run(folder)['failed'], 2)
            self.assertEqual(outside.read_text(), 'Existing original')


if __name__ == '__main__':
    unittest.main()
