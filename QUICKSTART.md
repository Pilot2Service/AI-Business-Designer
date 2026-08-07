# Quickstart — one path, five minutes

The shortest route to running your first skill. Full structure and all
packs: [`README.md`](README.md). How an agent uses this pack:
[`AGENT_GUIDE.md`](AGENT_GUIDE.md).

## 1. Install the marketplace

In a Claude Code environment (Cowork installs plugins from its own
connector panel — the principle is the same, the UI differs):

```
/plugin marketplace add Pilot2Service/AI-Business-Designer
/plugin
```

The first command reads this repo's `.claude-plugin/marketplace.json` from
GitHub in `owner/repo` form (the marketplace name comes from the file:
`ai-business-designer-skills`) — it doesn't clone the whole repo locally,
it registers the catalog. The second command opens a menu: choose
**Browse and install plugins**, select the marketplace, and install the
packs you want one at a time.

## 2. Pick one pack

You don't need all 8 core packs at once. Pick one based on the task:

| Situation | Pack |
|---|---|
| "Is there a business opportunity here?" | `opportunity-recognition` |
| "I need an ROI case for an investment" | `business-case-and-analysis` |
| "Which AI use cases are worth prioritizing?" | `ai-strategy-and-governance` |
| "I need to structure a big, unclear problem" | `strategic-thinking` |
| "How do I present a change to leadership?" | `change-and-communication` |

Install the pack you chose from the menu (e.g. `opportunity-recognition`).
Or directly with a command: `/plugin install
opportunity-recognition@ai-business-designer-skills`.

## 3. Run one skill

Example: the `opportunity-recognition` pack has
`opportunity-value-assessment`. Tell Claude something along these lines:

```
Use the opportunity-value-assessment skill to assess this idea: [describe
your situation in 2-3 sentences — what problem, for whom, why now]
```

## 4. What you should get back

Every skill produces a **structured draft**, not a finished answer:

- A structured analysis / score / framework — not a free-form essay.
- Visible assumptions — anything unknown is marked `[assumption —
  verify]`, not silently filled in.
- Visible maturity — Claude states whether the skill used is `scaffold`
  (structure in place, no own validated experience yet) or
  `validated`/`canonical` (tested in practice). Check `skills_index.json`
  if you need to confirm.
- **No final decision.** The output is always for a human to review and
  approve — see `meta/shared-guardrails.md`.

If the result doesn't look like this (e.g. Claude presents a number without
a source note, or claims a skill's content is your own validated
experience when it's at `scaffold` level), something went wrong — check
that the right pack's `CLAUDE.md` was read.

## 5. Next step

- Want a ready-made chain instead of a single skill? See `playbooks/` (e.g.
  `playbooks/idea-to-decision.md`).
- Want to challenge/cross-check a result before it moves forward? Four
  packs include a delegatable agent for this (`agents/` folder) — see the
  "Delegatable agents" table in the README.
- Want to add your own skill or fill in an `[OWNER INPUT]` section? See
  `CONTRIBUTING.md`.
