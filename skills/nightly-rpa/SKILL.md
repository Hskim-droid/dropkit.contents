---
name: nightly-rpa
description: Turn an explicitly authorized recurring download or file-transfer task into a repeatable script with a manifest, verification, bounded retries, and a readable run report. Use when a user asks to automate repeated work or schedule an existing job.
---

## Nightly RPA

Build a job that can run repeatedly and report what happened. This is an instruction package for an AI assistant, with an offline demonstration; it is not a ready-made connector to a production system.

### Define the job

Establish the source, destination, permitted actions, schedule, expected volume, and who handles exceptions. Use the user's existing authorization; ask only for missing decisions that change access, writes, cost, or recipients. Do not infer permission to submit records, send messages, or use a different system from permission to download.

Prefer an official API or export feature. When browser interaction is necessary, use the capabilities and constraints supported by the current environment. Record stable selectors and explicit failure signals; avoid coordinates for recurring automation. Never bypass access controls or authentication challenges.

### Make execution repeatable

- Separate credentials and runtime data from the published code. Use the platform's secret storage or process environment; redact credentials and sensitive content from reports.
- Record item IDs, source version or hash, destination, state, and an operation receipt in a manifest. Mark completion only after verifying the result. For writes, use a supported idempotency key or reconcile the destination before retrying an uncertain result.
- Provide dry-run and limited-run modes. Verify downloaded content against the expected format and source: an HTML login page is not a successful document download.
- Retry transient failures with bounded backoff. Stop on expired access, permission errors, or an uncertain external write; report the action needed. Keep business-sensitive details out of AI prompts unless their use is authorized.
- Test re-running completed work, interrupted transfers, changed input, and failed verification with synthetic fixtures before the authorized limited live run.

### Schedule and operate

After the limited run succeeds, use the target platform's scheduler. Verify the runtime path, credentials, working directory, timezone, and whether the device can execute while locked or asleep. Prevent overlapping runs. Give the user the schedule, log location, how to disable the job, and which steps still require a person.

Report completed, failed, skipped, and uncertain items with a run ID. Send the report only to an authorized destination. Diagnose failures from minimal logs first; make a targeted correction and repeat the relevant synthetic test before resuming.

### Try the offline demonstration

Requires Python 3.10 or later. Save this folder in your assistant's supported skill directory to use the instructions; installation conventions vary by assistant. The standalone example works without any AI product, account, network, credentials, or scheduler.

From this folder, run:

```bash
python3 scripts/demo.py --output /tmp/nightly-rpa-example --dry-run
python3 scripts/demo.py --output /tmp/nightly-rpa-example
python3 scripts/demo.py --output /tmp/nightly-rpa-example
```

The first command creates no output. The second copies two embedded synthetic files and reports one empty-file failure. The third verifies and skips the two completed files. The summary and manifest are in the output folder. Choose a fresh output folder; unexpected existing content is preserved and reported as a conflict.

The example demonstrates local manifests and verification only. It does not implement production downloads, external writes, retries, locking, or scheduling. Those depend on the authorized system and must be implemented and tested for the real job.
