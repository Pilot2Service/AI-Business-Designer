# Prompt library — AI-native Business Design workshop

Referenced by the pack's skills (`skills/*/SKILL.md`, "Method" section).
The prompts have been translated and lightly reworded for clarity from the
original `day1.md` (see `workshop-source.md`) — the meaning has not been
changed. Run the prompts in a project with your AI thinking partner
(Claude/ChatGPT) that has your own business context available.

## Prompt 1 — AI opportunity discovery (`ai-native-opportunity-scan`)

```
Act as a startup strategist who deeply understands AI — including
agentic and closed-loop approaches, not just basic productivity use.

Look at my business (use everything you know about it from this
project). Identify 5 areas where AI could create GENUINELY NEW business
opportunities for us — not just speed up an existing process.

I want advanced or agentic use for each of the five areas: closed-loop
processes, autonomous agents, new AI-powered features, products, or
business models that were previously too slow, too costly, or
impossible.

For each of the five areas, give me:
- a short name for the opportunity
- what it is, in 2-3 sentences
- why it's newly possible specifically because of AI
- what would roughly need to be true for us to do this

Be specific to my business. Avoid generic suggestions like "use AI to
save time" or "automate customer service with an AI agent."
```

## Prompt 2 — Pressure test and prioritization (`ai-native-opportunity-scan`)

First write your own brief comments and assessment of the five findings,
then attach the following:

```
Take the 5 opportunities above. Assess each one:

- Business potential: how big could this be for us, and why?
- Customer value: what real problem does it solve, and for whom?
- Feasibility for a small team with current AI tools and resources
  (low / medium / high)
- What would be the smallest first version we could prototype this
  week?

Then rank these 5 from most promising to least promising as an AI-related
business opportunity for us right now, and justify the ranking with one
sentence per item. Recommend the one you would prototype first, and why.
```

## Prompt 3 — Vision sharpening (`customer-vision-to-jtbd`)

```
Act as an experienced product strategist working with an early-stage
startup.

Below (and in this project) is my rough product vision and customer
situation. Read it and help sharpen it.

1. Tell me what is still unclear or undefined and needs a decision from
   me.
2. Ask at most 7 clarifying questions in priority order.
3. Surface any assumptions I seem to be making that are worth checking.

Don't write a plan yet — first help me think.
```

## Prompt 4 — Ideal Customer Profile

```
Explore multiple customer profiles who have this problem, describe each,
and prioritize who we should serve first and why.
```

## Prompt 5 — Jobs To Be Done

```
Walk through a Jobs To Be Done exercise with me. Go deeper into the
customer's behavior and the situation in which the problem needs to be
solved, and what they're really trying to achieve.
```

## Prompt 6 — Need Themes, NMB scoring, and AI wedge (`customer-vision-to-jtbd`)

```
Convert the Jobs To Be Done analysis above into Need Themes — give 5
functional and 2 psychological themes. Return as a table with columns:
Need Theme / Type / Underlying "why" / Related JTBD. Each theme should be
a one- or two-word noun phrase that captures the core of the need, e.g.
affordability, relevance, trust.
```

```
Score each need theme on five criteria, each 1-5: Need Depth (depth/
acuteness of the need), Frequency (how often the need is triggered),
Market Coverage (how broadly the need touches the target market),
Business Strength (my own starting position for serving this need),
AI Advantage (how much competitive advantage AI brings to precisely this
need). Calculate a total score (max 25) and classify each as a
Differentiator- or Table Stake-level need. Return as a table and explain
the highest scores.
```

```
Select one (or two) need theme(s) as the AI differentiator need (AI
wedge): a need that simultaneously has high depth, high frequency, weak
competitor coverage, a strong starting position for me, AND a high AI
advantage. Justify the choice and explain why the other high-scoring
needs don't satisfy all the criteria equally well.
```

## Prompt 7 — Mini-PRD (`ai-buildable-prd-writing`)

```
Act as an experienced product manager helping an early-stage startup
write a focused mini-PRD for a prototype to be built with AI.

Use everything you know about my business in this project, as well as
the opportunity and notes from our earlier work in this conversation.

Write a MINI-PRD with the following sections:

1. Problem & customer — who this is for, and what pain does it solve?
2. Product vision — describe the experience in the customer's own words.
3. Core features — list only the features the first version needs.
   Describe each as the outcome the user achieves, not as a technical
   implementation.
4. Scope boundaries — what we DELIBERATELY are not building in this
   version.
5. Success criteria — how we'll know the prototype works.

Keep it tight enough to be prototyped this week. After the draft, ask me
at most 5 questions that would sharpen the PRD, then give me a revised
version.
```

## PRD checklist (`ai-buildable-prd-writing`, step 4)

- [ ] Problem & customer is specific — not "for everyone who..."
- [ ] Product vision is written in the customer's words, not as a
      feature list
- [ ] Core features are described as outcomes ("the user can…"), not as
      a technical implementation
- [ ] The Scope boundaries section exists and is concrete (not empty)
- [ ] Success criteria are measurable or observable
- [ ] The PRD contains no technology choices or architecture decisions
- [ ] Scope is trimmed to MVP level: one customer, one core job

---

**Note on prompts 8–10:** these were added from the external "AI-first
SaaS Product" workshop (see `ai-first-saas-workshop-source.md`) and sit
in the workflow between prompt 6 (Need Themes / AI wedge) and prompt 7
(PRD) — use them when the solution direction isn't yet clear for the
chosen AI wedge.

## Prompt 8 — Three solution directions (`ai-differentiator-solution-ideation`)

```
Let's start from my chosen AI differentiator need (AI wedge):
[attach the need theme + NMB score here].

Ideate 3 completely different AI-native solution directions for this
need, through three different lenses:

1. Competitor lens: how do existing players solve this today, and what
   would AI make possible that isn't possible for them?
2. Future lens: how was this need solved before (heavily, manually,
   always refitted to context), and how will it be solved in the future
   when AI continuously builds and teaches context in dialogue with the
   user?
3. Connect-the-dots lens: what other separate tasks does the user
   perform around this need that could be combined into a single
   AI-native experience?

For each direction, give me: a name, the concept (2-3 sentences), the
primary output for the user, and why it's distinctive relative to
competitors/the status quo. Don't choose for me — present all three side
by side.
```

## Prompt 9 — RICE scoring and MVP synthesis (`rice-scoring-and-mvp-synthesis`)

```
Score the 3 solution directions above with the RICE model: Reach,
Impact, Confidence (all 1-5), and Effort inverted (5 = easiest/lowest
build cost, 1 = hardest). Briefly justify each score, especially Effort
relative to my current tech stack and existing tools/data. Recommend
what should be built as the MVP and why.
```

```
For the chosen MVP, write: a) an MVP definition (2-3 sentences), b) a
one-sentence positioning statement in the format "[Product] gives
[target customer] [core benefit] through [distinctive mechanism]", c) 3
"why we win" claims that tie my strengths to a concrete competitive
advantage.
```

## Prompt 10 — Conversational OS flow (`ai-native-conversational-os-design`)

```
Design a conversational UI architecture for the chosen MVP with six
stages:

1. Intent — what are the 3-6 main reasons a user comes to this product?
2. Strategy Cards — what internal "playbooks" (reasoning modules) can
   the AI choose from for each intent? Tie each card to one previously
   identified differentiator or table-stake need.
3. Clarification — what at most 2-4 clarifying questions are needed, and
   when are they asked?
4. Output Cards — what structured results does the user get from each
   strategy card?
5. Mission — what one-sentence mission frames the next steps around
   building trust?
6. Agent Execution — what can the AI do independently after the mission
   to create forward momentum?

Write each stage concretely as applied to this MVP, not generically.
```
