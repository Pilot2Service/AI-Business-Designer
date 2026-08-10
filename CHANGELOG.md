# Changelog

## Unreleased

**GitHub Pages landing site.** Added `docs/index.html` — a single-page,
no-build-step landing site mirroring the trust-mechanism framing from the
README (anchored-not-assumed, visible maturity, explicit scope limits,
human decision gate), plus tables for all 8 core packs, 3 specialisation
packs, and 4 delegatable agents, all linking through to their GitHub
detail pages. Includes a generated `docs/og-image.png` for social-preview
cards and a `docs/.nojekyll` marker so GitHub Pages serves the file
directly without a Jekyll build. Root `README.md` now links to the live
site. Requires enabling GitHub Pages once in repo Settings (Source:
Deploy from a branch, `main` / `docs`) — see the setup note in the PR/commit
this shipped in.

## 0.18.0 — 2026-08-07

**Full English translation.** The entire repo — all 8 core packs, all 3
populated specialisation packs, `meta/`, root docs (QUICKSTART.md,
CONTRIBUTING.md, AGENT_GUIDE.md, CHANGELOG.md, templates/, playbooks/),
`marketplace.json`/`plugin.json` descriptions, and the validation scripts'
console output — was translated from Finnish to English. English fully
replaces Finnish; this is not a bilingual repo. Piloted first on the
`strategic-thinking` pack to establish the pattern, then applied to the
rest.

Translation approach was tied to each skill's `source_layer` in
`skills_index.json`, not applied uniformly:

- **`source_layer: owner`** skills (the pack owner's own validated
  consulting IP — all of `research-commercialisation`, all of
  `ai-native-startup-design`, 3 skills in `opportunity-recognition`, 3 in
  `business-model-canvas`, `strategy-canvas-and-value-curve` in
  `business-design-frameworks`) were translated **faithfully, with no
  content enrichment** — every number, criterion, and step preserved
  exactly, since inventing additions would misrepresent real, hard-won
  expertise.
- **`source_layer: research` + `maturity: scaffold`** skills (public
  framework anchors, no owner experience yet) were translated **and
  enriched**: generic 4-step placeholder method sections were replaced
  with concrete, technique-specific methods genuinely grounded in each
  skill's named research anchor (Porter, Kirzner, Minto, Ward & Daniel,
  ISO 31000, BABOK, Prosci/ADKAR, Mendelow, and others already present or
  newly and accurately cited). `maturity` and `source_layer` values were
  never changed by this enrichment — richer public-framework grounding is
  not the same as the owner's own field-validated experience.

The README's "A note on language" section was rewritten to reflect that
skill content is now in English. `skills_index.json` regenerated;
`scripts/validate.py` passes with no errors (8 packs, 4 agents, 78
skills).

## 0.17.0 — 2026-08-07

**Infrastructure update** — a meta-level comparison analysis
(`claude-for-legal-finland` and other well-built open Claude skills repos)
showed that in content (78 skills) this repo was already in the same size
class, but behind on infrastructure: no CI validation, no shared root-level
standards document, no stats line in the README, no delegatable agent
layer, no single-path getting-started guide. This version fixes all of
that.

**CI validation.** `.github/workflows/validate.yml` runs `generate_index.py`
+ `validate.py` on every push and pull request — also checks that
`skills_index.json` hasn't drifted from what's actually on disk. Broken
frontmatter or an out-of-sync index blocks the merge automatically.

**Shared standards — one source, not twelve copies.**
`meta/shared-guardrails.md` is now the single source for the recurring
guardrails (disclaimer, no fabricated numbers, premise check, making
maturity visible, agent read-only principle). All 11 packs' `CLAUDE.md`
files (8 core packs + 3 populated specialisation packs) refactored to
reference this — leaving only genuinely pack-specific content. Reduces
maintenance burden and removes drift risk when guardrails are updated.

**QUICKSTART.md.** A single-path getting-started guide: install the
marketplace → pick one pack based on the task → run one skill → what you
should get back (structured draft, visible assumptions, visible maturity,
no final decision).

**Four delegatable audit agents** (`agents/*.md`, read-only, invoked via
the Task tool) — analogous to the six agents in the
`claude-for-legal-finland` repo, but for the business-design context: a
skill produces the analysis, an agent challenges or cross-checks it before
it moves into a decision.

- `business-case-and-analysis/agents/assumption-stress-tester` — an
  adversarial second opinion on a finished business case; a different role
  from the `assumption-and-evidence-audit` skill (which is the method used
  WHILE BUILDING the case — the agent is an independent check AFTER).
- `opportunity-recognition/agents/market-sizing-cross-validator` —
  cross-checks a TAM/SAM/SOM calculation using top-down and bottom-up
  methods, gives a confidence level (HIGH/MODERATE/LOW).
- `business-design-frameworks/agents/competitive-blind-spot-scanner` —
  looks for blind spots in a competitive/positioning analysis (five forces,
  strategy canvas); works on outputs from both its own pack and the
  `opportunity-recognition` pack.
- `ai-strategy-and-governance/agents/ai-initiative-readiness-auditor` —
  audits how rigorously an AI initiative's `ai-opportunity-portfolio`
  scoring and `responsible-ai-and-governance-check` checklist were done
  before approval.

`scripts/validate.py` extended to check agent frontmatter (its own,
slightly more permissive field set than a skill's: `name`+`description`
required, `tools`/`model` allowed) and to catch agents missing from the
index. `scripts/generate_index.py` now also indexes agents into
`skills_index.json`'s new `agents` field.

**External data MCPs — documented, not a dependency.**
`meta/external-data-mcp.md` lists candidates (primarily the Market Sizing
MCP Server / TAM-MCP-Server, 8 economic data sources: Alpha Vantage, BLS,
Census, FRED, IMF, Nasdaq Data Link, OECD, World Bank) that the
`market-sizing-tam-sam-som` skill and the `market-sizing-cross-validator`
agent can use if one happens to be connected in the user's environment.
Not required — the repo remains fully standalone, as established in
v0.15.0.

**README** got a measurable stats line ("8 core packs · 3 populated
specialisation packs · 78 skills · 4 audit agents · self-contained ·
CI-validated · MIT"), a new Agents table, and a link to QUICKSTART.md.

## 0.16.0 — 2026-08-06

**New core pack**, `data-strategy-and-literacy/` (6 skills, `maturity:
scaffold`, `source_layer: research`): built from user-supplied data
strategy and data literacy research, this section covers how an AI
Business Designer "reads" data — what role data plays in an organization,
how critically it needs to be read, how to communicate about it, and how
to use it strategically and monetize it. Enriched with consultant
heuristics and decision frameworks on top of the source material (at the
user's request), e.g. resale/flywheel/defensibility tests, the
Offense/Defense framework (Davenport & Bean), a DIKW-based
Data→Information→Insight→Action ladder, a four-point Data Flywheel
feasibility checklist, and a Data Readiness × Strategic Value
prioritization matrix.

6 skills:

- `data-role-diagnosis` — diagnoses whether data functions as an enabler
  or a strategic asset; resale, flywheel, and defensibility tests, the
  Offense/Defense framework.
- `data-literacy-competency-assessment` — assesses an organization's data
  literacy with a DALI-type four-quadrant framework (Understanding,
  Acting On, Influencing, Ethics) by role, plus a four-stage maturity
  ladder.
- `data-bias-and-quality-critical-reading` — reads a dataset critically:
  a five-type bias taxonomy (selection, survivorship, historical,
  measurement, aggregation), a vanity-vs-actionable-metric test.
- `data-storytelling-and-business-translation` — translates data/model
  logic through the Data→Information→Insight→Action ladder and a "so
  what" test into a decision-ready story (Minto Pyramid Principle).
- `data-ai-strategy-design-and-prioritization` — shapes a Data & AI
  strategy with a Driver Tree, separates "what we can do now" from "what
  needs to be built for the future" (Agile Value Assessment), prioritizes
  with a Data Readiness × Strategic Value matrix.
- `data-monetization-model-selection` — chooses a direct (DaaS,
  Insight-as-a-Service, data exchange) or indirect (product enrichment,
  resource optimization, risk minimization, Data Flywheel) monetization
  model via a decision tree.

Cross-linked to `ai-strategy-and-governance/ai-opportunity-portfolio` (the
Data Readiness dimension is developed further in this pack),
`change-and-communication/executive-narrative-and-storyline` (general
storyline vs. this pack's data-specific application),
`business-case-and-analysis/roi-npv-sensitivity-model`, and
`specialisation-packs/business-model-canvas` (data monetization patterns).
`playbooks/ai-initiative-scoping.md` updated: `data-role-diagnosis` added
as an optional first step before `ai-opportunity-portfolio` scoring.

Total now 78 skills, 8 core packs + 3 populated specialisation packs.

## 0.15.0 — 2026-08-06

Independence and anonymization cleanup requested by the owner ahead of the
public GitHub release: anyone should be able to install and use the repo,
so it must not contain links outside the repo, nor direct references to
the owner personally, to their other private projects, or to third-party
companies/reports. Named, publicly known academic or methodological
frameworks (Porter, Kim & Mauborgne, Kirzner, Brynjolfsson & Mitchell,
BABOK/PMI/SFIA, Cohan, Bryar & Carr, Hagel & Singer, MECE) were kept
unchanged — only company/personal source attributions and broken external
paths were removed.

- **External paths removed.** References in 38 files to two research
  background documents outside the repo removed. 13 references to another
  mounted folder or Cowork plugin not belonging to this repo (a previous
  private research repo, plus notes referencing regulatory/legal-domain
  plugins) replaced with generic mentions without hardcoded paths. One
  absolute filesystem path (containing a username) removed entirely.
- **Personal and company names removed/genericized**, content preserved:
  the owner's own name (~40 files) replaced with "the owner"; the owner's
  own service brand (60+ mentions, including 3 renamed reference files and
  their cross-references) genericized while preserving the method/template
  content; an external workshop organizer's name removed from 13 files
  (file renamed); company-specific citations from market research reports
  (two named AI use-case reports, consultancy names, a single public
  pattern platform) genericized — the pattern library's 13 pattern
  definitions, diagnostic questions, and risk lens stayed unchanged, only
  the source attribution changed.
- **`skills_index.json` updated** on the same principles (manual edit,
  since `grounded_in` fields aren't generated from SKILL.md).
- 60+ files touched in this version overall. Skill count, structure, and
  maturity levels didn't change — only source attribution and
  accessibility changed.

## 0.14.1 — 2026-08-06

A full validation/audit of the entire skills pack requested by the owner
(depth, clarity, gaps/overlaps, documentation, GitHub release readiness).
Findings compiled into a separate audit report. This version fixes all
mechanical/objective findings from the audit report:

- **33 broken relative links fixed** (wrong `../` depth, introduced in
  earlier sessions specifically when specialisation-pack skills linked to
  core packs — a specialisation-pack skill is one folder level deeper than
  a core-pack skill, which was missed in 29 links).
- **3 file paths broken by a mid-string line break fixed** (a long path
  had broken mid inline-code-block onto a new line, e.g. a workshop-source
  filename reference).
- **`meta/competency_map.md` updated** — rows for the
  `business-design-frameworks` and `prototyping-and-demonstration` packs
  were missing.
- **`playbooks/ai-initiative-scoping.md` updated** —
  `prototyping-and-demonstration` pack skills added to the chain between
  feasibility scoping and business case building.

**Identified but NOT fixed in this version** (fixed later in v0.15.0): 41
SKILL.md files referenced two research background documents located
OUTSIDE the repo — these links worked in the local workspace but not in a
GitHub clone. Likewise, 13 references pointed to either another Cowork
plugin not belonging to this repo, or another mounted folder.

## 0.14.0 — 2026-08-06

**New core pack**, `prototyping-and-demonstration/` (5 skills, `maturity:
scaffold`, `source_layer: research`): built at the user's request, this
section covers demonstration skills — how an AI consultant quickly builds
a working concept, correctly frames a demo/prototype, presents an
opportunity convincingly, and ties the result back into a business case
and ROI calculation. Anchored in broader external research (at the user's
request) before building:

- Cohan, Peter E. / Pearce, Paul H. — "Great Demo! Five Imperatives"
  (Discovery, Demo Prep, Demo Delivery, Documentation, Debrief; Situation
  Slide, Critical Business Issue, "do the last thing first" / inverted
  pyramid)
- Bryar & Carr — Amazon's "Working Backwards" method and the PR-FAQ
  document
- Vibe-coding best practices, 2026 (tool selection, iteration cycle,
  PRD-first, known risks: hallucinated interfaces, auth gaps)
- The PoC vs. Pilot vs. MVP distinction and "pilot purgatory" research
  (McKinsey/BCG/IDC/MIT syntheses: 80-95% of enterprise AI pilots don't
  reach production, the bottleneck is operational, not technical)
- Prototype-fidelity research (low vs. high fidelity)
- Research synthesis on translating a demo/PoC into ROI (technical
  performance vs. business impact, transparency of the assumption chain,
  fit of the ROI mechanism to the customer's organization)

5 skills: `opportunity-visioning-with-pr-faq` (Working Backwards/PR-FAQ),
`rapid-prototype-and-vibe-coding-craft` (fast, disciplined prototyping),
`demo-framing-and-expectation-setting` (PoC/Pilot/MVP framing, the
"proves/doesn't prove" pair, guarding against pilot purgatory),
`demo-delivery-and-storytelling` (applying Great Demo!),
`demo-to-business-case-bridge` (bridge into the business-case-and-analysis
pack).

Cross-linked to
`ai-strategy-and-governance/ai-use-case-feasibility-and-poc-scoping`
(technical scoping vs. customer-communication framing — a different
question), `change-and-communication/executive-narrative-and-storyline`
(general storyline vs. this pack's demo/visioning specialization), and
`business-case-and-analysis/business-case-builder` and
`roi-npv-sensitivity-model` (receive this pack's validated ROI inputs).

## 0.13.0 — 2026-08-06

AI use-case pattern library: at the user's request, a dedicated section
for systematically identifying AI use cases was added to the skills pack.
The starting point was the user-described **Capability Pattern Mapping**
abstraction method (a set of superficially different cases → one named,
industry-independent pattern → a diagnostic question for a new context)
and two user-supplied/identified primary sources: a broad industry report
(2026 edition, 130 use cases across 6 industries, a responsible-AI risk
framework) and a second, independent AI use-case compilation (63 use
cases, 16 functions). 81 cases were extracted and verified from the first
report by text extraction (5 of 6 industries) — every example reference in
this version is drawn directly from that extraction, not produced from
memory.

**Enriched** `opportunity-recognition/pattern-and-analogy-connector`
(stays `scaffold`): filled in a general, industry-independent Capability
Pattern Mapping method as a 7-step structure (collect 3+ different
observations → four-question abstraction of input/actor/cognitive
core/outcome → a one-sentence pattern definition → a diagnostic question →
coverage/sharpness testing → use in a new context → validation),
illustrated with the user's own invoice/customs/CV-document example.

**1 new reference file**,
`ai-strategy-and-governance/references/ai-capability-pattern-library.md`:
13 named AI capability patterns (e.g. multi-agent real-time trade-off
optimization, unstructured document validation and anomaly detection, a
persistent personal advisor/concierge agent, predictive equipment alerting
and autonomous intervention, vision-guided physical handling and quality
control, autonomous mobile physical operation, AI-assisted software
development, and others) — each with: a definition, a diagnostic signal
question, an AI type (Agentic/Physical/other), 3-6 real example cases drawn
from the primary source extraction, and a responsible-AI risk lens.
Includes a transparent source note and cross-check against a second source
(4 functions accounting for ~75% of value: customer operations, marketing
& sales, software development, R&D — all 4 covered in the patterns).

**1 new skill**, `ai-strategy-and-governance/ai-capability-pattern-matching`,
`maturity: scaffold`, `source_layer: research`: teaches how to use the
pattern library as a top-down alternative to the
`task-level-decomposition-and-automation-fit` skill's bottom-up approach
when assembling a raw list before `ai-opportunity-portfolio` scoring.
Cross-linked to both packs (`ai-opportunity-portfolio`,
`task-level-decomposition-and-automation-fit`,
`pattern-and-analogy-connector`).

## 0.12.0 — 2026-08-06

Analyzed a user-supplied research report, "Methods, frameworks, and
competencies for identifying AI opportunities and capacity in business"
(2026, a synthesis of several industry AI-capability reports and
Brynjolfsson & Mitchell research). Used to enrich and expand the
`ai-strategy-and-governance` pack.

**2 new skills**, `maturity: scaffold`, `source_layer: research`:

- `task-level-decomposition-and-automation-fit` — breaks roles/processes
  down to task level (People Path + Process Path Dual Decomposition) and
  classifies each task as Automate/Augment/Human-Only using SML criteria
  (Brynjolfsson & Mitchell); also includes process mining, task mining,
  and cognitive-friction analysis as a data-driven alternative to
  interviews
- `ai-discovery-engagement-design` — productizes the entire identification
  process into a billable or internal discovery engagement: a 4-phase
  structure, two service products (AI Opportunity Sprint, AI Maturity &
  Opportunity Audit), a standardized deliverable set

**Fully rewritten** `ai-opportunity-portfolio` (stays `scaffold`): the
earlier lightweight three-criterion triage replaced with a formal
5-dimension scoring model (Business Impact, Technical Feasibility & AI
Fit, Data Readiness, Strategic Alignment, Speed to Value &
Governance/Risk), a 2×2 prioritization matrix (Quick Wins/Strategic
Bets/Hard-Low Value/Deprioritize), a Value-Play taxonomy for transformative
opportunities (Zero-Marginal-Cost Expertise, Hyper-Personalization at
Scale, Outcome-Based/Agentic Business), and BCG's Deploy-Reshape-Invent
classification — explicitly distinguished from the `ai-capability-roadmap`
skill's Horizon split to avoid confusion.

**Enriched** `ai-capability-roadmap`: a three-horizon structure (0-6mo
efficiency / 6-18mo transformation / 18-36mo new business) and the AI
Target Operating Model (ATOM) / Readiness Scorecard concept (describing
the human-AI division of labor and the organization's readiness level).

**Lightly enriched** `ai-native-business-model-canvas`: a new explicit
"Human-AI Interaction Model" section (Copilot/Autonomous Agent/Generative
Interface), cross-linked to the `closed-loop-process-and-human-oversight-
design` and `ai-native-conversational-os-design` skills
(specialisation-packs/ai-native-startup-design), clarifying that
interaction form and oversight level are two separate questions.

Also: the pack's `CLAUDE.md` gained a clear distinction between four
similar three-/four-way splits (Automate/Augment/Human-Only, Quick
Wins/Strategic Bets/Hard-Low Value/Deprioritize, Deploy/Reshape/Invent,
Horizon 1/2/3) to prevent confusion. Pack README updated with a logical
skill flow diagram. Pack grew from 8 to 10 skills. Total now 66 skills.

## 0.11.0 — 2026-08-06

Analyzed an external "AI-first SaaS Product workshop" note uploaded by the
owner, and used it to enrich and expand the
`specialisation-packs/ai-native-startup-design/` pack. The note contains
both a general method and a full worked example the owner went through on
their own service product (the "Decision Coach" MVP).

**Enriched** `customer-vision-to-jtbd` (stays `validated`/`owner`):
verb-driven JTBD framing, the Need Themes table expanded (with "Type" /
"why" / "related JTBD" columns), the earlier single AI-advantage point
replaced with a 5-criterion NMB score (Need Depth, Frequency, Market
Coverage, Business Strength, AI Advantage → Differentiator vs. Table
Stake), a new step: explicit selection criteria for the AI-differentiator
need (the "AI wedge").

**3 new skills**, `maturity: draft` (applied once so far, to the owner's
own case — not yet as broadly validated as the pack's other skills),
`source_layer: owner`:

- `ai-differentiator-solution-ideation` — ideating 3 mutually different
  AI-native solution directions for a chosen AI wedge, through three
  lenses (competitor, future, connect-the-dots)
- `rice-scoring-and-mvp-synthesis` — RICE scoring (Reach, Impact,
  Confidence, Effort) to select an MVP + MVP definition + positioning
  statement + "why we win" claims
- `ai-native-conversational-os-design` — designing a conversational
  interface architecture (Intent → Strategy Cards → Clarification →
  Output Cards → Mission → Agent Execution) + 5 AI-first product
  principles ("5 shifts": click > question, menus > prompts, dashboards >
  dialogue, manual actions > agents, screens > chat + cards)

Also: `references/ai-first-saas-workshop-source.md` (new source, explains
why `draft` rather than `validated`), `cases/ai-decision-coach-mvp-case.md`
(a full worked example — the first file in the pack's `cases/` folder),
`references/prompt-library.md` expanded (prompt 6 updated + new prompts
8-10), the pack's `README.md`/`CLAUDE.md` updated to make the two-tier
maturity visible, cross-linked to the `ai-native-opportunity-scan` and
`ai-buildable-prd-writing` skills. Pack grew from 5 to 8 skills. Total now
64 skills.

## 0.10.0 — 2026-08-05

New specialisation pack `specialisation-packs/business-model-canvas/` (7
skills), built from two sources supplied by the owner:

- A public pattern platform's machine-readable 159-pattern innovation
  library (`business-model-patterns.json`, downloaded 2026-08-05) —
  converted into a full markdown reference,
  `references/bmc-innovation-pattern-library.md`
- The owner's own, non-public research work capturing BMC consulting
  expertise, split into an expert layer (an April 2026 consulting
  interview) and a research layer (a Jeffries/Williams/van der
  Linden/Blank/Ash Maurya synthesis)

3 skills `maturity: validated`, `source_layer: owner` (from the expert
layer):

- `bmc-innovation-pattern-matching` — identifying 3-5 compatible
  innovation patterns from the 159-pattern library using the expert's own
  four-part taxonomy (Financial/Operative/Value-based/Experience Model
  Innovations)
- `bmc-canvas-clarity-and-iteration` — variation logic, spotting when a
  session is stuck, the "clarity > depth" readiness criterion
- `bmc-antipattern-and-misunderstanding-correction` — 5 working-style
  antipatterns + 4 client misunderstandings about the BMC's role

4 skills `maturity: scaffold`, `source_layer: research` (from the research
layer):

- `bmc-session-facilitation-design` — session structure, starting point,
  fill-in order, evidence color-coding
- `bmc-canvas-diagnostic-reading` — 6 diagnostic rules (the Hook Rule and
  others) + a four-dimension quality rubric
- `bmc-tool-switching-decisions` — when to move to the VPC, Lean Canvas,
  Mission Model Canvas, or financial modeling
- `bmc-client-language-translation` — interpreting client statements + 3
  common concept misunderstandings

Also: `references/bmc-source-material-notes.md` (the two-layer background
of the source material), a pack-specific `CLAUDE.md` (mixed-maturity
disclosure) and `README.md`, a `marketplace.json` entry
`specialisation-business-model-canvas`. Total now 61 skills.

## 0.9.0 — 2026-08-05

A coverage audit against the "AI Business Designer in the Age of AI"
research report (the same report as in 0.5.0, now fully checked against
the whole repo via grep + content review). 4 genuine gaps identified and
filled (`maturity: scaffold`, `source_layer: research`):

- `business-design-frameworks/customer-journey-and-ai-touchpoint-mapping`
  — mapping service journeys and placing AI at friction points in a
  value-adding way
- `strategic-thinking/second-and-third-order-effects-mapping` —
  anticipating a decision's second/third-order effects (customer
  behavior, competitor reactions)
- `ai-strategy-and-governance/shadow-ai-response-and-safe-adoption` —
  mapping unsanctioned AI tool use and safely formalizing it
- `ai-strategy-and-governance/ai-output-curation-and-quality-control` —
  quality control of AI outputs, the shift from author to curator
- The rest of the report was confirmed already covered: AI opportunity
  identification, the AI-native Business Model Canvas, business case
  building, responsible AI, hypothesis-driven thinking, scenario planning,
  facilitation, agentic AI (see the `ai-native-startup-design` pack)
- Total now 54 skills

## 0.8.0 — 2026-08-05

Second fully populated specialisation pack —
`specialisation-packs/ai-native-startup-design/`, converted from an
**AI-native Business Design** workshop the owner facilitated for
pre-startup founders (the owner's own service, held 2026-06-01/02, the
owner's private material):

- 5 new skills (`maturity: validated`, `source_layer: owner`):
  `ai-native-opportunity-scan` (agentic/closed-loop opportunity discovery
  and prioritization), `customer-vision-to-jtbd` (ICP/JTBD/Need
  Themes/AI-advantage scoring), `ai-buildable-prd-writing` (a PRD handed
  to a build agent + supporting documents), `closed-loop-process-and-
  human-oversight-design` (the open/closed loop mental model +
  human-in/on/outside-the-loop), `ai-native-tool-stack-selection` (a
  12-category tool-selection heuristic)
- `references/workshop-source.md`, `prompt-library.md` (the workshop's
  prompts), `tool-category-map.md` (a timestamped tool-category map, June
  2026)
- Cross-linked to the `ai-strategy-and-governance` pack's
  `ai-opportunity-portfolio` and `responsible-ai-and-governance-check`
  skills, the `business-design-frameworks` pack's `value-chain-mapping`
  skill, and the corresponding skills in `opportunity-recognition` and
  `business-case-and-analysis`
- A pack-specific `CLAUDE.md` and a full `README.md` (placeholder removed)
- `marketplace.json`: `specialisation-ai-native-startup-design`
  description updated, scaffold marker removed
- Total now 50 skills, 6 core packs + 2 populated specialisation packs

## 0.7.0 — 2026-08-05

New skill `business-design-frameworks/skills/strategy-canvas-and-value-curve`
— a Blue Ocean Strategy-style structuring method for comparing competitors
and alternative solutions:

- Anchored in Kim & Mauborgne's (2005) *Blue Ocean Strategy* (Strategy
  Canvas, Value Curve, Four Actions Framework/ERRC grid, Six Paths
  Framework) and the owner's own productized **360 Comparison Factors**
  comparison tool (a user-uploaded table: 10 example factors, a 0-2 scale,
  own solution + 4 competitors)
- `maturity: validated`, `source_layer: owner` — the pack's first
  non-scaffold skill
- New `references/360-comparison-template.md` — the template and usage
  guide, including the original worked example
- Cross-linked to the pack's other skills and
  `opportunity-recognition/skills/competitive-and-five-forces-mapping` and
  `opportunity-value-assessment`
- README and CLAUDE.md updated to describe the pack's mixed maturity
- Total now 45 skills

## 0.6.0 — 2026-08-05

New core pack `business-design-frameworks/` — a deliberately open and
growing collection of ways to structure and model a business (layers,
value chains, category modeling, and more to be added later):

- `layer-based-business-structuring` — an OSI-model-style layered
  structure, anchored in Hagel & Singer's (1999) "Unbundling the
  Corporation" and Baldwin & Clark's modularity theory
- `value-chain-mapping` — Porter's (1985) value chain model
- `category-definition-and-modeling` — category design (Play Bigger,
  Ramadan et al. 2016) and Blue Ocean Strategy (Kim & Mauborgne 2005)
- All `maturity: scaffold`, `source_layer: research` — no own validated
  experience yet, deliberately built to be filled in
- The pack is designed to grow: the README includes instructions for
  adding a new structuring method
- Total now 44 skills, 6 core packs + 1 populated specialisation pack

## 0.5.0 — 2026-08-04

Based on a user-supplied research report ("The AI Business Designer in the
Age of AI"), added to the `ai-strategy-and-governance` pack:

- `ai-opportunity-portfolio` enriched with a concrete AI-fit triage
  (prediction/classification/generation + data availability), a data
  flywheel check, and an automation-vs-agentic distinction (stays
  `maturity: scaffold`, `source_layer: research`)
- New skill `ai-native-business-model-canvas` (`maturity: scaffold`) — an
  expanded, AI-specific Business Model Canvas (value proposition, key
  resources, cost structure, ecosystem)
- The rest of the report was assessed as repeating existing content
  (business case building, the skills matrix) already covered by
  `ai-opportunity-portfolio`, `build-vs-buy-vs-partner-ai`,
  `ai-capability-roadmap`, `responsible-ai-and-governance-check`,
  `meta/competency_map.md` — not added again
- Total now 41 skills

## 0.4.0 — 2026-08-04

Expansion of the `opportunity-recognition/` core pack based on the owner's
own service's Opportunity Value Assessment product (sales page, input
wizard, report template) and its supporting S1 background research
(Mullins' Seven Domains, Timmons, POEM, NABC, Opportunity Canvas):

- 3 new skills (`maturity: validated`, `source_layer: owner`):
  `opportunity-intake-elicitation`, `opportunity-value-assessment`,
  `opportunity-brief-writing` — the pack's first non-scaffold skills,
  alongside the 5 original scaffold skills
- `references/opportunity-frameworks-review.md`, `intake-questions.md`,
  `opportunity-brief-template.md`
- Cross-linked: `opportunity-evaluation-and-judgment` (scaffold) →
  `opportunity-value-assessment` (validated); `research-opportunity-
  recognition` (research-commercialisation) ↔ `opportunity-value-
  assessment`
- `CLAUDE.md` and `README.md` updated to describe mixed maturity within
  the same pack
- Total now 40 skills

## 0.3.0 — 2026-08-04

First fully populated specialisation pack —
`specialisation-packs/research-commercialisation/`, converted from the
owner's own published commercialisation guide and AFCA self-assessment
tool:

- 12 new skills (`maturity: validated`, `source_layer: owner`) — the first
  in this repo not at `scaffold` level
- `references/afca-framework.md`, `case-studies.md`, `terminology.md`,
  `sources.md`
- A pack-specific `CLAUDE.md` and full `README.md` (placeholder removed)
- `scripts/generate_index.py` and `scripts/validate.py` extended to also
  index and validate `specialisation-packs/*/skills/` content (not just
  top-level plugin.json packs)
- `marketplace.json`: `specialisation-research-commercialisation`
  description updated, scaffold marker removed
- Total now 37 skills, 5 core packs + 1 populated specialisation pack

## 0.2.0 — 2026-08-04

Structural fix based on a structural analysis of another, production-
deployed Finnish Claude plugin marketplace:

- SKILL.md frontmatter trimmed to a minimum (`name` + `description`) —
  maturity/source layer moved exclusively into `skills_index.json`
- Number prefixes removed from pack folders (`01-strategic-thinking` →
  `strategic-thinking`)
- A pack-level `CLAUDE.md` guardrail layer added to each of the 5 core
  packs
- Added `What this skill does NOT do` and `Continue from here` sections to
  every skill
- Added `scripts/generate_index.py` and `scripts/validate.py`
- `marketplace.json`: added `$schema` and `displayName` fields

## 0.1.0 — 2026-08-04

- First scaffold: 5 core packs, 25 skills (all `maturity: scaffold`)
- 3 specialisation-pack placeholders
- `skills_index.json` machine-readable index
- `AGENT_GUIDE.md`, meta governance documents applying architectural
  principles from a semantic-layer template
- 2 starter playbooks
