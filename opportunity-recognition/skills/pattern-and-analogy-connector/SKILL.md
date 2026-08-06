---
name: pattern-and-analogy-connector
description: "Yhdistää irrallisia havaintoja mielekkääksi mahdollisuudeksi tunnistamalla analogioita eri toimialojen/tilanteiden välillä käyttäen Capability Pattern Mapping -abstraktiomenetelmää: monta pintapuolisesti erilaista casea tiivistetään yhdeksi nimetyksi kyvykkyyspatterniksi, jota käytetään diagnostisena kysymyksenä uudessa kontekstissa. Käytä kun tarvitset opportunity recognition-tason tukea vastaavaan tehtävään."
---

# Pattern & Analogy Connector

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Yhdistää irrallisia havaintoja mielekkääksi mahdollisuudeksi tunnistamalla analogioita
eri toimialojen/tilanteiden välillä. Ydinmenetelmä on **Capability Pattern Mapping**:
sen sijaan että etsitään "onko meidän toimialallamme tehty jotain vastaavaa" —
mikä johtaa loputtomaan, pian vanhentuvaan case-listaan — pintapuolisesti erilaiset
casejoukot **abstrahoidaan yhdeksi nimetyksi, toimialariippumattomaksi kyvykkyys-
patterniksi**. Nimetty patterni muuttuu sitten **diagnostiseksi kysymykseksi**, jota
voi käyttää minkä tahansa uuden toimialan tai tilanteen kanssa ilman että pitää
ensin löytää juuri siltä toimialalta tunnettu esimerkki.

Tämä on eri asia kuin case-kirjasto. Case-kirjasto vastaa "onko tästä tehty joku
esimerkki" — se käy nopeasti vanhaksi ja houkuttelee kopioimaan pintatason ratkaisun
sellaisenaan. Patterni vastaa "millainen rakenteellinen tilanne tämä on" — se pysyy
käyttökelpoisena vuosia, ja pakottaa miettimään omaa kontekstia sen sijaan että
etsitään valmis vastaus.

## Ankkurointi tutkimukseen

- Tang, Kacmar & Busenitz — association and connection
- Opportunity recognition as pattern recognition -kirjallisuus
- Käyttäjän kuvaama Capability Pattern Mapping -menetelmä ja sen esimerkki
  (lasku-/tulli-/CV-dokumenttitapaus, ks. kohta 3 alla) — omistajan oma
  abstraktiotekniikka, ei akateeminen lähde

Sovellettu, valmiiksi rakennettu esimerkki AI-kyvykkyyspatterneista: ks.
`../../../ai-strategy-and-governance/references/ai-capability-pattern-library.md`
ja sen navigointiskilli `../../../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`.
Tämä skilli tässä on YLEINEN menetelmä; AI-strategy-pakin patternikirjasto on
sen yksi konkreettinen, toimialaan (AI-ratkaisut) sovellettu toteutus.

## Rakenne (luonnos — täydennettävä)

1. **Kerää 3+ pintapuolisesti erilaista havaintoa/casea**, joissa epäilet
   samankaltaista rakennetta. Ne voivat tulla eri toimialoilta, eri asiakkailta
   tai eri ajankohtina tehdyistä havainnoista. Älä aloita etsimällä "vastaavaa
   toimialaa" — aloita etsimällä *rakenteellista samankaltaisuutta pinnan alta*.
2. **Kysy jokaisesta casesta neljä abstraktiokysymystä**, jotka ohittavat
   toimialasanaston:
   - Mikä on **syöte**? (esim. "vapaamuotoinen teksti/PDF-dokumentti",
     ei "lainahakemus")
   - Mikä on **toimija/rooli**, joka tekee työn tänään? (esim. "korkeasti
     palkattu asiantuntija selaa dokumentin läpi", ei "luotonkäsittelijä")
   - Mikä on **kognitiivinen ydintoiminto**? (esim. "poikkeaman/puutteen
     etsintä suuresta määrästä vapaamuotoista sisältöä", ei "hakemuksen
     tarkistus")
   - Mikä on **lopputulos/päätös**, jota työ tukee? (esim. "hyväksy/hylkää/
     eskaloi-päätös", ei "luottopäätös")
3. **Kirjoita yksi lause, joka kuvaa kaikki casejoukon casen samalla tavalla
   käyttäen vain kohdan 2 vastauksia.** Tämä lause ON patternin nimi ja
   määritelmä. Esimerkki käyttäjän omasta materiaalista: kolme pintapuolisesti
   täysin erilaista casea — lainahakemusten dokumenttitarkistus rahoitusalalla,
   tulli-ilmoitusten tariffikoodien tarkistus logistiikassa, ja CV-seulonta
   HR:ssä — abstrahoituvat kaikki samaksi patterniksi: **"Rakenteettoman
   dokumentin validointi ja poikkeaman tunnistus"** (syöte: vapaamuotoinen
   dokumentti; toimija: asiantuntija; kognitiivinen ydin: poikkeaman etsintä
   suuresta tekstimassasta; lopputulos: hyväksy/hylkää/eskaloi-päätös).
4. **Muunna patterni diagnostiseksi kysymykseksi**, jota voi kysyä keneltä
   tahansa uudelta asiakkaalta ilman että etukäteen tietää heidän toimialaansa
   koskevia esimerkkejä. Esimerkki: patternista "Rakenteettoman dokumentin
   validointi ja poikkeaman tunnistus" syntyy kysymys: *"Missä kohtaa
   prosessianne korkeasti palkattu asiantuntija joutuu etsimään poikkeamia
   vapaamuotoisesta tekstistä tai PDF-dokumentista?"* — tätä samaa kysymystä
   voi kysyä rakennusalan, vakuutusalan tai julkishallinnon asiakkaalta ilman
   että on ensin nähnyt juuri heidän toimialaltaan tunnettua esimerkkiä.
5. **Testaa patternin kattavuus ja terävyys ennen käyttöä:**
   - **Kattavuus** — löydätkö patternille vähintään kolme aidosti erilaista
     (eri toimiala/eri konteksti) esimerkkiä? Jos et löydä kuin yhden, kyseessä
     ei vielä ole patterni vaan yksittäistapaus — älä yleistä liian aikaisin.
   - **Terävyys** — onko patterni tarpeeksi tarkka erotellakseen sen naapuri-
     patterneista? Liian laaja patterni ("AI auttaa päätöksenteossa") ei ohjaa
     diagnostista kysymystä mihinkään; liian kapea ("PDF-lainahakemusten
     tarkistus rahoitusalalla") ei yleisty toimialan yli.
6. **Käytä diagnostista kysymystä uudessa kontekstissa** (asiakastapaaminen,
   workshop, oma havainnointi) ja kirjaa vastaus jäsenneltynä hypoteesina:
   patternin nimi, miksi tämä tilanne täsmää patterniin, mitä eroa tällä
   tilanteella on tunnettuihin esimerkkeihin nähden.
7. **Validoi hypoteesi** sidosryhmillä tai omalla kokemuspohjaisella
   tarkistuslistalla ennen kuin viet sen eteenpäin (ks.
   `../opportunity-evaluation-and-judgment/SKILL.md`).

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä puolestasi — tuottaa jäsennellyn luonnoksen ihmisen
  päätöksenteon tueksi.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista — käyttää käyttäjän
  antamia lähtöarvoja tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).
- Ei takaa että löydetty analogia pitää paikkansa — tuottaa hypoteesin, joka pitää validoida.
- Ei ylläpidä valmista, kaiken kattavaa patternikirjastoa tässä yleisessä skillissä —
  se tehtäisiin turhan laajaksi ja vanhenisi nopeasti. Toimialaan/ratkaisutyyppiin
  sidotut valmiit patternikirjastot (esim. AI-kyvykkyyspatternit) elävät omissa
  pakeissaan ja viittaavat tähän menetelmään, eivät päinvastoin.
- Ei korvaa syvällistä toimialaselvitystä — patterni on hypoteesin nopeuttamiseen,
  ei toimiala-asiantuntemuksen korvike.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Menetelmä ja
lasku-/tulli-/CV-esimerkki ovat käyttäjän itsensä kuvaamia, mutta omaa laajempaa
käytännön kokemuspohjaa (muita validoituja omia patterneja, epäonnistuneita
yleistyksiä, nyrkkisääntöjä siitä milloin abstraktio menee liian pitkälle) ei
vielä ole liitetty. Täydennä tähän:

- omia validoituja patterneja opportunity recognition -työstä (ei pelkästään
  AI-kontekstista)
- konkreettisia esimerkkejä siitä, milloin abstraktio meni liian pitkälle
  (patterni osoittautui liian laajaksi ollakseen hyödyllinen) tai liian kapeaksi
- mallipohja diagnostisten kysymysten kokoamiseen (`../../references/`-kansioon)

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi: `../opportunity-evaluation-and-judgment/SKILL.md` — Arvioi tunnistetun mahdollisuuden elinkelpoisuuden jäsennellysti ennen resurssien sitomista.
- Konkreettinen sovellus AI-ratkaisuihin: `../../../ai-strategy-and-governance/references/ai-capability-pattern-library.md`
  (patternikirjasto) ja `../../../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`
  (miten kirjastoa käytetään asiakastyössä).
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt ja heuristiikat tässä tekniikassa
- konkreettiset mallipohjat (`../../references/`-kansioon)
- referenssitapaukset / omat caset
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi: `../opportunity-evaluation-and-judgment/SKILL.md` — Arvioi tunnistetun mahdollisuuden elinkelpoisuuden jäsennellysti ennen resurssien sitomista.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
