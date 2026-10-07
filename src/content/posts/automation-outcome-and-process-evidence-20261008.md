---
title: "What Counts as Success in AI Automation?"
pubDate: 2026-10-08
draft: false
approved: true
tags: ["automation", "research", "evidence"]
---

When an AI says a task is complete, what should exist for that claim to be true? A file being present, its contents being correct, and someone being able to use it are separate checks. For recurring work, the expected outcome and the criteria for judging it need to be defined before execution.

This research note presents a design hypothesis drawn from sources on artifact evaluation and process reuse. It does not report measured time or cost savings in an organization.

## Check the outcome behind the completion message

Anthropic's guide to agent evaluations distinguishes an execution transcript from the final state of the environment. An agent saying it booked a flight and a reservation actually existing are different things. That distinction is a useful starting point for evaluating artifact workflows. [Anthropic's evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

Applied to a report, success criteria could include required content, file format, and the scope of review. Applied to an automated operation, they could include the expected state change and the records that should remain after failure. File existence alone does not establish accuracy or actual use.

## Preserve how the result was produced

W3C PROV provides a vocabulary for relating entities, activities, and responsible agents. It can help connect an input version to the work performed and the result generated. A well-structured provenance record does not, by itself, establish that its assertions are true. [W3C PROV Primer](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/)

PROV-AGENT extends this approach to AI agent interactions and workflow context. It is a relevant research example, with a clear limitation: the paper describes a direct live connection between sensors and simulation that was still under development. Its implementation and evaluation scope should not be treated as proof of effectiveness in an unrelated workflow. [PROV-AGENT v3](https://arxiv.org/html/2508.02866v3)

My design proposal is to preserve the relationships between input versions, selected criteria, execution, results, and judgments or corrections. Subsequent runs can then be compared under the same conditions, with differences investigated rather than hidden.

## Test what happens when execution repeats

Automation also needs to handle repeated requests and cases where work finishes but the response is lost. AWS explains why recording an idempotency token and performing the associated mutations must form an atomic operation. This is a design principle to verify in a specific system, rather than a universal guarantee of exactly-once execution. [AWS on safe retries](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

## The operating hypothesis I want to test

Starting from AI and automation, I define the purpose and permitted scope, then follow a loop: plan and judge, map the paths, implement and execute, check the outcome, and update the map. The map records the criteria and the next steps for success, failure, and exceptions.

For one representative task type, I want to test three things:

1. Can the expected outcome be fixed before execution and compared with the actual result?
2. Can input versions and the production process be preserved so subsequent runs can be compared?
3. Can repeated requests, interrupted execution, and lost responses be distinguished while time, cost, and human intervention are measured?

One successful run is not sufficient to generalize the effectiveness of the process. Failures, counterexamples, and differences in conditions need to be reflected in the map. These sources help define the questions; they do not establish the effectiveness of my own operating model. Further investigation of contrary findings and failed approaches remains necessary.
