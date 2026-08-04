# AI Business Designer — Skills

**Versio:** 0.2.0 (scaffold) · **Tila:** perusrakenne, täydennettävä omalla osaamisella

Tämä on AI Business Designer -roolin skills-pack Claude Code / Cowork -ympäristöön.
Se yhdistää strategisen liiketoimintaosaamisen, opportunity recognitionin, business case
-laadinnan ja AI-strategian yhdeksi systemaattiseksi, koneluettavaksi skills-kokoelmaksi.

> **Tärkeää:** jokainen tämän pakin tuottama analyysi, laskelma tai suositus on
> päätöksenteon tueksi tehty luonnos — ei valmis päätös eikä korvaa toimialan tai
> talouden ammattilaisen vahvistusta. Ihminen tekee päätöksen ja kantaa siitä vastuun.
> (Sama periaate kuin claude-for-legal-finlandin "luonnos, ei oikeudellista neuvontaa".)

Rakennettu kolmen työvaiheen pohjalta:

1. **Markkinakartoitus** olemassa olevista business/AI-strategy-skills-packeista (GitHub,
   skills.sh, Claude-ekosysteemi) — ks. `../skills-tutkimus-analyysi.md`
2. **Markkinan taito-odotusten tutkimus** (WEF, LinkedIn, SFIA, IIBA/BABOK, McKinsey,
   akateeminen opportunity recognition -kirjallisuus) — ks.
   `../markkinan-taito-odotukset-analyysi.md`
3. **Rakenteellinen referenssi kahdesta lähteestä:**
   - oma `charlotte-semantic-layer-template`-repo (kypsyystaso- ja agent-guide-ajattelu)
   - [`[redacted]/claude-for-legal-finland`](https://github.com/[redacted]/claude-for-legal-finland)
     — tuotantokäytössä oleva suomalainen Claude-plugin-markkinapaikka, josta tämä repo
     omaksui: minimaalisen frontmatterin (vain `name`+`description`), pakkitason
     `CLAUDE.md`-suojauskerroksen, "mitä tämä EI tee" -rajaukset ja
     generointi/validointi-skriptimallin.

## Rakenne

```
ai-business-designer-skills/
├── README.md
├── AGENT_GUIDE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── skills_index.json                  koneluettava indeksi (generoitu — älä muokkaa käsin)
├── .claude-plugin/
│   └── marketplace.json               listaa kaikki pluginit (pakit)
├── scripts/
│   ├── generate_index.py              rakentaa skills_index.json levyltä ja frontmattereista
│   └── validate.py                    tarkistaa rakenteen ja frontmatterin ennen commitia
├── meta/
│   ├── repo_purpose.md
│   ├── skill_design_principles.md
│   ├── frontmatter_schema.md          name + description — EI muita kenttiä
│   ├── maturity_levels.md
│   └── competency_map.md              taitomatriisi ↔ tutkimuslähteet
├── strategic-thinking/                [plugin] 5 skilliä
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md                      pakin jaetut suojaukset (varaverkko)
│   ├── README.md
│   ├── skills/<skill-id>/SKILL.md     frontmatter: vain name + description
│   └── references/
├── opportunity-recognition/           [plugin] 5 skilliä
├── business-case-and-analysis/        [plugin] 6 skilliä
├── ai-strategy-and-governance/        [plugin] 5 skilliä
├── change-and-communication/          [plugin] 4 skilliä
├── specialisation-packs/              omat erikoistumisalueet (täydennettävä)
│   ├── ai-native-startup-design/
│   ├── public-sector-pilot-scaling/
│   └── research-commercialisation/
├── templates/
│   ├── skill-template/SKILL.md
│   └── specialisation-pack-template/README.md
└── playbooks/                         skillien ketjutusohjeet tehtävätyypeittäin
    ├── idea-to-decision.md
    └── ai-initiative-scoping.md
```

## Käyttöönotto (Claude Code / Cowork)

```
/plugin marketplace add <tämän repon polku tai GitHub-osoite>
/plugin
```

Valitse Discover-välilehdeltä haluamasi pakit (esim. `strategic-thinking`,
`business-case-and-analysis`).

## Laadunvarmistus

```
python3 scripts/validate.py
```

Tarkistaa: jokaisen SKILL.md-frontmatterin (vain `name`+`description`), että jokaisella
pakilla on `CLAUDE.md`+`README.md`+`.claude-plugin/plugin.json`, ja että
`skills_index.json` vastaa levyllä olevia tiedostoja. Aja tämä ennen kuin lisäät tai
muutat skillejä, ja aja `python3 scripts/generate_index.py` sen jälkeen kun olet lisännyt
uuden skillin — älä muokkaa `skills_index.json`:ia käsin.

## Tila ja jatkokehitys

Kaikki 25 ydinskilliä ovat `scaffold`-tasolla: rakenne, ankkurointi ja kysymysrunko on
valmis, mutta omat heuristiikat, mallipohjat ja case-esimerkit puuttuvat vielä (merkitty
`[OWNER INPUT — täydennettävä]` jokaisessa SKILL.md:ssä, ja kypsyys näkyy
`skills_index.json`:ssa — ei enää frontmatterissa).

`specialisation-packs/` sisältää kolme paikkaa varattuna erikoistumisalueille:
`ai-native-startup-design`, `public-sector-pilot-scaling`, `research-commercialisation`.
Nämä ovat tyhjiä runkoja odottamassa omaa syväosaamistasi — ei täytetty geneerisellä
sisällöllä, koska se ei edustaisi todellista osaamistasi.

## Lisenssi

MIT — vapaasti muokattavissa ja jaettavissa.
