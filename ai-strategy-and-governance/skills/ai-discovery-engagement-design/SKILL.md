---
name: ai-discovery-engagement-design
description: "Suunnittelee ja tuotteistaa AI-mahdollisuuksien tunnistamisen (discovery-vaiheen) maksulliseksi konsultointitoimeksiannoksi — 4-vaiheinen engagement-rakenne, kiinteähintaiset palvelutuotteet ja standardoitu luovutettava aineisto (Portfolio, Business Case, ATOM/Readiness Scorecard, Roadmap)."
---

# AI Discovery Engagement Design

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Auttaa AI Business Designeria (sisäisenä toimijana tai ulkoisena
konsulttina) pakkaamaan tämän pakin muut skillit (tehtäväpilkkominen,
opportunity-portfolio, feasibility, roadmap) yhdeksi selkeärajaiseksi,
myytäväksi tai sisäisesti perustelluksi **discovery-toimeksiannoksi**:
mitkä vaiheet, kuinka pitkään, mitä luovutetaan, ja millä tuotemuodolla.
Tämä on tämän pakin "meta-skilli" — se ei tuota itse analyysiä vaan
JÄSENTÄÄ prosessin, jonka aikana muut pakin skillit ajetaan.

## Ankkurointi tutkimukseen

- Tutkimuskooste "Tekoälymahdollisuuksien ja -kapasiteetin
  tunnistamismenetelmät, viitekehykset ja osaamiset liiketoiminnassa"
  (2026) — asiantuntijapalvelutalojen myynti- ja palvelumallit,
  tuotteistetut palvelut, luovutettava aineisto. Malli on yleistetty
  suurten konsulttitalojen julkisesta AI-discovery-käytännöstä, ei
  minkään yksittäisen talon tarkka kopio.

## Rakenne (luonnos — täydennettävä)

1. **Valitse tuotemuoto laajuuden mukaan.** Kaksi tyypillistä
   kiinteähintaista palvelutuotetta:
   - **AI Opportunity Sprint / Mapping (2–4 viikkoa)** — kevyempi:
     2–3 työpajaa, prosessien läpivalaisu, priorisoitu AI-tiekartta.
     Sopii kun asiakkaalla ei vielä ole selkeää käsitystä siitä missä
     AI-mahdollisuudet ovat.
   - **AI Maturity & Opportunity Audit (4–6 viikkoa)** — syvempi: yhdistää
     mahdollisuuksien tunnistamisen tekniseen data-/infrastruktuuri-
     valmiuteen ja hallintamalliin (AI Governance). Sopii kun asiakas
     tarvitsee myös arvion omasta valmiudestaan, ei vain
     mahdollisuuslistaa.
   Älä myy/skaalaa kumpaakaan tuotemuotoa suurempana kuin asiakkaan
   organisaation koko ja päätöksentekonopeus kestää — ylimitoitettu
   discovery-vaihe on itsessään riski (analysis paralysis).
2. **Rakenna toimeksianto neljällä vaiheella:**
   - **Vaihe 1 — Alustus & intentio.** Executive-haastattelut,
     tavoitetason ja AI-ambition asettaminen. Tuotos: yhteinen
     ymmärrys siitä mitä "onnistuminen" tarkoittaa tälle toimeksiannolle.
   - **Vaihe 2 — Discovery workshops & tehtäväanalyysi.** Prosessi- ja
     data-auditoinnit, arvoketjun kartoitus sidosryhmien kanssa. Käytä
     tässä vaiheessa
     `../task-level-decomposition-and-automation-fit/SKILL.md`-skilliä
     raakalistan tuottamiseen ja
     `../../../business-design-frameworks/skills/value-chain-mapping/SKILL.md`
     -skilliä prosessitason kartoitukseen.
   - **Vaihe 3 — Pisteytys, laskenta & portfolio.** Käyttötapausten
     identifiointi, 5D-pisteytys ja business case -mallinnus. Käytä
     `../ai-opportunity-portfolio/SKILL.md`-skilliä ja tarvittaessa
     `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
     -skilliä.
   - **Vaihe 4 — Tekoälytiekartta & luovutus.** Priorisoitu AI Backlog,
     investointilaskelmat, arkkitehtuurilinjaukset. Käytä
     `../ai-capability-roadmap/SKILL.md`-skilliä.
3. **Määritä luovutettava aineisto (deliverables) etukäteen, ennen
   toimeksiannon aloitusta** — asiakas tietää tarkalleen mitä saa:
   - **AI Opportunity Portfolio / Backlog** — luettelo luokitelluista ja
     pisteytetyistä kohteista (ks. `../ai-opportunity-portfolio/SKILL.md`).
   - **Detailed Business Cases** — ROI- ja säästölaskelmat, huomioiden
     kokonaiskustannus (TCO, *Total Cost of Ownership* — sisältää
     mallien inferenssikustannukset ja ylläpidon, ei vain
     rakennuskustannusta).
   - **AI Target Operating Model (ATOM) / Readiness Scorecard** — ks.
     `../ai-capability-roadmap/SKILL.md` kohta "ATOM/Readiness
     Scorecard" — kuvaus ihmisen ja tekoälyn työnjaosta sekä
     organisaation valmiustasosta.
   - **Strategic AI Roadmap** — ajoitettu suunnitelma kolmella
     horisontilla (ks. `../ai-capability-roadmap/SKILL.md`).
4. **Sovita toimeksiannon syvyys asiakkaan päätöksentekokypsyyteen.**
   Jos asiakkaalla ei ole vielä valtuutettua päätöksentekijää tuloksille,
   lyhennä Sprint-muotoon äläkä myy täyttä Auditia — täysi Audit ilman
   selkeää päätöksentekijää tuottaa hyvän raportin joka jää hyllylle.
5. **Aseta selkeä rajaus (out of scope) jo myyntivaiheessa.** Discovery-
   toimeksianto EI sisällä toteutusta, PoC-rakentamista tai teknistä
   arkkitehtuurisuunnittelua — nämä ovat erillisiä, discoveryn JÄLKEISIÄ
   toimeksiantoja. Sekoittaminen johtaa scope creepiin ja epäselvään
   hinnoitteluun.
6. **Kirjaa toimeksiannon onnistumiskriteerit ennen aloitusta:**
   toimitetaanko priorisoitu backlog, hyväksytäänkö se johtoryhmässä, ja
   syntyykö sen pohjalta vähintään yksi käynnistetty investointipäätös.
   Discovery-toimeksianto joka ei johda päätökseen on epäonnistunut
   riippumatta analyysin laadusta.

## Mitä tämä skilli EI tee

- Ei tee itse analyysiä — organisoi PROSESSIN, jonka aikana pakin muut
  skillit (task-level-decomposition, ai-opportunity-portfolio,
  ai-use-case-feasibility-and-poc-scoping, ai-capability-roadmap)
  tuottavat varsinaisen sisällön.
- Ei sisällä hinnoittelusuosituksia tai kiinteitä euromääriä — ne
  riippuvat markkinasta, toimialasta ja omasta kustannuspohjasta;
  merkitse ne aina `[oletus — tarkista]` jos niitä joudutaan arvioimaan.
- Ei korvaa `../../../opportunity-recognition/skills/opportunity-brief-writing/SKILL.md`
  -skilliä yksittäisen mahdollisuuden dokumentoinnissa — tämä skilli
  on ylemmän tason: se jäsentää koko toimeksiannon, ei yhtä
  mahdollisuutta.
- Ei sovi jokaiseen tilanteeseen — jos AI-mahdollisuudet on jo
  tunnistettu ja tarvitaan vain yksi analyysi (ei koko monivaiheista
  toimeksiantoa), käytä suoraan yksittäisiä skillejä ilman tätä
  kehystä ympärillä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä
sisällä omaa kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä
tähän:

- omat hinnoittelumallit ja -periaatteet (kiinteähintainen vs.
  aikaveloitus, mitä sisältyy mihinkin tuotemuotoon)
- konkreettiset myyntimateriaalit/tarjouspohjat (`../../references/`
  -kansioon)
- omia kokemuksia siitä, milloin Sprint riittää ja milloin tarvitaan
  täysi Audit
- referenssitapaukset omista toimeksiannoista

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä
`skills_index.json`:n `maturity`-kenttä arvoon `draft`, `validated` tai
`canonical` (ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei
lisätä uusia kenttiä** — `name` ja `description` ovat ainoat sallitut
(ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Käyttää alaskilleinä (vaihejärjestyksessä):
  `../task-level-decomposition-and-automation-fit/SKILL.md` →
  `../ai-opportunity-portfolio/SKILL.md` →
  `../ai-use-case-feasibility-and-poc-scoping/SKILL.md` →
  `../ai-capability-roadmap/SKILL.md`
- Liittyvä skilli toisessa pakissa (business case -syvennys):
  `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
- Liittyvä skilli toisessa pakissa (jos toimeksianto koskee julkista
  sektoria): ks. `julkiset-hankinnat`-plugin tarjouspyyntöjen ja
  hankintamenettelyjen osalta.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
