# Contributing — AI Business Designer Skills

## Design principle

SKILL.md encodes correct behavior; the pack's CLAUDE.md is a safety net. If
a skill's correct outcome depends on CLAUDE.md catching a mistake, that's a
design flaw — move the information into the SKILL.md. (Principle adopted
from a structural analysis of another Claude plugin marketplace.)

## Adding a new skill

1. Copy `templates/skill-template/SKILL.md` into the right pack
   (`<pack>/skills/<new-skill-id>/SKILL.md`).
2. Frontmatter has **only** `name` and `description` — no other fields.
   `name` is kebab-case and matches the folder name. `description` states
   what the skill does and when it triggers.
3. Write the `Purpose`, `Anchored in research`, and `Method` sections
   first — these can draw on public research/frameworks.
4. Write the `What this skill does NOT do` section — at least one
   skill-specific scope limit in addition to the general ones.
5. Add `Continue from here` links: which skill this naturally leads to
   next (within the same pack and, where relevant, into another pack).
6. Leave the `[OWNER INPUT — to be completed]` section open until you
   actually have your own, validated content for it. Don't fill it with
   generic text.
7. **Run `python3 scripts/generate_index.py`** — updates `skills_index.json`
   from disk and frontmatter. Don't edit `skills_index.json` by hand.
8. **Run `python3 scripts/validate.py` before committing.** It must pass.

## Adding a new specialisation pack

Use the `templates/specialisation-pack-template/README.md` template and add
it to the `specialisation-packs/` folder. Follow the same `skills/` +
`references/` + `cases/` structure as the core packs. Add your own
`CLAUDE.md` if needed.

## Raising a skill's maturity

Once the `[OWNER INPUT]` section is filled in and the skill has been used at
least once in a real situation: update `skills_index.json`'s `maturity:
scaffold` → `draft` (rerun generate_index.py after documenting, or update
by hand and validate). Once the content has been validated across several
situations: → `validated`. `canonical` is reserved for established
techniques elevated to the organization's official standard.

## Naming conventions

- Skill ID: `kebab-case`, verb-free noun form (e.g. `business-case-builder`)
- Pack folder: domain name only, **no number prefix**
  (`strategic-thinking`, not `01-strategic-thinking`) — plugin sources are
  referenced by name in `marketplace.json`, not by order.
- No special characters, no uppercase letters in folder/file names
