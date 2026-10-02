---
title: "Nightly RPA: a first reusable skill"
description: "Instructions for repeatable automation, with an offline Python example that verifies outputs and preserves run receipts."
pubDate: 2026-10-02
approved: true
draft: false
---

The first skill in this hub is [Nightly RPA](/skills/nightly-rpa/). It helps an AI assistant turn an explicitly authorized recurring task into a repeatable job with a manifest, verification, and a readable report.

The package includes a small offline Python example. A dry run creates no output. A real demonstration copies two synthetic files and reports one empty-file failure. Running it again verifies and skips the completed files. Existing conflicting content is preserved and reported.

This is a skill and demonstration, not a production connector. A live job still needs the system's access method, bounded retries, concurrency control, and an authorized schedule. The example requires Python 3.10 or later and uses no network or credentials.

[Read the skill and download the MIT-licensed package →](/skills/nightly-rpa/)
