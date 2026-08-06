---
status: validated
owner_input_needed: false
last_reviewed: 2026-08-04
---

# Research Commercialisation

Miten tutkimustulos tai IP muutetaan kaupallistettavaksi tuotteeksi, palveluksi tai
yhtiöksi: mahdollisuuden tunnistamisesta IP-strategiaan, TTO-yhteistyöhön,
rahoitukseen, tiiminrakennukseen ja perustajan valmiuden itsearviointiin.

## Tila

Tämä pakki on rakennettu suoraan omistajan julkaisemasta
**omistajan julkaisema kaupallistamisopas** -käsikirjasta (omistajan oma palvelu, 2025,
75 sivua) sekä sen AFCA-itsearviointityökalusta. Se ei ole tutkimustason scaffold
vaan omistajan validoituun, n. 500 kaupallistamisprojektin kokemukseen perustuvaan
menetelmään ankkuroitu sisältö — `source_layer: owner`, `maturity: validated`
kaikilla skilleillä (ks. `../../skills_index.json`).

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `research-opportunity-recognition` | Arvioi onko tutkimustuloksella todellista kaupallista potentiaalia — market pull vs. technology push. |
| `spinout-vs-licensing-pathway` | Valitse kaupallistamisreitti: spin-out, lisensointi vai hybridi. |
| `ip-disclosure-and-ownership-check` | Selvitä IP:n omistus ja tee oikea-aikainen keksintöilmoitus. |
| `tto-engagement-strategy` | Käytä Technology Transfer Officea tehokkaasti, tunnista milloin tarvitaan lisätukea. |
| `industry-specific-commercialisation-playbook` | Räätälöi strategia toimialan mukaan: life sciences, deep tech, ohjelmisto, impact. |
| `funding-pathway-design` | Yhdistä dilutoimaton ja dilutoiva rahoitus, hallitse runwayta. |
| `commercialisation-journey-roadmap` | Viiden vaiheen kokonaisroadmap: mahdollisuus → konsepti → validointi → strategia → toteutus. |
| `founding-team-design-and-agreements` | Rakenna tasapainoinen perustajatiimi ja Founders' Agreement. |
| `industry-partner-engagement` | Ota toimialakumppanit mukaan varhain. |
| `academic-entrepreneur-role-choice` | Valitse oma rooli: täysipäiväinen perustaja, neuvonantaja vai osa-aikainen. |
| `commercialisation-readiness-check` | Missio-, idea- ja valmiustesti ennen aloitusta. |
| `founder-competence-self-assessment` | AFCA — 10 osa-alueen / 76 kohdan itsearviointi perustajan valmiudesta. |

## Ankkurointi

- omistajan julkaisema kaupallistamisopas (omistaja, 2025)
- AFCA — Founder's Competence Assessment (omistajan oma työkalu), synteesi EU:n
  EntreComp- ja ResearchComp-kehyksistä
- Käsikirjan omat lähteet: ks. `references/sources.md`

## Skillien looginen kulku

```
research-opportunity-recognition
        │
        ▼
spinout-vs-licensing-pathway ──► ip-disclosure-and-ownership-check
        │                               │
        │                               ▼
        │                       tto-engagement-strategy
        │                               │
        ▼                               ▼
industry-specific-commercialisation-playbook ──► funding-pathway-design
        │
        ▼
commercialisation-journey-roadmap
        │
        ▼
founding-team-design-and-agreements ──► industry-partner-engagement
        │
        ▼
academic-entrepreneur-role-choice
        │
        ▼
commercialisation-readiness-check ──► founder-competence-self-assessment
```

Skillit on suunniteltu käytettäviksi myös itsenäisesti (ks.
`../../meta/skill_design_principles.md` — independence-testi), mutta yllä oleva
polku vastaa käsikirjan omaa etenemisjärjestystä ja sopii ensikertalaiselle.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  terminologia, AFCA-data, case-studyt, lähteet
cases/                       (varattu — tulevat omat, anonymisoidut projektitapaukset)
```

Katso `../../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin
sisältöä.
