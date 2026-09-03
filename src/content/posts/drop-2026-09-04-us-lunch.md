---
title: "drop-2026-09-04-us-lunch"
description: "This briefing summarizes recent developments in AI models, focusing on pricing, performance, and key features as reported in the field. The information is drawn directly from the p"
pubDate: 2026-09-04
draft: false
lane: scoreboard
tags: [scoreboard]
---


### August 2026 AI Model Release and Benchmark Overview

This briefing summarizes recent developments in AI models, focusing on pricing, performance, and key features as reported in the field. The information is drawn directly from the provided table without additional interpretation or external data.

GPT-5.6 Sol pricing was reported to be promotional. This pricing is noted as being lower than premium peers. It is set at $4 for input and $20 for output, with a promotional period extending through November 21, 2026.

GPT-5.6 Sol's performance on coding benchmarks showed variability when compared to Grok 4.6. On CursorBench, GPT-5.6 Sol scored 69.9% against Grok 4.6's 67.2%. However, on DeepSWE, GPT-5.6 Sol achieved 65.9% while Grok 4.6 scored 73%. Terminal-Bench results were 26% for GPT-5.6 Sol and 34.6% for Grok 4.6. There was also a report of Grok 4.6 and GPT-5.6 Sol tying on one AA Intelligence Index claim, with scores of 61 versus 61, though other harnesses presented differing results.

Claude Opus 5 was reported to have high SWE-bench numbers. It achieved 96.0% on SWE-bench Verified and 79.2% on SWE-bench Pro. Its API pricing is listed at $5 for input and $25 for output. Claude Opus 5 also appeared as a strong entry in dev-tool rankings, with a WebDev Arena Elo score of 1691.

Gemini 3.7 Flash launched with a focus on being a low-cost, fast workhorse model. It features a 1M context window. The introductory pricing is $0.75 for input and $3.75 for output, which will then increase to $1.50 for input and $7.50 for output. Gemini 3.7 Flash was described as a mid-tier performer on the Rails agent benchmark, completing 45 out of 63 runs at a campaign cost of $17.85.

Grok 4.6 was presented as a frontier agentic model. It landed near the top on one August benchmark, completing 52 out of 63 runs with a campaign cost of $49. Its pricing was reported as cheaper than premium flagships in one comparison, listed at $2 for input and $6 for output, with a 500K context.

GLM-5.3 and GLM-5.3-Flash were shipped as open-weight models with long context capabilities. They offer a 1M context and are released under an MIT license.

Qwen3.8-Flash-Next was reported as a low-priced open-weight preview. Its pricing is $0.16 per million for input and $0.47 per million for output.

Tencent Hy4 preview was reported as a million-token, low-cost model available through cloud APIs. Its pricing is 6 yuan per million for input and 18 yuan per million for output, with a 1,048,576-token window.

Here is a summary of the reported information:

| claim | label | order | numbers | URL |
|---|---|---|---|---|
| GPT-5.6 Sol pricing was reported as promotional and lower than premium peers. | 🟢 robust | 2 | $4/$20; promo through Nov 21, 2026 | https://developers.openai.com/model/gpt-5-6-sol |
| GPT-5.6 Sol split coding benchmarks versus Grok 4.6 depending on harness. | 🟢 robust | 1 | CursorBench 69.9% vs 67.2%; DeepSWE 65.9% vs 73%; Terminal-Bench 26% vs 34.6% | https://www.datacamp.com/blog/grok-4-6-vs-gpt-5-6-sol |
| Claude Opus 5 was reported with top SWE-bench numbers and premium API pricing. | 🟢 robust | 3 | 96.0% SWE-bench Verified; 79.2% SWE-bench Pro; $5/$25 | https://agathon.ai/whichllm |
| Claude Opus 5 also appeared as a strong dev-tool ranking entry. | 🟢 robust | 3 | WebDev Arena 1691 Elo | https://blog.logrocket.com/ai-dev-tool-power-rankings/ |
| Gemini 3.7 Flash launched as a low-cost, fast workhorse with 1M context. | 🟢 robust | 2 | $0.75/$3.75 intro, then $1.50/$7.50; 1M context | https://benchr.org/recent-releases |
| Gemini 3.7 Flash was described as mid-tier on the Rails agent benchmark. | 🟢 robust | 2 | 45/63 runs; $17.85 campaign | https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8 |
| Grok 4.6 was positioned as a frontier agentic model and landed near the top on one August benchmark. | 🟢 robust | 1 | 52/63 runs; $49 campaign | https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8 |
| Grok 4.6 pricing was reported as cheaper than premium flagships in one pricing roundup. | ⚠️ sensitive | 1 | $2/$6; 500K context | https://www.progressiverobot.com/2026/08/13/llm-api-pricing-comparison-2026/ |
| Grok 4.6 and GPT-5.6 Sol tied on one AA Intelligence Index claim, but other harnesses disagreed. | ⚠️ sensitive | 1 | 61 vs 61 | https://www.deeplearning.ai/the-batch/groks-cursor-alliance-pays-off |
| GLM-5.3 / GLM-5.3-Flash were shipped as open-weight long-context models. | 🟢 robust | 2 | 1M context; MIT license | https://gigazine.net/gsc_news/en/20260829-glm-5-3-open/ |
| Qwen3.8-Flash-Next was reported as a low-priced open-weight preview. | ⚠️ sensitive | 2 | $0.16/M input; $0.47/M output | https://www.requesty.ai/blog/open-weight-frontier-august-2026-glm-qwen-hy4 |
| Tencent Hy4 preview was reported as a million-token low-cost model via cloud APIs. | 🟢 robust | 2 | 6 yuan/M input; 18 yuan/M output; 1,048,576-token window | https://www.orcarouter.ai/blog/tencent-hy4-preview-launch |

**Practitioner Lines:**

*   **Act:** Evaluate lower-cost, high-context models like Gemini 3.7 Flash and Tencent Hy4 preview for cost-sensitive applications requiring large context windows.
*   **Watch:** Monitor the evolving performance benchmarks for coding and agentic tasks, particularly how Grok 4.6 and GPT-5.6 Sol continue to differentiate across various harnesses.
*   **Ignore:** Claims of overall "ties" or single-benchmark wins without cross-validation across multiple, diverse testing environments, as performance can be highly harness-dependent.

---
