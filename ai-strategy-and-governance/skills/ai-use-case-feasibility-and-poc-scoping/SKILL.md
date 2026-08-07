---
name: ai-use-case-feasibility-and-poc-scoping
description: "Determines the technical boundary conditions of an AI use case and scopes the PoC phase. Use when you need ai strategy & governance-level support for a comparable task."
---

# AI Use Case Feasibility & PoC Scoping

*Status: `scaffold` — see `../../../skills_index.json` and `../../../meta/maturity_levels.md`.*

## Purpose

Determines the technical boundary conditions of an AI use case and scopes
the PoC phase — narrow enough to run fast and cheap, but structured
enough that its result (pass or fail) actually tells you something about
production feasibility, instead of producing an impressive demo that
answers no real question.

## Anchored in research

- Perplexity research — PoC scoping through to productionization

## Method (draft — to be expanded)

1. **State the hypothesis the PoC is meant to test, as a single
   falsifiable sentence** — not "test whether AI can help with X," but
   e.g. "the model classifies inbound tickets into our 12 categories at
   ≥85% accuracy against a human-labeled sample." A PoC without an
   explicit hypothesis produces an opinion, not evidence.
2. **Set success criteria and a kill threshold before building
   anything**, together with the business owner, not after seeing the
   first results:
   - A quantitative success bar (accuracy, latency, cost per
     transaction, adoption rate) tied to the use case's Technical
     Feasibility and Business Impact scores from
     `../ai-opportunity-portfolio/SKILL.md`.
   - An explicit **kill criterion** — the result below which the PoC is
     called a "no" and the use case is retired or fundamentally
     re-scoped, not quietly extended for "one more sprint."
   - A named **human baseline** to compare against — an AI system that
     merely matches a mediocre existing process, without a cost or
     speed advantage, hasn't demonstrated feasibility.
3. **Assemble a golden test set before development starts.** A small
   (often 50–200 item), representative, human-labeled sample of real
   inputs, including edge cases and known failure modes — not just the
   easy majority case. Reusing this same set for evaluation prevents
   the common failure of quietly redefining "good enough" once actual
   outputs are seen.
4. **Separate what the PoC must prove from what it deliberately does
   not.** Explicitly out of scope for a PoC, unless the use case
   specifically requires it: production-grade security hardening,
   full-scale load handling, complete UI polish, integration with every
   downstream system. Naming these out loud up front prevents
   scope creep and prevents a stakeholder later treating "PoC passed"
   as "production-ready" (see
   `../../../prototyping-and-demonstration/skills/demo-framing-and-expectation-setting/SKILL.md`
   for framing this boundary in client/stakeholder communication).
5. **Identify the technical fit and risk profile up front:**
   - **Problem type** — classification, generation, prediction,
     extraction, or agentic decision-making? Each has different
     failure modes and evaluation methods.
   - **Data availability and quality** for the golden test set and any
     fine-tuning/retrieval corpus — is it accessible now, or does a
     data-access or cleaning task block the PoC before it can start?
   - **Hallucination/error tolerance** — reuse the SML error-tolerance
     assessment from
     `../task-level-decomposition-and-automation-fit/SKILL.md`
     if it exists for this task; a use case with low error tolerance
     needs a human-in-the-loop check built into the PoC design itself,
     not added afterward.
   - **Integration surface** — does the PoC need to read/write real
     systems, or can it run on an extracted, static dataset? A
     PoC that avoids live integration is faster but proves less about
     production feasibility — state which trade-off was chosen and
     why.
6. **Timebox the PoC explicitly** (typically 2–6 weeks) and name the
   decision point at the end: go to pilot, redesign and retest, or
   kill. An open-ended PoC without a decision date tends to drift into
   a permanent, unaccountable side project.
7. **Produce a structured PoC scope document**: hypothesis, success/
   kill criteria, golden test set description, explicit out-of-scope
   list, technical risk notes, timebox and decision point (see
   `../../references/` once a template is added).
8. Validate the scope with both the technical team (is it buildable in
   the timebox) and the business owner (does passing it actually
   justify a production investment) before starting.

## What this skill does NOT do

- Doesn't make the final decision for you — it produces a structured
  draft to support a human decision.
- Doesn't confirm figures, market data, or competitor data from
  memory — it uses the inputs you provide, or marks an assumption
  clearly (`[assumption — verify]`).
- Doesn't do technical architecture design or model selection for
  you — it scopes the PoC's boundaries and success criteria, not the
  implementation.
- Doesn't guarantee a PoC that passes will succeed in production — a
  PoC deliberately excludes scale, security-hardening, and full
  integration; passing it reduces risk, it doesn't eliminate it.

## [OWNER INPUT — to be completed]

This skill is a structural draft (`maturity: scaffold`). It doesn't yet
contain your own experience, heuristics, or case examples. Fill in
here:

- your own rules of thumb and heuristics for this technique — e.g.
  typical timebox lengths and golden-test-set sizes by use-case type
- concrete templates (into `../../references/`, e.g. a PoC scope
  document template)
- reference cases / your own examples
- what this skill deliberately does *not* do (guardrails, common
  mistakes) — add to the list above

Once this section is filled in and validated in practice, update the
`maturity` field in `skills_index.json` to `draft`, `validated`, or
`canonical` (see `../../../meta/maturity_levels.md`). **Don't add new
fields to the frontmatter** — `name` and `description` are the only
ones allowed (see `../../../meta/frontmatter_schema.md`).

## Continue from here

- Next in this pack: `../responsible-ai-and-governance-check/SKILL.md`
  — checks the regulatory, risk, and ethics dimensions of an AI
  initiative. Deeper EU AI Act compliance analysis requires separate
  regulatory expertise.
- Once the technical scope is done and the PoC needs to be built and
  presented: `../../../prototyping-and-demonstration/skills/rapid-prototype-and-vibe-coding-craft/SKILL.md`
  (prototyping) and `../../../prototyping-and-demonstration/skills/demo-framing-and-expectation-setting/SKILL.md`
  (turning the same scope into a client-communication frame — a
  different question from this skill's technical scoping, use both
  together).
- A ready-made skill chain for this situation: see `../../../playbooks/`
- This pack's shared guardrails: `../../CLAUDE.md`

## References

- `../../references/` — the pack's shared background material
- `../../CLAUDE.md` — the pack's shared guardrails
