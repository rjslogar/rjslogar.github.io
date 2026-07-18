# Two Cohorts, One Metric

**Customer intelligence simplified for efficient agent processing — with the audit record and causal training substrate built into the same design, so high-LTV progression drives auditable business decisions.**

*Filed provisional patent applications (two related filings). Full technical specification available on request.*

---

## The problem: analytics built for dashboards can't run in a prompt

Enterprise customer analytics was built for human consumption — fine-grained segments, dozens of scores, dashboards reviewed at monitoring consoles. LLM agents invert all of it: the intelligence must arrive *inside the prompt*, in milliseconds, compact enough to act on coherently, and computed off the request path — because analytics in the path scales cost with every conversation, and a multitude of signals in a system prompt makes an agent muddier, not sharper.

Cohort segmentation is as old as CRM; agent platforms already pipe customer context into prompts; the industry is bolting audit logs onto agents. Every ingredient exists — what doesn't is the unification, and the identity at its center: **the audit record and the causal training data are the same structure, written once at injection time.** Today's agent logs are forensic exhaust, built to reconstruct incidents after the fact; none are designed as the statistical instrument a causal model trains on. So this architecture bets against the industry's instinct for richer intelligence and heavier audit trails: make the signal simpler and write it once, so the same frozen record governs the agent, satisfies the auditor, and trains the model.

## The architecture

**Two cohorts, the threshold zone between them, one metric.** A customer is in the high-value cohort or is not — one classification, one boundary. The intelligence concentrates where it pays: the threshold zone of customers whose transition is genuinely in play, scored by an LTV-weighted causal uplift estimate of whether intervention will actually move them, and translated into a recommended agent approach. The executive output is a single number — the **Cohort Health Metric**, one business-health figure: the share of the customer base in the high-value cohort. Simplification isn't a compromise here; it's what makes the system fast enough to serve, cheap enough to run, legible enough for an agent to act on, and optimized for processing the signal set collectively — as one coherent unit — rather than piecemeal.

**A dual-layer system built on that simplicity.** The compact pre-computed signal — cohort membership, threshold-zone status, the uplift score, churn risk, the recommended approach — lives in an in-memory decision layer and is injected into the agent's prompt in under 15ms at the 99th percentile, at 10M-daily-active-user scale. All expensive analytics run asynchronously in a second layer on an independent schedule — approximately a 95% infrastructure cost reduction versus unified real-time analytics architectures, because nothing analytical ever sits in the request path.

**Causal, not correlational, on the one transition that matters.** Uplift modeling with treatment and control groups isolates the incremental effect of interventions on cohort transitions from baseline propensity — separating customers who moved because the agent acted from those who would have moved anyway — and weights that effect by lifetime value, so agent effort is spent where causation and value intersect.

**Every injection leaves a record — because prompt-delivered treatment is otherwise invisible.** A coupon leaves a ledger; a treatment mandate delivered through a system prompt leaves nothing, anywhere, unless the record is built deliberately. So a tamper-evident audit record is written at injection time, before the agent generates a word, capturing exactly which signals the enterprise supplied. The second filing closes the loop: that audit record and the causal training substrate are the same structure, written once — treatment assignment is read only from audit records, covariates are the values frozen at assignment time (eliminating feature leakage by construction), a small randomized-withholding cohort upgrades the system to true experimentation, and agent concessions are joined to the mandate in force so treatment economics feed back into the model.

**One number a board can trust and an auditor can verify.** The Cohort Health Metric decomposes causally into intervention-driven, organic, retention, and attrition components — and because the substrate beneath it is tamper-evident, every unit of high-LTV progression drills down to a verifiable record. Real business decisions — where to spend agent effort, which interventions to scale, which concessions pay for themselves — rest on audited causation rather than dashboard correlation.

## Why now

Agent platforms are winning deals on resolution rates and losing sleep on two fronts at once: the infrastructure cost of putting intelligence into every conversation, and the governance question regulators and enterprise buyers are already asking — *what did you tell the agent about me, and what happened because of it?* A two-cohort, one-metric design answers both with the same move: intelligence simple enough to serve at conversation scale is also simple enough to explain, audit, and learn from.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover post-inference evaluation of AI-generated artifacts and governed content delivery to agents.*

*Prepared by RJSlogar — 15+ years leading technical content organizations for Silicon Valley companies, most recently through an AI-native transformation of enterprise content architecture. These filings are shared as a portfolio of product thinking for the agent era; the conversations I'm looking for are about building, not licensing. https://rjslogar.github.io · https://www.linkedin.com/in/mba-ma-richs/*
