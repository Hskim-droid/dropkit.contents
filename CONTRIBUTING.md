# Contributing

Thank you for helping improve this public skills, services, and notes hub.

## Scope

- Site and content changes belong in the Astro source and publication folders.
- Kit changes belong in the private `dropkits` repository.
- Reviewed general-purpose skill sources belong here only after ownership,
  licensing and publication approval. See skills/README.md.
- Service introductions are added after launch; service implementation stays private.
- Keep fixtures synthetic. Do not add real ERP/QMS records, URLs, credentials,
  cookies, screenshots, mail addresses, or customer data.
- Do not add a live sender, unattended write action, or cloud fallback as a
  fixture convenience.

## Before opening a pull request

Run the checks relevant to the files you changed:

```bash
npm ci
python3 scripts/test_public_catalog.py
python3 scripts/test_import.py
npm run build
git diff --check
```

The kits have their own tests and CI in the dropkits repository.
The public site build remains runnable without service credentials.

Describe the behavior change, the test command, and any host-specific or
unverified limitation in the pull request. Never attach sensitive source files
to an issue or pull request.

## Licensing

Software source is covered by [`LICENSE`](LICENSE). Original writing, persona
files, social copy, and media are covered by [`CONTENT_LICENSE.md`](CONTENT_LICENSE.md)
unless a file states otherwise.
