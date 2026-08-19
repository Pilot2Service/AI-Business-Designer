# Task starter: AI Idea Portfolio Scoring

**When to use:** You (or your client) have a pile of AI ideas — five, ten,
twenty — and no reliable way to say which deserve real investment versus
which are a "quick win" or "not worth it."

**What to provide:** A list of the ideas, even as rough one-liners, plus
anything you know about your data situation and strategic priorities.

**Start with this:**

1. "Use the ai-opportunity-portfolio skill to score these AI ideas: [paste
   your list]. Score each on the 5-dimension model (business impact,
   technical feasibility, data readiness, strategic alignment, speed to
   value/risk) and place them on the Quick Wins / Strategic Bets /
   Deprioritize / Hard-Low Value matrix."
2. "Before scoring, run the ai-reshuffle-opportunity-framing skill on
   [specific idea] — is this a genuine value-chain reshuffle, or just
   automating something that already works the same way?"
3. "Get a second opinion: use the ai-initiative-readiness-auditor agent to
   check this portfolio's scoring and governance readiness for gaps before
   it goes to leadership."

**What you get:** A scored, prioritized shortlist with the reasoning visible
per dimension — not a gut-feel ranking — plus, if you use variant 2, an
explicit flag on any idea that's automation dressed up as transformation.

**What happens next:** Take the top 1–2 "Quick Wins" into
`ai-use-case-feasibility-and-poc-scoping`, or follow the full
`playbooks/ai-initiative-scoping.md` chain for the path to an approved
pilot.

## Skills used

1. `ai-strategy-and-governance/skills/ai-opportunity-portfolio`
2. `ai-strategy-and-governance/skills/ai-reshuffle-opportunity-framing`
3. `ai-strategy-and-governance/agents/ai-initiative-readiness-auditor`
4. `ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping`
