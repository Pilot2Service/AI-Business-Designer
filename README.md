# AI Business Designer — Skills

**Versio:** 0.13.0 · **Tila:** 6 ydinpakkia (pääosin scaffold, osin validated) + 3 täytettyä erikoistumispakkia (`research-commercialisation`, `ai-native-startup-design`, `business-model-canvas`)

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
├── opportunity-recognition/           [plugin] 8 skilliä
├── business-case-and-analysis/        [plugin] 6 skilliä
├── ai-strategy-and-governance/        [plugin] 11 skilliä
├── change-and-communication/          [plugin] 4 skilliä
├── business-design-frameworks/        [plugin] 4 skilliä — kasvava kokoelma, ks. alla
├── specialisation-packs/              omat erikoistumisalueet
│   ├── ai-native-startup-design/       [mixed] 8 skilliä (5 validated + 3 draft) — ks. alla
│   ├── business-model-canvas/          [mixed] 7 skilliä (3 validated + 4 scaffold) — ks. alla
│   ├── public-sector-pilot-scaling/    [placeholder — täydennettävä]
│   └── research-commercialisation/     [validated] 12 skilliä — ks. alla
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

Repossa on nyt 6 ydinpakkia (37 skilliä, joista 33 `scaffold`- ja 4 `validated`-tasolla)
ja 3 erikoistumispaikkaa. Suurin osa ydinskilleistä on edelleen `scaffold`-tasolla:
rakenne, ankkurointi ja kysymysrunko on valmis, mutta omat heuristiikat, mallipohjat ja
case-esimerkit puuttuvat vielä (merkitty `[OWNER INPUT — täydennettävä]` jokaisessa
SKILL.md:ssä, ja kypsyys näkyy `skills_index.json`:ssa — ei enää frontmatterissa).
Poikkeuksena `opportunity-recognition`-pakin 3 owner-skilliä (oma [redacted]-metodologia) ja
`business-design-frameworks`-pakin `strategy-canvas-and-value-curve` (Blue Ocean
Strategy + oma [redacted] 360 -vertailutyökalu).

Uusin ydinpakki, `business-design-frameworks/`, on tarkoituksella avoin ja kasvava
kokoelma liiketoiminnan jäsentämis- ja mallinnustapoja (kerrokset, arvoketjut,
kategoriamallinnus, strategiakartat/arvokäyrät) — sitä täydennetään jatkossa uusilla
malleilla sitä mukaa kun niitä tunnistetaan.

`specialisation-packs/` sisältää neljä paikkaa erikoistumisalueille:
`public-sector-pilot-scaling` on yhä placeholder. Kolme muuta on täytetty:

- **`research-commercialisation`** (`validated`/`owner`) — 12 skilliä,
  konvertoitu omistajan julkaisemasta *[redacted] Innovator's Guide to
  Commercialisation* -käsikirjasta ja AFCA-itsearviointityökalusta — ks.
  `specialisation-packs/research-commercialisation/README.md`.
- **`ai-native-startup-design`** (sekoitettu: 5 `validated`/`owner` + 3
  `draft`/`owner`) — 8 skilliä. Runko konvertoitu omistajan
  fasilitoimasta *AI-native Business Design* -työpajasta pre-startup-
  perustajille (1.–2.6.2026): AI-mahdollisuuksien tunnistus, ICP/JTBD-
  asiakasymmärrys, rakennusagentille annettava PRD, closed-loop-
  prosessisuunnittelu ja AI-työkalupinon valinta. Syvennetty ja
  laajennettu [redacted]n *AI-first SaaS Product* -työpajan menetelmällä
  (5+2 tarveteemapisteytys, AI wedge -valinta, ratkaisuideointi, RICE-
  MVP-valinta, keskusteleva OS-arkkitehtuuri), sovellettuna omistajan
  omaan [redacted]-caseen — ks.
  `specialisation-packs/ai-native-startup-design/README.md`.
- **`business-model-canvas`** (sekoitettu: 3 `validated`/`owner` + 4
  `scaffold`/`research`) — 7 skilliä, yhdistää [redacted]-alustan 159
  patternin innovaatiokirjaston omistajan omaan, huhtikuun 2026
  konsultointihaastattelusta poimittuun BMC-metodologiaan
  (`[redacted]`-repo) ja tunnettujen BMC-lähteiden
  (Jeffries, van der Linden, Blank, Ash Maurya) tutkimuspohjaiseen
  synteesiin — ks.
  `specialisation-packs/business-model-canvas/README.md`.

## Lisenssi

MIT — vapaasti muokattavissa ja jaettavissa.
