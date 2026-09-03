---
title: "August 2026 price and performance"
description: "Gemini, Claude, Grok pricing and a one-page scoreboard from public sources."
pubDate: 2026-09-02
draft: false
lane: scoreboard
tags: [scoreboard]
---

## August 2026 price and performance

This public ledger documents recent observations regarding model pricing and performance metrics, gathered from various sources.

### Key Observations

Gemini Deep Research Agent pricing is confirmed. The listed rates are $2 per 1 million input tokens, $0.2 per 1 million cached input tokens, and $12 for output. Web Search Request pricing, for Claude-supported search agents on the same platform, is listed at $10 per 1,000 searches. Grok 4.6 pricing shows tiered rates based on context length. These are $2 per 1 million tokens for input and $6 per 1 million tokens for output for contexts under 200K, and $4 per 1 million tokens for input and $12 per 1 million tokens for output for contexts above 200K.

Grok 4 API pricing appears in a separate August 2026 roundup. The listed rates are $5 per 1 million input tokens and $15 per 1 million output tokens. Grok 4 mini is listed at $0.30 per 1 million input tokens and $0.50 per 1 million output tokens. Gemini 3.1 Pro preview pricing is noted in a later August 2026 cost report. This lists $2 per 1 million input tokens and $12 per 1 million output tokens.

Gemini 3.7 Flash is reported with performance figures. It achieved 340.1 tokens per second and an index score of 56. Qwen3.8-Flash-Next showed the lowest time-to-first-answer-token in provider benchmarks, recorded at 25.44 seconds. Qwen3.8-27B provider benchmarking included DeepInfra timing and score data: $0.31 for an unnamed metric, 47.30 seconds, and a score of 61.51.

Qwen 3.8 Max was launched as a 2.4T Mixture-of-Experts (MoE) model with 95 billion active parameters and a 1 million token context window. Its pricing is given as $2 per 1 million tokens for input and $6 per 1 million tokens for output. Benchmark claims for Qwen 3.8 Max include scores of 93.0 on PaperBench, 67.7 on SWE-bench Pro, and 56.6 on DeepSWE.

DeepSeek V4-Pro-0813 is described as a 1.6T MoE model with API pricing. Off-peak rates are $0.66 per 1 million input tokens and $1.98 per 1 million output tokens. Peak rates are $1.32 per 1 million input tokens and $3.96 per 1 million output tokens. DeepSeek V4-Pro-0813 reportedly achieved 96.40% performance on SWE-bench Verified.

GLM-5.3 was presented as an open-weight coding model with a delayed weight release, approximately two weeks after launch. GLM-5.3 was reported to deliver a 6x gain on Terminal-Bench. Huawei open-sourced openPangu-2.0-Pro as a 505 billion-parameter open-weight model.

Qwen 3.8 and other open models were flagged in a China AI weekly roundup. They were expected by the end of August.

### Data Table

| claim | label | order (🟢 robust / ⚠️ sensitive) | numbers | URL |
|---|---|---|---|---|
| Gemini Deep Research Agent pricing is listed on Google’s agent platform page | 🟢 confirmed | 🟢 robust | $2 / 1M input; $0.2 / 1M cached input; $12 output | https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing |
| Web Search Request pricing on the same page is listed for Claude-supported search agents | 🟢 confirmed | 🟢 robust | $10 / 1,000 searches | https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing |
| Grok 4.6 pricing is listed with tiered rates by context length | 🟢 confirmed | 🟢 robust | $2/$6 under 200K; $4/$12 above 200K | https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing |
| Grok 4 API pricing is listed in a separate August 2026 pricing roundup | 🟢 confirmed | ⚠️ sensitive | $5/$15; Grok 4 mini $0.30/$0.50 | https://www.swfte.com/api-pricing |
| Gemini 3.1 Pro preview pricing is listed in a later August 2026 cost report | 🟡 partial | ⚠️ sensitive | $2 / 1M input; $12 / 1M output | https://cutoffreport.com/posts/cutoff-data-brief-2026-08-07 |
| Gemini 3.7 Flash is reported with strong speed and index scores | 🟡 partial | ⚠️ sensitive | 340.1 tokens/sec; index 56 | https://www.buildfastwithai.com/blogs/ai-news-today-august-22-23-2026 |
| Qwen3.8-Flash-Next had the lowest time-to-first-answer-token in provider benchmarks | 🟡 partial | ⚠️ sensitive | 25.44 s | https://artificialanalysis.ai/models/qwen3-8-flash-next/providers |
| Qwen3.8-27B provider benchmarking showed DeepInfra timing and score data | 🟡 partial | ⚠️ sensitive | $0.31; 47.30 s; 61.51 score | https://artificialanalysis.ai/models/qwen3-8-27b/providers |
| Qwen 3.8 Max was launched as a 2.4T MoE with 95B active parameters and 1M context | 🟡 partial | ⚠️ sensitive | 2.4T; 95B active; 1M context; $2/$6 per 1M tokens | https://www.developersdigest.tech/blog/qwen-3-8-max-release-2026 |
| Qwen 3.8 Max benchmark claims include PaperBench, SWE-bench Pro, and DeepSWE | 🟡 partial | ⚠️ sensitive | 93.0; 67.7; 56.6 | https://www.developersdigest.tech/blog/qwen-3-8-max-release-2026 |
| DeepSeek V4-Pro-0813 is described as a 1.6T MoE model with API pricing | 🟡 partial | ⚠️ sensitive | 1.6T; $0.66/$1.98 off-peak; $1.32/$3.96 peak | https://flowtivity.ai/blog/glm-5-3-vs-deepseek-v4-pro-comparison/ |
| DeepSeek V4-Pro-0813 reportedly reached strong SWE-bench Verified performance | 🟡 partial | ⚠️ sensitive | 96.40% | https://flowtivity.ai/blog/glm-5-3-vs-deepseek-v4-pro-comparison/ |
| GLM-5.3 was presented as an open-weight coding model with delayed weight release | 🟡 partial | ⚠️ sensitive | weights promised ~2 weeks after launch | https://apidog.com/blog/what-is-glm-5-3/ |
| GLM-5.3 was reported to deliver a large Terminal-Bench gain | 🟡 partial | ⚠️ sensitive | 6x Terminal-Bench gain | https://zenn.dev/neotechpark/articles/7003e20300d7e5 |
| Huawei open-sourced openPangu-2.0-Pro as a 505B-parameter open-weight model | 🟡 partial | ⚠️ sensitive | 505B | https://www.opensourceforu.com/2026/08/huawei-open-sources-505b-openpangu-ai-drops-weights-and-code/ |
| Qwen 3.8 and other open models were flagged in a China AI weekly roundup | 🔴 hype | ⚠️ sensitive | expected by end of August | https://www.bighatgroup.com/blog/china-ai-weekly-2026-08-01/ |

### Practitioner Lines

*   **Act:** Review the confirmed agent pricing structures for Gemini and Claude-supported search agents to optimize operational costs for confirmed use cases.
*   **Watch:** Monitor the actual release and performance metrics of Grok 4 API and Gemini 3.1 Pro once their sensitive pricing and performance data are fully confirmed and made robust.
*   **Ignore:** Dismiss the general expectation of "Qwen 3.8 and other open models" by a specific date, as it lacks precise detail and is categorized as hype.

---
