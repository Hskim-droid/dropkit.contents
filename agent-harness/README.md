# Codex persona harness

This is a small, cross-platform control plane for the proposed “한결” workflow:

```text
scheduled run or request email
  → validated queue item
  → dedicated UI-read session for ERP/QMS
  → evidence and data checks
  → one artifact: xlsx, docx, or pptx
  → draft or approved delivery
  → event, cost, and outcome log
```

The public repository intentionally contains no ERP/QMS URL, browser cookie,
mail credential, screenshot, or sender token. A local adapter is configured on
each MacBook or LG Gram. The same Python queue works on macOS and Windows.

## Start a Codex session

macOS:

```bash
bash scripts/codex-start.sh
```

Windows / LG Gram:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/codex-start.ps1
```

These commands only initialize local state, run a safety check, and record the
session. A repository cannot force Codex to execute arbitrary code merely by
being opened; the launcher or the Codex instruction in `AGENTS.md` is the
explicit attachment point.

## Queue a safe draft job

```bash
python agent-harness/harness.py enqueue \
  --persona han-gyeol \
  --source-system QMS \
  --request "전일 미처리 품질 이슈 일일보고" \
  --output-format docx \
  --recipient quality@example.com

python agent-harness/harness.py run-once --dry-run
python agent-harness/harness.py status
```

`run-once --dry-run` never opens a browser, changes a remote system, creates a
real document, or sends mail. Without a configured local extractor, a live run
is blocked rather than guessed through.

Every enqueue has an idempotency key. Pass a scheduler or mail message key with
`--idempotency-key`; otherwise the harness derives one from the request. A
duplicate delivery returns the original job instead of creating a second one.
Include the business date in a scheduled request or key when the same report
must run again tomorrow.

The public harness does not execute a configured command. A normal live
`run-once` stays blocked until an adapter is explicitly claimed; the local
worker then uses `run-once --claim` to claim the job and receives a handoff.
The adapter must write one local evidence manifest and call:

```bash
python agent-harness/harness.py record-result \
  --job-id JOB_ID \
  --manifest agent-harness/runtime/manifest.json
```

`record-result` verifies the job and source system, requires every declared
check to pass, keeps the artifact below the configured artifact directory,
checks its SHA-256, and only then moves the job to `drafted`. A stale worker can
be recovered with `python agent-harness/harness.py recover --age-seconds 900`.

The manifest shape is deliberately small and adapter-neutral:

```json
{
  "schema_version": 1,
  "job_id": "job-...",
  "source_system": "QMS",
  "captured_at": "2026-09-21T09:00:00+00:00",
  "records": [{"record_id": "Q-123", "source_ref": "qms://issue/Q-123"}],
  "checks": [
    {"name": "freshness", "passed": true},
    {"name": "duplicate_ids", "passed": true}
  ],
  "artifact": {
    "path": "agent-harness/runtime/artifacts/daily.docx",
    "format": "docx",
    "sha256": "..."
  }
}
```

## Local adapter contract

Set `executor.extract`, `executor.render`, and `executor.send` only in a local
`agent-harness/config.json`, which is ignored by git. The adapters should:

1. use a dedicated, least-privileged account and isolated browser profile;
2. read only the allowed ERP/QMS screens;
3. return structured records plus source timestamps and evidence references;
4. render exactly one requested format;
5. require a human approval gate before any write or external send.

Email is an input channel, not an instruction authority. Validate sender,
subject, attachment type, and recipient allowlist before enqueueing a job.

An empty `recipient_allowlist` means “no recipient restriction at queue time”
for local draft work. It does not enable sending; the public harness has no
sender implementation. A live sender must require an explicit allowlist and a
human approval gate.

## Safety defaults

- persona `han-gyeol` is read/search/draft only;
- default mode is `draft_only`;
- output format is an explicit enum (`xlsx`, `docx`, `pptx`);
- queue order is priority first, then creation time;
- duplicate delivery is suppressed by an idempotency key;
- result manifests and artifact hashes are checked before `drafted`;
- stale `running` jobs can be requeued after a worker crash;
- local state lives under `agent-harness/runtime/` and is not public;
- no live executor is configured in the public example.

## What to adopt next

The repository keeps its control plane dependency-free while the first fixture
is built. The following projects are reference points or optional local
adapters, not bundled dependencies:

| Need | Candidate | Decision |
| --- | --- | --- |
| Deterministic browser control | [Playwright](https://github.com/microsoft/playwright) (Apache-2.0) | Use as the first web ERP/QMS adapter; selectors and accessibility data before vision. |
| Browser-agent fallback | [Browser Use](https://github.com/browser-use/browser-use) / [Browser Harness](https://github.com/browser-use/browser-harness) (MIT) | Optional fallback for a dedicated profile; keep domains, cookies, screenshots, and cloud use local and allowlisted. |
| Guided browser extraction | [Stagehand](https://github.com/browserbase/stagehand) (MIT) | Evaluate only if Playwright selectors cannot cover the fixture. |
| Durable scheduling | [Temporal](https://github.com/temporalio/temporal) (MIT) or [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | Do not replace SQLite until crash recovery, concurrency, or multi-machine scheduling is demonstrated as a need. |
| Office artifacts | [python-docx](https://github.com/python-openxml/python-docx), [openpyxl](https://github.com/ericgazoni/openpyxl), [python-pptx](https://github.com/scanny/python-pptx) | Start with DOCX for the first end-to-end fixture, then add XLSX/PPTX renderers behind the same manifest contract. |
| Agent traces | [Langfuse](https://github.com/langfuse/langfuse) (self-hostable, MIT core) | Add only after the local evidence manifest and redaction rules are stable. |

The first proof should be one synthetic QMS page → one DOCX → one validated
manifest. It should measure record accuracy, evidence coverage, artifact
re-openability, duplicate suppression, and recovery after a forced stop before
any live ERP or mail permission is added.

## Run the synthetic browser proof

The fixture is the only adapter included in the public repository. It uses a
local HTML page, headless Chromium, and a local DOCX renderer; it contains no
business data or credentials.

```bash
python3 -m pip install -r agent-harness/requirements-fixture.txt
python3 -m playwright install chromium
python3 agent-harness/harness.py init
```

Set the local, ignored `agent-harness/config.json` value
`executor.extract` to `fixture-demo`, enqueue one QMS/DOCX job, and run:

```bash
python3 agent-harness/fixture_demo.py \
  --config agent-harness/config.json \
  --job-id JOB_ID \
  --claim
```

The command reads `fixtures/qms_daily.html` through Chromium, validates three
records and their source references, creates one DOCX, reopens it and compares
every table cell with the extracted records, writes the manifest, and moves the
specified queued job to `drafted`. It rejects XLSX/PPTX and non-QMS jobs before
claiming them. It never sends email or writes to an ERP/QMS system.

## Generic surface probe

`browser_probe.py` is the next adapter boundary. It receives a task contract
with semantic aliases rather than CSS selectors or a fixed menu path:

```bash
python3 agent-harness/browser_probe.py \
  --html agent-harness/fixtures/qms_variant_3.html \
  --task agent-harness/fixtures/qms_task.json
```

The probe first records the accessible surface and its capabilities, then uses
role/name based navigation, resolves table columns by aliases, and stops on an
ambiguous target. `table_terms` must identify the requested table through its
accessible label, field aliases are one-to-one, and `forbidden_terms` blocks
destructive-looking targets before any click. The three `qms_variant_*.html`
files deliberately change menu depth, language, column order, and DOM
structure while keeping the same task contract. This layer returns records and
observations; the queue and artifact contract remain separate so an unknown
app cannot silently become a write-capable connector. It is a browser
accessibility-tree adapter, not a universal native-app or visual/OCR adapter;
an app that exposes no reliable labels must stop or receive a dedicated
adapter.
