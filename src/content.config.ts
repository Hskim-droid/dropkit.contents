import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string().trim().min(40).max(320),
    pubDate: z.coerce.date(),
    draft: z.boolean().default(false),
    approved: z.boolean().default(false),
    lane: z.enum(['deep', 'scoreboard', 'writing']).default('writing'),
    tags: z.array(z.string()).default([]),
  }),
});

const skills = defineCollection({
  loader: glob({ pattern: '*/SKILL.md', base: './skills', generateId: ({ entry }) => entry.split('/')[0] }),
  schema: z.object({ name: z.string(), description: z.string() }),
});
export const collections = { posts, skills };
