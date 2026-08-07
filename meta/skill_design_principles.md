# Skill Design Principles

Every SKILL.md should pass these six tests:

1. **Independence test** — Would this content still work if we swapped the
   Claude model for another one? If yes, it belongs in this repo as
   structure. If the content is your own validated experience, it's even
   more valuable — a model won't invent it on its own.
2. **Concreteness test** — Does the skill contain a usable structure (steps,
   questions, a table), not just a heading list or buzzword description?
3. **Anchoring test** — Does the skill reference a recognized framework
   (Liedtka, BABOK, Kirzner, McKinsey, SFIA) or your own validated
   experience — not neither?
4. **Maturity honesty test** — Does the skill clearly separate what's
   research-grounded structure from what's still unfilled with your own
   experience (`[OWNER INPUT]`)?
5. **Scope test** — Does the skill also state what it does NOT do? A skill
   without stated limits invites the user to trust it more broadly than
   they should.
6. **Discoverability test** — Is the skill included in `skills_index.json`
   with the right metadata, so an agent can find it without reading the
   entire repo?

## Frontmatter minimalism

SKILL.md frontmatter contains **only** `name` and `description`. All other
metadata (maturity, source layer, anchoring) lives in `skills_index.json` or
in the skill body itself. This keeps skills compatible with any agent that
supports the SKILL.md format, without tying them to this repo's own extra
fields. (Principle adopted from a structural analysis of another Claude
plugin marketplace — see CONTRIBUTING.md.)
