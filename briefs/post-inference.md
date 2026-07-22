# Bias Doesn't Stay Where It Started

**Post-inference evaluation of AI-generated text and code — with propagation risk scoring and graduated containment for multi-agent systems.**

*Filed provisional patent application. Full technical specification available on request.*

---

## The problem: flawed output is contagious

Every serious evaluation product today answers the same question: *is this AI output good?* It's the wrong question to stop at. In a multi-agent system, one agent's output is another agent's input — a summary becomes a planning context, generated code becomes a dependency, a drafted analysis becomes the ground truth for the next reasoning step. A subtle bias or fabrication that survives its first review doesn't stay put. It propagates across agent boundaries, laundering itself into "established context" at each hop, gaining apparent credibility precisely because it now arrives from a trusted internal source.

The chain is concrete. A skewed framing in one generated summary enters a retrieval index; a downstream agent retrieves it as context and inherits its trajectory in chain-of-thought; the conclusion it reaches selects the tool call; the tool's output ships to the customer — and the flaw is now three hops from its origin, wearing internal provenance. In code, the same epidemiology runs through completion context: one opaque generated module seeds its identifier vocabulary and structural patterns into every completion that reads it, until the pattern is load-bearing in a dozen files and nobody can name the commit that introduced it.

Evaluation vendors compete on detection accuracy for a single artifact. Nobody scores the epidemiology: *if this flaw is real, how far will it travel?*

## The architecture

**Evaluate the frozen artifact — no model access required.** The pipeline operates post-inference, on the finished text or code artifact itself. That makes it deployable where instrumentation-based observability can't go: third-party audit, procurement review, regulated environments, and outputs from models the evaluator doesn't control.

**Each detection stage is epistemically matched to what it detects.** Rather than delegating all judgment to a single judge model — which collapses interpretability into one opaque score — each stage applies the inference method suited to its phenomenon, and each emits its own influence signal. The output is a calibrated posterior probability, not a threshold verdict, accompanied by an evidence vector: per-signal contributions, with posteriors and artifact locations. Amplification and suppression factors are derived parameters, empirically calibrated against human-labeled corpora and recalibrated from audit-record outcomes — not fixed constants asserted by the vendor.

**Transferability is a score, not a metaphor.** For each detected signal, a transferability score quantifies the probability it propagates across an agent boundary — computed from the detection posterior, a propagation-efficiency parameter, and a consumption-mode weight covering the ways downstream systems actually ingest output: retrieval, chain-of-thought continuation, prompt templates, code-completion context, training ingestion. The filing models seven named propagation pathways — four for text, three for code — so "how far will it travel" is a computed answer per pathway, not a risk-register adjective.

**Containment is graduated — and explicit about its verb.** Five tiers, each doing something different: *Monitor* logs, *Review* flags to a human, *Verify* demands independent confirmation, *Quarantine* blocks the artifact as downstream input, and *Sanitize-and-substitute* replaces it with an epistemically neutralized equivalent. Post-inference scoring is reactive by construction — so the design says precisely where reaction ends and enforcement begins: a per-deployment maturity state (advisory, soft-gate, hard-gate) governs whether a finding is recorded, escalated, or blocks a merge, deployment, or display. Moving from flagging to blocking is a configuration change over an invariant pipeline, not a redesign.

**Three explainability layers, each with its own technique.** The end-user layer is a clause-level annotation map — every finding pinned to the exact span or code region that produced it. The auditor layer is the evidence vector and audit record — per-signal posteriors, factor weights, and outcome history, aggregable across artifacts and time. The attribution layer traces detected patterns to their provenance in the prompt and context that shaped the artifact. Layer one explains it to the person reading the output, layer two to the person accountable for the system, layer three to the person debugging where the pattern came from.

## Why now

Multi-agent architectures are moving from demo to default, and every hop added to a pipeline multiplies the surface a single flawed artifact can reach. Evaluation tooling hasn't followed: the market benchmarks single-artifact detection while enterprises deploy systems whose real risk is propagation. Scoring the artifact *and* its blast radius — with containment that graduates from logging to blocking as trust matures — is the missing control plane. And it's the natural companion to governed delivery: one system governs what enters the agent, the other scores what leaves it.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover governed content delivery to agents and closed-loop customer intelligence for LLM agents.*
