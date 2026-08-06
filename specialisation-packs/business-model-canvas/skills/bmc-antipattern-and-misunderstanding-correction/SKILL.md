---
name: bmc-antipattern-and-misunderstanding-correction
description: "Tunnistaa viisi BMC-työn asiantuntijan omaa antipatternia (mm. liikaa sisältöä per lohko, liian syvälle liian aikaisin, canvas strategia-asiakirjana) ja neljä yleisintä asiakkaan väärinkäsitystä BMC:n roolista, sekä tarjoaa suorat korjausliikkeet kumpaankin."
---

# BMC Antipattern and Misunderstanding Correction

*Tila: `validated`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Tunnistaa nopeasti, kun BMC-työ on menossa vikaan — joko tekemisen tavassa
(antipatternit) tai siinä, mitä asiakas/tiimi olettaa BMC:n tekevän
puolestaan (väärinkäsitykset) — ja tarjota asiantuntijan omat, suorat
korjausliikkeet kumpaankin. Tämä on diagnostinen ja korjaava skilli:
käytä sitä kesken session, kun jokin tuntuu jumiutuvan.

## Perustuu

- Omistajan huhtikuun 2026 asiantuntijahaastattelu,
  kaksi `status: accepted` / `confidence: high` -tiedostoa
  omistajan tutkimusmuistiinpanoissa:
  - `30_domain_packs/bmc/antipatterns/bmc_antipatterns_expert.md` — viisi
    asiantuntijan omaa antipatternia.
  - `30_domain_packs/bmc/facilitation/bmc_client_misunderstandings.md` —
    neljä yleisintä asiakkaan väärinkäsitystä BMC:n roolista.

## Rakenne

### A. Viisi antipatternia — tunnista tekemisen tavasta

1. **Liikaa sisältöä per lohko.** Merkki: useita tulovirtoja,
   segmenttejä, kanavia "aktiivisena" samanaikaisesti. Seuraus: selkeys
   katoaa, ei synny johdonmukaista polkua (fokussegmentti → fokuskanava
   → fokusarvolupaus → fokustulovirrat). **Korjaus:** pakota valintoja.
   Yksi segmentti, yksi kanava, selkeät tulovirrat. Ylimääräiset
   vaihtoehdot → uusi variantti, ei lisäys samaan canvasiin.
2. **Liian syvälle liian aikaisin.** Merkki: tiimi investoi raskaasti
   yhden canvasin hiomiseen ennen varianttien tuottamista. Seuraus: ei
   variantteja synny, canvas jää "moni-optioiseksi" sen sijaan että
   terävöityisi. **Korjaus:** pakota sprinttirakenne, aikaraja per vaihe
   — ks. `../bmc-canvas-clarity-and-iteration/SKILL.md`.
3. **Canvas strategia-asiakirjana.** Merkki: tiimi kohtelee canvasia
   lopullisena strategia- tai suunnitteludokumenttina, ei
   iterointityökaluna. Seuraus: ylihiominen yksittäisten sanavalintojen
   kanssa uniikin yhdistelmän etsimisen sijaan. **Korjaus:** muistuta
   roolista — BMC on ajattelu- ja innovaatiotyökalu, ei suunnitelma.
4. **Aloitus vasemmalta puolelta.** Merkki: sessio alkaa avaintoiminnoista
   / -resursseista / -kumppaneista. Seuraus: canvas rakentuu
   tuotantologiikan mukaan, ei asiakaslogiikan; arvolupaus jää irralliseksi.
   **Korjaus:** aloita aina oikealta: asiakas → ongelma → ratkaisu →
   arvolupaus → tulovirrat → vasen puoli.
5. **Yksi canvas riittää.** Merkki: tiimi tuottaa yhden canvasin ja
   pitää työtä valmiina. Seuraus: ei vertailupohjaa, innovaatiopatterneja
   ei voi tunnistaa yhdestä canvasista. **Korjaus:** vähintään 2-3
   varianttia ennen analyysi- ja synteesivaihetta — ks.
   `../bmc-canvas-clarity-and-iteration/SKILL.md`.

### B. Neljä asiakkaan väärinkäsitystä — tunnista puheesta

1. **"Tämä voisi määritellä kaiken kerralla."** Asiakas ajattelee: BMC
   on avain kaikkeen — kertatäyttö tuottaa valmiin liiketoimintasuunnitelman.
   Todellisuus: BMC on ensisijaisesti ajattelutyökalu. Se ei korvaa
   tarkempia suunnittelutyökaluja. **Vastaus:** käy läpi BMC:n rooli
   ajattelu- ja innovaatiotyökaluna — ei suunnitteludeliverabelina.
2. **Liian syvälle liian aikaisin (asiakkaan versio).** Asiakas yrittää
   tuottaa täydellisen canvasin ensimmäisellä yrittämällä. Seuraukset:
   ei aikaa varianteille, selkeys katoaa, ei fokusta missään.
   **Vastaus:** työn on oltava iteratiivista ja nopeaa. Kevyt ensin,
   varioi, syvennä sitten.
3. **Canvas = täydellinen liiketoiminnan suunnittelutyökalu.** Asiakas
   odottaa BMC:n riittävän kaikkeen suunnitteluun. Todellisuus: kun
   liiketoimintamalli on innovoitu, BMC:n jälkeen tulevat tarkemmat
   tuotespesifikaatiot, kannattavuus- ja kasvumarginaaliskenaariot, muut
   tarkemmat työkalut. BMC ei ole enää optimaalinen työkalu sen jälkeen
   kun innovaatiopäätös on tehty. **Vastaus:** ks.
   `../bmc-tool-switching-decisions/SKILL.md` seuraavista työkaluista.
4. **Yksi canvas riittää (asiakkaan versio).** Todellisuus: arvo tulee
   varianteista ja niiden vertailusta, ei yhdestä canvasista. Yksi canvas
   → yksi liiketoimintamalli. Arvo syntyy kun on 2-3 varianttia →
   voidaan analysoida, skenaariotestata, syntetisoida.

## Mitä tämä skilli EI tee

- Ei korvaa varsinaista variointiprosessia — ks.
  `../bmc-canvas-clarity-and-iteration/SKILL.md` konkreettisesta
  iterointimekaniikasta. Tämä skilli on tunnistus- ja korjausvälineistö,
  ei prosessiohje.
- Ei käsittele canvasin sisäistä diagnostiikkaa (Hook Rule, evidenssiaste
  jne.) — ks. `../bmc-canvas-diagnostic-reading/SKILL.md`. Antipatternit
  tässä skillissä koskevat TYÖTAPAA ja ASIAKKAAN ODOTUKSIA, ei valmiin
  canvasin sisällön laatua.
- Ei ole tyhjentävä lista kaikista mahdollisista virheistä — nämä 5+4
  ovat asiantuntijan omasta käytännöstä nousseet yleisimmät, ei
  kattava taksonomia.

## Jatka tästä

- Liittyvä skilli samassa pakissa:
  `../bmc-canvas-clarity-and-iteration/SKILL.md` — antipatternit 2 ja 5
  korjataan suoraan tämän skillin variointilogiikalla.
- Liittyvä skilli samassa pakissa:
  `../bmc-canvas-diagnostic-reading/SKILL.md` — kun canvas on valmis,
  tarkempi sisäisen johdonmukaisuuden lukeminen.
- Liittyvä skilli samassa pakissa:
  `../bmc-tool-switching-decisions/SKILL.md` — väärinkäsitys 3:n
  korjaus, kun BMC ei enää ole oikea työkalu.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
