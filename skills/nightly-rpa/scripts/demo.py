"""Offline synthetic transfer demonstration. No network or production connector."""
import argparse
import hashlib
import json
from pathlib import Path
import uuid

FIXTURES = {'sample-a.txt': b'Synthetic sample A\n',
            'sample-b.csv': b'id,value\nexample,42\n', 'empty.txt': b''}


def run(output, dry_run=False):
    output = Path(output)
    if dry_run:
        return {'dry_run': True, 'planned': list(FIXTURES)}
    if output.is_symlink():
        raise ValueError('Output cannot use symlinks')
    # Canonicalize platform aliases such as the macOS temporary directory.
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest = []
    counts = {'completed': 0, 'failed': 0, 'skipped': 0}
    for name, content in FIXTURES.items():
        target = output / name
        digest = hashlib.sha256(content).hexdigest()
        item = {'id': name, 'source_sha256': digest}
        if not content:
            state, reason = 'failed', 'empty synthetic file'
        elif target.is_symlink():
            state, reason = 'failed', 'symlink destination'
        elif target.exists():
            if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == digest:
                state, reason = 'skipped', 'existing output verified'
            else:
                state, reason = 'failed', 'destination conflict; existing content preserved'
        else:
            with target.open('xb') as stream:
                stream.write(content)
            if hashlib.sha256(target.read_bytes()).hexdigest() == digest:
                state, reason = 'completed', 'output hash verified'
            else:
                state, reason = 'failed', 'verification failed'
        counts[state] += 1
        item.update(state=state, reason=reason)
        manifest.append(item)
    report = {'run_id': str(uuid.uuid4()), **counts, 'items': manifest}
    # Unique receipts preserve previous runs and avoid overwriting existing files.
    for prefix, data in [('manifest', manifest), ('summary', report)]:
        path = output / f'{prefix}-{report["run_id"]}.json'
        with path.open('x') as stream:
            json.dump(data, stream, indent=2)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.dry_run), indent=2))
