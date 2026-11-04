# Correct Isn't the Same as Understood

***Can anyone on your team explain what your agents shipped?***

**TL;DR:** A patent-pending method that measures whether a human can understand and validate AI-generated code, even when it passes every test and complexity check. Seven independent checks combine into one Comprehensibility Opacity Score: a calibrated probability that a reviewer will fail to validate the code. That probability drives a merge gate, and it keeps opaque code from spreading to other agents. We're looking for a partner to pilot and co-develop it.

**Audience:** Engineering, platform and AI leaders · **Reading time:** about 3 minutes

**Status:** Patent pending, U.S. provisional application filed in 2026 · Non-confidential overview

## The problem

AI agents now write code faster than people can review it. Releases speed up, but stability and confidence drop, because the problems agents introduce are rarely loud:

- **The code is correct, but nobody can follow it.** Tests pass, linters pass, and complexity metrics rate it well, yet a reviewer can't tell what it does or why.
- **Review fatigue hides the real issues.** Large diffs, extra layers and unused code bury a step taken in the wrong order or an error swallowed without a trace.
- **Opacity spreads.** One agent's output is the next agent's input and training data, so code nobody understood becomes the pattern the next agent copies.

Existing tools check correctness, security, style and complexity. None of them measures whether a person can actually validate what shipped.

## The approach

1. **Check what complexity metrics can't see.** Seven independent checks, each using the method suited to what it detects. They cover hidden structure, complexity beyond what the problem needs, names that echo the prompt instead of the problem, architecture that serves no purpose, how much simpler the same behavior could be, steps that surprise a reader at runtime, and whether the code can be explained on its own.
2. **Combine them into one calibrated probability, with reasons.** Every score comes with each check's contribution and the lines that caused it. Comments that state assumptions, and evidence that a human understood the code, lower the score.
3. **Act on the score.** A merge gate records, reviews or blocks opaque code that no one has shown they understand, and recommends tightening itself as incidents accumulate. Containment keeps opaque code out of other agents' context and training data, or replaces it with a simpler equivalent.

## What a working demonstration shows

A simulated corpus of 3,000 AI-generated functions with known, planted problems, so every result can be checked against the truth:

| Result | Simulated outcome |
|---|---|
| **Correct isn't understood** | Every function passes its tests and earns the top maintainability grade from standard complexity metrics (Radon). Among the 90 hardest to validate, the method flagged 87% |
| **More accurate than the alternatives** | Separated hard-to-validate code at 0.83 AUC, near the best possible 0.85, vs 0.77 for a single neural judge and 0.67 for complexity metrics |
| **The score means what it says** | Within 0.06 of the true probability on average, less than half the single judge's error |
| **Every score explained** | Each finding points to a line of code and the check that found it |
| **Humans close the loop** | A second reviewer's sign-off cut an example's score from 0.66 to 0.32; flagged merges without that evidence had 3.9 times the incident rate |
| **Opacity contained** | Replacing flagged code with simpler equivalents halved the opaque code a downstream agent learned to write, from 21% to 10% |

Results are from simulated data and show the method working, not results for any real codebase.

## The value to a partner

- **Faster releases without losing stability,** by gating merges on demonstrated understanding, not just green checks
- **Review effort aimed where it matters,** with each finding pinned to the lines that caused it
- **Audit-ready evidence** of what was reviewed, by whom, and why it was allowed to merge
- **Cleaner inputs for every agent downstream,** including the data future agents learn from
- **A differentiated capability** for code-review, developer-platform and AI-agent products

## Next step

A 30-minute call to walk through the working demonstration and discuss a pilot on your own agent-generated pull requests.

**Contact:** rjslogar@gmail.com
