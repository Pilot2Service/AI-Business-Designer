---
name: bmc-canvas-diagnostic-reading
description: "Lukee valmiin BMC-canvasin diagnostisena instrumenttina kuudella tutkimuspohjaisella säännöllä (Hook Rule, arvo-kustannus-johdonmukaisuus, segmentin spesifisyys, evidenssiaste, puolustava canvas, puuttuva lohko) ja nelidimensioisella laaturubriikilla."
---

# BMC Canvas Diagnostic Reading

*Tila: `scaffold`, `source_layer: research` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Antaa systemaattinen tapa lukea valmis (tai lähes valmis) BMC-canvas
diagnostisena instrumenttina — ei vain tarkistuslistana täytettyjä
lohkoja, vaan kuutena kysymyksenä siitä, onko canvas sisäisesti
johdonmukainen, rehellinen evidenssin suhteen, ja valmis
hypoteesitestausvaiheeseen. Käytä tätä KUN canvas (tai variantti) on
valmis arvioitavaksi — ei kesken session rakentamisen (siihen ks.
`../bmc-session-facilitation-design/SKILL.md` ja
`../bmc-canvas-clarity-and-iteration/SKILL.md`).

## Ankkurointi tutkimukseen

Perustuu omistajan yksityiseen tutkimuskerrokseen (huhtikuun 2026 asiantuntijahaastattelu)
(`30_domain_packs/bmc/diagnostics/bmc_diagnostic_rules.md`,
`canvas_quality_rubric.md`, `antipatterns/counterexamples.md` —
kaikki `status: template`, `source: research_layer`), synteesi
van der Lindenin, Jeffriesin, Williamsin ja käytännön havaintojen
pohjalta. `[EXPERT INPUT]`-kohdat ovat vielä täyttämättä.

**Huom:** Tämä on eri asia kuin
`../bmc-canvas-clarity-and-iteration/SKILL.md`:n omistajan oma
"selkeys > syvyys" -valmiuskriteeri. Se kriteeri on tarkoituksella
yksinkertaisempi ja opinionoidumpi ("kertooko canvas yhden asian
selkeästi?"). Tämän skillin kuusi sääntöä ovat tarkempia ja
analyyttisempia ("onko canvas sisäisesti johdonmukainen ja
evidenssipohjainen?"). Käytä molempia — ne vastaavat eri kysymyksiin.

## Rakenne (luonnos — täydennettävä)

1. **DR-01 — Hook Rule.** Jokaisella oikean puolen elementillä on
   oltava vastaava koukku vasemmalla — ja päinvastoin. Jos
   asiakassuhteet määrittelee "omistautunut henkilökohtainen palvelu",
   avainresursseissa on oltava asiakasrajapinnan seniorihenkilöstöä ja
   avaintoiminnoissa suhteenhallintaa. Piirrä yhteydet toisiinsa
   liittyvien elementtien välille — orvot elementit (ilman koukkuja)
   ovat oletusaukkoja.
2. **DR-02 — Arvo-kustannus-johdonmukaisuus.** Jos arvolupaus lupaa
   premium-laatua, ainutlaatuisuutta tai korkean kosketuksen palvelua,
   kustannusrakenteen on heijastettava tätä. "Paras laatu" + "kustannus­
   johtajuus" -yhdistelmä on sisäisesti ristiriitainen. Ristiriita ei
   tarkoita että liiketoiminta on väärä — se tarkoittaa että tiimi ei
   ole ratkaissut perustavanlaatuista strategista jännitettä. Kysy:
   "voimmeko toimittaa tämän arvon tällä kustannuksella?"
3. **DR-03 — Segmentin spesifisyystesti.** Segmentti on liian laaja
   kun: se on määritelty vain demografialla ("25-45-vuotiaat"); se
   voisi sisältää minkä tahansa kilpailijan minkä tahansa asiakkaan
   ("pk-yritykset"); se yhdistää useita erillisiä ostologiikoita yhdeksi
   ryhmäksi; se sisältää sekä käyttäjän että maksajan erottelematta.
   Segmentti on riittävän spesifi kun tiimin jäsen voisi kävellä ulos
   ja tunnistaa viisi tiettyä ihmistä, jotka sopivat siihen, ja selittää
   miksi näillä viidellä on sama työ, kipu ja hyöty.
4. **DR-04 — Evidenssiasteen tarkistus.** Lue jokainen lohko ja
   luokittele: todistettu (testattu oikeilla asiakkailla/datalla),
   heikosti todistettu (sisäinen oletus tai toisen käden tieto),
   oletus (testaamaton uskomus). Eniten punaista sisältävät lohkot ovat
   testausprioriteetti. Kokonaan vihreä canvas joko kuvaa hyvin kypsää
   liiketoimintamallia tai ei ole ollut rehellinen sen suhteen mitä
   oikeasti tiedetään.
5. **DR-05 — Puolustava canvas -signaali.** Kun tiimi täyttää canvasin
   nopeasti, itsevarmasti ja ilman debattia, kaksi asiaa on mahdollista:
   (1) malli on aidosti kypsä ja hyvin ymmärretty (harvinaista), tai
   (2) tiimi esittää varmuutta sen sijaan että tutkisi sitä (yleistä).
   Signaaleja: mitään lohkoa ei ole debatoitu tai muutettu session
   aikana; jokainen elementti on positiivinen (ei jännitteitä tai
   kompromisseja nimettynä); tiimi viittaa canvasiin "tarinanamme" eikä
   "oletuksinamme"; asiakassegmentit esitetään faktoina, ei hypoteeseina.
6. **DR-06 — Puuttuva lohko kertoo jotain.** Kun lohko jätetään tyhjäksi
   tai merkitään "TBD", tämä on diagnostista tietoa, ei muotoiluvirhe.
   Tyhjä tulovirrat-lohko tarkoittaa että tiimi ei ole ratkaissut miten
   arvo kaapataan. Tyhjä avainkumppanit-lohko tarkoittaa yleensä ettei
   riippuvuuksia ole vielä mietitty. Diagnostisin tyhjä lohko:
   asiakassuhteet — tiimit ohittavat sen usein sekoittamalla sen
   kanaviin, mikä paljastaa ettei vuorovaikutuksen luonnetta (transak­
   tionaalinen vs. relationaalinen, korkea kosketus vs. automatisoitu)
   ole vielä mietitty.
7. **Käytä nelidimensioista rubriikkia lopullisena pisteytyksenä**
   (kukin 1-5): segmentin spesifisyys, arvolupauksen laatu, sisäinen
   johdonmukaisuus, evidenssin rehellisyys. Tulkinta: 16-20 = vahva
   canvas, valmis testausvaiheeseen. 11-15 = toimiva, korjattavaa ennen
   testausta. 6-10 = merkittävää uudelleentyötä. Alle 6 = aloita alusta.
8. **Varo kahta counterexamplea, jotka näyttävät hyvältä työltä muttei
   ole:** (C-01) spesifi mutta silti väärä segmentti — spesifisyys ei
   takaa validiteettia, jos segmentti on liian pieni, sisäisesti
   heterogeeninen tai perustajan omaan verkostoon rajoittunut; testi:
   osaako tiimi nimetä kolme kilpailijaa jotka tavoittelevat samaa
   ryhmää? (C-02) rehellinen mutta silti puutteellinen canvas — rehellisyys
   epävarmuudesta ei tarkoita että OIKEAT epävarmuudet on tunnistettu;
   testi: kun kysytään "mikä tappaisi tämän liiketoimintamallin?",
   vastaavatko riskit mitään canvasilla näkyvää?

## Mitä tämä skilli EI tee

- Ei sisällä omistajan omaa tulkintaa siitä, mikä on yleisin koukku­
  virhe, arvo-kustannus-ristiriita tai segmentin spesifisyystesti
  hänen omassa käytännössään — nämä ovat auki `[EXPERT INPUT]`-kohtina
  lähdetiedostoissa.
- Ei korvaa `../bmc-canvas-clarity-and-iteration/SKILL.md`:n
  yksinkertaisempaa, omistajan validoimaa valmiuskriteeriä — käytä
  molempia rinnakkain, ei toista toisen sijaan.
- Ei tee lopullista proceed/return-päätöstä puolestasi — tarjoaa
  pisteytyksen ja diagnostiikan, päätös testausvaiheeseen etenemisestä
  on ihmisen.

## [OWNER INPUT — täydennettävä]

- Mikä on yleisin koukkuvirhe (DR-01) jonka löydät käytännössä?
- Mikä on yleisin arvo-kustannus-ristiriita (DR-02) jonka näet, ja
  miten nostat sen esiin ilman puolustusreaktiota?
- Mikä on oma segmentin spesifisyystestisi (DR-03)?
- Miten ajat evidenssiasteen tarkistuksen (DR-04) live-sessiossa?
  Vastustavatko asiakkaat punaisen merkitsemistä?
- Miten erotat aidon itsevarmuuden puolustavasta varmuudesta (DR-05)?
- Mikä tyhjä lohko (DR-06) kertoo sinulle eniten kokemuksesi mukaan?
- Miten oma laatuarviosi toimii — mikä dimensio painottuu eniten?

## Jatka tästä

- Edellinen skilli samassa pakissa:
  `../bmc-canvas-clarity-and-iteration/SKILL.md` — omistajan oma,
  kevyempi valmiuskriteeri, käytä ensin.
- Seuraava skilli samassa pakissa:
  `../bmc-tool-switching-decisions/SKILL.md` — kun diagnostiikka
  paljastaa että BMC ei enää ole oikea työkalu.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
