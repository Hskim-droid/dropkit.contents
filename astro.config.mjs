import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://dropkit-contents.pages.dev',
  base: '/',
  markdown: {
    shikiConfig: { theme: 'github-dark' },
  },
});
