# Published Is Not a Policy

**Governed content delivery to AI agents and humans — per-field release control, bound to the moments of agent cognition.**

*Filed provisional patent application. Full technical specification available on request.*

---

## The problem: fragments of governance, no unifying binding

Enterprises already signal to agents where publish-or-don't falls short — an llms.txt here, JSON-LD there, robots directives and even HTML comments pressed into service as machine hints. But every one of these mechanisms is format-bound, advisory, and coarse: whole-document suggestions an agent may honor or ignore, with no shared settings across formats and nothing governing what happens after discovery. An agent that reaches a document still takes all of it — the current fact and the deprecated warning, the public spec and the internal caveat — then quotes, summarizes, and acts on it with equal confidence, and hands it to the next agent with no record of where it came from or what conditions attached.

So content governance today is scattered where it exists and binary where it doesn't: open the content and surrender control of how agents use it, or wall it off and watch agents answer customer questions from someone else's stale copy. What's missing is the unification — one binding mechanism with collective settings, operating *per field, per audience, per moment of use* — and a chain of custody that survives the content's journey through an agent pipeline.

## The architecture

**Govern the schema you already have.** A schema-agnostic binding engine normalizes any input content schema into a format-agnostic field inventory with a lossless passthrough guarantee — nothing is altered or dropped during ingestion, so adoption requires no re-authoring and no content migration. An inference-based auto-assignment model then proposes governance bindings by matching field-name semantics against an extensible pattern vocabulary and performing schema ontology alignment, with a per-field confidence score — so a thousand-field enterprise schema gets a governed baseline in a single automated pass, and human review is spent where confidence is low.

**Four interception layers, matched to the moments of agent cognition.** Agent engagement with content isn't one event — it's a sequence, and the architecture intercepts at each named stage of the reasoning loop: *discovery* (can the agent find this at all), *context* (what framing accompanies it), *credibility* (what trust weight it carries), and *handling* (what the agent may do with it — quote it, summarize it, or execute an action). A structured conditioning key isolates the discovery stage from rule content as an architectural constraint, so an agent can be permitted to discover a document without exposing the governance logic attached to it.

**Release is a cascade, not a switch.** Per-field release decisions evaluate against five graduated release tiers, mapping disclosure against verified roles and replacing the publish/don't-publish bit with graduated disclosure — the identical source object can yield different governed views for a public agent, a partner agent, and an internal tool, from a single configuration.

**One binding, two audiences.** A serialization engine produces both agent-readable payloads — dynamically generated llms.txt, skill.md, or metadata schemas — and human-readable layouts (HTML, PDF) from the same unified binding configuration. To deliver tailored variations, a personalization module applies named merge operations (replace, inject, suppress) from a co-located extension file onto structural zone references defined by a formal heading grammar, with the base content as the fallback. Single-sourcing, extended to the agent era: the human page and the machine payload are governed siblings, not divergent copies.

**Every release explains itself — and travels with its papers.** Each delivery event generates a complete machine-readable explainability record: a trust indicator with decomposed factor weights (freshness, authorship, contextual alignment), the counterfactual decisions documenting what would have been released under alternative conditions, and a provenance token embedded in the served output itself, carrying an append-only chain array that receives handling records from downstream nodes. When content surfaces three agents downstream, its origin, its handling constraints, and every hand it passed through are still attached.

**Governance that watches itself.** Passive observability subsystems trace cross-node lineage, run counterfactual drift detection across structural and contextual dimensions, and place configuration changes behind a human-approval gate — so the governance layer is itself auditable, not a new black box between content and agents.

## Why now

The content feeding AI agents has become the product — resolution rates rise and fall on knowledge quality, enterprises are watching answer engines consume their documentation on someone else's terms, and the market is consolidating around exactly this convergence: agent platforms acquiring content platforms to own the pipeline from source to answer. Emerging explainability and documentation obligations for automated systems are turning the un-instrumented content layer into a compliance liability. And the bindings cut both ways: as agent-mediated search and answer engines reshape how content gets found, the structured signals that govern release — credibility weights, freshness, per-field structure, provenance — are the same signals ranking systems reward. Agent search optimization is a natural extension of the binding framework: govern the content, and it is already instrumented to compete. The architecture is also the natural companion to evaluation: one system governs what enters the agent, the other scores what leaves it.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover closed-loop customer intelligence for LLM agents and post-inference evaluation of AI-generated artifacts.*

*Prepared by RJSlogar — 15+ years leading technical content organizations for Silicon Valley companies, most recently through an AI-native transformation of enterprise content architecture. These filings are shared as a portfolio of product thinking for the agent era; the conversations I'm looking for are about building, not licensing. https://rjslogar.github.io · https://www.linkedin.com/in/mba-ma-richs/*
