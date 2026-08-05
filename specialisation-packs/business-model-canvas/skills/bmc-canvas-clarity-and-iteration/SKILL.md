---
name: bmc-canvas-clarity-and-iteration
description: "Ohjaa BMC-työn variointilogiikalla kohti selkeyttä syvyyden sijaan: rakentaa 2-3 vaihtoehtoista canvas-varianttia, tunnistaa milloin tiimi on jumissa yhdessä canvasissa, ja arvioi canvas-valmiuden asiantuntijan kolmen kriteerin mukaan."
---

# BMC Canvas Clarity and Iteration

*Tila: `validated`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin BMC-työn sudenkuoppa: yhden canvasin hiominen loputtomiin
sen sijaan että rakennettaisiin useampi vaihtoehtoinen malli ja verrattaisiin
niitä. Skilli tuo asiantuntijan oman ydinperiaatteen käytäntöön: arvo
syntyy varianttien vertailusta, ei yhden canvasin täydellisyydestä, ja
selkeys voittaa aina syvyyden.

## Perustuu

- Omistajan (Tommi Järvinen) huhtikuun 2026 asiantuntijahaastattelu,
  kolme `status: accepted` / `confidence: high` -tiedostoa
  `[redacted]`-repossa:
  - `07_reasoning_model/reasoning_patterns/bmc_iteration_logic.md` —
    variointilogiikka, analyysi-/synteesivaiheet, "uniikki yhdistelmä"
    -tavoite, neljä riittävyyskriteeriä.
  - `12_quality_model/bmc_canvas_readiness.md` — "selkeys > syvyys"
    -filosofia, valmiin canvasin merkit, selkeysasteikko.
  - `06_expertise_and_cognition/cognitive_signatures/bmc_cognitive_signature.md` —
    nopeat havainnot canvasin kypsyydestä, tiimin taustan näkyminen
    canvasissa, jumissa-olevan tiimin tunnistaminen.

## Rakenne

1. **Rakenna ensimmäinen variantti nopeasti, kevyesti.** Täytä kaikki
   yhdeksän lohkoa yhdellä kevyellä kierroksella — älä hio. Tavoite: yksi
   liiketoimintamalli, ei täydellinen liiketoimintamalli.
2. **Rakenna toinen (ja tarvittaessa kolmas) variantti eri
   yhdistelmällä.** Käytä jäljelle jääneitä vaihtoehtoja tai valittua
   toista `../bmc-innovation-pattern-matching/SKILL.md`-skillin
   patternia. Minimissään 2-3 varianttia ennen analyysivaihetta —
   yksi canvas ei koskaan riitä patternien tunnistamiseen.
3. **Tunnista jumissa-olon merkit kesken työn:** tiimi hioo yhtä
   canvasia syvälle ilman varianttien tuottamista; sama canvas käsittelyssä
   pitkään ilman iterointia; liikaa vaihtoehtoja per lohko (useampi
   segmentti/kanava/tulovirta "aktiivisena" samanaikaisesti). Jos näet
   näitä merkkejä: pakota sprinttirakenne, aikaraja per vaihe, siirry
   uuteen varianttiin sen sijaan että jatkat hiomista.
4. **Tunnista tiimin taustan vinouma canvasissa.** Markkinointi-/
   asiakastaustaiset täyttävät herkästi asiakassegmentit ja kanavat;
   operatiivis-/tuotantotaustaiset täyttävät vahvasti vasemman puolen
   (avaintoiminnot, -resurssit); talousvetoiset ajattelevat luontaisesti
   kustannus-/marginaalilogiikkaa. Tasapainota työtä ohjaamalla keskustelu
   siihen lohkoon, joka jää vajaaksi tiimin taustan vuoksi.
5. **Kun 2-3 varianttia on valmiina, siirry analyysi-/
   synteesivaiheeseen:**
   - Marginaalinäkökulma: mikä malli tuottaa parhaan katteen?
   - Kilpailijanäkökulma: miten kilpailijat reagoisivat kuhunkin?
   - Uutuusnäkökulma: mikä on aidosti uutta kussakin?
   - Skenaarioanalyysi: miten malli kestää markkinaolosuhteiden muutoksen?
   - Synteesi: rakenna yhdistelmä varianttien parhaista elementeistä
     kohti "uniikkia yhdistelmää" — ei täydellistä canvasia vaan yhtä
     selkeää, fokusoitua asiakassegmenttiä + kanavaa + tulovirtaa +
     arvolupausta.
6. **Arvioi valmius asiantuntijan kolmella kriteerillä ennen
   siirtymistä eteenpäin:**
   - **Kertoo yhden asian:** yksi liiketoimintamalli, yksi valintajoukko,
     yksi fokus — ei useita vaihtoehtoisia tai päällekkäisiä valintoja
     per lohko.
   - **Selkeät valinnat:** ei "kaikki auki" -tilaa missään lohkossa.
   - **Yksinkertainen:** hyvä canvas voi olla yksi lause per lohko —
     pituus ei ole laadun mitta.
   Käytä asteikkoa: Korkea selkeys (yksi segmentti, yksi kanava, valitut
   tulovirrat, fokusoitu arvolupaus) / Matala selkeys (useita vaihtoehtoja
   per lohko, ei selkeitä valintoja) / Jumissa (yhtä canvasia työstetty
   liian syvälle ilman iterointia).
7. **Työ on riittävä kun:** kaikki lohkot on käyty läpi kevyellä
   ensimmäisellä kierroksella, vähintään kaksi varianttia on tuotettu,
   valinnat alkavat kiteytyä, ja malli on kommunikoitavissa yksinkertaisesti.
   Tässä vaiheessa: joko syvennä tai siirry tarkempiin työkaluihin
   (ks. `../bmc-tool-switching-decisions/SKILL.md`).

## Mitä tämä skilli EI tee

- Ei tuota patterneja tai innovaatiosuuntia itse — käyttää
  `../bmc-innovation-pattern-matching/SKILL.md`-skillin tuottamia tai
  käyttäjän omia vaihtoehtoja variointimateriaalina.
- Ei arvioi canvasin sisäistä ristiriitaisuutta tai diagnostisia
  signaaleja systemaattisesti — se on kapeampi, tarkempi tehtävä, ks.
  `../bmc-canvas-diagnostic-reading/SKILL.md`. Tämä skilli keskittyy
  PROSESSIIN (miten iteroidaan), ei canvasin lukemiseen analyyttisesti.
  Huomaa: tämän skillin valmiuskriteerit ovat asiantuntijan oma,
  tarkoituksella yksinkertaisempi ja opinionoidumpi näkemys kuin
  tutkimuskerroksen laajempi nelidimensioinen rubriikki — ks. ristiriita
  eksplisiittisesti kohdassa "Jatka tästä".
- Ei tee lopullista liiketoimintamallin valintaa puolestasi — synteesi
  tuottaa suosituksen, ihminen valitsee.

## Jatka tästä

- Edellinen skilli samassa pakissa:
  `../bmc-innovation-pattern-matching/SKILL.md` — patternien valinta
  ennen varianttien rakentamista.
- Seuraava skilli samassa pakissa:
  `../bmc-canvas-diagnostic-reading/SKILL.md` — kun variantti on valittu,
  lue se systemaattisesti sisäisten ristiriitojen ja evidenssiaukkojen
  varalta. **Huom:** tämän skillin "selkeys > syvyys" -kriteerit ovat
  asiantuntijan oma, kevyempi näkemys; `bmc-canvas-diagnostic-reading`
  käyttää laajempaa, tarkempaa tutkimuskerroksen rubriikkia. Käytä
  molempia — ne eivät korvaa toisiaan, ne vastaavat eri kysymyksiin
  ("onko tämä selkeä?" vs. "onko tämä sisäisesti johdonmukainen ja
  evidenssipohjainen?").
- Liittyvä skilli samassa pakissa:
  `../bmc-antipattern-and-misunderstanding-correction/SKILL.md` —
  jumissa-olon ja liika-syvyyden korjaaminen on yksi keskeinen
  antipatterni tässä skillissä; katso tarkempi korjauskeinovalikoima
  sieltä.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
