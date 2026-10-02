"""Validate public catalog entries and package only explicitly reviewed files."""
import json
from pathlib import Path
import re
import zipfile
from urllib.parse import urlparse


def build(root):
    root = Path(root).resolve()
    # Public Git sources are readable even if an HTML route is hidden.
    notes = root / 'src/content/posts'
    for note in notes.rglob('*.md') if notes.exists() else []:
        if note.is_symlink() or any(p.is_symlink() for p in note.parents):
            raise ValueError('Public notes cannot be symlinks')
        text = note.read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError('Public note requires frontmatter')
        header = text[4:].split('\n---\n', 1)[0]
        for field, required in [('approved', 'true'), ('draft', 'false')]:
            values = re.findall(r'^' + field + r':\s*(.*?)\s*$', header, re.M)
            if values != [required]:
                raise ValueError('Unapproved notes must remain in private staging')
    entries = json.loads((root / 'skills/catalog.json').read_text())['skills']
    ids = set()
    planned = []
    for entry in entries:
        sid = entry['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', sid) or sid in ids:
            raise ValueError('Invalid or duplicate skill ID')
        ids.add(sid)
        for flag in ('ownershipConfirmed', 'generalizationReviewed', 'syntheticExamplesOnly', 'publicationApproved'):
            if entry.get(flag) is not True:
                raise ValueError(f'{sid}: {flag} must be explicitly confirmed')
        if entry.get('companyDerived') is not False:
            raise ValueError(f'{sid}: employer-derived material requires separate handling')
        if not all(isinstance(entry.get(key), str) and entry[key].strip() for key in ('title', 'description', 'license', 'provenance')):
            raise ValueError(f'{sid}: title, description, license and provenance required')
        files = entry.get('files', [])
        if len(files) != len(set(files)) or not {'SKILL.md', 'LICENSE'}.issubset(files):
            raise ValueError(f'{sid}: unique files, SKILL.md and LICENSE required')
        folder = root / 'skills' / sid
        if folder.is_symlink():
            raise ValueError(f'{sid}: symlink skill folder')
        actual = {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
        if actual != set(files):
            raise ValueError(f'{sid}: all source files must be individually declared')
        for name in files:
            relative = Path(name)
            if relative.is_absolute() or '..' in relative.parts or any(part.startswith('.') for part in relative.parts):
                raise ValueError(f'{sid}: unsafe file path')
            source = folder / relative
            if any(p.is_symlink() for p in (source, *source.parents)) or not source.is_file():
                raise ValueError(f'{sid}: symlink or missing file')
            if source.suffix.lower() in ('.md', '.txt', '.json', '.py', '.sh'):
                text = source.read_text()
                if re.search(r'한림|hanlim|/Users/|/home/', text, re.I):
                    raise ValueError(f'{sid}: company-specific or local-host text requires generalization')
        planned.append((entry, folder))
    folders = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if folders != ids:
        raise ValueError('Unlisted skill sources must remain in private staging')
    services = json.loads((root / 'services/catalog.json').read_text())['services']
    service_ids = set()
    for service in services:
        sid = service.get('id', '')
        url = urlparse(service.get('url', ''))
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', sid) or sid in service_ids:
            raise ValueError('Invalid or duplicate service ID')
        service_ids.add(sid)
        if service.get('launched') is not True or service.get('publicationApproved') is not True:
            raise ValueError('Service must be launched and explicitly approved')
        if url.scheme != 'https' or not url.hostname or url.hostname in ('localhost', '127.0.0.1'):
            raise ValueError('Service requires a public HTTPS URL')
        if not service.get('title') or not service.get('description'):
            raise ValueError('Service title and description required')
    output = root / 'public/skills'
    if any(p.is_symlink() for p in (output, *output.parents)):
        raise ValueError('Public download output cannot use symlinks')
    allowed = {f'{sid}{ext}' for sid in ids for ext in ('.zip', '.md')}
    if output.exists() and any(p.is_symlink() or not p.is_file() or p.name not in allowed for p in output.iterdir()):
        raise ValueError('Unlisted public download found; retire it before building')
    output.mkdir(parents=True, exist_ok=True)
    for entry, folder in planned:
        sid = entry['id']
        (output / f'{sid}.md').write_bytes((folder / 'SKILL.md').read_bytes())
        with zipfile.ZipFile(output / f'{sid}.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(entry['files']):
                archive.write(folder / name, f'{sid}/{name}')
    return len(planned), len(services)


if __name__ == '__main__':
    skills, services = build(Path(__file__).resolve().parents[1])
    print(f'Public catalog validated: {skills} skills, {services} launched services')
