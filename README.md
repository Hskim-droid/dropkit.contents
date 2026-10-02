# dropkit.contents

The canonical site is https://dropkit-contents.pages.dev/. GitHub Pages forwards
visitors to that same site, avoiding a second copy with conflicting links.

One public hub for reusable AI skills, launched services, and selected notes by
[Hosang Kim](https://github.com/Hskim-droid).

- [Skills](https://dropkit-contents.pages.dev/skills/)
- [Services](https://dropkit-contents.pages.dev/services/)
- [Notes](https://dropkit-contents.pages.dev/notes/)
- [Website](https://dropkit-contents.pages.dev/)

```text
src/                website code and selected, approved notes
skills/             reviewed skill sources and public catalog
services/catalog.json  launched and approved service introductions
```

```bash
npm ci
npm run dev
```

`npm run build` requires Python 3 and validates the catalogs before building.
Published skills get a reading page, a standalone SKILL.md, and a ZIP package.
The first skill, Nightly RPA, includes an offline Python demonstration. There
are no listed services yet; a service is listed only after launch.

Imports require CT_CONTENT_HUB and CT_PRIVATE_STAGING. The latter must be an
absolute owner-only directory outside this checkout. Imports write private
drafts there; the public build rejects any note lacking literal approved: true
and draft: false frontmatter. Never commit an unreviewed candidate to any branch
of this public repository: CI cannot retract a source file already pushed.

Only this repository is public. Service code, private kits, employer-specific
materials, and unpublished candidates stay in private repositories or staging.
See [the publication boundary](docs/REPOSITORY_BOUNDARY.md) and
[skill contribution instructions](skills/README.md).

The old dropkits introduction, AI news archive, and media pages are retired.
They are absent from current site output. Previous public Git history and any
copies already retrieved by others are not erased by this change.
