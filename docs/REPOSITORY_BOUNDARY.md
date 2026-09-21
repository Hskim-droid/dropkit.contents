# Public repository boundary

The public project is intentionally kept to two repositories with different jobs:

| Repository | Responsibility | Start here |
| --- | --- | --- |
| [`dropkit.contents`](https://github.com/Hskim-droid/dropkit.contents) | Publication shell, project introductions, public writing, and document content | [README](../README.md) |
| [`local-llm`](https://github.com/Hskim-droid/local-llm) | Local model engine, document packs, and the integrated `agent-harness/` UI-to-document code lane | [README](https://github.com/Hskim-droid/local-llm#readme) · [harness](https://github.com/Hskim-droid/local-llm/tree/main/agent-harness) |

The UI-to-document harness and the local translation/document engine were merged
into `local-llm` on 2026-09-21. The former standalone public repository is no
longer the canonical code location. This content hub keeps only publication
infrastructure and public material; application code belongs in `local-llm`.

Neither public repository contains a real ERP/QMS connector, browser cookie,
mail credential, customer dataset, or unattended production sender.
