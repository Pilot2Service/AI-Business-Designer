# AI Business Designer — Skills

**8 ydinpakkia · 3 täytettyä erikoistumispakkia · 78 skilliä · 4 audit-agenttia ·
itsenäinen (ei ulkoisia riippuvuuksia) · CI-validoitu · MIT**

**Versio:** 0.17.0 · **Tila:** 8 ydinpakkia (pääosin scaffold, osin validated) + 3 täytettyä erikoistumispakkia (`research-commercialisation`, `ai-native-startup-design`, `business-model-canvas`)

Uusi tässä repossa? Aloita [`QUICKSTART.md`](QUICKSTART.md):stä — yksi polku, viisi
minuuttia, ensimmäinen skilli ajossa.

Tämä on AI Business Designer -roolin skills-pack Claude Code / Cowork -ympäristöön.
Se yhdistää strategisen liiketoimintaosaamisen, opportunity recognitionin, business case
-laadinnan ja AI-strategian yhdeksi systemaattiseksi, koneluettavaksi skills-kokoelmaksi.

> **Tärkeää:** jokainen tämän pakin tuottama analyysi, laskelma tai suositus on
> päätöksenteon tueksi tehty luonnos — ei valmis päätös eikä korvaa toimialan tai
> talouden ammattilaisen vahvistusta. Ihminen tekee päätöksen ja kantaa siitä vastuun.

Rakennettu kolmen työvaiheen pohjalta:

1. **Markkinakartoitus** olemassa olevista business/AI-strategy-skills-packeista
   (avoimet GitHub-repot, skills-markkinapaikat, Claude-ekosysteemi).
2. **Markkinan taito-odotusten tutkimus** (mm. WEF Future of Jobs, LinkedIn
   Skills on the Rise, SFIA, IIBA/BABOK, ja akateeminen opportunity
   recognition -kirjallisuus).
3. **Rakenteellinen referenssi:** kypsyystaso- ja agent-guide-ajattelu
   omasta aiemmasta työstä, sekä rakenneanalyysi toisesta, tuotantokäytössä
   olevasta suomalaisesta Claude-plugin-markkinapaikasta, josta tämä repo
   omaksui: minimaalisen frontmatterin (vain `name`+`description`), pakkitason
   `CLAUDE.md`-suojauskerroksen, "mitä tämä EI tee" -rajaukset ja
   generointi/validointi-skriptimallin.

## Rakenne

```
ai-business-designer-skills/
├── README.md
├── QUICKSTART.md                      aloita tästä — yksi polku, yksi skilli, 5 min
├── AGENT_GUIDE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── skills_index.json                  koneluettava indeksi (generoitu — älä muokkaa käsin)
├── .claude-plugin/
│   └── marketplace.json               listaa kaikki pluginit (pakit)
├── .github/workflows/
│   └── validate.yml                   CI: generate_index.py + validate.py jokaisessa pushissa
├── scripts/
│   ├── generate_index.py              rakentaa skills_index.json levyltä ja frontmattereista
│   └── validate.py                    tarkistaa rakenteen ja frontmatterin ennen commitia
├── meta/
│   ├── repo_purpose.md
│   ├── skill_design_principles.md
│   ├── frontmatter_schema.md          name + description — EI muita kenttiä
│   ├── maturity_levels.md
│   ├── competency_map.md              taitomatriisi ↔ tutkimuslähteet
│   ├── shared-guardrails.md           yksi lähde: vastuuvapaus, ei keksittyjä lukuja, premissientarkistus
│   └── external-data-mcp.md           valinnaiset ulkoiset data-MCP:t (ei riippuvuuksia)
├── strategic-thinking/                [plugin] 6 skilliä
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md                      pakin jaetut suojaukset (varaverkko)
│   ├── README.md
│   ├── skills/<skill-id>/SKILL.md     frontmatter: vain name + description
│   └── references/
├── opportunity-recognition/           [plugin] 8 skilliä + agents/market-sizing-cross-validator.md
├── business-case-and-analysis/        [plugin] 6 skilliä + agents/assumption-stress-tester.md
├── ai-strategy-and-governance/        [plugin] 11 skilliä + agents/ai-initiative-readiness-auditor.md
├── change-and-communication/          [plugin] 4 skilliä
├── business-design-frameworks/        [plugin] 5 skilliä + agents/competitive-blind-spot-scanner.md
├── prototyping-and-demonstration/     [plugin] 5 skilliä
├── data-strategy-and-literacy/        [plugin] 6 skilliä
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

## Agentit (delegoitavat audit-roolit)

Neljä read-only-agenttia täydentää skillejä: skilli tuottaa analyysin, agentti haastaa
tai ristiintarkistaa sen ennen kuin se menee päätöksentekoon. Kutsutaan Task-työkalulla
(`<pakki>:<agentti>`), eivät muokkaa mitään — palauttavat vain löydöstaulukon.

| Agentti | Pakki | Tehtävä |
|---|---|---|
| `assumption-stress-tester` | `business-case-and-analysis` | Haastaa business casen oletukset adversariaalisesti ennen kuin luku menee johdolle |
| `market-sizing-cross-validator` | `opportunity-recognition` | Ristiintarkistaa TAM/SAM/SOM-laskelman logiikan ja lähteet usealla riippumattomalla menetelmällä |
| `competitive-blind-spot-scanner` | `business-design-frameworks` | Etsii kilpailu-/five forces -analyysin katvealueet ja tarkistamattomat suunnat |
| `ai-initiative-readiness-auditor` | `ai-strategy-and-governance` | Auditoi AI-aloitteen opportunity-portfolion 5 ulottuvuutta ja governance-tarkistuslistaa vasten ennen hyväksyntää |

Ks. kunkin agentin oma `.md` pakin `agents/`-kansiossa täydelliset ohjeet ja tulostusmuoto.

## Käyttöönotto (Claude Code / Cowork)

```
/plugin marketplace add <tämän repon polku tai GitHub-osoite>
/plugin
```

Valitse Discover-välilehdeltä haluamasi pakit (esim. `strategic-thinking`,
`business-case-and-analysis`).

## Laadunvarmistus

```
python3 scripts/generate_index.py
python3 scripts/validate.py
```

Tarkistaa: jokaisen SKILL.md- ja agents/*.md-frontmatterin (vain sallitut kentät), että
jokaisella pakilla on `CLAUDE.md`+`README.md`+`.claude-plugin/plugin.json`, ja että
`skills_index.json` vastaa levyllä olevia tiedostoja. Aja tämä ennen kuin lisäät tai
muutat skillejä, ja aja `python3 scripts/generate_index.py` sen jälkeen kun olet lisännyt
uuden skillin — älä muokkaa `skills_index.json`:ia käsin.

**CI:** `.github/workflows/validate.yml` ajaa saman tarkistuksen automaattisesti
jokaisessa pushissa ja pull requestissa — rikkinäinen frontmatter tai indeksin
epäsynkronointi estää mergen ilman että kukaan tarkistaa sitä käsin.

## Tila ja jatkokehitys

Repossa on nyt 8 ydinpakkia (51 skilliä, joista 47 `scaffold`- ja 4 `validated`-tasolla)
ja 3 erikoistumispaikkaa. Suurin osa ydinskilleistä on edelleen `scaffold`-tasolla:
rakenne, ankkurointi ja kysymysrunko on valmis, mutta omat heuristiikat, mallipohjat ja
case-esimerkit puuttuvat vielä (merkitty `[OWNER INPUT — täydennettävä]` jokaisessa
SKILL.md:ssä, ja kypsyys näkyy `skills_index.json`:ssa — ei enää frontmatterissa).
Poikkeuksena `opportunity-recognition`-pakin 3 owner-skilliä (oma metodologia) ja
`business-design-frameworks`-pakin `strategy-canvas-and-value-curve` (Blue Ocean
Strategy + oma 360-vertailutyökalu).

`business-design-frameworks/` on tarkoituksella avoin ja kasvava kokoelma
liiketoiminnan jäsentämis- ja mallinnustapoja (kerrokset, arvoketjut,
kategoriamallinnus, strategiakartat/arvokäyrät) — sitä täydennetään jatkossa uusilla
malleilla sitä mukaa kun niitä tunnistetaan.

`prototyping-and-demonstration/` vastaa kysymykseen "miten mahdollisuus
tehdään konkreettiseksi ja uskottavaksi": nopea protoilu (AI-avusteinen
"vibe coding"), demon/PoC:n oikea kehystäminen asiakkaalle (PoC vs.
Pilotti vs. MVP, "pilot purgatory" -riskin torjunta), demon esitystaito
(Great Demo! -metodologia) ja tarina (Amazon Working Backwards/PR-FAQ),
sekä silta demosta business caseen ja ROI-laskelmaan.

Uusin ydinpakki, `data-strategy-and-literacy/`, vastaa kysymykseen "mitä
data organisaatiossa oikeasti on ja miten sitä pitäisi kohdella": datan
roolin diagnostiikka (mahdollistaja vs. strateginen assetti),
datalukutaidon nelikenttäarviointi, datan kriittinen lukeminen (bias,
laatu, edustavuus), data-storytelling liiketoimintakielelle, Data & AI
-strategian muotoilu (Driver Tree, Agile Value Assessment) ja datan
monetisointimallin valinta (suora vs. epäsuora, Data Flywheel-
toteutettavuustarkistus).

`specialisation-packs/` sisältää neljä paikkaa erikoistumisalueille:
`public-sector-pilot-scaling` on yhä placeholder. Kolme muuta on täytetty:

- **`research-commercialisation`** (`validated`/`owner`) — 12 skilliä,
  konvertoitu omistajan julkaisemasta kaupallistamisoppaasta ja
  AFCA-itsearviointityökalusta — ks.
  `specialisation-packs/research-commercialisation/README.md`.
- **`ai-native-startup-design`** (sekoitettu: 5 `validated`/`owner` + 3
  `draft`/`owner`) — 8 skilliä. Runko konvertoitu omistajan
  fasilitoimasta *AI-native Business Design* -työpajasta pre-startup-
  perustajille (1.–2.6.2026): AI-mahdollisuuksien tunnistus, ICP/JTBD-
  asiakasymmärrys, rakennusagentille annettava PRD, closed-loop-
  prosessisuunnittelu ja AI-työkalupinon valinta. Syvennetty ja
  laajennettu ulkopuolisen *AI-first SaaS Product* -työpajan menetelmällä
  (5+2 tarveteemapisteytys, AI wedge -valinta, ratkaisuideointi, RICE-
  MVP-valinta, keskusteleva OS-arkkitehtuuri), sovellettuna omistajan
  omaan caseen — ks.
  `specialisation-packs/ai-native-startup-design/README.md`.
- **`business-model-canvas`** (sekoitettu: 3 `validated`/`owner` + 4
  `scaffold`/`research`) — 7 skilliä, yhdistää julkisen 159 patternin
  innovaatiokirjaston omistajan omaan, huhtikuun 2026
  konsultointihaastattelusta poimittuun BMC-metodologiaan
  (omistajan oma, ei-julkinen tutkimustyö) ja tunnettujen BMC-lähteiden
  (Jeffries, van der Linden, Blank, Ash Maurya) tutkimuspohjaiseen
  synteesiin — ks.
  `specialisation-packs/business-model-canvas/README.md`.

## Ulkoiset datalähteet (valinnainen, ei riippuvuus)

Tämä repo ei vaadi mitään ulkoista MCP-palvelinta toimiakseen — kaikki skillit toimivat
itsenäisesti käyttäjän antamalla lähtödatalla. Jos ympäristössä on kytketty relevantti
data-MCP (esim. markkinakoko-/talousdatalähde), kyseinen skilli voi käyttää sitä
oletusten sijaan tai niiden ristiintarkistukseen. Ks. `meta/external-data-mcp.md`
kandidaattilistaus ja käyttöperiaate.

## Lisenssi

MIT — vapaasti muokattavissa ja jaettavissa.
