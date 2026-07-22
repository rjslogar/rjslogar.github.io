# Published Is Not a Policy

**Governed content delivery to AI agents and humans — per-field release control through four interception layers, Discovery, Context, Credibility, and Handling, bound to the moments of agent cognition.**

*Filed provisional patent application. Full technical specification available on request.*

---

## The problem: one bit of governance for an agent-scale world

Enterprise content has exactly one access control: published or not. That binary was tolerable when the audience was human — people read selectively, respect context, and can be trained. Agents can't be published *at*. An agent that can reach a document takes all of it: the current fact and the deprecated warning, the public spec and the internal caveat, the authoritative answer and the draft beside it — then quotes, summarizes, and acts on that content with equal confidence, and hands it to the next agent with no record of where it came from or what conditions attached to it.

So enterprises face a false choice: open the content and surrender control of how agents use it, or wall it off and watch agents answer customer questions from someone else's stale copy. What's missing is the middle — governance that answers four questions, in the order an agent actually asks them: can the agent **find** this at all (Discovery), what **framing** accompanies it (Context), what **trust weight** does it carry (Credibility), and what may the agent **do** with it — quote it, summarize it, act on it (Handling). Publishing answers none of these. This architecture answers each one, per field, per audience, at the moment of use.

## Where this sits

Pieces of this exist, and the overlap is the point — it proves the problem is real. Some companies ship strong Discovery and Context today, with ranking and citations standing in for trust; others govern Discovery and Handling as data protection, strong on classification but are silent on what an agent may do with content once retrieved; when strongest on Credibility and policy definition, others catalog and approve rather than operating in the retrieval path. What none of them provides — and what this filing adds rather than replaces — is a formal, computed credibility score in place of ranking proxies, and a declarative, per-action Handling policy in place of binary include/exclude, both enforced as a runtime layer at the moment of use.

The policy itself needs an owner, and this design doesn't invent a new one: it gives whoever already owns content risk — security for exposure, legal for claims, the content and knowledge team for accuracy — a single enforcement point where their existing policies finally execute.

## The architecture

**Govern the schema you already have.** A schema-agnostic binding engine normalizes any input content schema into a format-agnostic field inventory with a lossless passthrough guarantee — nothing is altered or dropped, so adoption requires no re-authoring and no migration. An inference-based auto-assignment model then proposes governance bindings by matching field names against a pattern vocabulary and aligning schema ontologies, with a per-field confidence score — so a thousand-field enterprise schema gets a governed starting point in one pass, and human review is spent only where confidence is low.

**Four interception layers, matched to the moments of agent cognition.** Agent engagement with content isn't one event — it's a sequence, and the architecture intercepts at each named stage: *Discovery* (can the agent find this at all), *Context* (what framing accompanies it), *Credibility* (what trust weight it carries), and *Handling* (what the agent may do with it — quote, summarize, act). A conditioning key isolates the discovery stage from rule content, so an agent can be permitted to find a document without ever seeing the rules that govern it. And because each layer is a policy check, not a data store — the key resolves once per session, and the later layers travel in-band with the governed content itself — the latency cost is bounded and cacheable per session, not a per-request analytics call inside the agent loop.

**Release is a cascade, not a switch.** Per-field release decisions evaluate against five named release tiers, replacing the publish/don't-publish bit with graduated disclosure — the same source object can yield different governed views for a public agent, a partner agent, and an internal one.

**One binding, every delivery surface.** A serialization engine produces both agent-readable and human-readable governed artifacts from the same unified binding configuration — the human page and the agent payload are governed siblings, not divergent copies. The binding governs fields, not file types: the reference implementation targets published content — documentation, knowledge bases, structured repositories — and a pluggable serialization adapter registry carries the same bindings to new delivery surfaces, including feed- and API-style output, as a configuration entry rather than a redesign.

**Every release explains itself — and travels with its papers.** Each release event generates a complete machine-readable explainability record: a trust indicator with decomposed factor weights, the counterfactual decisions (what would have been released under different conditions), and a provenance token embedded in the governed output itself, carrying a chain array for multi-agent chain-of-custody. When content surfaces three agents downstream, its origin, its conditions, and every hand it passed through are still attached.

## Why now

The content feeding AI agents has become the product — resolution rates rise and fall on knowledge quality, enterprises are watching answer engines consume their documentation on someone else's terms, and the market is consolidating around exactly this convergence: agent platforms acquiring content platforms to own the pipeline from source to answer. Conventions like llms.txt are the first, crude acknowledgment that agents need different delivery than humans. What they lack is everything after discovery: context, credibility, handling, and custody. That's the layer this architecture supplies — and it's the natural companion to evaluation: one system governs what enters the agent, the other scores what leaves it.

---

*One of three filed provisionals on agent-era enterprise architecture — the others cover closed-loop customer intelligence for LLM agents and post-inference evaluation of AI-generated artifacts.*
