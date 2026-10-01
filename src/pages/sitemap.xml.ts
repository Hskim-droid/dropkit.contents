import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { skills } from '../lib/catalog';

export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() || 'https://dropkit-contents.pages.dev').replace(/\/$/, '');
  const posts = await getCollection('posts', ({ data }) => !data.draft && data.approved);
  const extra = ['/', '/about/', '/skills/', '/services/', '/notes/'];
  const urls = [
    ...extra.map((p) => `${base}${p}`),
    ...posts.map((p) => `${base}/posts/${p.id}/`),
    ...skills.map((skill) => `${base}/skills/${skill.id}/`),
  ];
  const body = `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls.map((u) => `<url><loc>${u}</loc></url>`).join('')}</urlset>`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
