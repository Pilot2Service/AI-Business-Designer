# Changelog

## 0.6.0 — 2026-08-05

Uusi ydinpakki `business-design-frameworks/` — tarkoituksella avoin ja kasvava
kokoelma liiketoiminnan jäsentämis- ja mallinnustapoja (kerrokset, arvoketjut,
kategoriamallinnus, ja lisää myöhemmin käyttäjän toimesta):

- `layer-based-business-structuring` — OSI-mallin analoginen kerrosjäsennys,
  ankkuroitu Hagel & Singer (1999) "Unbundling the Corporation" ja
  Baldwin & Clark modulaarisuusteoriaan
- `value-chain-mapping` — Porterin (1985) arvoketjumalli
- `category-definition-and-modeling` — category design (Play Bigger,
  Ramadan et al. 2016) ja Blue Ocean Strategy (Kim & Mauborgne 2005)
- Kaikki `maturity: scaffold`, `source_layer: research` — ei vielä omaa
  validoitua kokemusta, tarkoituksella rakennettu täydennettäväksi
- Pakki on suunniteltu kasvamaan: README sisältää ohjeen uuden
  jäsentämistavan lisäämiseksi
- Yhteensä nyt 44 skilliä, 6 ydinpakkia + 1 täytetty erikoistumispakki

## 0.5.0 — 2026-08-04

Käyttäjän toimittaman tutkimusraportin ("AI Business Designer tekoälyn
aikakaudella") pohjalta lisätty `ai-strategy-and-governance`-pakkiin:

- `ai-opportunity-portfolio` rikastettu konkreettisella AI-soveltuvuuden
  triagilla (ennustus/luokittelu/generointi + datan saatavuus), data
  flywheel -tarkistuksella ja automaatio-vs-agenttisuus-erottelulla
  (edelleen `maturity: scaffold`, `source_layer: research`)
- Uusi skilli `ai-native-business-model-canvas` (`maturity: scaffold`) —
  laajennettu, tekoälyspesifi Business Model Canvas (arvolupaus,
  avainresurssit, kustannusrakenne, ekosysteemi)
- Muu osa raportista (business case -rakennus, taitomatriisi) arvioitiin
  toistavan jo olemassa olevaa sisältöä (`ai-opportunity-portfolio`,
  `build-vs-buy-vs-partner-ai`, `ai-capability-roadmap`,
  `responsible-ai-and-governance-check`, `meta/competency_map.md`) — ei lisätty
  uudelleen
- Yhteensä nyt 41 skilliä

## 0.4.0 — 2026-08-04

Laajennus ydinpakkiin `opportunity-recognition/` omistajan (Tommi Järvinen)
[redacted]-palvelun Opportunity Value Assessment -tuotteesta (sales page,
input wizard, raporttipohja) ja sitä tukevasta S1-taustatutkimuksesta
(Mullins Seven Domains, Timmons, POEM, NABC, Opportunity Canvas):

- 3 uutta skilliä (`maturity: validated`, `source_layer: owner`):
  `opportunity-intake-elicitation`, `opportunity-value-assessment`,
  `opportunity-brief-writing` — pakin ensimmäiset ei-scaffold-skillit,
  rinnakkain 5 alkuperäisen scaffold-skillin kanssa
- `references/[redacted]-frameworks-review.md`, `intake-questions.md`,
  `opportunity-brief-template.md`
- Ristiinlinkitys: `opportunity-evaluation-and-judgment` (scaffold) →
  `opportunity-value-assessment` (validated); `research-opportunity-recognition`
  (research-commercialisation) ↔ `opportunity-value-assessment`
- `CLAUDE.md` ja `README.md` päivitetty kuvaamaan sekoitettua kypsyystasoa
  saman pakin sisällä
- Yhteensä nyt 40 skilliä

## 0.3.0 — 2026-08-04

Ensimmäinen täysin täytetty erikoistumispakki — `specialisation-packs/research-commercialisation/`,
konvertoitu omistajan (Tommi Järvinen) julkaisemasta *[redacted] Innovator's Guide to
Commercialisation* -käsikirjasta ja AFCA-itsearviointityökalusta:

- 12 uutta skilliä (`maturity: validated`, `source_layer: owner`) — ensimmäiset
  tässä repossa, jotka eivät ole `scaffold`-tasolla
- `references/afca-framework.md`, `case-studies.md`, `terminology.md`, `sources.md`
- Pakkikohtainen `CLAUDE.md` ja täysi `README.md` (placeholder poistettu)
- `scripts/generate_index.py` ja `scripts/validate.py` laajennettu indeksoimaan ja
  validoimaan myös `specialisation-packs/*/skills/`-sisältöä (ei vain top-level
  plugin.json-pakkeja)
- `marketplace.json`: `specialisation-research-commercialisation`-kuvaus päivitetty,
  scaffold-merkintä poistettu
- Yhteensä nyt 37 skilliä, 5 ydinpakkia + 1 täytetty erikoistumispakki

## 0.2.0 — 2026-08-04

Rakennekorjaus `[redacted]/claude-for-legal-finland`-repon (tuotantokäytössä oleva
suomalainen Claude-plugin-markkinapaikka) rakenneanalyysin pohjalta:

- SKILL.md-frontmatter siivottu minimiin (`name` + `description`) — kypsyys/lähdekerros
  siirretty yksinomaan `skills_index.json`:iin
- Pakkikansioista poistettu numeroprefiksit (`01-strategic-thinking` → `strategic-thinking`)
- Lisätty pakkitason `CLAUDE.md`-suojauskerros jokaiseen 5 ydinpakkiin
- Lisätty jokaiseen skilliin `Mitä tämä skilli EI tee` ja `Jatka tästä` -osiot
- Lisätty `scripts/generate_index.py` ja `scripts/validate.py`
- `marketplace.json`: lisätty `$schema` ja `displayName`-kentät

## 0.1.0 — 2026-08-04

- Ensimmäinen scaffold: 5 ydinpakkia, 25 skilliä (kaikki `maturity: scaffold`)
- 3 erikoistumispakin placeholder
- `skills_index.json` koneluettava indeksi
- `AGENT_GUIDE.md`, meta-hallintodokumentit Charlotte-semantic-layer-templaten
  arkkitehtuuriperiaatteita soveltaen
- 2 aloitusplaybookia
