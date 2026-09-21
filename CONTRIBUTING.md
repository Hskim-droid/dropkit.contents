# Contributing

Thank you for helping improve this public research and prototype repository.

## Scope

- Site and content changes belong in the Astro source and publication folders.
- Harness changes belong under `agent-harness/` and must preserve the
  read/search/draft-first boundary.
- Keep fixtures synthetic. Do not add real ERP/QMS records, URLs, credentials,
  cookies, screenshots, mail addresses, or customer data.
- Do not add a live sender, unattended write action, or cloud fallback as a
  fixture convenience.

## Before opening a pull request

Run the checks relevant to the files you changed:

```bash
npm ci
npm run build
python3 -m unittest discover -s agent-harness/tests -p 'test_*.py'
git diff --check
```

The browser and Office fixture tests require the packages in
`agent-harness/requirements-fixture.txt` and a local Playwright Chromium
install. The public default remains runnable without real service credentials.

Describe the behavior change, the test command, and any host-specific or
unverified limitation in the pull request. Never attach sensitive source files
to an issue or pull request.

## Licensing

The repository's code and publication content do not yet have a single
repository-wide license. Until the maintainer adds an explicit license, do not
assume that public visibility grants permission to copy, redistribute, or build
derivative work from the code or content.
