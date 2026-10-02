# Codex work rules for dropkit.contents

This is the only public repository: a website and sharing hub for reviewed,
general-purpose AI skills, launched services, and selected notes. Private kit
and service implementation stays outside this repository.

When Codex starts work here:

1. Keep edits within the site, public writing, content ledger, or publication
   configuration unless the user explicitly asks for a repository-level change.
2. Run `npm ci`, `npm run build`, and `git diff --check` for site or content
   changes.
3. Keep examples synthetic. Never add credentials, cookies, screenshots with
   business data, ERP/QMS records, mail addresses, or local runtime state.
4. Do not add executable ERP/QMS connectors, mail senders, unattended writes, or
   cloud model fallbacks to this content repository.
5. Only explicitly approved skill sources belong in skills/. Unpublished
   candidates stay in private staging. Do not assume that removing company
   names establishes ownership or permission to publish.
6. Services are listed only after launch and publication approval. Imports go to
   private staging outside this checkout. Only reviewed notes with approved:
   true and draft: false belong in public sources, including PR branches.
7. Run python3 scripts/test_public_catalog.py and python3 scripts/test_import.py.
   Retired archives must not reappear in generated routes, feeds or assets.
