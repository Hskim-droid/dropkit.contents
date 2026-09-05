---
title: "drop-2026-09-06-us-lunch"
description: "DeepSeek V4 Pro API pricing moved to peak and off-peak tiers. Peak pricing is $1.32 per million input tokens and $3.96 per million output tokens. Off-peak pricing is $0.66 per mill"
pubDate: 2026-09-06
draft: false
lane: scoreboard
tags: [scoreboard]
---


### 8.13.2026 Lab Note: Pricing and Benchmarks

DeepSeek V4 Pro API pricing moved to peak and off-peak tiers. Peak pricing is $1.32 per million input tokens and $3.96 per million output tokens. Off-peak pricing is $0.66 per million input tokens and $1.98 per million output tokens. This change was reported as an increase ranging from 50% to 1,100%. After this adjustment, DeepSeek V4 Pro was noted at the higher pricing tier, which is $1.32 for input and $3.96 for output tokens. These figures are from a Reuters report dated August 13, 2026.

Qwen3.8-Max API pricing was reported at standard hosted rates, with input tokens at $2 per million and output tokens at $6 per million. Cached-token pricing for Qwen3.8-Max was disclosed separately as $0.25 per million for cached input and $0.17 per million for explicit cache read.

Grok offered paid tiers, which were listed as $30 per month and $300 per month. Claude Opus was noted with a 1 million token context window and a claim of 88.6% on SWE-bench Verified. Grok’s latency was claimed to be 1.1 seconds, compared to 2.5 seconds for Gemini and 3.2 seconds for Claude in a comparison article.

DeepSeek V4 Pro’s benchmark leadership was summarized in a 2026 roundup, showing 87.9 on Terminal-Bench 2.1 and 96.4% on SWE-bench Verified. Alibaba/Qwen open-weight and cost-performance were framed in China-lab coverage. This coverage cited open weights, 27B and 125B models, and the $2/$6 pricing. China open-model pricing pressure was reflected in DeepSeek and Qwen coverage. This included the 50% to 1,100% price increase and $2/$6 price parity.

The strongest cross-check is Reuters-backed DeepSeek pricing. Other items are mostly secondary snapshots or comparison-table claims.

| claim | label | order | numbers | URL |
|---|---|---|---:|---|
| DeepSeek V4 Pro API pricing moved to peak/off-peak tiers | price | 🟢 robust | $1.32 in / $3.96 out peak; $0.66 in / $1.98 out off-peak | https://www.reuters.com/world/china/deepseek-raises-api-pricing-its-v4-models-2026-08-13/ |
| DeepSeek V4 Pro pricing increase was reported as 50% to 1,100% depending on model/token/time | price | 🟢 robust | 50% to 1,100% | https://www.reuters.com/world/china/deepseek-raises-api-pricing-its-v4-models-2026-08-13/ |
| DeepSeek V4 Pro was reported at the higher pricing tier after the change | price | 🟢 robust | $1.32 in / $3.96 out | https://www.reuters.com/world/china/deepseek-launches-v4-pro-at-prices-up-to-14-times-higher-than-v4-flash-2026-08-14/ |
| Qwen3.8-Max API pricing was reported at standard hosted rates | price | ⚠️ sensitive | $2 in / $6 out | https://www.forbes.com/sites/jonmarkman/2026/08/05/alibabas-qwen38-max-prices-frontier-ai-at-2-per-million-tokens/ |
| Qwen3.8-Max cached-token pricing was disclosed in secondary coverage | price | ⚠️ sensitive | $0.25 cached input / $0.17 explicit cache read | https://www.101aitools.com/guides/reviews-qwen3-8-max |
| Grok paid tiers were listed in comparison coverage | price | ⚠️ sensitive | $30/mo; $300/mo | https://albato.com/blog/publications/grok-chatgpt-gemini-claude-overview |
| Claude Opus was listed with a 1M-token context window and benchmark claim in comparison coverage | coding | ⚠️ sensitive | 1M context; SWE-bench Verified 88.6% | https://albato.com/blog/publications/grok-chatgpt-gemini-claude-overview |
| Grok latency was claimed to beat Gemini and Claude in a comparison article | latency | ⚠️ sensitive | 1.1 s vs 2.5 s vs 3.2 s | https://www.aiapps.com/blog/chatgpt-vs-gemini-vs-grok-vs-claude-worth-paying-for/ |
| DeepSeek V4 Pro benchmark leadership was summarized in 2026 roundup coverage | agents | ⚠️ sensitive | Terminal-Bench 2.1 87.9; SWE-bench Verified 96.4% | https://ofox.ai/blog/deepseek-v4-pro-0813-price-weights-benchmarks-api-access-2026/ |
| Alibaba/Qwen open-weight and cost-performance framing appeared in China-lab coverage | search | ⚠️ sensitive | open weights; 27B / 125B; $2 / $6 pricing | https://datanorth.ai/news/alibaba-releases-qwen3-8-27b |
| China/open-model pricing pressure was reflected in DeepSeek and Qwen coverage | price | ⚠️ sensitive | 50% to 1,100%; $2 / $6 parity | https://techwireasia.com/2026/08/deepseek-v4-pro-us-china-open-ai-model-race/ |

**Act:** Investigate DeepSeek V4 Pro peak/off-peak tier usage patterns and actual cost implications for existing workloads.

**Watch:** Monitor the reported latency claims for Grok against further independent verification.

**Ignore:** Claims of benchmark leadership from single, isolated secondary sources without additional context or replication.

---
