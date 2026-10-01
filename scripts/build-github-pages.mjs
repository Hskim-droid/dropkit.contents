import { mkdir, writeFile } from 'node:fs/promises';

// GitHub Pages is an entry point to the single canonical Cloudflare site.
const url = 'https://dropkit-contents.pages.dev/';
const html = `<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0;url=${url}">
<link rel="canonical" href="${url}"><title>dropkit</title>
<body><p>This site has one home: <a href="${url}">dropkit — skills, services and notes</a>.</p></body></html>`;
await mkdir('dist-github-pages', { recursive: true });
for (const name of ['index.html', '404.html']) {
  await writeFile(`dist-github-pages/${name}`, html);
}
