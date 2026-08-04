# AFCA — Founder's Competence Assessment (full data)

Lähde: [redacted] AFCA-työkalu ("[redacted] Tools for Researchers"). Itsearviointi
perustajan tai perustajatiimin valmiudesta akateemiseen spin-outiin tai
tutkimuspohjaiseen startupiin. Synteesi EU:n **EntreComp**- ja **ResearchComp**
-kehyksistä sekä vertaisarvioidusta tutkimuksesta kaupallistamisosaamisesta.

Käyttää `founder-competence-self-assessment`-skilli. Alkuperäiset kohdat on
säilytetty englanniksi lähdedatan mukaisesti (ei käännetty, jotta pisteytys ja
tooltip-tekstit pysyvät tarkkoina).

## Pisteytyslogiikka

- Jokainen kohta pisteytetään asteikolla **1-7**.
- Osa-alueen raakapiste = kohtien painotettu keskiarvo (`weight`-kentät kohdissa,
  oletus 1.0, osa vahvempia kohtia painotettu 1.25).
- Normalisointi 0-100 %: `(raakapiste - 1) / 6 * 100`.
- Taso: **Expert** ≥75 % · **Advanced** ≥50 % · **Intermediate** ≥25 % ·
  **Foundational** <25 %.
- Kokonaispisteet = osa-aluepisteiden keskiarvo.
- Osa-alueiden painot (`weight`) kokonaispisteessä: Opportunity Orientation 0.12,
  Market & Customers 0.12, Financial Planning & Management 0.12, IP & Evidence 0.12,
  Venture Building 0.10, Partnerships & Networks 0.10, Communication & Influence 0.10,
  Execution & Roadmap 0.10, Regulatory & Quality 0.06, Founder Mindset & Teaming 0.06.

---

## 1. Opportunity Orientation (paino 0.12)

*"I connect a real user problem to a focused first use case and a clear edge, then
adjust fast when evidence changes."*

| ID | Kohta | Paino |
|---|---|---|
| O1 | I can state the target user's core problem in one simple sentence that non-experts understand. | 1.25 |
| O2 | I can list the main alternatives users rely on today and explain why they fall short for our case. | 1.0 |
| O3 | I can show our specific edge (e.g., performance, cost, time) with real evidence—not slogans. | 1.25 |
| O4 | We have chosen a focused first use case with a concrete early-adopter profile we can reach. | 1.0 |
| O5 | I can justify our pathway to impact (licensing vs. company) with practical reasons and constraints. | 1.0 |
| O6 | When evidence contradicts our thesis, we change direction quickly and visibly. | 1.0 |
| O7 | I consider ethical and sustainability implications when selecting and framing opportunities. | 1.0 |

## 2. Market & Customers (paino 0.12)

*"I learn directly from users, turn insights into product changes, and build early
traction in a reachable segment."*

| ID | Kohta | Paino |
|---|---|---|
| M1 | I can explain how our market works (size, structure, lifecycle, dynamics) in plain language. | 1.0 |
| M2 | I analyse customer needs from real interactions—not assumptions. | 1.0 |
| M3 | We keep an ongoing customer dialogue and log insights that actually guide decisions. | 1.0 |
| M4 | We have early traction that goes beyond interest (e.g., LOIs, pilot MoUs, real usage). | 1.0 |
| M5 | We prioritised one segment we can realistically access within 3–6 months. | 1.0 |
| M6 | Customer feedback leads to tangible changes in our proposition within weeks. | 1.0 |
| M7 | We track traction metrics that predict adoption or revenue, not vanity metrics. | 1.0 |

## 3. Financial Planning & Management (paino 0.12)

*(sisäinen `area_id`/nimi: "Economics & Funding")*
*"I build a simple unit economics view, tie funding to de-risking milestones, and
communicate numbers transparently."*

| ID | Kohta | Paino |
|---|---|---|
| ECO1 | I can read basic financial statements (P&L, balance sheet) and make sense of investment cases. | 1.0 |
| ECO2 | I can build a basic unit-economics model for our first offer (costs, price, gross margin). | 1.25 |
| ECO3 | I can design and compare alternative business/revenue models with pros, cons, and key risks. | 1.0 |
| ECO4 | I understand the trade-offs between non-dilutive funding and equity, including dilution. | 1.0 |
| ECO5 | I can calculate our next-phase funding need and link it to concrete milestones. | 1.25 |
| ECO6 | Our funding plan is structured around technical and market de-risking gates—not the calendar. | 1.0 |
| ECO7 | We test key sensitivities (price, adoption, costs) to see where the model breaks. | 1.0 |
| ECO8 | We have evidence of willingness-to-pay (quotes, budgets, pilot fees). | 1.0 |

## 4. IP & Evidence (paino 0.12)

*"I time publications and protection wisely, grasp FTO and licence basics, and keep
diligence-ready data packs."*

| ID | Kohta | Paino |
|---|---|---|
| IP1 | We plan publications with IP timing in mind (e.g., file before public disclosure). | 1.25 |
| IP2 | I can prepare a concise invention disclosure for our TTO that covers novelty and intended claims. | 1.0 |
| IP3 | I understand practical freedom-to-operate (FTO) and know when to involve IP counsel. | 1.0 |
| IP4 | I understand core licence terms (scope, field, territory, milestones) and their growth implications. | 1.0 |
| IP5 | Our data packs are reproducible and traceable, with methods, negatives, and limitations recorded. | 1.25 |
| IP6 | Together with TTO/advisors, we maintain a claims roadmap aligned with our strategy. | 1.0 |

## 5. Venture Building (paino 0.10)

*"I make the right path choice, set up roles, governance and equity fairly, and plan
the first hires/partners to execute."*

| ID | Kohta | Paino |
|---|---|---|
| VB1 | We chose licensing vs. spin-out after honestly assessing our capacity to execute. | 1.0 |
| VB2 | We are clear which roles founders can fill and which operator roles we must hire (e.g., CEO/COO/CTO). | 1.0 |
| VB3 | I understand cap-table basics (founder equity, vesting, ESOP) and how they drive incentives. | 1.0 |
| VB4 | We have defined an advisory/board cadence and who decides what. | 1.0 |
| VB5 | We have a plan for the first 2–3 critical hires/partners and the trigger conditions. | 1.0 |
| VB6 | We know the practical steps and documents needed to incorporate at the right time. | 1.0 |
| VB7 | We understand why a founders' agreement matters and what it should broadly cover. | 1.0 |
| VB8 | I can prepare a negotiation brief with trade-offs, red lines, and fallback options. | 1.0 |

## 6. Partnerships & Networks (paino 0.10)

*"I target the few people and organisations that change our trajectory, secure warm
intros, and keep relationships reciprocal."*

| ID | Kohta | Paino |
|---|---|---|
| P1 | I can name 5–10 high-leverage people or organisations and the value we exchange with each. | 1.0 |
| P2 | I understand which channel partners can give us market access and why they would care. | 1.0 |
| P3 | I can identify partners with the production or operational capabilities we critically need. | 1.0 |
| P4 | I can reliably secure warm introductions instead of relying on cold outreach alone. | 1.0 |
| P5 | Our first meetings have a clear agenda, a concrete ask, and agreed next steps. | 1.0 |
| P6 | We track a simple partner pipeline with stages and realistic probabilities. | 1.0 |
| P7 | I routinely offer helpful intros or resources to keep relationships strong and reciprocal. | 1.0 |

## 7. Communication & Influence (paino 0.10)

*"I craft evidence-first stories, answer diligence calmly, and tailor the message
without losing accuracy—so decisions move faster."*

| ID | Kohta | Paino |
|---|---|---|
| COM1 | I can deliver a tight 3-minute pitch covering problem, solution, proof, and the ask. | 1.0 |
| COM2 | We maintain an 8–12 slide deck that shows evidence, differentiation, and milestones (not just claims). | 1.0 |
| COM3 | I adapt our story for investors, corporate partners, and non-experts without losing precision. | 1.0 |
| COM4 | I handle typical diligence Q&A on IP, data, economics, and team clearly and calmly. | 1.0 |
| COM5 | We keep a crisp one-pager or teaser aligned to our latest proof points. | 1.0 |
| COM6 | I can communicate our financials (growth model, scenarios) clearly and transparently. | 1.0 |
| COM7 | We avoid hype and back key statements with numbers or third-party references. | 1.0 |
| COM8 | We keep a small backlog of upcoming proof points and the matching communications. | 1.0 |

## 8. Execution & Roadmap (paino 0.10)

*"I run a gated plan with real owners and risks, keep a steady demo cadence, and stop
weak work early to conserve runway."*

| ID | Kohta | Paino |
|---|---|---|
| EX1 | We set clear gate criteria (pass/kill/iterate) for technical and market milestones and write them down. | 1.25 |
| EX2 | Our time and cost estimates are credible, and we update them when facts change. | 1.0 |
| EX3 | We maintain a risk register with owners and active mitigations. | 1.25 |
| EX4 | We coordinate with the TTO and partners on one shared timeline and set of deliverables. | 1.0 |
| EX5 | We demo or validate on a regular cadence (e.g., monthly), not just at deadlines. | 1.0 |
| EX6 | We prioritise across lines of work and stop weak ones early. | 1.0 |
| EX7 | We use simple shared tools (boards/docs) so everyone stays aligned asynchronously. | 1.0 |

## 9. Regulatory & Quality (paino 0.06)

*"I map the relevant pathway, align our MVP and data to expectations, and make
documentation audit-ready without slowing speed."*

| ID | Kohta | Paino |
|---|---|---|
| R1 | We know which regulatory or QA frameworks apply to us (e.g., MDR/IVDR/FDA/AI Act) and why they matter. | 1.0 |
| R2 | We have a view of the simplest MVP that still meets early customer and regulatory expectations. | 1.0 |
| R3 | Our data and documentation plan reflects what the chosen pathway requires at each step. | 1.0 |
| R4 | We mapped critical regulatory steps with realistic time and cost implications. | 1.0 |
| R5 | We know when to onboard QA/RA specialists and have budgeted for them. | 1.0 |
| R6 | Our methods and records are captured to a standard an external party could audit. | 1.0 |
| R7 | We can produce a concise regulatory/QA summary suitable for investor diligence. | 1.0 |

## 10. Founder Mindset & Teaming (paino 0.06)

*"I keep momentum through uncertainty with small tests, reflective learning, healthy
conflict, and sustainable pace."*

| ID | Kohta | Paino |
|---|---|---|
| FM1 | We run small, safe-to-fail tests routinely and adjust course within weeks. | 1.0 |
| FM2 | We bounce back quickly from funding, IP, or partner setbacks and keep momentum. | 1.0 |
| FM3 | We use retros and premortems, and the lessons actually change our plans. | 1.0 |
| FM4 | We are honest about founder-operator fit and where we need external operators. | 1.0 |
| FM5 | We handle conflict productively and value diverse viewpoints in decisions. | 1.0 |
| FM6 | We engage mentors with clear preparation, specific asks, and follow-up. | 1.0 |
| FM7 | We protect wellbeing routines under pressure without sacrificing quality. | 1.0 |

---

*76 kohtaa yhteensä 10 osa-alueella. Käytä `founder-competence-self-assessment`-skilliä
arvioinnin läpivientiin ja tulosten tulkintaan.*
