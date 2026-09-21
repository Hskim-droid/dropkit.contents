# dropkit.contents

AI work notes by **Hosang Kim**. I use Codex to build tools for everyday work; Codex handles the coding.

- [Public projects](https://dropkit-contents.pages.dev/work/)
- [About and working approach](https://dropkit-contents.pages.dev/about/)
- [LinkedIn](https://www.linkedin.com/in/hosang-kim-a0b5a0370/)
- [GitHub profile](https://github.com/Hskim-droid)

## What this repository contains

This public repository is the site and content hub. It also keeps one experimental
software project, [`agent-harness`](agent-harness/README.md), so the implementation
history and the public project page can be reviewed together.

| If you want to… | Start here |
| --- | --- |
| Browse the published work and project introductions | [dropkit-contents.pages.dev](https://dropkit-contents.pages.dev/work/) |
| Run or inspect the local UI-to-document proof | [`agent-harness/README.md`](agent-harness/README.md) |
| Read the RPA and computer-use reference lineage | [`agent-harness/RPA_REFERENCE_LINEAGE.md`](agent-harness/RPA_REFERENCE_LINEAGE.md) |

`agent-harness` is experimental and fixture-based. Its current proof is
read/search/draft-first: synthetic UI data can be observed, optionally translated
through a loopback-only adapter, and rendered as one DOCX, XLSX, or PPTX. The
public code does not connect to a real ERP/QMS, mail sender, scheduler, browser
profile, credential, or customer dataset. Real-host permissions, production
authentication, mail delivery, and unattended write actions remain unverified.

The harness is kept here for provenance while its public boundary is being tested;
it should not be read as a production RPA product or as permission to automate a
system merely by cloning this repository.

The home page introduces the person and public projects. External-source summaries remain in the [reading archive](https://dropkit-contents.pages.dev/reading/), with existing post URLs preserved. Repeated AI judgments in older entries are not independent fact verification.

## Site structure

Public contents ledger. GitHub is the source. Cloudflare Pages is the hub. Other platforms are branches.

```
persona/               voice, philosophy (not published as posts)
src/content/posts/     what the hub lists
drops/                 same files, ledger copy
social/                short copies for X etc.
media/                 small images (video stays off git)
```

Factory staging and health-fails live in `content-hub`, not here.

Hub: https://dropkit-contents.pages.dev/

Lanes: **deep** (systems) · **scoreboard** (tables). Lab Notes is a writing voice, not the repo name.

```bash
npm install && npm run dev
```

To run the harness unit tests without the optional browser and Office fixture
dependencies:

```bash
python3 -m unittest discover -s agent-harness/tests -p 'test_*.py'
```

## Public repository policies

- [Contributing](CONTRIBUTING.md) explains the site/harness boundary and local checks.
- [Security policy](SECURITY.md) explains what must never enter a public issue or fixture.
- The repository does not yet declare a single code/content license; public visibility is not reuse permission.

## Publication language

Public pages, project introductions, and new content are written in English for a global audience. Original-language source material and historical filenames are preserved. New articles remain subject to evidence and editorial review.
