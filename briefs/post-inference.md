# Bias Doesn't Stay Where It Started

**Comprehensibility scoring for AI-generated text and code — the model-agnostic evaluation layer that makes propagation containment possible in multi-agent systems.**

*Filed provisional patent application. Full technical specification available on request.*

---

## The problem: flawed output is contagious

Every serious evaluation product today answers the same question: *is this AI output good?* It's the wrong question to stop at. In a multi-agent system, one agent's output is another agent's input — a summary becomes a planning context, generated code becomes a dependency, a drafted analysis becomes the ground truth for the next reasoning step. A subtle bias or fabrication that survives its first review doesn't stay put. It propagates across agent boundaries, laundering itself into "established context" at each hop, gaining apparent credibility precisely because it now arrives from a trusted internal source.

Evaluation vendors compete on detection accuracy for a single artifact. Nobody scores the epidemiology: *if this flaw is real, how far will it travel?*

## The architecture

**One invariant pipeline, two artifact classes: text and code.** The same architecture evaluates both natural-language responses and AI-generated source code — two problems served today by entirely separate vendor categories. The code track is the deeper and more urgent of the two: with AI now generating a substantial share of production code, the evaluation question shifts from *"is this output valid?"* to *"can anyone on the team actually explain the mechanics of what we just shipped?"* — a question conventional static analysis and security review tooling was never engineered to answer.

**Evaluate the frozen artifact — no access to model weights, training data, or internal states.** The pipeline operates post-inference on the finished artifact itself. This model-agnostic decoupling makes it deployable where instrumentation-based observability cannot go: third-party compliance audits, procurement reviews, air-gapped regulated environments, and outputs from proprietary models the evaluator cannot look inside.

**Each detection stage is epistemically matched to what it detects.** Rather than a single judge model that collapses interpretability, the pipeline applies independent stages matched to specific phenomena. Text artifacts pass through five stages applying frameworks such as evidence theory and causal calculus to map rhetorical drift. Code artifacts run through seven syntax and behavioral checks — evaluating structural inflation, abstraction-layer bloat, prompt-lock vocabulary inheritance, execution-path divergence, and cold explanation quality, the stage that directly probes the comprehension question above.

**Signals combine in a reasoning graph, not a weighted average.** Nodes connect via typed *amplifier* edges that raise the joint posterior when dangerous signals co-occur, and typed *suppressor* edges that reduce risk when markers of epistemic honesty — symmetric hedging, explicit scope boundaries, clear sourcing — are verified. The system is designed to reward well-calibrated, honest responses rather than issue blanket penalties. The output is a calibrated **comprehensibility score** — not merely *is this output correct*, but *can its reasoning be followed, explained, and defended by the people who must own it* — accompanied by an evidence vector and clause-level annotations, not a verdict. Comprehensibility is the concept that unifies the two tracks: it's what rhetorical-drift detection measures in text and what cold explanation quality measures in code.

**Then the question no one else asks: will it spread?** Scoring is what makes containment possible — a flaw must be detected and scored before its spread can be assessed. On top of the detected patterns, a transferability score quantifies the probability of propagation across agent boundaries, and a five-tier containment architecture matches enforcement to that risk — from real-time metadata tagging and human-in-the-loop review through programmatic quarantine and context sterilization. Operational enforcement is governed by a portable Maturity State parameter — Advisory, Soft-Gate, Hard-Gate — so an organization can move its guardrails from flagging an unstable output to blocking an unexplainable code deployment without modifying the evaluation pipeline underneath.

**Three explainability layers, because three audiences ask.** Layer 1 gives end users clause-level vulnerability mapping on the artifact; Layer 2 gives auditors reproducible computation traces through the reasoning graph; Layer 3 attributes which prompt features triggered which generation pathways — all without model access. Domain Configuration Manifests let domain experts adjust risk priors and sensitivity weights for medical, legal, or financial contexts without changing core code.

## Why now

Multi-agent architectures went mainstream before multi-agent quality control existed. Enterprises are wiring autonomous agents into production chains whose intermediate artifacts nobody reviews, evaluation platforms are racing each other on single-artifact detection accuracy, and AI-generated code is merging faster than humans can attest they comprehend it. As regulatory frameworks worldwide converge on documentation and technical-control obligations for automated systems, the next competitive line in the evaluation market isn't a better hallucination detector — it's knowing which detected flaws are contained and which are contagious, and having the enforcement tiers to act on the difference.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover closed-loop customer intelligence for LLM agents and governed content delivery to agents.*

*Prepared by RJSlogar — 15+ years leading technical content organizations for Silicon Valley companies, most recently through an AI-native transformation of enterprise content architecture. These filings are shared as a portfolio of product thinking for the agent era; the conversations I'm looking for are about building, not licensing. https://rjslogar.github.io · https://www.linkedin.com/in/mba-ma-richs/*
