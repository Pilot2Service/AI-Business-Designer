# Maturity Levels

Kypsyystaso ei ole SKILL.md-frontmatterissa (ks. `frontmatter_schema.md`) vaan
`skills_index.json`:ssa jokaisella skillillä.

| Taso | Merkitys | Kuka voi asettaa |
|---|---|---|
| `scaffold` | Rakenne ja ankkurointi valmis, omaa kokemusta ei vielä lisätty | Oletusarvo uudelle skillille |
| `draft` | `[OWNER INPUT]` täytetty, käytetty kerran käytännössä, ei vielä validoitu laajemmin | Omistaja |
| `validated` | Käytetty useammassa oikeassa tilanteessa, toimivaksi todettu | Omistaja |
| `canonical` | Vakiintunut, organisaation viralliseksi standardiksi nostettu tekniikka | Omistaja |

**Agentin luottamussääntö:** `canonical` > `validated` > `draft` > `scaffold`.
`scaffold`-tason sisältöä saa käyttää rakenteena, mutta agentin tulee tehdä näkyväksi,
että omaa validoitua kokemusta ei vielä ole liitetty (ks. pakin `CLAUDE.md`).
