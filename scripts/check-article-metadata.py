"""Project conventions for approved English article metadata, not ranking rules."""
import json
from pathlib import Path
import re


def metadata(path):
    text = path.read_text()
    if not text.startswith('---\n'):
        raise ValueError('missing_frontmatter:' + path.name)
    header = text[4:].split('\n---\n', 1)[0]
    fields = {}
    for name in ('title', 'description'):
        matches = re.findall(r'^' + name + r': (.+)$', header, re.M)
        if len(matches) != 1:
            raise ValueError('missing_or_duplicate_' + name + ':' + path.name)
        fields[name] = json.loads(matches[0])
    date = re.findall(r'^pubDate: (\d{4}-\d{2}-\d{2})$', header, re.M)
    if len(date) != 1:
        raise ValueError('missing_date:' + path.name)
    fields['date'] = date[0]
    description = fields['description']
    if not isinstance(description, str) or description != description.strip() or not 40 <= len(description) <= 320:
        raise ValueError('description_40_to_320_local_convention:' + path.name)
    if re.search(r'[<>\r\n\[\]]|https?://|/Users/|/home/|hanlim|[\u1100-\u11ff\u3130-\u318f\uac00-\ud7a3\u3040-\u30ff\u3400-\u9fff]', description, re.I):
        raise ValueError('unsafe_or_non_english_description:' + path.name)
    if description.casefold() == fields['title'].casefold() or description in {
        'Imported from content-hub',
        'Reusable AI skills, launched services, and practical notes by Hosang Kim.',
    }:
        raise ValueError('generic_description:' + path.name)
    return fields


def check(root):
    seen = set()
    paths = sorted((root / 'src/content/posts').glob('*.md'))
    for path in paths:
        value = metadata(path)
        key = value['description'].casefold()
        if key in seen:
            raise ValueError('duplicate_article_description:' + path.name)
        seen.add(key)
    return len(paths)


if __name__ == '__main__':
    print(json.dumps({'article_metadata_checked': check(Path(__file__).resolve().parents[1]),
                      'indexing_or_ranking_verified': False}))
