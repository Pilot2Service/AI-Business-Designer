---
name: rice-scoring-and-mvp-synthesis
description: "Pisteyttää useamman ratkaisusuunnan RICE-mallilla (Reach, Impact, Confidence, Effort) MVP:n valitsemiseksi, ja kääntää valinnan MVP-määritelmäksi, yhden lauseen positiointilauseeksi ja kolmeksi 'miksi voitamme' -väittämäksi."
---

# RICE Scoring and MVP Synthesis

*Tila: `draft`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Muuttaa useamman ratkaisuvaihtoehdon vertailu objektiiviseksi,
perustelluksi MVP-valinnaksi RICE-mallilla, ja kääntää valinta suoraan
käyttökelpoiseksi strategiaksi: mitä MVP tarkalleen tekee, miten se
asemoidaan yhdellä lauseella, ja miksi juuri tämä voittaa. Tämä on
sillanrakennusskilli ratkaisuideoinnin (moniin vaihtoehtoihin) ja PRD:n
kirjoittamisen (yhteen valittuun suuntaan) välissä.

## Perustuu

- RICE-priorisointimalli (Reach, Impact, Confidence, Effort) — yleisesti
  tunnettu tuotepriorisointikehys, ei omistajan oma.
- [redacted]n "AI-first SaaS Product" -työpajan menetelmä, sovellettu
  omistajan (Tommi Järvinen) toimesta [redacted]-caseen — ks.
  `../../references/[redacted]-workshop-source.md` ja worked example
  `../../cases/[redacted]-decision-coach-mvp.md` kohdat 6–7. **Huom:** sovellettu
  toistaiseksi vain kerran — ei laajasti validoitu.

## Rakenne (luonnos — täydennettävä)

1. **Pisteytä jokainen ratkaisusuunta neljällä kriteerillä (1–5):**
   - **Reach** — kuinka montaa käyttäjää tämä koskettaisi.
   - **Impact** — kuinka merkittävä vaikutus sillä on käyttäjälle kun se
     koskettaa.
   - **Confidence** — kuinka varma olet että arviosi Reach/Impact/Effort
     pitävät paikkansa (korkea = paljon evidenssiä, matala = arvaus).
   - **Effort (käänteinen: 5 = helpoin/matalin effort, 1 = vaikein/korkein
     effort)** — huomaa käänteisyys: tässä mallissa korkea effort-piste
     tarkoittaa MATALAA rakennuskustannusta, jotta kaikki neljä kriteeriä
     summautuvat samaan suuntaan (korkeampi = parempi MVP-ehdokas).
2. **Laske RICE-kokonaispisteet** (max 20 per neljä kriteeriä, tai
   skaalaa tarpeen mukaan) jokaiselle suunnalle ja järjestä paremmuus-
   järjestykseen.
3. **Perustele pisteet lyhyesti jokaiselle kriteerille** — älä jätä
   pisteitä ilman selitystä. Erityisesti Effort-arvio kannattaa sitoa
   konkreettisesti olemassa olevaan tekniseen pinoon/dataan/työkaluihin
   (mikä on jo olemassa vs. mikä pitää rakentaa tyhjästä).
4. **Valitse MVP korkeimmalla RICE-pistemäärällä**, ELLEI jokin
   erityinen strateginen syy puolla toista (esim. korkeamman Effortin
   suunta on ainoa joka todistaa aidon differentiaattorin, ei vain
   table-stake-arvoa). Jos poikkeat korkeimmasta pistemäärästä,
   perustele eksplisiittisesti miksi.
5. **Kirjoita MVP-määritelmä (2-3 lausetta).** Yhdistä valittu AI wedge
   (differentiaattoritarve) ja olennaiset table-stake-tarpeet yhdeksi
   ytimekkääksi kuvaukseksi siitä mitä MVP tekee ja kenelle.
6. **Piirrä MVP-flow tiiviisti** (5-8 vaihetta): käyttäjän syöte → AI:n
   synteesi/pisteytys → päätösmoottori/logiikka → AI:n output(it) →
   seuraavan askeleen suunnitelma → (valinnainen) viestintä-/kommunikointi-
   tuki → (valinnainen) polku syvempiin työkaluihin.
7. **Kirjoita yhden lauseen positiointilause.** Muoto: "[Tuote] antaa
   [kohdeasiakkaalle] [ydinhyödyn] [erottuvalla mekanismilla]." Testaa:
   voisiko tämä lause kuvata mitä tahansa kilpailijaa? Jos kyllä, se ei
   ole vielä tarpeeksi spesifi.
8. **Kirjoita 3 "miksi voitamme" -väittämää.** Jokainen väittämä sitoo
   yhden vahvuuden (differentiaattoritarve, olemassa oleva data/työkalu,
   ainutlaatuinen lähestymistapa) konkreettiseen kilpailuetuun — ei
   yleisiä väitteitä ("olemme parempia") vaan perusteltuja syitä.
9. Vie MVP-määritelmä, -flow, positiointilause ja "miksi voitamme"
   `../ai-buildable-prd-writing/SKILL.md`-skilliin PRD:n pohjaksi.

## Mitä tämä skilli EI tee

- Ei tee lopullista MVP-valintaa puolestasi täysin mekaanisesti — RICE-
  pisteet ovat päätöksenteon tuki, ei automaattinen sääntö; strateginen
  poikkeama korkeimmasta pistemäärästä on sallittu jos perusteltu.
- Ei arvioi taloudellista kannattavuutta tai yksikkötaloutta — vain
  suhteellista priorisointia ratkaisuvaihtoehtojen välillä. Ks.
  `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`
  syvempään taloudelliseen mallinnukseen kun MVP on jo valittu.
- Ei korvaa `../../../opportunity-recognition/skills/opportunity-evaluation-
  and-judgment/SKILL.md`-skilliä — tämä on kapeampi, nopeampi valinta
  jo tunnistettujen 2-3 ratkaisusuunnan välillä, ei koko mahdollisuuden
  arviointi tyhjästä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on sovellettu toistaiseksi yhteen caseen ([redacted]). Kun sovellat
sitä useampaan eri liiketoimintaan, täydennä:

- omia nyrkkisääntöjä siitä milloin kannattaa poiketa korkeimmasta
  RICE-pistemäärästä
- konkreettisia esimerkkejä positiointilauseista ja "miksi voitamme"
  -väittämistä eri caseista `../../cases/`-kansioon

Kun tämä osio on täytetty useammalla caseella, nosta
`skills_index.json`:n `maturity`-kenttä arvoon `validated`
(ks. `../../../../meta/maturity_levels.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa:
  `../ai-differentiator-solution-ideation/SKILL.md` — tuottaa kolme
  vaihtoehtoa joita tässä pisteytetään.
- Seuraava skilli samassa pakissa: `../ai-buildable-prd-writing/SKILL.md`
  — kirjoittaa PRD:n valitusta MVP:stä.
- Liittyvä skilli samassa pakissa, jos valittu MVP on keskusteleva/
  agenttinen tuote: `../ai-native-conversational-os-design/SKILL.md`.
- Worked example: `../../cases/[redacted]-decision-coach-mvp.md` kohdat 6–7.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/[redacted]-workshop-source.md` — lähdetiedot
- `../../cases/[redacted]-decision-coach-mvp.md` — worked example
- `../../CLAUDE.md` — pakin jaetut suojaukset
