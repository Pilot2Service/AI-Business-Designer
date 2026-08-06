---
name: data-role-diagnosis
description: "Diagnosoi ja perustelee, toimiiko data organisaatiossa mahdollistajana (kustannus, operatiivinen tehokkuus) vai strategisena assettina (tuottava, monetisoitava, defensoitava) — heuristisilla testeillä (resale, flywheel, defensibility) ja Offense/Defense-kehyksellä. Käytä ennen datastrategian tai AI-liiketoimintamallin muotoilua, kun pitää määrittää mitä roolia data organisaatiossa TÄNÄÄN näyttelee ja mitä roolia sen HALUTAAN näyttelevän."
---

# Data Role Diagnosis

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin datastrategiakeskustelun sekaannus: puhutaan "datastrategiasta"
tarkoittaen kahta eri asiaa samaan aikaan. Osa organisaatiosta tarkoittaa
datan **hallintaa** (governance, laatu, integraatiot — kustannus joka pitää
koneiston pyörimässä). Osa tarkoittaa datan **hyödyntämistä uuden arvon
lähteenä** (monetisaatio, defensoitava kilpailuetu, uudet liiketoiminta-
mallit). Kumpikaan ei ole väärin, mutta ne vaativat eri työkalut, eri
mittarit ja eri johdon puheen. Tämä skilli tuottaa diagnoosin: mikä rooli
datalla on TÄNÄÄN kussakin osa-alueessa, ja onko siirtymä mahdollistajasta
assetiksi edes tavoiteltavaa juuri nyt.

## Ankkurointi tutkimukseen

- Mahdollistaja vs. strateginen assetti -jaottelu (toimialan konsultointi-
  käytäntö, usean lähteen synteesi 2026): data hyödykkeenä joka mahdollistaa
  operaatiot vs. data omaisuutena jonka arvo kasvaa ja tuottaa mitattavaa
  tuottoa.
- Davenport, Thomas H. & Bean, Randy — "offense vs. defense" -kehys
  datastrategialle (Harvard Business Review / MIT Sloan Management Review
  -kirjoitukset): data governance on puolustuspeliä (riskinhallinta,
  compliance, laatu), datan hyödyntäminen uuden liiketoiminnan lähteenä on
  hyökkäyspeliä (kasvu, kilpailuetu, uudet tulovirrat).
- Collins, Jim — flywheel-käsite (*Good to Great*, 2001) yleisenä
  liiketoimintamekanismina, sovellettuna tässä datan itseään vahvistavaan
  arvosilmukkaan (ks. kohta 3 alla ja
  `../data-monetization-model-selection/SKILL.md`).

## Rakenne (luonnos — täydennettävä)

1. **Kysy mahdollistaja-kysymys jokaisesta merkittävästä datalähteestä:**
   *"Auttaako tämä data meitä tekemään nykyisen asiamme nopeammin,
   halvemmin tai laadukkaammin?"* Jos vastaus on kyllä mutta ei mitään
   muuta, data toimii tänään mahdollistajana — se on hyödyke, ei
   liiketoiminnan ydin. Tyypillinen merkki: data mahdollistaa
   operatiivisen siilon purkamista (esim. raportointi, integraatiot)
   mutta ei itse tuota myytävää arvoa.
2. **Kysy assetti-kysymys samasta datalähteestä:** *"Voisimmeko myydä
   tätä dataa suoraan tai käyttää sitä kouluttamaan mallia, jota
   kilpailija ei pysty kopioimaan pelkällä pääomalla?"* Jos vastaus on
   kyllä, data on potentiaalinen strateginen assetti — mutta pelkkä
   potentiaali ei riitä, se pitää validoida kohdan 3 testeillä.
3. **Validoi assetti-väite kolmella testillä ennen kuin uskot siihen:**
   - **Resale-testi:** onko olemassa toimija, joka maksaisi tästä datasta
     tai siitä johdetusta oivalluksesta TÄNÄÄN, ilman että sinun tarvitsee
     ensin rakentaa mitään uutta? Jos ei, kyse on potentiaalista, ei
     nykyisestä assetista.
   - **Flywheel-testi:** paraneeko tuote/malli mitattavasti, kun dataa
     kertyy lisää, ja houkutteleeko parempi tuote lisää käyttäjiä (jotka
     tuottavat lisää dataa)? Jos silmukka ei sulkeudu jossain kohtaa
     (esim. lisädata ei paranna mallia havaittavasti), "flywheel" on
     toiveajattelua — ks. tarkempi tarkistuslista
     `../data-monetization-model-selection/SKILL.md`.
   - **Defensibility-testi:** voisiko kilpailija replikoida tämän
     kilpailuedun ostamalla saman määrän laskentatehoa/pääomaa, vai
     vaatiiko se juuri tätä dataa, jota ei ole muualla saatavilla? Jos
     kilpailija pääsisi samaan tulokseen rahalla ilman tätä dataa,
     assetti ei ole niin defensoitava kuin luultiin.
4. **Sijoita diagnoosi Offense/Defense-nelikenttään** kahdella akselilla:
   nykyinen kypsyys (matala/korkea data governance) ja tavoiteltu rooli
   (mahdollistaja/assetti). Tämä paljastaa tyypillisen sudenkuopan:
   organisaatio yrittää rakentaa assetti-tason liiketoimintaa (esim.
   datan monetisointia) heikon governance-perustan päälle — silloin
   ensimmäinen investointi ei olekaan monetisointi vaan governance.
5. **Kommunikoi rooli-diagnoosi johdolle yhden lauseen väitteenä per
   datalähde**, esim. "Asiakkaan ostokäyttäytymisdata toimii tänään
   pelkkänä raportointimahdollistajana, mutta läpäisee resale- ja
   flywheel-testin — se on potentiaalinen assetti, joka vaatii
   [nimeä puuttuva investointi] ennen kuin sitä voi monetisoida." Älä
   esitä potentiaalia jo toteutuneena arvona.
6. **Kytke diagnoosi seuraavaan päätökseen:** jos data on mahdollistaja
   eikä siihen ole tarkoitus muuttaa, priorisoi governance/laatu-
   investoinnit (ei tämän pakin ydinaluetta, ks. muut lähteet). Jos data
   validoituu assetiksi, siirry
   `../data-ai-strategy-design-and-prioritization/SKILL.md`-skilliin
   arvon priorisoimiseksi ja sitten
   `../data-monetization-model-selection/SKILL.md`-skilliin mallin
   valitsemiseksi.

## Mitä tämä skilli EI tee

- Ei tee data governance -toteutusta tai teknistä arkkitehtuuria — vain
  diagnosoi roolin ja perustelee sen.
- Ei laske datan rahallista arvoa tai ROI:ta — ks.
  `../data-monetization-model-selection/SKILL.md` ja
  `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`.
- Ei väitä, että jokainen datalähde pitäisi pyrkiä muuttamaan assetiksi —
  moni datalähde on ja saa pysyä pelkkänä mahdollistajana; pakottaminen
  assetti-ajatteluun ilman resale/flywheel/defensibility-läpäisyä johtaa
  yliarvioituihin datastrategioihin.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista —
  käyttää käyttäjän antamia lähtöarvoja tai merkitsee oletuksen selvästi
  (`[oletus — tarkista]`).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia esimerkkejä siitä, miten asiakas on yliarvioinut datansa assetti-
  arvon (mikä testi olisi paljastanut tämän etukäteen)
- konkreettinen diagnoosityöpaja-/haastattelupohja per datalähde
  (`../../references/`-kansioon)
- nyrkkisääntöjä siitä, missä toimialoissa/tilanteissa mahdollistaja-rooli
  on lähes aina oikea vastaus eikä assetti-tavoittelu kannata

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (jos data on jo epäilty vinoutuneeksi tai puutteelliseksi):
  `../data-bias-and-quality-critical-reading/SKILL.md`
- Samassa pakissa seuraavaksi (jos data validoitui assetiksi):
  `../data-ai-strategy-design-and-prioritization/SKILL.md`
- Jos rooli on jo selvä ja kysymys on MITEN monetisoida:
  `../data-monetization-model-selection/SKILL.md`
- Liittyvä skilli toisessa pakissa: `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
  — käyttää Data Readiness -ulottuvuutta AI-mahdollisuuksien pisteytyksessä;
  tämä skilli syventää sitä yhden datalähteen roolin tasolla.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/data-role-heuristics.md` — laajempi kokoelma
  diagnostisia kysymyksiä ja esimerkkejä
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
