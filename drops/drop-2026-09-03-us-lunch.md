---
title: "Grok 4.20 vs Gemini Flash latency, September prices"
description: "Grok 4.20 538 ms total / 513 ms TTFT; Gemini 2.5 Flash 667 ms. Claude Sonnet 5 and Grok 4.6 list prices."
pubDate: 2026-09-03
draft: false
lane: scoreboard
tags: [scoreboard]
---

A latency snapshot for Grok 4.20 reports 538 ms total and 513 ms TTFT. Gemini 2.5 Flash latency is 667 ms total and 506 ms TTFT, with an output cost of $0.0025 per 1K output tokens.

Pricing updates are noted for several models. Claude Sonnet 5 is $2 per 1M input tokens and $10 per 1M output tokens, rising to $3 per 1M input tokens and $15 per 1M output tokens from September 1. Grok 4.6 is $2 per 1M input tokens and $6 per 1M output tokens. Gemini 3.6 Flash is $1.50 per 1M input tokens and $7.50 per 1M output tokens.

Coding leaderboard results are available. Claude Code / Fable 5 scored 83.1% on Terminal-Bench 2.1, 95.0% on SWE-bench Verified, and 80.3% on SWE-bench Pro. Codex CLI / GPT-5.5 scored 83.4% on Terminal-Bench 2.1, 88.7% on SWE-bench Verified, and 58.6% on SWE-bench Pro. Gemini CLI / Gemini 3.1 Pro scored 70.7% on Terminal-Bench 2.1, 80.6% on SWE-bench Verified, and 54.2% on SWE-bench Pro.

Benchmark claims for Qwen3.8-27B local-model include OSWorld 84.3, AndroidWorld 81.9, SWE-MM 38.6, CharXiv 83.7, and OmniDocBench 91.1. Qwen3.8-Max launch benchmark claims include PaperBench 93.0, Terminal Bench 2.1 86.6, and SWE-bench Pro 67.7. Its pricing claims are $2 per 1M input tokens and $6 per 1M output tokens.

GLM-5.3-Flash claims a total of 320B parameters, with 18B active parameters, and a 1M context. Its pricing claims are $0.15 per 1M input tokens and $0.50 per 1M output tokens.

DeepSeek V4-Pro pricing claims are $0.435 per 1M cache-miss input tokens and $0.87 per 1M output tokens. Its benchmark claims include Terminal Bench 2.1 87.9, Toolathlon-Verified 74.1, and AutomationBench 31.8.

The open-weight frontier shifts toward China, with a reported monthly ceiling of 754B to 2.78T.

### Harvested Data

| claim | label | order (🟢 robust / ⚠️ sensitive) | numbers | URL |
|---|---|---|---:|---|
| Grok 4.20 latency snapshot | 🟢 confirmed | 🟢 robust | 538 ms total; 513 ms TTFT | https://www.ailatency.com/reports/daily-v2/2026-08-19.html |
| Gemini 2.5 Flash latency and output cost | 🟢 confirmed | 🟢 robust | 667 ms total; 506 ms TTFT; $0.0025 / 1K output tokens | https://www.ailatency.com/reports/daily-v2/2026-08-19.html |
| Claude Sonnet 5 pricing update | 🟢 confirmed | 🟢 robust | $2 / $10 per 1M tokens; rising to $3 / $15 from Sept 1 | https://aitoolsrecap.com/Blog/ai-price-war-august-2026-openai-anthropic-deepseek |
| Grok 4.6 pricing update | 🟢 confirmed | 🟢 robust | $2 / $6 per 1M tokens | https://aitoolsrecap.com/Blog/ai-price-war-august-2026-openai-anthropic-deepseek |
| Gemini 3.6 Flash pricing update | 🟢 confirmed | 🟢 robust | $1.50 / $7.50 per 1M tokens | https://aitoolsrecap.com/Blog/ai-price-war-august-2026-openai-anthropic-deepseek |
| Claude Code / Fable 5 coding leaderboard | 🟢 confirmed | 🟢 robust | 83.1% Terminal-Bench 2.1; 95.0% SWE-bench Verified; 80.3% SWE-bench Pro | https://neuralcoretech.com/best-ai-coding-agents-august-2026/ |
| Codex CLI / GPT-5.5 coding leaderboard | 🟢 confirmed | 🟢 robust | 83.4% Terminal-Bench 2.1; 88.7% SWE-bench Verified; 58.6% SWE-bench Pro | https://neuralcoretech.com/best-ai-coding-agents-august-2026/ |
| Gemini CLI / Gemini 3.1 Pro coding leaderboard | 🟢 confirmed | 🟢 robust | 70.7% Terminal-Bench 2.1; 80.6% SWE-bench Verified; 54.2% SWE-bench Pro | https://neuralcoretech.com/best-ai-coding-agents-august-2026/ |
| Qwen3.8-27B local-model benchmark claims | 🟡 partial | ⚠️ sensitive | OSWorld 84.3; AndroidWorld 81.9; SWE-MM 38.6; CharXiv 83.7; OmniDocBench 91.1 | https://gigazine.net/gsc_news/en/20260817-qwen3-8-27b/ |
| Qwen3.8-Max launch benchmark and pricing claims | 🟡 partial | ⚠️ sensitive | PaperBench 93.0; Terminal Bench 2.1 86.6; SWE-bench Pro 67.7; $2 / $6 per 1M tokens | https://www.developersdigest.tech/blog/qwen-3-8-max-release-2026 |
| GLM-5.3-Flash price and scale claim | 🟡 partial | ⚠️ sensitive | 320B total; 18B active; 1M context; $0.15 / $0.50 per 1M tokens | https://www.requesty.ai/blog/open-weight-frontier-august-2026-glm-qwen-hy4 |
| DeepSeek V4-Pro pricing claim | 🟡 partial | ⚠️ sensitive | $0.435 cache-miss input; $0.87 output per 1M tokens | https://www.digitalapplied.com/blog/china-open-frontier-august-2026-scoreboard |
| DeepSeek V4-Pro benchmark claim | 🟡 partial | ⚠️ sensitive | Terminal Bench 2.1 87.9; Toolathlon-Verified 74.1; AutomationBench 31.8 | https://www.digitalapplied.com/blog/china-open-frontier-august-2026-scoreboard |
| Open-weight frontier shifts toward China | 🔴 hype | ⚠️ sensitive | 754B to 2.78T monthly ceiling | https://hug |

---
**Act:** Prioritize monitoring Claude Sonnet 5 pricing changes effective September 1, given its reported increase.
**Watch:** Observe coding agent leaderboard shifts, specifically comparing Claude Code / Fable 5 and Codex CLI / GPT-5.5 performance on SWE-bench Verified.
**Ignore:** Claims of a general "open-weight frontier shift toward China" without specific, actionable metrics beyond a wide monthly ceiling range.

---
