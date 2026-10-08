"""Inspect the actual static build, including feed and JSON-LD propagation."""
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location('metadata', Path(__file__).with_name('check-article-metadata.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta, self.canonical, self.schemas, self.visible = {}, [], [], []
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'meta':
            key = values.get('name') or values.get('property')
            self.meta[key] = values.get('content')
        if tag == 'link' and values.get('rel') == 'canonical':
            self.canonical.append(values.get('href'))
        if tag == 'script' and values.get('type') == 'application/ld+json':
            self.in_schema = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_schema = False

    def handle_data(self, value):
        if self.in_schema:
            self.schemas.append(json.loads(value))
        else:
            self.visible.append(value)


def check(root):
    base = 'https://dropkit-contents.pages.dev'
    feed = json.loads((root / 'dist/feed.json').read_text())
    rss = ET.parse(root / 'dist/rss.xml')
    count = 0
    for path in sorted((root / 'src/content/posts').glob('*.md')):
        fields = module.metadata(path)
        url = base + '/posts/' + path.stem + '/'
        page = Head()
        page.feed((root / 'dist/posts' / path.stem / 'index.html').read_text())
        assert page.meta['description'] == page.meta['og:description'] == fields['description'], path.name
        assert page.meta['og:type'] == 'article' and page.canonical == [url], path.name
        assert len(page.schemas) == 1, path.name
        schema = page.schemas[0]
        assert schema['@type'] == 'BlogPosting' and schema['headline'] == fields['title'], path.name
        assert schema['description'] == fields['description'] and schema['url'] == schema['mainEntityOfPage'] == url, path.name
        assert schema['datePublished'] == fields['date'] and 'dateModified' not in schema, path.name
        assert schema['author']['name'] == 'Hosang Kim' and schema['inLanguage'] == 'en', path.name
        assert schema['author']['name'] in ''.join(page.visible) and fields['date'] in ''.join(page.visible), path.name
        item = next(item for item in feed['items'] if item['url'] == url)
        assert item['description'] == fields['description'], path.name
        rss_item = next(item for item in rss.findall('./channel/item') if item.findtext('link') == url)
        assert rss_item.findtext('description') == fields['description'], path.name
        count += 1
    return count


if __name__ == '__main__':
    print(json.dumps({'rendered_articles_checked': check(Path(__file__).resolve().parents[1]),
                      'live_indexing_or_traffic_verified': False}))
