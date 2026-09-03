import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

function esc(s: string) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() || 'https://dropkit-contents.pages.dev').replace(/\/$/, '');
  const posts = (await getCollection('posts', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
  );
  const items = posts.map((p) => {
    const link = `${base}/posts/${p.id}/`;
    const desc = esc(p.data.description || p.data.title);
    return `<item><title>${esc(p.data.title)}</title><link>${link}</link><guid>${link}</guid><pubDate>${p.data.pubDate.toUTCString()}</pubDate><description>${desc}</description></item>`;
  }).join('');
  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>dropkit.contents</title><link>${base}/</link><description>Public contents ledger</description>${items}</channel></rss>`;
  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
};
