import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() || 'https://dropkit-contents.pages.dev').replace(/\/$/, '');
  const posts = (await getCollection('posts', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
  );
  const body = {
    title: 'dropkit.contents',
    home: `${base}/`,
    items: posts.map((p) => ({
      id: p.id,
      title: p.data.title,
      lane: p.data.lane,
      date: p.data.pubDate.toISOString().slice(0, 10),
      url: `${base}/posts/${p.id}/`,
      description: p.data.description || '',
    })),
  };
  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
