---
name: bmc-client-language-translation
description: "Tulkitsee asiakkaan tyypillisiä BMC-lauseita ('meidän pitää päivittää liiketoimintamallimme', 'olemme jo tehneet BMC:n') strategisiksi signaaleiksi, ja korjaa kolme yleisintä käsiteväärinkäsitystä: arvolupaus ominaisuuslistana, asiakassegmentti demografiana, tulovirta hinnoitteluna."
---

# BMC Client Language Translation

*Tila: `scaffold`, `source_layer: research` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Antaa sanasto sille, mitä asiakas TARKOITTAA sanoessaan tyypillisiä
BMC-työhön liittyviä lauseita — ja mitä kysyä seuraavaksi. Sekä korjata
kolme yleisintä käsitteellistä väärinkäsitystä (arvolupaus, asiakas­
segmentti, tulovirta vs. hinnoittelu), jotka näkyvät suoraan siinä miten
asiakas TÄYTTÄÄ canvasia, ei vain siinä miten hän puhuu siitä.

## Ankkurointi tutkimukseen

Perustuu `[redacted]`-repon tutkimuskerrokseen
(`03_domain_model/vocabulary/client_language_translation.md` ja
`concept_misunderstandings.md`, `status: template`, `confidence: low/medium`),
synteesi van der Lindenin ja Jeffriesin havainnoista. Huomaa: nämä ovat
KAKSI ERI tiedostoa kuin
`../bmc-antipattern-and-misunderstanding-correction/SKILL.md`:n
lähdetiedostot (`bmc_client_misunderstandings.md`,
`bmc_antipatterns_expert.md`) — tämä skilli käsittelee SANASTOA ja
KÄSITTEITÄ, se skilli käsittelee BMC:N ROOLIA koskevia väärinkäsityksiä.
Käytä molempia rinnakkain, ne eivät ole päällekkäisiä.

## Rakenne (luonnos — täydennettävä)

### A. Asiakaslauseiden tulkinta

1. **"Meidän pitää päivittää liiketoimintamallimme."** Tulkinta:
   asiakas kokee mallin vanhentuneeksi, usein kilpailupaineen tai
   laskevien marginaalien laukaisemana. Ei ole vielä tunnistanut mitä
   erityisesti pitäisi muuttua. Kysy seuraavaksi: mikä konkreettisesti
   sai tämän tuntumaan vanhentuneelta juuri nyt?
2. **"Olemme jo tehneet BMC:n."** Tulkinta: klassinen "kertatäyttö"
   (Jeffries) — tiimi täytti lohkot, pitää työtä valmiina. Canvasista on
   tullut juliste. Kysy seuraavaksi: saanko nähdä sen? (Usein
   paljastuu yksi staattinen canvas ilman variantteja tai iterointia —
   ks. `../bmc-canvas-clarity-and-iteration/SKILL.md`.)
3. **"Meidän pitää löytää arvolupauksemme."** Tulkinta: yleensä
   signaloi ominaisuusvetoista ajattelua. Tiimi osaa kuvata MITÄ he
   tekevät, ei sitä MITÄ asiakas siitä hyötyy.
4. **"Haluamme validoida mallimme."** Tulkinta: lähes aina tarkoittaa
   "puhuimme muutamalle ihmiselle ja he pitivät siitä" — ei todellista
   hypoteesitestausta. Ks. `../bmc-tool-switching-decisions/SKILL.md`
   hypoteesin laatukriteereistä ennen kuin kutsut jotain validoiduksi.
5. **"Asiakkaamme ovat [hyvin laaja segmentti]."** Tulkinta: yleisin
   yksittäinen mainittu virhe (van der Linden, Jeffries).
   Demografiaa ilman töitä, kipuja tai ostologiikkaa. Ks. DR-03 ja
   segmentin validiteettipäätös `../bmc-tool-switching-decisions/SKILL.md`:ssä.

### B. Kolme käsiteväärinkäsitystä

6. **Arvolupaus.** Tyypillinen asiakaskäyttö: ominaisuuslista
   ("Tarjoamme korkealaatuista X:ää erinomaisella palvelulla ja
   kilpailukykyisellä hinnalla"). Mitä se oikeasti on: spesifi,
   testattavissa oleva väite arvosta, joka on luotu tietylle segmentille
   valmiiden töiden, helpotettujen kipujen tai tuotettujen hyötyjen
   termein. Tunnusmerkki: jos se voisi koskea mitä tahansa kategorian
   kilpailijaa, se ei ole arvolupaus — se on kategoriakuvaus.
7. **Asiakassegmentit.** Tyypillinen asiakaskäyttö: laaja demografia
   ("pk-yritykset", "yritysasiakkaat", "kuluttajat 25-45v"). Mitä se
   oikeasti on: ryhmä, jolla on samat työt, kivut ja hyödyt — vaatii
   merkittävästi erilaisen arvolupauksen tai kanavan. Määritelty sen
   mukaan MITÄ he tarvitsevat, ei KEITÄ he ovat.
8. **Tulovirrat vs. hinnoittelu.** Väärinkäsitys: täytetään
   hinnoittelulla ("veloitamme 500€/projekti") tulologiikan sijaan
   ("transaktioperusteinen, projektikohtainen"). Erottelu: tulomalli
   (miten arvo kaapataan) vs. hinnoittelu (kuinka paljon veloitetaan) —
   nämä ovat kaksi eri kysymystä.

## Mitä tämä skilli EI tee

- Ei sisällä omistajan omaa vastausta siihen mitä hän kysyy seuraavaksi
  näiden lauseiden jälkeen, tai mitkä fraasit HÄNEN omassa
  asiakaskunnassaan ovat yleisimpiä — nämä ovat auki
  `[EXPERT INPUT]`-kohtina lähdetiedostoissa.
- Ei ole tyhjentävä sanasto — kattaa vain viisi tutkimuskerroksen
  dokumentoimaa lausetta ja kolme käsitettä, ei kaikkia mahdollisia
  asiakaspuheen muotoja.
- Ei korvaa `../bmc-antipattern-and-misunderstanding-correction/SKILL.md`:ää
  — se käsittelee BMC:n ROOLIA koskevia laajempia väärinkäsityksiä
  (esim. "BMC määrittelee kaiken kerralla"), tämä skilli käsittelee
  YKSITTÄISTEN KÄSITTEIDEN (arvolupaus, segmentti, tulovirta) sisältöä.

## [OWNER INPUT — täydennettävä]

- Mitä "liiketoimintamallin päivitys" -pyyntö yleensä tarkoittaa
  kokemuksesi mukaan? Onko se yleensä aito strateginen tarve vai
  jonkin muun oireilua? Mitä kysyt seuraavaksi?
- Miten vastaat "olemme jo tehneet BMC:n" -väitteeseen? Pyydätkö
  näkemään sen? Mitä "jo tehty" yleensä paljastaa?
- Mikä on vaistosi kun kuulet "haluamme löytää arvolupauksemme"?
  Mikä on todellinen ongelma sen takana kokemuksesi mukaan?
- Miten käsittelet "validointi"-sanan käytön? Miten resetoit
  odotukset siitä mitä validointi vaatii?
- Miten käsittelet hyvin laajan segmentin määrittelyn huoneessa?
  Painostatko heti vai annatko sen kehittyä ensin? Mikä on
  avauskysymyksesi?
- Miten näet arvolupaus-väärinkäsityksen omissa asiakkaissasi? Mikä
  on oma ohjausliikkeesi?
- Mikä on pahin segmenttimäärittely jonka olet nähnyt? Mitä teit?
- Erotatko tulomallin ja hinnoittelun? Miten käsittelet
  hinnoittelukeskustelun BMC-kontekstissa?
- Mitkä fraasit OMASSA asiakaskunnassasi käännät useimmin?
- Mitkä väärinkäsitykset ovat yleisimpiä juuri sinun
  asiakaskontekstissasi?

## Jatka tästä

- Liittyvä skilli samassa pakissa:
  `../bmc-antipattern-and-misunderstanding-correction/SKILL.md` —
  laajemmat BMC:n roolia koskevat väärinkäsitykset (omistajan
  validoima, `validated`-tasoinen — käytä ensisijaisena kun
  kysymys koskee BMC:n ROOLIA eikä yksittäistä käsitettä).
- Liittyvä skilli samassa pakissa:
  `../bmc-tool-switching-decisions/SKILL.md` — segmentin ja
  hypoteesin validiteettikriteerit, joita tämän skillin
  käsiteselitykset tukevat.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
