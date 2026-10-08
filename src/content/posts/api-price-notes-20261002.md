---
title: "API price notes: Claude Opus 5.5, Gemini 3.8 Flash, and Grok 4.7"
description: "Provider-published API token prices checked on October 2, 2026, with an arithmetic cost illustration and limits on comparisons of total application cost."
pubDate: 2026-10-02
draft: false
approved: true
tags: ["AI", "API pricing", "Claude", "Gemini", "Grok"]
---

Checked on October 2, 2026. These are provider-published token prices, not a performance ranking or an estimate of total application cost.

| Model and provider API | Input / million tokens | Output / million tokens | Pricing scope |
| --- | --- | --- | --- |
| Claude Opus 5.5 — Claude API | $4 | $20 | Standard token rates |
| Gemini 3.8 Flash — Gemini Developer API | $0.75 | $3.75 | Standard paid tier through December 31, 2026; output includes thinking tokens |
| Grok 4.7 — Grok API | Starting at $2 | Starting at $6 | Published starting rates |

[Anthropic's pricing documentation](https://platform.claude.com/docs/en/about-claude/pricing) lists the Claude rates and separate prompt-cache charges. [Google's pricing page](https://ai.google.dev/gemini-api/docs/pricing) lists Gemini's temporary rates and an increase to $1.50 input and $7.50 output from January 1, 2027. The [Grok 4.7 announcement](https://x.ai/news/grok-4-7) also describes a fast variant with twice the output speed at twice the price; that is the provider's statement, not my measurement.

For a simple arithmetic illustration, one million uncached input tokens plus 100,000 billed output tokens would cost $6 for Claude, $1.125 for Gemini at the temporary rates, and $2.60 for Grok at its starting rates. This illustration assumes the listed token rates apply and excludes tools, caching, storage, and other charges. It does not imply that each model uses the same number of tokens to complete a task.

My next comparison would use the same representative tasks and record accepted outputs, retries, latency, and billed usage. The table provides a starting point for budgeting; it does not establish which model delivers the best result.
