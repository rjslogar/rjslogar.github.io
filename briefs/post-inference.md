# Bias Doesn't Stay Where It Started

**Comprehensibility scoring for AI-generated text and code — the model-agnostic evaluation layer that makes propagation containment possible in multi-agent systems.**

*Filed provisional patent application. Full technical specification available on request.*

---

## The problem: flawed output is contagious

Every serious evaluation product today answers the same question: *is this AI output good?* It's the wrong question to stop at. In a multi-agent system, one agent's output is another agent's input — a summary becomes a planning context, generated code becomes a dependency, a drafted analysis becomes the ground truth for the next reasoning step. A subtle bias or fabrication that survives its first review doesn't stay put. It propagates across agent boundaries, laundering itself into "established context" at each hop, gaining apparent credibility precisely because it now arrives from a trusted internal source.

Evaluation vendors compete on detection accuracy for a single artifact. Nobody scores the epidemiology: *if this flaw is real, how far will it travel?*

## The architecture

**One pipeline, two artifact classes: text and code.** The same evaluation framework scores both LLM text responses and AI-generated code — two problems served today by entirely separate vendor categories. In the filed design, the text/code split is a configuration dimension, not two products: five detection stages for text, seven for code, applied over one invariant pipeline. The code track is the attention-getter: with AI writing a growing share of production code, the evaluation question shifts from *"is this output correct?"* to *"can anyone on the team explain what we just shipped?"* — a question no correctness, security, or style tool is built to answer.

**It evaluates the frozen artifact — no model access required.** The pipeline operates post-inference, on the finished output alone, with no access to weights, training data, or internal activations. That makes it deployable where instrumentation-based observability can't go: third-party audit, procurement review, regulated environments, and outputs from models the evaluator doesn't control.

**Each stage applies the inference method matched to what it detects.** For text: Dempster–Shafer evidence theory for factual claims, modeling *genuinely unverifiable* as its own belief state rather than forcing a true/false call; causal-graph validation for causal claims; distributional divergence for sycophancy drift; a multi-head sequence model for rhetorical patterns; and an adversarial-twin probe that strips the original query of tone, certainty adverbs, presuppositions, and loaded framing, re-poses it, and measures whether the position survives. For code: AST structural analysis, complexity and call-graph analysis, identifier-embedding comparison against the prompt vocabulary (catching code whose architecture mirrors the prompt rather than the problem), dependency-graph pattern matching, an adversarial refactor generating a complexity-minimized equivalent, execution-trace surprise scoring, and cold-explanation quality — whether a model given only the code, with no prompt context, can explain it confidently.

**Conflicting signals reconcile through a typed causal graph, not an average.** Amplifier edges raise the joint posterior when independent stages corroborate each other; suppressor edges lower it when the artifact shows epistemic honesty — explicit uncertainty, source attribution, counter-framing, stated scope limits. The suppressors are the point: the system credits well-calibrated output rather than only penalizing poor output. The result is a calibrated probability — a Comprehensibility Influence Score for text, a Comprehensibility Opacity Score for code — not an opaque letter grade.

**Propagation risk is scored, not just presence.** Each detected flaw carries a transferability estimate: its detection posterior, weighted by how efficiently that flaw type crosses agent boundaries and by how the artifact will be consumed downstream — RAG retrieval, chain-of-thought continuation, prompt template, code-completion context, or training ingestion. Seven propagation pathways are modeled, from trajectory inheritance in text chains to identifier-vocabulary and complexity-baseline inheritance in code chains, where one agent's inflated structure quietly becomes the next agent's generative prior.

**Enforcement is tiered to the risk.** Five containment actions — monitor, review, verify, quarantine, sterilize-and-substitute — trigger on configurable thresholds, and per-team maturity states (advisory, soft-gate, hard-gate) let an organization run in observation mode first and tighten enforcement as its own outcome data accumulates, without re-architecting anything.

**Every score is explainable at three depths.** An end-user layer annotates the artifact clause by clause; an auditor layer exposes the full aggregation trace showing which amplifiers and suppressors fired and why; and a prompt-attribution layer identifies which features of the *input prompt* activated which generation pathways in the model — still without model access. That third layer turns evaluation into prevention: it tells the prompt author what to change.

**Domain standards are configuration, not code.** Medical, legal, financial, and enterprise manifests adjust priors, stage sensitivities, and suppressor evidence bars over the same fixed pipeline — a medical deployment can demand a systematic-review citation before crediting a source, where a general deployment accepts any citation. Domain experts contribute manifests; the architecture doesn't change.

## Why now

Multi-agent architectures went mainstream before multi-agent quality control existed. Enterprises are wiring autonomous agents into production chains whose intermediate artifacts nobody reviews, evaluation platforms are racing each other on single-artifact detection accuracy, and AI-generated code is merging faster than humans can attest they comprehend it. As regulatory frameworks worldwide converge on documentation and technical-control obligations for automated systems, the next competitive line in the evaluation market isn't a better hallucination detector — it's knowing which detected flaws are contained and which are contagious, and having the enforcement tiers to act on the difference.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover closed-loop customer intelligence for LLM agents and governed content delivery to agents.*

*Prepared by RJSlogar — 15+ years leading technical content organizations for Silicon Valley companies, most recently through an AI-native transformation of enterprise content architecture. These filings are shared as a portfolio of product thinking for the agent era; the conversations I'm looking for are about building, not licensing. https://rjslogar.github.io · https://www.linkedin.com/in/mba-ma-richs/*
