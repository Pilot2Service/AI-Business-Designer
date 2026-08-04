# Frontmatter Schema

Kaikki `SKILL.md`-tiedostot käyttävät **ainoastaan** näitä kahta kenttää:

```yaml
---
name: kebab-case-skill-id          # pakollinen, sama kuin kansion nimi
description: "..."                  # pakollinen — milloin ja miksi tätä käytetään
---
```

Ei muita kenttiä. Ei `maturity`, ei `pack`, ei `grounded_in`, ei `last_reviewed`.

**Miksi:** `name` ja `description` ovat Claude Agent Skills -formaatin (nyt ~26
työkalun standardi) vakiokentät. Lisäkentät eivät riko mitään, mutta ne sitovat skillin
tämän repon omaan skeemaan ja hajauttavat totuuden useaan paikkaan. Pidä yksi totuuden
lähde:

| Tieto | Missä elää |
|---|---|
| Kypsyys, lähdekerros, ankkurointi, omistajan syötteen tarve | `skills_index.json` (generoitu, ks. `../scripts/generate_index.py`) |
| Rakenne, tekniikka, mitä EI tee, jatkolinkit | SKILL.md:n leipäteksti |
| Pakkitason suojaukset | `<pack>/CLAUDE.md` |

Tämä konvensio omaksuttu `[redacted]/claude-for-legal-finland`-repon
CONTRIBUTING.md:stä: "Frontmatterissa vain `name` ja `description` — ei muita kenttiä."

## marketplace.json ja plugin.json

Näissä (repon omaa hallintoa, ei SKILL.md) saa olla enemmän kenttiä: `$schema`, `name`,
`displayName`, `description`, `version`, `author`/`owner`.
