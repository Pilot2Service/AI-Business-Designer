# Prototyping & Demonstration — shared guardrails

General guardrails (disclaimer, no fabricated numbers, premise-checking, making
maturity visible) are collected in one place: **see
[`../meta/shared-guardrails.md`](../meta/shared-guardrails.md) — read that first.**
This file only contains what's genuinely specific to this pack.

---

## A demo is not a product — say so out loud, every time

This pack's core risk is **conflating proto/demo success with production
readiness.** A quickly built, "vibe-coded" prototype proves an idea works in
principle — it does not prove the solution is safe, scalable, maintainable, or
secure in production. In every output this pack produces:

- Clearly mark what is a demo-level finding ("worked on 3 test cases in a
  controlled environment") versus a production-level claim ("works reliably in
  all cases") — never let the two blur together.
- Remind that AI-assisted ("vibe-coded") code typically contains hallucinated
  interfaces, incomplete error handling, and weak authentication/authorization
  checks until a human has separately reviewed it — this applies especially to
  any demo that touches real data or is presented in a live environment.
- Never present a demo to a customer as "almost a finished product" — always
  frame it for what it actually is (a proof of concept, not a production
  application).

## PoC / Pilot / MVP — different terms, different questions

These are often used interchangeably by mistake. They answer different
uncertainties — don't conflate them:

- **PoC (Proof of Concept)** — answers "does this work technically at all,
  with representative data?" Time-boxed, low-risk, not yet production data or
  load.
- **Pilot** — answers "does this work with real people and real operational
  conditions?" Assumes technical feasibility and value have already been
  predicted — the pilot confirms it in practice.
- **MVP (Minimum Viable Product)** — answers "what should be built next, based
  on real user feedback?" A product-development stance, not a proof stage.

Use the correct term and don't use them as synonyms in customer
communication — the wrong term creates the wrong expectation about budget,
timeline, and what happens next.

## The "pilot purgatory" risk is real, and it's countered with framing, not code

Research (McKinsey, BCG, IDC, MIT among others) repeatedly shows that a large
share (estimates vary by source, roughly 80–95%) of enterprise AI pilots never
reach production — the bottleneck is typically operational (workflow
redesign, management commitment, scale-up investment), not technical. This
pack's skills can't solve that at the demo stage, but they MUST make the risk
visible already in the demo/PoC framing (see
[`skills/demo-framing-and-expectation-setting/SKILL.md`](skills/demo-framing-and-expectation-setting/SKILL.md))
— don't let the customer believe that a successful demo automatically means
production is next.

## No fabricated numbers in this pack — scale-up assumptions in particular

In addition to the general principle (`shared-guardrails.md`): a PoC-scale
result (e.g. "saved 2 hours across 10 cases") does not extrapolate in a
straight line to production scale without an explicit, clearly marked
assumption about why the scale-up would be linear.

## Maturity in this pack

This pack's skills are currently at `maturity: scaffold` (see
[`../skills_index.json`](../skills_index.json) and
[`../meta/maturity_levels.md`](../meta/maturity_levels.md)) — the structure
and research anchoring are solid (Great Demo! methodology, vibe coding
practices, PoC/Pilot/MVP literature, Amazon Working Backwards, prototype
fidelity research), but the owner's own validated consulting experience
hasn't been attached yet.

## Shared standards

See [`../meta/frontmatter_schema.md`](../meta/frontmatter_schema.md) (what's
allowed in a SKILL.md frontmatter) and
[`../meta/skill_design_principles.md`](../meta/skill_design_principles.md)
(what a good skill in this repo has to pass).
