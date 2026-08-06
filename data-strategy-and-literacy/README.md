# Data Strategy & Literacy

Miten AI Business Designer "lukee" dataa: hahmottaa datan todellisen roolin
(mahdollistaja vs. strateginen assetti), arvioi organisaation
datalukutaidon, lukee datasetin kriittisesti ennen kuin sen perusteella
tehdään päätöksiä, kääntää datan/mallin logiikan liiketoiminnan tarinaksi,
muotoilee Data & AI -strategian holistisesti ja valitsee sopivan
monetisointimallin. Vastaa kysymykseen "mitä data organisaatiossa oikeasti
on ja miten sitä pitäisi kohdella" — perusta, jonka päälle
`ai-strategy-and-governance`-, `business-case-and-analysis`- ja
`business-model-canvas`-pakkien AI-/liiketoimintapäätökset rakentuvat.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `data-role-diagnosis` | Diagnosoi toimiiko data mahdollistajana vai strategisena assettina — resale-, flywheel- ja defensibility-testit, Offense/Defense-kehys. |
| `data-literacy-competency-assessment` | Arvioi organisaation datalukutaidon nelikenttäkehyksellä (Ymmärtäminen, Toimintaan vieminen, Vaikuttaminen, Etiikka) roolikohtaisesti. |
| `data-bias-and-quality-critical-reading` | Lukee datasetin kriittisesti: vinoumataksonomia (valinta, selviytyjä, historiallinen, mittaus, aggregointi), turhamaisuus- vs. toimintamittari. |
| `data-storytelling-and-business-translation` | Kääntää datan/mallin logiikan Data→Information→Insight→Action-tikapuulla päätökseen johtavaksi tarinaksi. |
| `data-ai-strategy-design-and-prioritization` | Muotoilee Data & AI -strategian Driver Tree -työkalulla ja priorisoi investoinnit Data Readiness × Strategic Value -nelikentällä. |
| `data-monetization-model-selection` | Valitsee suoran (DaaS, Insight-as-a-Service, datavaihdanta) tai epäsuoran (tuotteen rikastaminen, optimointi, riskien minimointi, Data Flywheel) monetisointimallin päätöspuulla. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Skillien looginen kulku

```
data-literacy-competency-assessment   (valinnainen lähtökohta: missä osaamisvaje on)
              │
              ▼
data-bias-and-quality-critical-reading   (varmista datan luotettavuus ennen käyttöä)
              │
              ▼
data-role-diagnosis                      (mahdollistaja vai strateginen assetti?)
              │
        ┌─────┴─────┐
        ▼           ▼
data-ai-strategy-   data-monetization-
design-and-         model-selection
prioritization      (jos assetti-rooli
(priorisoi mitä      validoitui, valitse
data/AI-investointia miten monetisoidaan)
tehdä nyt/myöhemmin)
        │           │
        └─────┬─────┘
              ▼
data-storytelling-and-business-translation
   (käytä koko ajan rinnalla — jokainen löydös
    pitää kääntää päätökseen johtavaksi tarinaksi)
```

Skillit on suunniteltu käytettäviksi myös itsenäisesti (ks.
`../meta/skill_design_principles.md` — independence-testi), mutta yllä
oleva polku vastaa tyypillistä datastrategiatoimeksiannon etenemistä:
ensin varmista osaaminen ja datan luotettavuus, sitten diagnosoi rooli,
sitten priorisoi ja valitse malli, ja käännä jokainen löydös koko ajan
tarinaksi joka johtaa päätökseen.

## Suhde muihin pakkeihin

- **`ai-strategy-and-governance/ai-opportunity-portfolio`** — vastaanottaa
  tämän pakin `data-ai-strategy-design-and-prioritization`-skillin
  tuottamat priorisoidut data/AI-mahdollisuudet osaksi laajempaa
  5-ulotteista pisteytystä (erityisesti Data Readiness -ulottuvuus).
- **`business-case-and-analysis/roi-npv-sensitivity-model`** —
  vastaanottaa tämän pakin `data-monetization-model-selection`-skillin
  valitseman mallin taloudellisen laskennan syötteeksi.
- **`change-and-communication/executive-narrative-and-storyline`** —
  yleinen johdon tarinarakenne, jota `data-storytelling-and-business-
  translation` erikoistaa datalöydöksiin.
- **`specialisation-packs/business-model-canvas`** — sen innovaatio-
  patternikirjaston Financial Model -osiossa on data-monetisaatio-
  patterneja (mm. `financial.rev.data_monetization`); tämän pakin
  `data-monetization-model-selection` syventää valintaa niiden taakse.
- **`strategic-thinking/hypothesis-driven-strategy`** — sama issue tree
  -logiikka kuin tämän pakin Driver Tree -työkalussa, sovellettuna
  yleisemmin strategisiin kysymyksiin.

## Ankkurointi

- Mahdollistaja vs. strateginen assetti -jaottelu ja Data & AI Design
  Thinking -perinne (Driver Tree, Agile Value Assessment, "Systems over
  Objects") — toimialan konsultointikäytäntö, usean lähteen synteesi 2026.
- DALI-tyyppinen datalukutaitokehys (kansalais- ja ammattilaistason
  datalukutaidon nelikenttä: Understanding, Acting, Engaging, Ethics &
  Privacy).
- Ackoff, Russell L. — DIKW-hierarkia (1989), sovellettuna Data →
  Information → Insight → Action -tikapuuna.
- Davenport, Thomas H. & Bean, Randy — Offense/Defense-kehys
  datastrategialle.
- Minto, Barbara — Pyramid Principle (1996) data-storytellingin
  rakenteena.
- Collins, Jim — flywheel-käsite (*Good to Great*, 2001), sovellettuna
  data-/AI-kontekstiin.
- Tilastotieteen ja koneoppimisen vakiintunut vinoumataksonomia
  (selection/survivorship/historical/measurement/aggregation bias).
- Suoran ja epäsuoran datan monetisoinnin mallit — toimialan
  konsultointikäytäntö, usean lähteen synteesi 2026.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, heuristiikkakokoelmat
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
