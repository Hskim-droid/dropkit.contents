# Contributing

Thank you for helping improve this public research and prototype repository.

## Scope

- Site and content changes belong in the Astro source and publication folders.
- Harness changes belong in
  [`local-llm/agent-harness`](https://github.com/Hskim-droid/local-llm/tree/main/agent-harness)
  and must preserve its read/search/draft-first boundary.
- Keep fixtures synthetic. Do not add real ERP/QMS records, URLs, credentials,
  cookies, screenshots, mail addresses, or customer data.
- Do not add a live sender, unattended write action, or cloud fallback as a
  fixture convenience.

## Before opening a pull request

Run the checks relevant to the files you changed:

```bash
npm ci
npm run build
git diff --check
```

The harness has its own fixture requirements and CI in the code repository.
The public site build remains runnable without service credentials.

Describe the behavior change, the test command, and any host-specific or
unverified limitation in the pull request. Never attach sensitive source files
to an issue or pull request.

## Licensing

Software source is covered by [`LICENSE`](LICENSE). Original writing, persona
files, social copy, and media are covered by [`CONTENT_LICENSE.md`](CONTENT_LICENSE.md)
unless a file states otherwise.
