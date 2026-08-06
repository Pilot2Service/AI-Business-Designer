---
name: rapid-prototype-and-vibe-coding-craft
description: "Rakentaa nopeasti toimivan, riittävän uskottavan prototyypin AI-mahdollisuuden todistamiseksi käyttäen AI-avusteista koodausta (\"vibe coding\") — työkaluvalinta tehtävätyypin mukaan, tiukka prompt/review/testaa/committaa-iteraatiosykli, oikea fideliteettitaso ja tunnetut riskit (hallusinoidut rajapinnat, auth-aukot). Käytä kun tarvitset nopean, todistevoimaisen prototyypin ennen kuin sitoudut isompaan rakennusprojektiin."
---

# Rapid Prototype & Vibe Coding Craft

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Rakentaa mahdollisimman nopeasti prototyypin, joka on **riittävän uskottava
todistamaan yhden tietyn hypoteesin** — ei enempää. Yleisin virhe AI-konsultin
protoilussa ei ole liian huono prototyyppi, vaan väärän tason prototyyppi:
joko liian ohut todistamaan mitään, tai tarpeettoman valmis (aikaa tuhlattu
viimeistelyyn, jota kukaan ei vielä ole pyytänyt). Tämä skilli auttaa
valitsemaan oikean fideliteettitason ja käyttämään AI-avusteista koodausta
("vibe coding") kurinalaisesti niin, että nopeus ei osta huomaamattomia
riskejä.

## Ankkurointi tutkimukseen

- Vibe coding -parhaat käytännöt 2026 (useamman lähteen synteesi, ks.
  Referenssit): työkaluvalinta tehtävätyypin mukaan, tiukka iteraatiosykli,
  PRD ennen promptausta, tunnetut riskit ja rajat sille mihin vibe codingia
  kannattaa käyttää.
- Prototyyppifideliteetti-tutkimus (matala vs. korkea fideliteetti): matalan
  fideliteetin prototyypit tunnistavat suuren osan rakenteellisista
  ongelmista murto-osalla korkean fideliteetin kustannuksesta — ks.
  Referenssit.

## Rakenne (luonnos — täydennettävä)

1. **Määritä TÄSMÄLLEEN yksi hypoteesi, jonka prototyypin pitää todistaa**
   ennen kuin avaat mitään työkalua. Esimerkki hyvästä hypoteesista: "AI
   pystyy poimimaan oikean toimittajan Y-tunnuksen ja summan 20 satunnaisesta
   ostolaskusta ilman ihmisen korjausta." Esimerkki huonosta (liian laajasta)
   hypoteesista: "AI voisi auttaa ostolaskuprosessissa." Jos et pysty
   kirjoittamaan hypoteesia yhteen lauseeseen, jota voi arvioida
   kyllä/ei-vastauksella, olet vielä liian aikaisessa vaiheessa protoiluun.
2. **Valitse fideliteettitaso hypoteesin, ei mukavuuden, mukaan:**
   - **Matala fideliteetti** (staattinen mockup, käsin rakennettu esimerkki,
     ei toimivaa koodia) — riittää kun kyse on rakenteellisesta kysymyksestä:
     ymmärtääkö käyttäjä työnkulun, tekeekö UI-järjestys järkeä, onko
     visio ylipäätään houkutteleva. Nopein ja halvin tapa löytää perustavat
     ongelmat ennen kuin mitään koodataan.
   - **Toimiva, kapea prototyyppi** (oikeasti toimiva, mutta vain yhdellä
     polulla, ilman virhekäsittelyä, ilman tuotantoinfraa) — tarvitaan kun
     hypoteesi on teknisluonteinen ("pystyykö AI tekemään X datallamme
     riittävällä tarkkuudella"). Tämä on vibe coding -työn ydinalue.
   - **Korkea fideliteetti** — vasta kun matalampi taso on jo validoinut
     idean ja seuraava kysymys koskee oikeaa käyttökokemusta tuotantomaisessa
     ympäristössä. Tämä ei yleensä ole konsultin ensimmäisen demon tehtävä.
3. **Valitse työkalu tehtävätyypin mukaan, älä käytä yhtä työkalua
   kaikkeen.** Karkea nyrkkisääntö: full-stack-sovelluksen luonnos →
   yleiskäyttöinen AI-koodausagentti; monimutkainen olemassa olevan koodin
   muokkaus/refaktorointi → agentti jolla on hyvä koko-koodikannan konteksti;
   nopea, ei-dataa-tallentava demo/mockup → kevyt no-code/low-code-työkalu.
   Yhdistä useampaa työkalua tarpeen mukaan sen sijaan että pakotat yhden
   työkalun jokaiseen tehtävään.
4. **Kirjoita lyhyt PRD (yksi sivu riittää) ennen promptausta**, vaikka
   prototyyppi olisi pieni: mitä syötettä käsitellään, mikä on odotettu
   tuotos, mitkä 2-3 tapausta pitää TODELLA toimia demoa varten. Tämä estää
   yleisimmän vibe coding -sudenkuopan: AI-agentti rakentaa jotain
   teknisesti toimivaa mutta väärää asiaa, koska tehtävä oli ali-
   spesifioitu.
5. **Pidä iteraatiosykli tiukkana ja lyhyenä:** prompttaa yksi rajattu muutos
   → tarkista tulos → testaa heti oikealla (tai oikeaa muistuttavalla)
   datalla → committaa tai kumoa. Älä anna virheiden kasaantua usean
   promptin ketjuun ennen tarkistusta — silloin on vaikea jäljittää mikä
   muutos rikkoi mitä.
6. **Sovella "tee viimeinen asia ensin" -periaatetta myös rakentamiseen:**
   rakenna ensin se osa, joka tuottaa demo-hetken "aha"-vaikutuksen
   (ks. `../demo-delivery-and-storytelling/SKILL.md` kohta 3), älä aloita
   infrastruktuurista tai reunatapauksista joita demo ei koskaan näytä.
7. **Tarkista tietoisesti ennen esittämistä tai oikean datan syöttämistä:**
   onko autentikointi/oikeustarkistus edes karkealla tasolla kunnossa, onko
   koodissa selviä hallusinoituja rajapintakutsuja, käsitteleekö prototyyppi
   oikeasti arkaluonteista dataa (jos kyllä, älä käytä oikeaa dataa ilman
   erillistä lupaa ja turvatoimia). Merkitse näkyvästi mitä EI ole
   tarkistettu, äläkä anna vaikutelmaa että "toimii demoni" tarkoittaa
   "on tuotantovalmis" (ks. pakin `../../CLAUDE.md`).
8. **Vie tuotos** joko suoraan `../demo-delivery-and-storytelling/SKILL.md`
   -skilliin esitystä varten, tai jos hypoteesi ei vielä ollut riittävän
   selvä testattavaksi koodilla, `../opportunity-visioning-with-pr-faq/SKILL.md`
   -skilliin visioinnin syventämiseksi ennen seuraavaa protoilukierrosta.

## Mitä tämä skilli EI tee

- Ei tee tuotantovalmiin sovelluksen arkkitehtuurisuunnittelua — tuottaa
  kapean, hypoteesin todistavan prototyypin.
- Ei takaa AI-avusteisesti tuotetun koodin tietoturvaa tai luotettavuutta —
  muistuttaa aina tarkistamaan autentikoinnin, virhekäsittelyn ja
  rajapintakutsujen oikeellisuuden ennen kuin prototyyppiä käytetään oikealla
  datalla tai esitetään ulkopuolisille (ks. pakin `../../CLAUDE.md`).
- Ei valitse teknistä arkkitehtuuria tuotantovaihetta varten — jos hypoteesi
  todistuu ja seuraava askel on tuotantokelpoinen ratkaisu, käytä
  `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`
  ja `../../../ai-strategy-and-governance/skills/build-vs-buy-vs-partner-ai/SKILL.md`.
- Ei mittaa tai laske ROI:ta prototyypin tuloksista — se on
  `../demo-to-business-case-bridge/SKILL.md`-skillin tehtävä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat suosikkityökalut ja niiden käyttötilanteet (mikä työkalu mihinkin
  tehtävätyyppiin omassa käytännössäsi)
- konkreettisia esimerkkejä epäonnistuneista protoiluista ja mikä niissä
  meni pieleen (fideliteettitaso väärä, hypoteesi liian laaja, jne.)
- oma PRD-mallipohja lyhyeen prototyyppiin (`../../references/`-kansioon)

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi: `../demo-framing-and-expectation-setting/SKILL.md`
  — kehystä mitä tämä prototyyppi TARKOITTAA asiakkaalle ennen esittämistä.
- Samassa pakissa (esitys): `../demo-delivery-and-storytelling/SKILL.md`
- Jos hypoteesi ei vielä ollut selvä ennen koodausta:
  `../opportunity-visioning-with-pr-faq/SKILL.md`
- Ennen tätä (jos toimialaan sopiva pattern puuttuu vielä):
  `../../../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- Vibe coding -parhaat käytännöt 2026 — työkaluvalinta, iteraatiosykli,
  PRD-ensin-periaate ja tunnetut riskit (hallusinoidut rajapinnat, puutteet
  auth-/oikeuslogiikassa, ylläpidettävyys) — usean 2026-lähteen synteesi
- Prototyyppifideliteetti-tutkimus (UX-tutkimusperinne: matalan
  fideliteetin prototyypit paljastavat suuren osan rakenteellisista
  ongelmista murto-osalla korkean fideliteetin kustannuksesta)
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
