# Public Sector AI Service Design

A lens, not a rebuild: this pack does not re-teach AI opportunity scoring,
business case building, or stakeholder mapping — the core packs already
cover that. It adds the specific things that change when the client is a
city, a regional administration, a public agency, or a non-profit rather
than a private company: public value instead of pure ROI, elected
officials and budget cycles instead of a single sponsor, procurement law
instead of a purchase order, and a decision body that has to defend its
choice publicly.

Typical use case: a consultant or in-house designer is scoping an AI
initiative for a municipality or public agency — screening which AI ideas
are actually worth pursuing, working out who really needs to say yes,
navigating procurement and funding constraints, and building a case and a
decision document that a public board can actually approve without it
stalling in political limbo.

## Sources

This pack combines two layers:

1. **The owner's own commercialisation methodology for public-sector pilot
   projects** (the Pilot2Service framework, a published, commercially
   licensed toolkit — see `references/source-notes.md` for exactly what
   was adapted and how). The public-sector-specific material — most
   importantly a six-element decision-readiness model for presenting
   options to public decision-makers — is rewritten here at the level of
   transferable method and principle, not reproduced from the source
   text. The deeper, step-by-step workbook version of this framework
   (20 planning modules, a 3-sprint project model, full deliverable
   templates) is commercial IP and out of scope for this pack; see the
   note in `references/source-notes.md` if a future, more extensive
   specialisation pack is built from it.
2. **General public-sector management and public-value literature**
   (public value theory, public procurement practice, digital-government
   AI guidance) used to frame the opportunity-screening, procurement, and
   regulatory-guardrail skills that are new to this pack rather than
   adapted from the owner's material.

## Client profile

Public sector organizations, regional administrations and municipalities,
non-profits, and any private company whose customer is one of these —
i.e. anyone designing or advising on an AI-enabled public service, not
just theorizing about "AI in government" abstractly.

## Skills in this pack

### Opportunity and business case

| Skill | Description |
|---|---|
| `ps-ai-opportunity-screening-for-public-value` | Screens a raw AI idea for public-sector fit before it enters formal scoring: mandate alignment, public-value type, and the "would this survive being on the front page" test. |
| `ps-public-value-business-case-framing` | Reframes the business case around the four public-value types (efficiency, service quality, equity, trust/legitimacy) instead of defaulting to a private-sector ROI story. |

### Stakeholders, procurement, and rules

| Skill | Description |
|---|---|
| `ps-stakeholder-and-political-landscape-mapping` | Extends stakeholder/RACI mapping with the distinct public-sector actor types (elected officials, civil servants, unions, oversight bodies, citizens) and their veto points. |
| `ps-procurement-and-public-funding-navigation` | Flags when an AI idea has crossed from "just build it" into procurement-law and public-funding territory, and what that changes about timeline and design freedom. |
| `ps-regulatory-and-ethical-guardrails-for-public-ai` | Frames the distinct regulatory and ethical stakes of public-facing AI — higher transparency/accountability bar, disparate-impact risk, due-process concerns — and where to get real regulatory expertise instead of guessing. |

### Decision and impact

| Skill | Description |
|---|---|
| `ps-decision-readiness-and-public-communication` | A six-element model for presenting an AI proposal so a public decision body can actually approve it: options, relevancy/focus, trust, urgency, strategic alignment, and public-sector decision dynamics. |
| `ps-community-and-equity-impact-assessment` | Checks an AI service design for differential impact across community groups before launch — digital divide, accessibility, disparate treatment. |

## Logical flow of skills

```
ps-ai-opportunity-screening-for-public-value
        │
        ▼
ps-stakeholder-and-political-landscape-mapping ──► ps-procurement-and-public-funding-navigation
        │                                                    │
        ▼                                                    ▼
ps-regulatory-and-ethical-guardrails-for-public-ai   ps-community-and-equity-impact-assessment
        │                                                    │
        └───────────────────► ps-public-value-business-case-framing
                                       │
                                       ▼
                    ps-decision-readiness-and-public-communication
```

## What this pack does NOT do

- It doesn't replace the core AI-strategy, business-case, or
  stakeholder-mapping skills — it sits on top of them and should be used
  alongside `ai-strategy-and-governance`, `business-case-and-analysis`,
  and `change-and-communication`, not instead of them.
- It doesn't give legal advice on procurement law or the EU AI Act.
  `ps-procurement-and-public-funding-navigation` and
  `ps-regulatory-and-ethical-guardrails-for-public-ai` tell you *when*
  you've hit a question that needs a lawyer or procurement specialist —
  they don't answer that question themselves.
- It doesn't cover the deep, step-by-step mechanics of moving a completed
  pilot through commercialisation planning (IP inventory, results
  ownership, a full exploitation plan) — that is a separate, larger body
  of work the owner is deliberately holding back for now (see
  `references/source-notes.md`).
