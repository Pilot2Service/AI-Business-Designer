---
name: bmc-tool-switching-decisions
description: "Päättää milloin siirtyä BMC:stä toiseen työkaluun (Value Proposition Canvas, Lean Canvas, Mission Model Canvas, taloudellinen mallinnus, useampi rinnakkainen canvas) ja arvioi canvasin, hypoteesin ja segmentin laadun kolmella päätöskriteeristöllä ennen testausvaiheeseen siirtymistä."
---

# BMC Tool Switching Decisions

*Tila: `scaffold`, `source_layer: research` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Auttaa tunnistamaan, kun BMC ei enää ole (tai ei koskaan ollut) oikea
työkalu käsillä olevaan kysymykseen, ja mihin siirtyä sen sijaan. Sisältää
myös kolme päätöskriteeristöä, jotka määrittävät milloin canvas,
hypoteesi tai segmentti on riittävän laadukas edetäkseen seuraavaan
vaiheeseen.

## Ankkurointi tutkimukseen

Perustuu omistajan yksityiseen tutkimuskerrokseen (huhtikuun 2026 asiantuntijahaastattelu)
(`30_domain_packs/bmc/facilitation/tool_switching_logic.md` ja kolme
`08_decision_model/decision_types/*.md`-tiedostoa — kaikki
`status: template`, `source: research_layer`), synteesi Jeffriesin,
Strategyzerin, Ash Mauryan (Lean Canvas), Blankin (Mission Model
Canvas) ja van der Lindenin lähteistä.

## Rakenne (luonnos — täydennettävä)

### A. Milloin vaihtaa työkalua

1. **Siirry Value Proposition Canvasiin (VPC)**, kun tiimi ei pysty
   selkeästi artikuloimaan asiakkaan töitä, kipuja ja hyötyjä
   pääsegmentille — BMC:n arvolupauslohko on liian pieni tähän työhön.
   VPC on monissa ammattikäytännöissä esityö ENNEN BMC-sessiota, ei
   pakotie siitä.
2. **Siirry Lean Canvasiin**, kun ensisijainen epävarmuus on
   ongelma-ratkaisu-sopivuus, ei liiketoimintamallin sopivuus. Lean
   Canvas korvaa: avainkumppanit → ongelma, avaintoiminnot → ratkaisu,
   asiakassuhteet → epäreilu etu, tulovirrat → nykyiset vaihtoehdot.
   Käytä kun: hyvin varhainen vaihe, tekijävetoinen, kysymys "onko tämä
   todellinen ongelma?" on vielä auki.
3. **Siirry Mission Model Canvasiin**, kun organisaatio ei toimi
   tulologiikalla — voittoa tavoittelematon, julkishallinto, missio­
   vetoinen. Korvaukset: asiakassegmentit → edunsaajat, tulovirrat →
   rahoituslähteet, asiakassuhteet → sitoutumis-/tukimekanismit.
4. **Siirry taloudelliseen mallinnukseen**, kun kustannusrakenne tai
   tulovirrat vaativat numeerista tarkkuutta, jota post-it-laput eivät
   tarjoa. BMC ei ole laskentataulukko. Kun päätökset riippuvat
   yksikkötaloudesta, marginaaleista tai kassavarannosta, tarvitaan
   erillinen taloudellinen malli.
5. **Pysy BMC:ssä mutta jaa useampaan canvasiin**, kun organisaatiolla
   on useampi erillinen liiketoimintamalli (eri segmentit vaativat
   perustavanlaatuisesti erilaisia arvolupauksia, kanavia ja
   kustannusrakenteita). Yksi canvas tuottaa väärää keskiarvoistamista —
   jokainen erillinen malli tarvitsee oman canvasinsa.

### B. Kolme päätöskriteeristöä

6. **Canvasin laatupäätös** — kynnyskriteeri: läpäiseekö canvas Hook
   Rulen (ks. `../bmc-canvas-diagnostic-reading/SKILL.md`)? Jos
   perustavanlaatuinen ristiriita on olemassa arvolupauksen ja
   kustannusrakenteen tai segmenttien ja tulovirtojen välillä, canvas
   ei ole valmis — korjaa ristiriita ensin. Jos johdonmukainen, arvioi:
   segmentin spesifisyys, arvolupauksen laatu, evidenssin rehellisyys.
   Tulokset: **etene testaukseen** (12+ pistettä rubriikilla EIKÄ
   perustavanlaatuisia ristiriitoja), **etene lipulla** (8-11 pistettä,
   tunnistettu heikkous joka ei estä alkutestausta mutta on korjattava
   kahden ensimmäisen testaussyklin aikana), **palauta uudelleentyöhön**
   (alle 8 pistettä TAI perustavanlaatuinen ristiriita).
7. **Hypoteesin laatupäätös** — kolme vaatimusta: **testattavissa**
   (muuttaisiko kokeen tulos tiimin uskomusta?), **täsmällinen**
   (sisältääkö lukuja, aikarajoja tai kynnysarvoja — "asiakkaat
   maksaisivat enemmän nopeammasta toimituksesta" EI ole täsmällinen,
   "60% nykyisistä käyttäjistä maksaisi 5% lisän samana päivänä
   toimituksesta" ON), **erillinen** (testaako täsmälleen yhtä
   muuttujaa — jos hypoteesissa on "ja", testaa kaksi erillistä
   hypoteesia). "Clueless Corner" -priorisointi: kartoita hypoteesit
   liiketoiminnan onnistumisen tärkeyden (pystyakseli) ja nykyisen
   evidenssin vahvuuden (vaaka-akseli) mukaan — vasen yläkulma
   (korkea tärkeys, ei evidenssiä) testataan ENSIN, ei viimeiseksi,
   koska epämukavuus signaloi riskiä.
8. **Segmentin validiteettipäätös** — neljä kriteeriä: segmentti
   kuvattavissa työn, ei vain demografian kautta; maksaja ja käyttäjä
   erotettu kun ne eroavat; segmentti riittävän spesifi tuottaakseen
   testattavia hypoteeseja; segmentti ei ole määritelty perustajan
   omalla verkostolla (yleisin piilo-invaliditeetti: segmentti on
   oikeasti "ihmiset joita jo tunnemme ja jotka ovat ilmaisseet
   kiinnostusta" — tämä on löytämisen lähtökohta, ei validoitu segmentti).

## Mitä tämä skilli EI tee

- Ei tee taloudellista mallinnusta itse — vain tunnistaa milloin se
  tarvitaan ja ohjaa sinne.
- Ei sisällä omistajan omaa rajaa canvas-työn ja taloudellisen
  mallinnuksen välillä, omaa VPC-käytön ajoitusta, tai omaa Lean
  Canvas / Mission Model Canvas -käyttökokemusta — nämä ovat auki
  `[EXPERT INPUT]`-kohtina lähdetiedostoissa.
- Ei korvaa `../bmc-canvas-diagnostic-reading/SKILL.md`:ää canvasin
  sisäisen laadun arvioinnissa — käyttää sen Hook Rule -käsitettä
  kynnyskriteerinä mutta ei toista koko diagnostiikkaa.

## [OWNER INPUT — täydennettävä]

- Milloin tuot VPC:n mukaan? Käytätkö sitä rutiininomaisesti ennen
  BMC:tä vai vain kun BMC juuttuu?
- Käytätkö Lean Canvasia? Milloin? Vaihdatko niiden välillä kesken
  toimeksiannon?
- Oletko käyttänyt Mission Model Canvasia? Mitä mukautuksia teet
  missiovetoisille asiakkaille vaikka he käyttäisivät tavallista BMC:tä?
- Missä on OMA rajasi canvas-työn ja taloudellisen mallinnuksen
  välillä? Teetkö molemmat vai ohjaatko eteenpäin?
- Milloin olet käyttänyt useampaa rinnakkaista canvasia? Mikä
  laukaisi jakamisen?
- Mikä on todellinen etene/palauta-kynnyksesi canvasin laadussa?
- Miten autat tiimejä priorisoimaan hypoteeseja? Mikä on yleisin
  virhe hypoteesipriorisoinnissa?
- Mikä on oma segmenttivaliditeettitestisi käytännössä?

## Jatka tästä

- Edellinen skilli samassa pakissa:
  `../bmc-canvas-diagnostic-reading/SKILL.md` — Hook Rule ja muut
  diagnostiset säännöt, joita tämän skillin kynnyskriteeri käyttää.
- Liittyvä skilli samassa pakissa:
  `../bmc-innovation-pattern-matching/SKILL.md` — kun BMC:stä
  siirrytään taloudelliseen mallinnukseen, patternivalinnat ovat jo
  tehty ennen sitä.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
