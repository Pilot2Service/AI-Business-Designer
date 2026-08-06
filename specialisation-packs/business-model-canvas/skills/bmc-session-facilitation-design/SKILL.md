---
name: bmc-session-facilitation-design
description: "Suunnittelee BMC-työpajan rakenteen tutkimuspohjaisilla heuristiikoilla: aloituskohdan valinta, täyttöjärjestys, session pituus/tiimikoostumus, milloin canvas ei ole vielä valmis, evidenssin värikoodaus ja canvasin esittäminen sidosryhmille."
---

# BMC Session Facilitation Design

*Tila: `scaffold`, `source_layer: research` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Antaa tutkimuspohjainen runko BMC-työpajan/-session suunnitteluun ennen
kuin sessio alkaa: mistä lohkosta aloitetaan, missä järjestyksessä lohkot
täytetään, kuinka pitkä ja minkä kokoinen tiimin pitäisi olla, milloin
canvas EI ole vielä valmis vaikka lohkot ovat täynnä, miten evidenssi
erotetaan oletuksesta, ja miten canvas esitetään sidosryhmille.

## Ankkurointi tutkimukseen

Tämä skilli perustuu omistajan yksityiseen tutkimuskerrokseen (huhtikuun 2026 asiantuntijahaastattelu)
(`30_domain_packs/bmc/facilitation/bmc_facilitation_heuristics.md` ja
`domain_scope.md`, `status: template`, `source: research_layer`) —
esitäytetty synteesi tunnetuista BMC-lähteistä: Jeffries, Williams,
van der Linden, Blank (Strategyzer), Business Models Inc., sekä
nimeämätön "YouTube-synteesi" -lähde. Näissä tiedostoissa on
`[EXPERT INPUT]`-merkittyjä kohtia, joita omistaja ei ole vielä
täyttänyt — ks. "Mitä tämä skilli EI tee".

## Rakenne (luonnos — täydennettävä)

1. **Valitse aloituskohta tietoisesti — se ei ole neutraali valinta.**
   Kolme validia tapaa:
   - **Asiakaslähtöinen** (yleisin): aloita asiakassegmenteistä, kun
     tiimin suurin epävarmuus on onko todellista markkinaa. Käytetään
     varhaisen vaiheen startupeissa ja design thinking -konteksteissa.
   - **Arvolähtöinen**: aloita arvolupauksesta, kun vahva teknologia tai
     kyvykkyys on jo olemassa ja kysymys on kenelle sitä tarjotaan.
   - **Nykytila-lähtöinen** (vakiintuneet organisaatiot): kartoita
     rehellisesti TÄMÄN HETKEN malli ennen tulevaisuuteen koskemista
     (van der Linden: "Ensimmäisen canvasin pitäisi kuvata todellisuutta,
     ei tavoitetilaa").
   Huomio (Blank): bioteknologiassa ja säännellyillä toimialoilla IP,
   sääntely ja korvauslogiikka voivat olla asiakaspuolta tärkeämpiä —
   järjestyksen on mukauduttava sinne, missä suurimmat riskioletukset ovat.
2. **Täytä oikea puoli ennen vasenta.** Segmentit → arvolupaus → kanavat
   → asiakassuhteet → tulovirrat → sitten avainresurssit → avaintoiminnot
   → avainkumppanit → kustannusrakenne. Perustelu (van der Linden): älä
   rakenna moottoria ennen kuin tiedät mihin ajat. Poikkeus: kun
   organisaatiolla on lukittu infrastruktuuri (patentoitu teknologia,
   sääntelyomaisuus, fyysinen verkosto), aloitus resursseista on
   perusteltu — mutta oikean puolen on oltava valmis ennen kuin canvas
   on johdonmukainen.
3. **Mitoita session pituus ja tiimikoostumus.** Ensimmäisen kierroksen
   työpaja: 2-3 tuntia. Alle 90 minuuttia on riittämätön. Yli 4 tuntia
   tuottaa ylianalysointia. Optimaalinen tiimi: 4-7 henkeä,
   monialainen — myynnin, tuotteen, markkinoinnin ja talouden väliset
   erimielisyydet tekevät piilo-oletukset näkyviksi. Yksin tai
   yksialaisesti tehty sessio tuottaa konsensuscanvaksen, joka ei
   paljasta todellisia jännitteitä.
4. **Tarkista onko canvas valmis oikealla mittarilla.** Canvas EI ole
   valmis vain siksi että lohkot ovat täynnä ("checklist thinking",
   "one and done" -virheet). Canvas on valmis kun se ohjaa päätöksiä —
   paljastaa missä malli on vahva, missä se vuotaa arvoa, ja mitkä
   oletukset ovat vielä testaamatta.
5. **Käytä evidenssin värikoodausta.** Vihreä = todistettu, keltainen =
   ohut evidenssi, punainen = puhdas oletus. Punaiset lohkot määrittävät
   testausprioriteetin. Jokaiselle oletukselle: mikä testi todistaisi/
   kumoaisi sen, mikä signaali kertoisi läpäisystä/epäonnistumisesta,
   mikä on minimievidenssikynnys ennen päätöstä.
6. **Suunnittele esitystapa etukäteen.** Kaikkien yhdeksän lohkon
   paljastaminen kerralla ylikuormittaa yleisön kognitiivisen
   kapasiteetin. Paljasta post-it kerrallaan, synkronoi puhe visuaaliin.
   Käytä juonirakennetta: alku (ongelma), nouseva toiminta (löytö),
   huippukohta (mallin muutos).

## Mitä tämä skilli EI tee

- Ei sisällä omistajan omaa validoitua näkemystä session
  facilitoinnista — tämä on tutkimuskerroksen synteesi, ei omistajan
  omaa kokemusta. Vertaa: `../bmc-canvas-clarity-and-iteration/SKILL.md`
  ja `../bmc-antipattern-and-misunderstanding-correction/SKILL.md` OVAT
  omistajan validoitua kokemusta — käytä niitä ensisijaisena lähteenä
  kun ne ovat saatavilla, ja tätä skilliä täydentävänä runkona.
- Ei kerro TÄMÄN pakin omistajan omaa oletusaloituskohtaa, tyypillistä
  session pituutta tai tapaa, jolla hän itse kommunikoi "canvas ei ole
  vielä valmis" -viestin asiakkaalle — nämä ovat auki
  omistajan tutkimusmuistiinpanojen avoimissa kohdissa.
- Ei anna kiinteää sääntöä poikkeustapauksille — tutkimuskerros antaa
  yleiset ohjenuorat, ei kaikkia tilanteita kattavaa päätöspuuta.

## [OWNER INPUT — täydennettävä]

Näihin kysymyksiin ei ole vielä vastausta omistajan tutkimusmuistiinpanoissa
(session 1/2 on merkitty "pending" repon `SESSION_GUIDE.md`:ssä):

- Mikä on sinun oletusaloituskohtasi? Milloin ohitat sen?
- Noudatatko oikea-ennen-vasenta-järjestystä? Missä poikkeat siitä?
- Mikä on standardisession pituutesi ja paras tiimikoostumus
  kokemuksesi mukaan?
- Mitä sanot asiakkaalle kun hän julistaa canvasin "valmiiksi" mutta
  tiedät ettei se ole?
- Käytätkö evidenssin värikoodausta tai vastaavaa omaa systeemiäsi?
- Miten esität canvasin sidosryhmille — mikä on oma narratiivinen
  lähestymistapasi?

## Jatka tästä

- Seuraava skilli samassa pakissa:
  `../bmc-canvas-diagnostic-reading/SKILL.md` — kun sessio on tuottanut
  canvasin, sen systemaattinen lukeminen.
- Liittyvä skilli samassa pakissa:
  `../bmc-canvas-clarity-and-iteration/SKILL.md` — omistajan oma,
  validoitu näkemys variointilogiikasta ja valmiuskriteereistä.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
