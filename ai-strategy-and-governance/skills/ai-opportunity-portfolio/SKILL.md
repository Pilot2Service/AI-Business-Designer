---
name: ai-opportunity-portfolio
description: "Tunnistaa, pisteyttää (5-ulotteinen malli: Business Impact, Technical Feasibility, Data Readiness, Strategic Alignment, Speed to Value/Risk) ja priorisoi AI-käyttötapaukset 2x2-matriisilla (Quick Wins / Strategic Bets / Deprioritize / Hard-Low Value) — sekä luokittelee inkrementaaliset ja transformatiiviset mahdollisuudet erikseen."
---

# AI Opportunity Portfolio

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Muuttaa raaka lista AI-käyttötapausehdokkaita (tyypillisesti 20–100
kohdetta) objektiivisesti pisteytetyksi, priorisoiduksi portfolioksi,
josta valitaan jatkoon 3–5 korkeimman arvon ja matalimman riskin
kohdetta. Skilli erottelee tarkoituksella kaksi eri mahdollisuustyyppiä —
**inkrementaalinen tehostaminen** (nykyisen prosessin nopeuttaminen/
halventaminen) ja **transformatiivinen innovaatio** (uusi liiketoiminta,
jota ei voinut tehdä ennen nykyisiä AI-kyvykkyyksiä) — koska niitä
arvioidaan osin eri kriteerein.

## Ankkurointi tutkimukseen

- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity-tutkimus: Senior AI Business Designer (Solita/HP)
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — AI-mahdollisuuksien tunnistaminen strategisella
  tasolla (alkuperäinen ongelmatyyppi/data/flywheel/agenttisuus-triagi,
  nyt sisällytetty kohtaan 4 alla)
- Käyttäjän toimittama tutkimusraportti "Tekoälymahdollisuuksien ja
  -kapasiteetin tunnistamismenetelmät, viitekehykset ja osaamiset
  liiketoiminnassa" (2026) — 5-ulotteinen pisteytysmalli ([redacted], Alice
  Labs, McKinsey -synteesi), 2x2-priorisointimatriisi, Value-Play-
  taksonomia transformatiivisille mahdollisuuksille, BCG:n
  Deploy-Reshape-Invent-taksonomia

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. **Kokoa raakalista ehdokkaista.** Lähde liikkeelle olemassa olevista
   kitkakohdista ja arvoketjun pullonkauloista — ei teknologiasta. Kaksi
   täydentävää tapaa koota raakalista:
   - **Bottom-up** (jos prosessi on jo kuvattu tarkasti): käytä
     `../task-level-decomposition-and-automation-fit/SKILL.md`-skilliä —
     sen Automate/Augment-luokitellut tehtävät ryhmitellään tässä
     suuremmiksi mahdollisuuksiksi.
   - **Top-down** (nopea ensimmäinen kartoitus ennen tarkkaa prosessi-
     kuvausta): käytä `../ai-capability-pattern-matching/SKILL.md`-skilliä
     — se esittää valmiin kyvykkyyspatternikirjaston diagnostiset
     kysymykset asiakkaalle ja tuottaa validoidun raakalistan.
   Jos kumpaakaan ei ole käytetty, kerää lista suoraan sidosryhmiltä.
2. **Jaa jokainen ehdokas kahteen kaistaan ennen pisteytystä:**
   - **Inkrementaalinen tehostaminen** — nykyinen prosessi tehdään
     nopeammin/halvemmalla. Kustannussäästö- ja nopeusvetoinen (*bottom-
     line impact*).
   - **Transformatiivinen innovaatio** — uusi liiketoiminta, tuote tai
     tulovirta, joka ei ollut mahdollinen ennen nykyisiä AI-kyvykkyyksiä.
     Kasvuvetoinen (*top-line impact*). Tarkista jokainen transformatiivi-
     seksi väitetty ehdokas Value-Play-taksonomialla (kohta 3) — jos se ei
     osu mihinkään kolmesta arkkitehtuurista, se on todennäköisesti
     itse asiassa inkrementaalinen tehostus naamioituna isoksi ideaksi.
3. **Transformatiivisille ehdokkaille: tarkista Value-Play-taksonomiaa
   vasten.** Kolme tunnettua arkkitehtuuria uuden AI-arvon luonnille:
   - **Rajattomasti skaalautuva asiantuntijuus** (*Zero-Marginal-Cost
     Expertise*) — monimutkaisen erikoisosaamisen (juridinen, tekninen,
     lääketieteellinen) paketointi reaaliaikaiseksi, skaalautuvaksi
     palveluksi.
   - **Reaaliaikainen hyperpersonointi** (*Hyper-Personalization at
     Scale*) — tuote/palvelu dynamisoituu jokaiselle käyttäjälle
     yksilöllisesti (esim. räätälöidyt opintopolut, rahoitustuotteet).
   - **Tulospohjaiset liiketoimintamallit** (*Outcome-Based / Agentic
     Business*) — siirtymä käyttöoikeus-/paikkapohjaisesta (seat-based)
     hinnoittelusta tulospohjaiseen (esim. veloitus vain ratkaistusta
     tiketistä tai toteutuneesta kaupasta).
   Jos ehdokas ei osu mihinkään näistä eikä ole selkeästi näiden
   yhdistelmä, harkitse uudelleen kuuluuko se transformatiiviseen kaistaan.
4. **Pisteytä jokainen ehdokas viidellä ulottuvuudella (1–5 per
   ulottuvuus, max 25 yhteensä):**
   - **Business Impact** — mitattavissa oleva euro- tai aika-arvo (ROI,
     säästetyt työtunnit, uusi liikevaihto, churn-vaikutus).
   - **Technical Feasibility & AI Fit** — onko ongelma luonteeltaan
     probabilistinen vai deterministinen? Sopiiko nykyinen LLM/AI-
     teknologia tehtävään ilman kohtuutonta hallusinointiriskiä? (Käytä
     tässä `../task-level-decomposition-and-automation-fit/SKILL.md`
     -skillin SML-arviota jos saatavilla — ongelmatyyppi ennustus/
     luokittelu/generointi kuuluu myös tähän ulottuvuuteen.)
   - **Data Readiness** — onko tarvittava data saatavilla, rakenteisessa
     muodossa, laadukasta ja rajapinnoitettavissa? Arvioi myös
     **data flywheel -potentiaali**: tuottaako ratkaisu käytössä uniikkia
     dataa joka parantaa mallia ajan myötä ja vahvistaa kilpailuetua, vai
     onko kyse kertaluonteisesta datasta ilman itseään vahvistavaa
     silmukkaa?
   - **Strategic Alignment** — tukeeko kohde organisaation 1–3 vuoden
     päästrategiaa, vai on se irrallinen kokeilu?
   - **Speed to Value & Governance/Risk** — toteutusaika sekä
     sääntelyllinen riskiprofiili (esim. EU AI Act -luokittelu: kielletty,
     korkea riski, matala riski — ks.
     `../responsible-ai-and-governance-check/SKILL.md`). Sisällytä tähän
     myös **agenttisuuden aste**: riittääkö perinteinen sääntöpohjainen
     automaatio vai vaatiiko mahdollisuus agenttista, itsenäistä
     päätöksentekoa ennalta-arvaamattomissa tilanteissa — agenttinen
     ratkaisu on kalliimpi rakentaa ja hallita, mikä hidastaa Speed to
     Value -pistettä ja pitäisi näkyä pisteessä.
5. **Sijoita jokainen ehdokas 2x2-priorisointimatriisiin** (pystyakseli:
   Business Impact, vaaka-akseli: Technical Feasibility — käytä kohdan 4
   pisteitä):
   - **Quick Wins** (korkea vaikutus, korkea toteutettavuus) — matalat
     kustannukset, nopea toteutus. Aktiiviset pilotointiehdokkaat.
   - **Strategic Bets** (korkea vaikutus, matala toteutettavuus) — usein
     transformatiivisia, vaativat merkittäviä data-/arkkitehtuuri-
     investointeja ennen kuin ne kannattaa aloittaa.
   - **Hard / Low Value** (matala vaikutus, matala toteutettavuus) —
     korkea tekninen kynnys, pieni ROI. Vältä.
   - **Deprioritize** (matala vaikutus, korkea toteutettavuus) — helppo
     tehdä mutta ei kannata; matala arvo ei oikeuta resursseja edes
     kun toteutus olisi helppoa.
6. **Luokittele valitut Quick Wins- ja Strategic Bets -kohteet lisäksi
   BCG:n Deploy-Reshape-Invent-taksonomialla** — TÄMÄ on eri kysymys
   kuin kohdan 5 matriisi: matriisi vastaa "kannattaako tämä ja onko se
   helppo", Deploy-Reshape-Invent vastaa "millaista muutosta tämä
   organisaatiolta vaatii":
   - **Deploy** — valmiiden tekoälytyökalujen (esim. Copilotit)
     käyttöönotto pistemäisissä tehtävissä. Ei vaadi prosessin
     uudelleensuunnittelua.
   - **Reshape** — ydintoimintojen ja end-to-end-prosessien
     uudelleensuunnittelu tekoälyn ympärille. Vaatii prosessimuutosta.
   - **Invent** — täysin uusien liiketoimintamallien, tuotteiden ja
     tulovirtojen luominen. Vaatii uuden liiketoiminnan rakentamista.
   **Älä sekoita tätä `../ai-capability-roadmap/SKILL.md`-skillin
   Horisontti 1/2/3 -jaotteluun** — Deploy-Reshape-Invent kuvaa
   MUUTOKSEN LAATUA (kuinka syvälle organisaatiota se koskettaa), Horisontti
   1/2/3 kuvaa AIKATAULUA (milloin se tehdään). Sama Reshape-tason
   mahdollisuus voi sijoittua mihin tahansa horisonttiin riippuen
   resursseista ja riippuvuuksista.
7. **Tuota lopullinen tulos: priorisoitu AI Opportunity Portfolio /
   Backlog** — jokaiselle valitulle kohteelle: nimi, kaista
   (inkrementaalinen/transformatiivinen; jos transformatiivinen, mikä
   Value Play), 5D-pisteet ja kokonaispiste, 2x2-sijainti, Deploy/
   Reshape/Invent-luokka. Vie 3–5 korkeimman prioriteetin kohdetta
   `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
   -skilliin syvempää liiketoimintaperustelua varten.
8. Validoi tulos sidosryhmillä tai omalla kokemuspohjaisella
   tarkistuslistalla. Varmista erityisesti, että mahdollisuuksia ei
   arvioida erillisenä siilona vaan suhteessa organisaation olemassa
   oleviin strategisiin tavoitteisiin.

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä puolestasi — tuottaa jäsennellyn luonnoksen ihmisen
  päätöksenteon tueksi.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista — käyttää käyttäjän
  antamia lähtöarvoja tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).
- Ei arvioi teknistä toteutettavuutta syvällisesti — Technical Feasibility
  -ulottuvuus tässä on karkea 1–5-arvio, ei tekninen due diligence. Syvempään
  arvioon ks. `../ai-use-case-feasibility-and-poc-scoping/SKILL.md`.
- Ei tee tehtävätason pilkkomista itse — jos raakalistaa ei ole vielä
  koottu tehtävätasolta, käytä ensin
  `../task-level-decomposition-and-automation-fit/SKILL.md`.
- Ei korvaa `../ai-capability-roadmap/SKILL.md`-skilliä aikataulutuksessa
  — tuottaa priorisoidun listan, ei ajoitettua roadmapia.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt ja heuristiikat tässä tekniikassa — esim. mitkä
  ulottuvuudet ovat käytännössä painoarvoltaan tärkeimpiä eri
  toimialoilla
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  5D-pisteytystaulukko-template)
- referenssitapaukset / omat caset
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa (jos raakalistaa ei vielä ole):
  `../task-level-decomposition-and-automation-fit/SKILL.md` (bottom-up) tai
  `../ai-capability-pattern-matching/SKILL.md` (top-down)
- Samassa pakissa seuraavaksi (liiketoimintamallin suunnittelu): `../ai-native-business-model-canvas/SKILL.md` — Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla Business Model Canvasilla.
- Samassa pakissa seuraavaksi (tekninen validointi): `../ai-use-case-feasibility-and-poc-scoping/SKILL.md` — Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen.
- Samassa pakissa seuraavaksi (aikataulutus): `../ai-capability-roadmap/SKILL.md`
  — sijoittaa valitut kohteet Horisontti 1/2/3 -aikajanalle (eri kysymys
  kuin tämän skillin Deploy/Reshape/Invent-luokittelu, ks. kohta 6).
- Liittyvä skilli toisessa pakissa: `../../../opportunity-recognition/skills/opportunity-value-assessment/SKILL.md`
  — yleisempi, ei-AI-spesifi mahdollisuuksien arviointimalli.
- Jos koko prosessi tehdään maksullisena konsultointitoimeksiantona:
  `../ai-discovery-engagement-design/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
