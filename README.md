# AI Business Designer — Skills

🌐 [Browse the pack online](https://pilot2service.github.io/AI-Business-Designer/)

A skills pack for Claude Code and Cowork that helps business designers,
consultants, and entrepreneurs do higher-quality business planning, analysis,
and problem definition — spotting and sizing opportunities, building a
decision-ready business case, prioritizing AI initiatives, and framing a demo
without overpromising — instead of ad hoc prompting. Taken as a whole, the
pack also works as a map of the competence field around AI-assisted business
design: what the discipline actually consists of, broken into named,
independently usable pieces.

`8 core packs · 3 populated specialisation packs · 78 skills · 4 audit agents
· self-contained (no required external services) · CI-validated · MIT license`

New here? [`QUICKSTART.md`](QUICKSTART.md) gets you from zero to your first
skill run in about five minutes.

## Why this exists

Most "business strategy" prompting is either too generic to be useful or
too confident about numbers nobody actually verified. This pack tries to fix
both: each skill is a narrow, named technique anchored to a public framework
or method (cited in the skill itself), and every output is explicitly framed
as a decision-support draft, not a finished decision — assumptions are marked,
not hidden.

**On depth — read this before you assume more than is here.** The pack
includes a number of heuristics and decision rules, drawn from general
practice and from the owner's own experience. It does **not** contain deep
proprietary playbooks, hard-won pricing/negotiation heuristics, or strong,
opinionated value judgments about how business should be done — the kind of
thing a consultancy keeps for paying clients. In that sense this pack is
intentionally open and general-purpose rather than a proprietary methodology
in disguise.

**Nothing here is speculative.** Every technique in this pack — at every
maturity level — is grounded in either the owner's own real consulting
engagements or an established, professionally used framework (cited in the
skill itself). There is nothing invented or experimental: applied with sound
judgment, in the right context and to a fitting client situation, it works.
The maturity marking below tells you something narrower than "does this
work" — it tells you whether the *owner personally* has run that specific
skill through a real engagement yet, or whether it's still a well-grounded
framework awaiting that. Both are real and usable; the marking exists so
you always know which one you're looking at. See
["How maturity is tracked"](#how-maturity-is-tracked) below.

## When to use this — and when not to

| Use it when... | Don't reach for it when... |
|---|---|
| You're in Claude Code / Cowork doing business opportunity, business case, AI-strategy, or change-communication work and want a structured technique instead of a blank page | You need legal, tax, regulatory, or financial advice — that requires a licensed professional, not a skills pack |
| You want to know *how confident* to be in a given technique before you rely on it | You want a single number or decision handed to you with no visible reasoning — that's not what this produces, by design |
| You want something that works offline, with your own numbers, no external accounts required | Your task is software engineering — this pack is about business design, not code |

## Quick start

```
/plugin marketplace add Pilot2Service/AI-Business-Designer
/plugin
```

The first command registers this repository's `.claude-plugin/marketplace.json`
catalog (marketplace name: `ai-business-designer-skills`); the second opens
the interactive menu — choose **Browse and install plugins**, pick the
packs you need (e.g. `opportunity-recognition`, `business-case-and-analysis`),
and install. Full walkthrough, including what a good first run looks like:
[`QUICKSTART.md`](QUICKSTART.md).

## What's inside

Eight core packs cover the parts of AI-assisted business design that come up
across most engagements; three specialisation packs go deeper into a
specific situation (research commercialisation, AI-native startup design,
Business Model Canvas facilitation). Read the two tables below as much as a
map of the discipline as a list of what to install — **click a pack name to
see its actual skill-by-skill list** (every skill in this repo, named and
described in one line, lives in that pack's own `README.md`; nothing here is
just a number).

### Core packs

| Pack | Helps you... | Status |
|---|---|---|
| [`strategic-thinking`](strategic-thinking/README.md) | break down a fuzzy problem into a testable hypothesis (MECE / issue trees) | scaffold |
| [`opportunity-recognition`](opportunity-recognition/README.md) | scan, evaluate, size, and write up a business opportunity | mixed — 3 of 8 skills validated from a real, previously operated service methodology |
| [`business-case-and-analysis`](business-case-and-analysis/README.md) | build an ROI/NPV business case with risks and assumptions made explicit | scaffold |
| [`ai-strategy-and-governance`](ai-strategy-and-governance/README.md) | prioritize AI use cases, scope a PoC, and check responsible-AI readiness | scaffold |
| [`change-and-communication`](change-and-communication/README.md) | plan change management and executive communication | scaffold |
| [`business-design-frameworks`](business-design-frameworks/README.md) | apply classic business/value-modeling frameworks (value chain, strategy canvas, category design) — an intentionally growing collection | mixed — 1 of 5 skills validated |
| [`prototyping-and-demonstration`](prototyping-and-demonstration/README.md) | frame and deliver a credible demo or PoC without creating false expectations of production-readiness | scaffold |
| [`data-strategy-and-literacy`](data-strategy-and-literacy/README.md) | diagnose data's role in a business and read data critically before trusting it | scaffold |

### Specialisation packs

| Pack | What it gives you | Status |
|---|---|---|
| [`research-commercialisation`](specialisation-packs/research-commercialisation/README.md) | A structured path from a research result to a commercialisation decision: IP disclosure and ownership checks, route selection (licensing vs. spin-out), funding-option mapping, and team/equity questions, plus a working self-assessment tool | validated (12 skills) |
| [`ai-native-startup-design`](specialisation-packs/ai-native-startup-design/README.md) | A founder-facing path from a raw AI opportunity to a buildable spec: customer understanding (ICP/JTBD), a PRD an AI coding agent can act on, human-oversight design for the resulting product, and a tool-stack decision | mixed (5 validated, 3 draft — 8 skills) |
| [`business-model-canvas`](specialisation-packs/business-model-canvas/README.md) | Facilitation-grade Business Model Canvas work: running the session, diagnosing a finished canvas for weak spots, correcting common misunderstandings about what a canvas is, and matching a model against a library of known innovation patterns | mixed (3 validated, 4 scaffold — 7 skills) |

## How maturity is tracked

Every skill's frontmatter only ever contains `name` and `description` — no
confidence claims live there. Instead, `skills_index.json` tracks two things
for every skill: `maturity` (`scaffold` → `draft` → `validated` → `canonical`)
and `source_layer` (`research` = built from a public framework,
`owner` = converted from the owner's own field-tested experience). Claude is
instructed (`AGENT_GUIDE.md`) to say out loud which one it's using and to
never present a scaffold skill's structure as if it were validated
experience. Details: [`meta/maturity_levels.md`](meta/maturity_levels.md).

## Delegatable agents

Four packs include a read-only subagent (`agents/*.md`) that you can invoke
separately (via the Task tool) to stress-test a skill's output *before* it
goes to a decision-maker — a second, independent pass, not a rubber stamp.

| Agent | Pack | What it checks |
|---|---|---|
| [`assumption-stress-tester`](business-case-and-analysis/agents/assumption-stress-tester.md) | `business-case-and-analysis` | Adversarially challenges a business case's assumptions before the number goes to leadership |
| [`market-sizing-cross-validator`](opportunity-recognition/agents/market-sizing-cross-validator.md) | `opportunity-recognition` | Cross-checks a TAM/SAM/SOM calculation with an independent top-down/bottom-up method |
| [`competitive-blind-spot-scanner`](business-design-frameworks/agents/competitive-blind-spot-scanner.md) | `business-design-frameworks` | Looks for un-scanned competitors or angles in a competitive/positioning analysis |
| [`ai-initiative-readiness-auditor`](ai-strategy-and-governance/agents/ai-initiative-readiness-auditor.md) | `ai-strategy-and-governance` | Audits an AI initiative's scoring and governance checklist for gaps before approval |

None of these agents edit anything — each returns a findings table for a
human to act on.

## Optional external data (not a dependency)

This pack never requires an external service to function — every skill works
with numbers you provide, and marks assumptions explicitly when you don't
have one. If your environment happens to have a relevant data MCP connected
(e.g. a market-sizing data source), the `market-sizing-tam-sam-som` skill and
its cross-validator agent can use it instead of, or to cross-check, an
assumption. See [`meta/external-data-mcp.md`](meta/external-data-mcp.md) for
the (unaudited, third-party) candidates considered.

## Quality assurance

```
python3 scripts/generate_index.py   # rebuilds skills_index.json from disk
python3 scripts/validate.py         # checks structure + frontmatter
```

`.github/workflows/validate.yml` runs both automatically on every push and
pull request, so a broken frontmatter or an out-of-sync index blocks the
merge without anyone having to remember to check by hand.

## A note on language

The skill instructions themselves (`SKILL.md`, `CLAUDE.md`, reference files)
are written in English, so the pack is usable and reviewable without a
Finnish-language dependency. Regardless of the instruction language, Claude
will respond to you in whichever language you use.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to add a skill, fill in an
`[OWNER INPUT]` section, or raise a skill's maturity level once it's actually
been used.

<details>
<summary>Full repository layout</summary>

```
ai-business-designer-skills/
├── README.md
├── QUICKSTART.md                      start here
├── AGENT_GUIDE.md                     how an agent should use this pack
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── skills_index.json                  machine-readable index (generated — don't hand-edit)
├── .claude-plugin/
│   └── marketplace.json               lists every installable pack
├── .github/workflows/
│   └── validate.yml                   CI: generate_index.py + validate.py on every push
├── scripts/
│   ├── generate_index.py
│   └── validate.py
├── meta/
│   ├── repo_purpose.md
│   ├── skill_design_principles.md
│   ├── frontmatter_schema.md          name + description only — nothing else allowed
│   ├── maturity_levels.md
│   ├── competency_map.md
│   ├── shared-guardrails.md           single source for the disclaimers every pack shares
│   └── external-data-mcp.md
├── strategic-thinking/                [plugin] 6 skills
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md                      pack-wide guardrails (a safety net, not the main mechanism)
│   ├── README.md
│   ├── skills/<skill-id>/SKILL.md
│   └── references/
├── opportunity-recognition/           [plugin] 8 skills + agents/market-sizing-cross-validator.md
├── business-case-and-analysis/        [plugin] 6 skills + agents/assumption-stress-tester.md
├── ai-strategy-and-governance/        [plugin] 11 skills + agents/ai-initiative-readiness-auditor.md
├── change-and-communication/          [plugin] 4 skills
├── business-design-frameworks/        [plugin] 5 skills + agents/competitive-blind-spot-scanner.md
├── prototyping-and-demonstration/     [plugin] 5 skills
├── data-strategy-and-literacy/        [plugin] 6 skills
├── specialisation-packs/
│   ├── ai-native-startup-design/       8 skills
│   ├── business-model-canvas/          7 skills
│   └── research-commercialisation/     12 skills
├── templates/
│   ├── skill-template/SKILL.md
│   └── specialisation-pack-template/README.md
└── playbooks/                         pre-built skill chains for common tasks
    ├── idea-to-decision.md
    └── ai-initiative-scoping.md
```

</details>

## About this project

This repository serves two purposes at once. First, and primarily, it's a
working tool — skills meant to actually be installed and used. Second, it's a
deliberate demonstration piece: of what a modern AI Business Designer's skill
set looks like broken down into its component parts, and of the ability to
design, structure, and maintain a production-quality, skills-based AI toolkit
— the context-engineering decisions (maturity tracking instead of unverifiable
confidence claims, a single source for shared guardrails instead of drift
across a dozen copies, delegatable audit agents instead of a single pass of
self-review, CI validation instead of an honor system) that make a toolkit
like this trustworthy rather than just extensive. If you're evaluating this
repository rather than using it, that structure is the part worth looking at
closely.

## License & author

MIT — see [`LICENSE`](LICENSE).

Author: **Tommi Järvinen** · Adductor Magnus Oy.
