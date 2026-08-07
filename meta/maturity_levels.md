# Maturity Levels

Maturity is not in the SKILL.md frontmatter (see `frontmatter_schema.md`) —
it lives in `skills_index.json`, per skill.

| Level | Meaning | Who can set it |
|---|---|---|
| `scaffold` | Structure and anchoring are in place; own experience not yet added | Default for a new skill |
| `draft` | `[OWNER INPUT]` filled in, used once in practice, not yet validated more broadly | Owner |
| `validated` | Used in several real situations, proven to work | Owner |
| `canonical` | Established, elevated to the organization's official standard technique | Owner |

**Agent trust rule:** `canonical` > `validated` > `draft` > `scaffold`.
`scaffold`-level content may be used as structure, but the agent must make
visible that no own validated experience has been added yet (see the
pack's `CLAUDE.md`).
