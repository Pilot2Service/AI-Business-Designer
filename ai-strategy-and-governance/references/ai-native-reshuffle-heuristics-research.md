# AI-native reshuffle heuristics — research and selection

Input: 12 items supplied by the owner (10 heuristics + 2 case examples)
on how experts (Sangeet Paul Choudary, Alex Osterwalder, Howard Yu, and
a Strategyzer-affiliated practitioner named "Paris Thomas") frame AI as
a restructuring of industries and business models, rather than a
productivity tool. This document is the research/selection step only —
for each item, it checks fit against the pack's existing 88 skills and
looks for independent grounding beyond the owner's own description. No
skills are written yet.

**Result: 6 new skills, 2 enhancements to existing skills, 1 item
already covered by an existing skill, 2 case examples recommended as
grounding material rather than standalone skills.**

## What's already covered — no new skill needed

### Sensing → Sensemaking

This is the exact same heuristic, under the exact same name, already
built as `bmc-sensemaking-question-mapping` in the `business-model-canvas`
pack (written last session, from a different but overlapping source
list). No action needed — if this pack's material is ever consulted
again for this theme, point to that existing skill rather than writing
a second one.

## New skills recommended

### 1. AI reshuffle framing (merges two of the owner's items)

Combines "Strategy for the world AI creates" and "Containerization vs.
Automation" into one skill, because independent research shows they are
literally two levels of the SAME framework, not two separate ideas: the
top-level maxim ("don't build a strategy for AI, build a strategy for
the world AI creates") and the concrete diagnostic mechanism beneath it
(the shipping-container's three orders of effect — 1st automation, 2nd
standardization, 3rd unbundling and rebundling the whole value chain
around new constraints) both come from the same source and the same
book.

**Why valuable as a skill:** This pack currently has no premise-level
check before `ai-strategy-and-governance/ai-opportunity-portfolio` —
opportunities go straight to scoring without first testing whether the
team is scoring "apply AI to what we already do" ideas instead of
"what does AI change about where value sits" ideas. This closes that
gap, positioned to run BEFORE the opportunity portfolio, not as a
replacement for it. Concrete mechanism: apply the three-orders-of-effect
test to the company's own value chain (what's the 1st-order automation
move being proposed; is there a 2nd-order standardization effect; what
would the 3rd-order unbundle-and-rebundle move actually look like, and
is anyone in the room even discussing it).

**Grounding found:** Strong and precise. Both ideas are from Sangeet
Paul Choudary's *Reshuffle: Who Wins When AI Restacks the Knowledge
Economy* (2025), winner of the 2025 Thinkers50 Strategy Award — his
central thesis, independently confirmed across multiple sources, is
that "AI is a coordination technology that unbundles existing systems
and rebundles them around new constraints," illustrated with the
shipping-container's three-order effects (port automation →
standardization → the much bigger third-order effect of unbundling
vertically integrated manufacturing and creating global supply chains).
Good, precise citations available.

**Case material to attach:** Perplexity AI is a strong worked example —
not just automating search (faster results) but a genuine 3rd-order
reshuffle: it doesn't return a link list, it reads sources, synthesizes
an answer, and cites — a different value-chain position ("answer
engine") than the one search occupied, independently confirmed with
current 2026 figures (subscription-only since February 2026, ~$500M
ARR, enterprise/API tiers).

### 2. Capability complementarity and commoditization tracking

**What it is:** A recurring capability-investment heuristic, distinct
from the framing check above: track which of the company's capabilities
are becoming commoditized (AI makes them cheap and easily reproduced by
a prompt) versus which are becoming genuinely complementary (AI makes
previously siloed, messy, industry-specific knowledge newly combinable
with other domains) — and move investment away from the former, toward
the latter.

**Why valuable as a skill:** This pack's `ai-capability-roadmap` builds
a three-horizon roadmap and readiness scorecard, but doesn't include
this specific commoditization-tracking lens — it schedules capabilities,
it doesn't test whether a capability is about to become worthless to
defend. A genuine, recurring gap.

**Grounding found:** Also from Choudary's *Reshuffle* — "the complement
has to be commoditized to capture value at complementary layers," and
AI "unbundles expertise from individual experts, turning specialized
knowledge into scalable, rentable, and recombinable capabilities" (a
"building block economy" where advantage shifts from what you own to
how you assemble blocks). Reinforced by Howard Yu's LEAP thesis (IMD,
2023 Thinkers50 Strategy Award): competitive longevity depends on
deliberately moving into adjacent disciplines before copycats
commoditize what already exists — a second, independent expert making
essentially the same capability-investment point. Strong grounding, two
independent named sources.

**Case material to attach:** Shutterstock is the reference case — image
licensing (its core capability) was about to be commoditized by
free/unlimited AI-generated images, so it moved investment toward a
complementary, harder-to-commoditize layer instead: a six-year OpenAI
training-data deal plus a Contributor Fund and "content-usage governance
and legal safety" for enterprises, independently confirmed as real,
current (six-year agreement, hundreds of thousands of artists
compensated). This case also directly strengthens this pack's existing
`ai-output-curation-and-quality-control` skill (the creator → curator
shift) — recommend adding it there as a worked example, not just to the
new skill.

### 3. Conway's Law for AI architecture

**What it is:** An organization's communication structure gets mirrored
in whatever AI system it builds — fragmented teams produce fragmented,
siloed AI tools with no shared capability across the organization. The
practical rule: restructure (or at least deliberately decide not to)
BEFORE building the AI system, not after — once the AI architecture
reflects the org chart, changing either becomes very hard.

**Why valuable as a skill:** Checked against `business-design-frameworks/layer-based-business-structuring`
(the closest existing skill — structures a business into build/partner
layers using OSI-model and Hagel & Singer logic) — related but
genuinely different: that skill designs a modular structure; this
heuristic diagnoses and prevents a SPECIFIC failure mode (org
communication structure silently dictating AI architecture, with the
sequencing trap of discovering this only after the system is built).
No existing skill in this pack or `change-and-communication` addresses
this specific AI-architecture risk. Genuine gap.

**Grounding found:** Very strong and current — this is an active,
independently-arrived-at 2026 discourse theme across multiple unrelated
sources (FourWeekMBA's "Conway's Law in AI: Your Org Chart is Your AI
Architecture," Forrester's "Conway's Law: Your Operating Model Matters
More Than The AI Model," CIOReview, and others), all making the same
point independently: fragmented teams produce fragmented AI tools with
no shared capability, and RAND Corporation research is cited showing
AI projects fail at twice the rate of non-AI technology projects, most
often from miscommunication about intent and purpose — directly
supporting the "restructure before you build" sequencing rule. Easy,
solid citations. Conway's Law itself (Melvin Conway, 1967) is
well-established and uncontested as the base concept being extended.

### 4. Workshop-to-agent productization

**What it is:** Convert a company's own unique expert material —
recorded/transcribed workshops, proprietary methodology sessions — into
an interactive AI agent that customers can query, rather than leaving
it as a static recording or document. The agent then also functions as
an upsell/retention touchpoint, not just a learning aid.

**Why valuable as a skill:** Checked against `ai-strategy-and-governance/ai-discovery-engagement-design`
(productizes the DISCOVERY PROCESS/engagement structure into a paid
service) — different mechanism: this heuristic productizes EXISTING
CONTENT into a queryable product, not the engagement process itself.
Also checked against `ai-output-curation-and-quality-control` (curating
AI outputs) — different question again (this is about creating an
agent FROM the company's own content, not curating AI-generated
output). Genuine gap, and a concrete, easily-actionable technique.

**Grounding found:** No single named source for this specific
technique (the "5 minutes" framing in particular is the owner's own
compression, not independently verified), but the underlying tooling
capability is mainstream and well-documented in 2026 (transcription
tools like Fireflies/Avoma, conversational AI agent platforms that
handle Q&A plus upsell/cross-sell within the same conversation). Treat
this as the owner's own applied productization pattern, built on
genuinely mainstream, currently-available tooling — grounded but not
tied to a named framework or person.

### 5. AI-assisted canvas/document drafting ("start from edit")

**What it is:** Don't start business-model or brand analysis from a
blank page — feed the target company's public material (its website,
in the example given) to an AI model to get an instant first-draft
brand audit and Business Model Canvas sketch, then have the human
team's actual work be editing, rejecting, and enriching that draft
rather than generating it from nothing.

**Why valuable as a skill:** Best fit is `business-model-canvas`, as a
facilitation-acceleration technique that pairs naturally with
`bmc-session-facilitation-design` — speeds up the START of a session
specifically, which none of that pack's 17 skills currently address (they
assume a blank canvas being filled by a team, not an AI-generated
starting draft the team then edits). Also relevant to this pack's own
`ai-discovery-engagement-design` as a faster intake step. Recommend
`business-model-canvas` as the primary home since the concrete example
given is a BMC draft specifically.

**Grounding found:** The named source, "Paris Thomas," is independently
identifiable and credible: an executive advisor on strategy and
innovation, a certified Business Model Generation (BMG) facilitator/
coach, a contributor to *Value Proposition Design* (the well-known
Osterwalder/Strategyzer book), and a workshop leader for Strategyzer's
own "Accelerating Innovation with AI" program — i.e., a real,
Strategyzer-affiliated practitioner, not an unverifiable name. This is
meaningfully stronger sourcing than the earlier, unverifiable "Paris
Thomas" attribution the owner supplied for the BMC pack's two-week
experiment rule. That said, the SPECIFIC "start from edit" phrase and
workflow could not be independently located in public material (the
search surfaced the person and their credible affiliation, not a
matching direct quote) — if the owner attended or watched this specific
Strategyzer workshop personally, the attribution is reasonable to keep
as a first-hand account; if it's secondhand, recommend citing it more
cautiously ("a technique demonstrated in a Strategyzer AI workshop")
rather than naming the specific phrase as a direct quote.

### 6. Large-scale AI-agent customer interviewing

**What it is:** Use AI agents (not human interviewers) to conduct
customer discovery interviews at a scale no human team could match —
hundreds or thousands of short interviews in parallel — then treat the
aggregate as a filter: mine it for the most interesting outliers or
patterns, and follow up on THOSE personally.

**Why valuable as a skill:** Checked against `business-model-canvas/bmc-proxy-expert-validation`
(uses adjacent professionals, not AI, as a fast validation source) and
`bmc-experiment-method-selection` (decides build-vs-proxy method for
testing a hypothesis) — genuinely distinct mechanism from both: this is
about scaling DIRECT customer interviews themselves via AI moderation,
not substituting a proxy source or choosing between building and
testing. Recommend `business-model-canvas` as the home, alongside its
two siblings, completing a three-part customer-validation toolkit
(proxy experts / AI-scaled direct interviews / build-vs-proxy
decision).

**Grounding found:** Excellent, current, and independent of the "Paris
Thomas" attribution entirely — this is now a well-documented, mainstream
2026 practice with real adoption figures: roughly 40% of B2B SaaS
product teams report AI-moderated interviews monthly (up from under 10%
in 2024), early-stage founders running a median of 47 completed
interviews per discovery round (up from 8–12 in 2022), named tools
(Perspective AI, Anthropic's interview agent) and cost data (under $5
in compute per conversation). Strong enough grounding that this skill
doesn't need to rely on the Paris Thomas attribution at all — cite the
broader 2026 AI-customer-research-tooling trend as the primary anchor.

## Enhancements to existing skills, not new skills

### 7. Data-source relevance test → enhance `data-role-diagnosis`

**What it is:** A warning against a specific, common mistake: assuming
that because a company already owns SOME data related to a domain, it's
positioned to win with AI in that domain — when the data that actually
has predictive power for the target AI use case is a different kind of
data entirely (the example given: a skincare company's purchase-history
data vs. the health/microbiome data genuinely personalized AI skincare
would need).

**Why an enhancement, not a new skill:** `data-role-diagnosis` already
has a three-test structure for validating a data asset claim (resale,
flywheel, defensibility — see that skill's Method step 3). This
heuristic is a natural fourth test in the same family: a **relevance
test** — is this specifically the data type with genuine predictive
power for the target outcome, or just the data the company happens to
already have for a different reason? Adding it as DR-style test 4
avoids creating a near-duplicate skill and strengthens an existing one,
the same pattern used for the BMC pack's gravity-creators addition last
session.

**Grounding found — flag clearly:** The underlying point is sound and
worth keeping, but the specific attribution to Alex Osterwalder and the
skincare/microbiome example could **not** be independently verified —
no matching public source was found despite a direct search. Recommend
either (a) keeping the example but dropping the "Osterwalder" attribution
and presenting it as an illustrative, unattributed example, or (b) if
the owner has a first-hand source for this (a talk, a workshop, a
personal note), keeping the attribution but flagging it as
owner-sourced rather than independently verified in the skill's
"Anchored in research" section — consistent with how the BMC pack
already handles similarly-unverified attributions.

### 8. Proprietary learning-engine architecture → enhance `ai-native-business-model-canvas`

**What it is:** The moat in an AI-native business isn't any single AI
module (modules commoditize once unbundled) — it's the continuous,
proprietary INTEGRATION of modules into one feedback loop spanning the
full chain, from experimentation through to go-to-market signal,
getting stronger with every transaction.

**Why an enhancement, not a new skill:** Checked against two existing
skills. `ai-native-business-model-canvas`'s Method step 6 ("data
flywheel check") already asks whether usage feeds data back into the
model — but as a one-line check, not a design principle about WHY the
moat has to be the integration rather than any module. `data-monetization-model-selection`'s
four-point flywheel checklist (unique collection channel / measurable
model improvement / observable UX improvement / the loop closing as
growth) already audits whether a flywheel CLAIM is real — a validation
lens. This heuristic is a design/architecture lens (how to BUILD the
loop so modules don't commoditize away the advantage), which is
different from both but close enough to either that a new, third
skill risks redundant restating. Recommend deepening
`ai-native-business-model-canvas` step 6 with this design principle,
explicitly cross-referencing `data-monetization-model-selection`'s
checklist as the place to validate the claim once designed.

**Grounding found:** Strong and current — well-documented in active AI
moat/data-engine discourse (Label Studio's "Your Data Engine Is the
Moat," Y Combinator's "7 Real Moats for AI Startups," McKinsey's "From
AI Table Stakes to AI Advantage"), consistently making the same point:
proprietary data/feedback loops, not algorithms, are the durable moat,
because algorithms commoditize faster than data streams. Strong,
independently verifiable worked example available to replace the
original heuristic's vague "chemicals" reference: **Recursion
Pharmaceuticals**, which records millions of cellular images to train
models on how diseases change cell morphology — a proprietary
"wet-lab" feedback loop that's more durable than the underlying
algorithms, cited as scoring highest on defensibility among AI drug-
discovery business models. Recommend using Recursion as the concrete
case in place of the original, unnamed "chemicals" example.

## Summary table

| # | Item | Recommendation | Grounding strength |
|---|---|---|---|
| — | Sensing → Sensemaking | Already covered (`bmc-sensemaking-question-mapping`) | — |
| 1 | Strategy for the world AI creates + Containerization vs. Automation | New skill (merged) | Strong — named Choudary/*Reshuffle* source |
| 2 | Complementarity and Commoditization | New skill | Strong — Choudary + Howard Yu, two independent named sources |
| 3 | Conway's Law & Architectural Reshuffle | New skill | Strong — active, independent 2026 discourse, well-established base concept |
| 4 | Workshop-to-Agent Rule | New skill | Moderate — mainstream tooling, technique itself is the owner's own pattern |
| 5 | Thoughtful use of AI / "Start from edit" | New skill (in `business-model-canvas`) | Moderate — Paris Thomas independently identified and credible; specific phrase unverified |
| 6 | Large-scale AI-agent interviewing | New skill (in `business-model-canvas`) | Strong — current 2026 adoption data, independent of the Paris Thomas attribution |
| 7 | Data-Source Alignment Heuristic | Enhance `data-role-diagnosis` (4th test) | Weak on attribution — Osterwalder/skincare example unverified; underlying point sound |
| 8 | Proprietary Learning Engine Heuristic | Enhance `ai-native-business-model-canvas` (step 6) | Strong — active AI-moat discourse, verified Recursion Pharmaceuticals case |
| 9 | Perplexity AI case | Grounding material for skill #1 | Strong — verified current figures |
| 10 | Shutterstock case | Grounding material for skill #2 and existing `ai-output-curation-and-quality-control` | Strong — verified current deal terms |

## Next step

Once this selection is confirmed: write 6 new skills (4 in
`ai-strategy-and-governance`, 2 in `business-model-canvas`) and apply 2
enhancements to existing skills (`data-role-diagnosis`,
`ai-native-business-model-canvas`) — not done yet, per the brief for
this pass.
