---
name: ai-buildable-prd-writing
description: "Kirjoittaa PRD:n (Product Requirements Document) AI-rakennusagentille annettavana työmääräyksenä — ongelma, visio, core-ominaisuudet, rajaukset ja onnistumiskriteerit — sekä tukidokumentit ja tuotantosuunnitelman."
---

# AI-Buildable PRD Writing

*Tila: `validated`, `source_layer: owner` — ks. `../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Kirjoittaa PRD (Product Requirements Document), joka toimii selkeänä
työmääräyksenä AI-rakennusagentille (esim. Lovable, Bolt, v0) — samalla
tavoin kuin urakoitsija rakentaa piirustuksista. Ydinperiaate: rakentaminen
on nykyään nopeaa, mikä tarkoittaa että väärään suuntaan rakentaminen on
myös nopeaa. Suunnittelu on se, mikä pitää nopeuden osoitettuna oikeaan
suuntaan. Hyvä PRD tekee päätöksiä; huono PRD on toivelista, joka jättää
tärkeät valinnat AI:n arvattavaksi.

## Perustuu

- Omistajan AI-native Business Design -työpaja
  (omistajan oma työpaja), pidetty 1.–2.6.2026, Day 1 —
  Session 2 "Planning in the AI Era", vaiheet 4–6 (PRD:n rakenne,
  tukidokumentit, tuotantosuunnitelma, handoff rakennusagentille).
- Työpajan pääperiaate: **Spec → Plan → Implement → Test** -työnkulku;
  PRD kertoo *mitä* ja *miksi*, ei *miten*.

## Rakenne

1. **Kokoa syötteet.** Visio + ICP/JTBD/Need Themes/NMB-pisteytys/AI wedge
   (`../customer-vision-to-jtbd/SKILL.md`-skillistä), mahdollinen deep
   research -tausta, ja jos ratkaisusuuntia oli useampi vaihtoehto: valittu
   MVP-suunta perusteluineen (`../rice-scoring-and-mvp-synthesis/SKILL.md`
   -skillin RICE-valinta ja MVP-synteesi). Jos ratkaisusuunta oli alusta
   asti selvä eikä ideointi-/RICE-vaihetta käytetty, riittää pelkkä
   `customer-vision-to-jtbd`-syöte.
2. **Kirjoita PRD viidellä pakollisella osiolla**
   (`../../references/prompt-library.md` promptti 7):
   - **Ongelma & asiakas** — kenelle tämä on, ja mitä kipua se ratkaisee.
   - **Tuotevisio** — kuvaa kokemus asiakkaan omin sanoin.
   - **Core-ominaisuudet** — lista vain niistä ominaisuuksista, joita
     ensimmäinen versio tarvitsee. Kuvaa jokainen käyttäjän saavuttamana
     lopputuloksena ("käyttäjä voi…"), ei teknisenä toteutuksena.
   - **Rajaukset / Out of scope** — mitä TIETOISESTI ei rakenneta tässä
     versiossa. Yhtä tärkeä osio kuin ominaisuuslista.
   - **Onnistumiskriteerit** — miten tiedämme, että prototyyppi toimii.
3. **Sovella MVP-kuria.** Karsi laajuutta rajusti: yksi asiakas, yksi
   ydin-job, vähiten ominaisuuksia jotka todistavat idean. MVP-spec on
   sama PRD, laajuus armottomasti karsittuna.
4. **Testaa PRD:n laatu.** Tekeekö se päätöksiä — onko se spesifinen
   asiakkaasta, armoton rajauksesta, eksplisiittinen siitä mitä jätetään
   pois? Vai onko se toivelista, joka jättää tärkeät valinnat AI:n
   arvattavaksi? Jälkimmäinen on merkki siitä, että suunnittelu ei ole
   valmis.
5. **Kirjoita tarvittavat tukidokumentit:**
   - **Brand style & personality** — sävy, ääni, millaiselta tuotteen
     pitäisi tuntua.
   - **Design system** — värit, fontit, käyttöliittymän peruskomponentit,
     jotta lopputulos on yhtenäinen.
   - **Skills plan** — mitä valmiita, uudelleenkäytettäviä kykyjä
     (skillejä) annetaan rakennusagentille/agenteille sen sijaan että
     sama työnkulku selitetään joka kerta uudelleen.
6. **Rakenna tuotantosuunnitelma.** Päätä missä järjestyksessä
   rakennetaan. Tyypillinen kaava: scaffolding ensin (kirjautuminen,
   tietokanta, tyhjä runko) ja sitten ominaisuus kerrallaan sen päälle.
7. **Vie PRD ja tukidokumentit rakennusagentille**
   (ks. `../ai-native-tool-stack-selection/SKILL.md` kenelle). Vahvista
   tuotantosuunnitelma ja pääasialliset rakenteelliset valinnat agentin
   kanssa ennen varsinaista rakentamista.

## Mitä tämä skilli EI tee

- Ei sisällä teknisiä arkkitehtuuripäätöksiä tai tarkkoja teknologia-
  valintoja — PRD kertoo MITÄ ja MIKSI, ei MITEN; tekninen toteutus jää
  build-vaiheeseen ja rakennusagentille.
- Ei takaa prototyypin onnistumista — hyvä PRD vähentää väärään suuntaan
  rakentamisen riskiä, ei poista sitä.
- Ei korvaa `business-case-and-analysis`-pakin `business-case-builder`-
  tai `requirements-and-scope-framing`-skillejä isommassa, rahoitusta tai
  organisaation muodollista hyväksyntää vaativassa liiketoimintaperustelussa
  — tämä on kevyt, nopea spec yhden prototyypin rakentamiseen viikon
  aikataululla.

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../customer-vision-to-jtbd/SKILL.md`,
  mahdollisesti `../ai-differentiator-solution-ideation/SKILL.md` ja
  `../rice-scoring-and-mvp-synthesis/SKILL.md` (jos useampi ratkaisusuunta
  puntaroitiin ennen tätä).
- Liittyvä skilli samassa pakissa: `../ai-native-tool-stack-selection/SKILL.md`
  — kenelle PRD annetaan rakennettavaksi. Jos MVP on keskusteleva/agenttinen
  tuote, ks. myös `../ai-native-conversational-os-design/SKILL.md` PRD:n
  "Core-ominaisuudet"-osion syventämiseksi.
- Liittyvä skilli toisessa pakissa:
  `../../../../opportunity-recognition/skills/opportunity-brief-writing/SKILL.md`,
  `../../../../business-case-and-analysis/skills/requirements-and-scope-framing/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/prompt-library.md` — promptti 7 + PRD-tarkistuslista
- `../../references/workshop-source.md` — lähdetiedot
- `../../CLAUDE.md` — pakin jaetut suojaukset
