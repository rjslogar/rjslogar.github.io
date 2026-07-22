# Two Cohorts, One Metric

**Customer intelligence simplified until an agent can actually use it — and one record, written at injection time, that is both the audit trail and the source of the causal training data.**

*Filed provisional patent applications (two related filings). Full technical specification available on request.*

---

## The problem: analytics built for dashboards can't run in a prompt

Enterprise customer analytics evolved for human consumption — ever-finer segmentations, dozens of scores, real-time feature pipelines feeding dashboards that analysts interpret at leisure. LLM agents invert every one of those assumptions. An agent needs intelligence in milliseconds, in a form a prompt can carry, and with a durable record of what it was told — because what an agent is told about a customer silently changes how that customer is treated, and prompt-injected treatment leaves no artifact in any conventional system of record.

The industry's instinct is to make customer intelligence richer. This architecture bets the opposite way — make it simpler, and make the simplification do work that was never possible before.

## The thesis: audit and training from one write

Agent platforms today run these as two unconnected systems: an audit and observability layer on one side, a training and knowledge pipeline on the other, with no structural relationship between them. This design unifies them. At the moment customer intelligence is injected into the agent's context — before any response is generated — a single tamper-evident record is written, hash-chained, capturing exactly what the agent was told and under which treatment mandate.

That record is the source of truth. The compliance trail reads it directly. The causal training corpus is a **derived, PII-scrubbed view of it** — not the same object, so the two demands never conflict: the immutable record satisfies retention and tamper-evidence, while the derived view stays curated, current, and erasure-compatible (per-customer encryption keys mean a deletion request destroys content without breaking the chain). Treatment assignment is read only from these records; training covariates are the values frozen at injection time, eliminating feature leakage by construction; and agent concessions — discounts, waivers, credits — are joined to the mandate in force, so treatment economics feed back into the model.

## The design: two cohorts, the threshold zone between them, one metric

The entire customer base resolves to a high-value cohort, everyone else, and the threshold zone between them — the narrow band where transition is genuinely in play and where intelligence concentrates. Each customer's state compresses to a ~200-byte pre-computed signal structure — cohort, trajectory, transition score, churn risk, friction, threshold-zone status, recommended approach, freshness — served to the agent in under 15 milliseconds by a single in-memory lookup, with all analytics running asynchronously. The filed estimate: approximately 95% infrastructure cost reduction versus computing equivalent intelligence in the request path.

Cohort segmentation itself is as old as CRM — which is exactly the objection this design anticipates. What the simplification buys is three properties no dashboard-era segmentation has: intelligence an LLM can consume mid-conversation, scores that are causal about transition rather than correlational, and a per-session audit record for every injection.

## The causal claim, with the counterfactual named

The transition score is not a propensity score. It estimates the incremental effect of a specific intervention — what the treatment *causes*, not who *looks likely* — against a named counterfactual: matched control groups on behavioral covariates at cold start, upgraded by an always-on randomized-withholding cohort (1–5% of eligible sessions, assignment recorded in the audit substrate itself) to experimentally identified inference, with every model validated on an out-of-sample holdout before its scores reach production. Without that structure, a transition metric is cohort correlation wearing a causal label; with it, the counterfactual is not an assumption but a recorded, verifiable design element.

## One number a board can trust and an auditor can verify

The Cohort Health Metric decomposes causally into intervention-driven, organic, retention, and attrition components — intervention effects counted net of modeled baseline, the withholding cohort reported alongside as the empirical benchmark. Because the substrate beneath it is tamper-evident, every unit of high-LTV progression drills down to a verifiable record. Real business decisions — where to spend agent effort, which interventions to scale, which concessions pay for themselves — rest on audited causation rather than dashboard correlation.

## Why now

Agent platforms are winning deals on resolution rates and losing sleep on two fronts at once: the infrastructure cost of putting intelligence into every conversation, and the governance question regulators and enterprise buyers are already asking — *what did you tell the agent about me, and what happened because of it?* A two-cohort, one-metric design answers both with the same move: intelligence simple enough to serve at conversation scale is also simple enough to explain, audit, and learn from.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover post-inference evaluation of AI-generated artifacts and governed content delivery to agents.*
