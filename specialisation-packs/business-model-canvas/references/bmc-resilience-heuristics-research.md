# BMC resilience & risk heuristics — research and selection

Input: 13 heuristics supplied by the owner, describing how experienced
practitioners use the Business Model Canvas beyond static planning — for
resilience assessment, risk-spotting, and steering experimentation. This
document is the research/selection step only: for each of the 13, it
checks fit against this pack's existing 7 skills and client profile, and
looks for independent grounding beyond the owner's own description. No
skills are written yet — that's the next step, once this list is
confirmed.

**Result: 10 selected, 3 not recommended for this pack** (reasons below).
Selection criteria used: (1) does it pass the pack's own concreteness
test — steps, a table, or a decision rule, not just a heading
(`meta/skill_design_principles.md`); (2) does it fit the pack's stated
client profile (early-stage/growth-stage companies, founder closely
involved — explicitly *not* large-enterprise innovation units); (3) does
it duplicate one of the 7 existing skills or the 159-pattern library.

## Selected — recommended for skill-writing

### 1. Prototype the numbers immediately

**What it is:** Force pricing, unit economics, and revenue-model
assumptions into a live, testable form (a spreadsheet, a real price
quoted to a real prospect) at the start of BMC work, not after the model
is otherwise "done."

**Why valuable as a skill:** This is the single most common failure mode
in BMC facilitation — teams fill sticky notes on Value Proposition and
Customer Segments for an hour and wave hands at Revenue Streams/Cost
Structure. A skill that structurally forces early quantification (a
minimal dynamic pricing model + a willingness-to-pay test design) closes
a gap none of the pack's 7 existing skills currently cover — the closest,
`bmc-canvas-diagnostic-reading`, checks a *finished* canvas; this
heuristic intervenes *during* the session.

**Grounding found:** Matches a well-documented practitioner pattern:
Lean Canvas (Ash Maurya) explicitly promotes Revenue Streams/Cost
Structure earlier and more rigorously than the original Osterwalder BMC
precisely because teams skip them; general pricing-validation practice
(A/B price offers, willingness-to-pay interviews) is standard
Strategyzer/Lean Startup material. No single named "minute zero" source
was found under that exact phrase — treat the label as the owner's own
framing of an established practice, not a citation.

**Relationship to other packs:** Feeds `business-case-and-analysis/roi-npv-sensitivity-model`
once the model matures past the canvas stage — this skill is the cheap,
early version of that same discipline.

### 2. Corporate antibodies (Law of the Existing Business Model)

**What it is:** A new business model triggers organizational rejection —
sales teams refuse to sell a lower-margin offer, finance blocks a
different metric — because it threatens existing incentives/processes.
Reading a canvas for where this will happen, and designing a protected
"sandbox" for the experiment, before it launches.

**Why valuable as a skill:** None of the 7 existing skills address
*organizational* resistance to a new model — they cover the model's own
internal quality (diagnostic reading), facilitation mechanics, and
client misunderstandings about the *tool*, not resistance from the
client's *own organization* to the *model itself*. Genuinely new angle.

**Grounding found:** Well-established, independently documented concept
under this exact name — Harvard Business Review ["Get the Corporate
Antibodies on Your Side"](https://hbr.org/2012/05/get-the-corporate-antibodies-o),
plus a substantial body of corporate-innovation writing (Forbes,
Wellspring, Idea to Value, CIO.com) all using the same biological
metaphor independently. Strong, easy citation.

### 3. Better revenue vs. more revenue

**What it is:** Score Revenue Streams / Customer Relationships not on
size but on predictability — recurring/contractual revenue rated far
above one-off transactional revenue, because it changes the business's
actual resilience, not just its top line.

**Why valuable as a skill:** Directly operationalizable as a scoring
rubric (the owner's supplied -3 to +3 scale). Concrete, table-driven,
and gives the Revenue Streams block a rigor it currently lacks in this
pack — none of the 7 existing skills score revenue quality.

**Grounding found:** This is a named, current Strategyzer concept —
["Revenue Resilience"](https://www.strategyzer.com/library/revenue-resilience),
directly from Osterwalder's own team, consistent with the "recurring
revenue commands a higher valuation multiple" point that shows up
consistently across independent valuation sources (recurring-revenue
businesses valued at meaningfully higher multiples than one-time-sale
businesses at identical earnings). Good citation available.

### 4. CAC-to-budget alignment for channels

**What it is:** Don't just list Channels — cost each one (cost to
acquire a lead/customer through it) and check that cost against the
company's actual budget and ROI timeline before committing to it.

**Why valuable as a skill:** The pack currently has no skill that puts
real numbers against the Channels block — `bmc-canvas-diagnostic-reading`
checks structure, not channel economics. Fills a concrete, standalone
gap without overlapping `business-case-and-analysis` (which builds a
full business case, not a channel-by-channel CAC check at BMC-sketch
stage).

**Grounding found:** Standard growth/unit-economics discipline (CAC vs.
LTV, payback period) — not tied to one named source but universally
practiced; safe to cite as general SaaS/growth-marketing practice rather
than any one author.

### 5. Reading the left side (Partners/Activities/Resources) as a risk map

**What it is:** Use Key Partners, Key Activities, and Key Resources not
just as a "how we operate" description but as an operational risk and
security scan — e.g., an outsourced partner with unmonitored access to
sensitive customer data is a canvas-visible risk, not just a logistics
note.

**Why valuable as a skill:** This is the most novel angle of the ten —
it repurposes the BMC's structure for something it's not normally used
for (risk/security reading rather than business design), and it's
exactly the kind of thing the owner described wanting the pack to do
(resilience and risk analysis, not just planning). No existing skill in
this pack or in `business-case-and-analysis` (`risk-matrix-and-mitigation`)
does this from the canvas specifically — that skill is a generic
probability×impact matrix with no BMC-block anchoring.

**Grounding found:** No single named source uses this exact framing;
grounded instead in general operational/third-party risk management
practice (the pack's sibling `business-case-and-analysis` pack already
cites ISO 31000). Treat as a genuine synthesis — cite ISO 31000 as the
risk-management anchor, be explicit in the skill that the *canvas
reading* method itself is the owner's own applied technique, not a
textbook one.

### 6. Low-tech ↔ high-tech repositioning

**What it is:** A model can win by deliberately moving *up* the
technology-sophistication axis (automating what was manual) or *down*
it (stripping out expensive tech competitors over-invest in) — the
win comes from the business model fit, not the tech level itself.

**Why valuable as a skill:** Checked against the pack's own 159-pattern
library (`references/bmc-innovation-pattern-library.md`) — this
direction is **not** currently in it (no "low tech"/"high tech" pattern
found). Genuine content gap, not a duplicate.

**Grounding found:** Directly confirmed as one of Osterwalder & Pigneur's
own named patterns in *The Invincible Company* (2020) — a "Value
Proposition Shift" pattern, "From Low Tech to High Tech" (and its
reverse). Reinforced by two well-documented, independently verifiable
cases: Nintendo Wii's deliberate under-specification as Blue Ocean
value innovation (Kim & Mauborgne), and TRISA's opposite move
(automating Swiss toothbrush manufacturing with robotics to defend a
high-cost location). Strong citations on both directions.

### 7. The two-week experiment rule

**What it is:** If a hypothesis can be built and tested with real
customers in under two weeks, build it now. If it would take longer
(hardware, regulated products), don't start building — find a cheaper
proxy test instead (interviews, a landing page, a brochure).

**Why valuable as a skill:** A decision *gate* that sits logically
before `prototyping-and-demonstration/rapid-prototype-and-vibe-coding-craft`
(which assumes the decision to build has already been made) — this
heuristic is about *whether* to build at all, which belongs at the BMC/
experiment-design stage, not the prototyping stage. No overlap; a
genuine missing link between the two packs.

**Grounding found:** The general two-week/short-sprint testing discipline
is well documented in Ash Maurya's Lean Startup methodology (*Running
Lean*, *Scaling Lean* — explicit "LEAN sprints" for testing ideas fast).
**Caveat:** the owner's specific attribution to "Paris Thomas" could not
be independently verified — no source under that name surfaced. Recommend
citing the Maurya/Lean Startup tradition as the anchor and treating the
named attribution as unverified, per this repo's own no-fabrication rule.

### 8. The adjacent-salesperson interview

**What it is:** Before investing heavily in validating a value
proposition, find someone who sells something adjacent to it for a
living — their job is already listening to Jobs/Pains/Gains all day —
and interview them (informally, e.g. over dinner) instead of running a
costly formal study first.

**Why valuable as a skill:** A cheap, specific, non-obvious customer-
research technique that isn't already covered — the pack's
`bmc-client-language-translation` skill interprets client language
*after* you have it; this is about *getting* fast, high-quality signal
*before* talking to real prospective customers at all.

**Grounding found:** **Caveat, stated plainly:** no independently
documented source uses this specific "salesperson dinner" framing — it
reads as either a personal practitioner heuristic or a memorable
paraphrase passed down informally. The underlying technique — proxy/
surrogate interviews with people who already talk to your target
customer professionally — is well-established customer-development
practice (Steve Blank's customer development interviews; Rob
Fitzpatrick's *The Mom Test* on talking to people who already have the
problem). Recommend citing that broader tradition as the anchor and
flagging the specific "dinner" framing as the owner's own memorable
version of it, not an external citation.

### 9. Sensing → sensemaking

**What it is:** In an environment where AI makes raw information and
"answers" cheap and abundant, the differentiator shifts from *collecting*
data to *asking the right questions* and *making meaning* of what's
collected — use the BMC as a question-generating map, not a data
template.

**Why valuable as a skill, with a caveat:** This is the **weakest on the
concreteness test** of the ten — it's a reframe more than a step-by-step
method, and it overlaps conceptually with this pack's own stated
identity ("BMC is a thinking tool... to help the team think in new ways"
per the README). To become an actual skill it needs real operationalizing
— e.g., "generate the canvas as a list of open, falsifiable questions per
block instead of filled-in answers" — rather than staying at the level of
a philosophy. Recommend keeping it in the list but flagging it in the
skill-writing step as needing the most work to pass the concreteness
test.

**Grounding found:** Reasonably current — "sensemaking" as an
organizational-cognition concept traces to Karl Weick's established
sensemaking theory; the specific AI-era framing (answers becoming cheap,
question-asking becoming the scarce skill) is an active 2026 discourse
theme, e.g. ["Sensemaking: The Leadership Skill That Will Define
2026"](https://www.aristotleperformance.com/post/sensemaking-the-leadership-skill-that-will-define-2026-beyond)
and a 2026 CHI proceedings track on sensemaking and AI. Cite Weick as the
theoretical root, the 2026 sources as the current applied context.

### 10. Hunting zones

**What it is:** Leadership sets a clear, inspiring, non-budget strategic
direction (megatrend × owned assets × attractive segment) that bounds
where bottom-up BMC experimentation is allowed to roam, so exploration
doesn't fragment into unrelated one-off bets.

**Why valuable as a skill:** Even at small-company scale (this pack's
actual client profile), an unbounded "let's brainstorm business models"
session produces scattered, incomparable canvases. A lightweight
version of this heuristic — define the hunting zone in one sentence
before sketching any canvas — is usable by a single founder, not just a
corporate innovation unit. This is what separates it from heuristic #12
below (VC portfolio approach), which does *not* translate down to
founder scale.

**Grounding found:** Strong, precise citation — "Hunting Zones" is a
named term from Andy Binns, Charles O'Reilly, and Michael Tushman's
*The Corporate Explorer* / *The Corporate Explorer Fieldbook*, covered
independently in [MIT Sloan Management
Review](https://sloanreview.mit.edu/article/leading-disruption-in-a-legacy-business/)
and [Wazoku's summary](https://www.wazoku.com/blog/hunting-zones-focused-innovation-in-the-era-of-total-innovation/).
The MasterCard "Kill Cash" example the owner supplied is independently
confirmed as Ajay Banga's actual stated company mission, and works well
as the "clear, inspiring, non-budget vision" illustration this pattern
needs.

## Not recommended for this pack

### 11. Rita McGrath + Osterwalder 50% leadership-time rule

Excluded, with a caveat on sourcing. This is an organizational-capacity
*gate* ("does this company have any real ability to innovate at all")
that sits one level above a specific BMC — it never touches the canvas
itself, unlike all 10 selected above. It also couldn't be verified as an
exact, jointly-authored "test" under this name; McGrath's real published
work centers on strategic inflection points, discovery-driven planning,
and more recently "strategic centering" (choosing and defending a center
of gravity for resource allocation) — related in spirit to a leadership
time-allocation check, but the specific "50%" figure and the McGrath+
Osterwalder joint framing didn't surface in independent sources. If this
capability is wanted, it fits better as an *organizational readiness*
check in `ai-strategy-and-governance` (which already has a
`responsible-ai-and-governance-check` skill in a similar spirit) than as
a Business Model Canvas skill.

### 12. VC portfolio approach

Excluded on client-profile fit, not on grounding — this is a real,
well-documented corporate venture-building practice (parallel small
bets, strict short-cycle kill gates, double-down on the top decile).
But this pack's own stated client profile explicitly excludes "large
enterprises or their innovation units," and this heuristic doesn't
translate down to a solo founder or small team the way Hunting Zones
does — running "100-200 teams" and killing 90% at the 3-month mark
requires an innovation department's headcount and budget that this
pack's actual clients don't have. Recommended as a future addition
*if and when* a corporate-innovation-scale pack or client segment is
added — not for this pack as currently scoped.

### 13. Gravity creators

Excluded as a *standalone new skill*, not as a concept — this heuristic
substantially overlaps two patterns already present and in active use in
`references/bmc-innovation-pattern-library.md`: `operating.chain.lock_in`
and `experience.relationships.switching_costs`, both already reachable
through the existing `bmc-innovation-pattern-matching` skill. The
distinction (this heuristic is an *evaluative lock-in-resilience score*
for an existing model, the pattern library is a *generative* pattern-
matching tool for building a new one) is real, but it's better solved by
extending the existing `bmc-canvas-diagnostic-reading` skill with a
seventh diagnostic rule ("does this model have a gravity creator, or is
it a wide-open door for switching?") than by writing an entirely new
skill that would compete with a skill already covering the same ground.
Flag this for the skill-writing step as an *enhancement to an existing
skill*, not a new one.

## Summary table

| # | Heuristic | Recommendation | Concreteness | Grounding strength |
|---|---|---|---|---|
| 1 | Prototype the numbers immediately | New skill | Strong | Strong (Lean Canvas tradition) |
| 2 | Corporate antibodies | New skill | Strong | Strong (named HBR concept) |
| 3 | Better revenue vs. more revenue | New skill | Strong | Strong (named Strategyzer concept) |
| 4 | CAC-to-budget alignment | New skill | Strong | Moderate (general practice, no single author) |
| 5 | Left-side risk/security reading | New skill | Strong | Moderate (owner's own synthesis + ISO 31000 anchor) |
| 6 | Low-tech ↔ high-tech repositioning | New skill | Strong | Strong (named Osterwalder pattern + 2 verified cases) |
| 7 | Two-week experiment rule | New skill | Strong | Moderate (Maurya tradition; named attribution unverified) |
| 8 | Adjacent-salesperson interview | New skill | Strong | Weak-moderate (technique well-established; specific framing unverified) |
| 9 | Sensing → sensemaking | New skill, needs concretizing | Weak | Moderate (Weick + current 2026 discourse) |
| 10 | Hunting zones | New skill | Strong | Strong (named Binns/O'Reilly/Tushman concept) |
| 11 | McGrath 50% leadership-time rule | Not this pack | Moderate | Weak (exact test unverified) |
| 12 | VC portfolio approach | Not this pack (client-profile mismatch) | Strong | Strong (but wrong audience) |
| 13 | Gravity creators | Enhance existing skill, not new | Strong | Strong (named Osterwalder pattern, already in library) |

## Next step

Once this selection is confirmed, write the actual skills (10 new
`SKILL.md` files, or 9 new + 1 enhancement to `bmc-canvas-diagnostic-reading`
for gravity creators) — not done yet, per the brief for this pass.
