# Frontmatter Schema

All `SKILL.md` files use **only** these two fields:

```yaml
---
name: kebab-case-skill-id          # required, matches the folder name
description: "..."                  # required — when and why to use this
---
```

No other fields. No `maturity`, no `pack`, no `grounded_in`, no
`last_reviewed`.

**Why:** `name` and `description` are the standard fields of the Claude
Agent Skills format (now a standard across ~26 tools). Extra fields don't
break anything, but they tie the skill to this repo's own schema and spread
the source of truth across multiple places. Keep one source of truth:

| Information | Where it lives |
|---|---|
| Maturity, source layer, anchoring, need for owner input | `skills_index.json` (generated, see `../scripts/generate_index.py`) |
| Method, technique, what it does NOT do, follow-on links | SKILL.md body text |
| Pack-level guardrails | `<pack>/CLAUDE.md` |

This convention is adopted from another, production-deployed Claude plugin
marketplace's CONTRIBUTING.md: "Frontmatter has only `name` and
`description` — no other fields."

## marketplace.json and plugin.json

These (the repo's own governance files, not SKILL.md) are allowed more
fields: `$schema`, `name`, `displayName`, `description`, `version`,
`author`/`owner`.
