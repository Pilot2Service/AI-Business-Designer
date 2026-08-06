---
name: demo-framing-and-expectation-setting
description: "Kehystää demon/protoilun/PoC:n asiakkaalle ennen esittämistä oikealla termillä (PoC vs. Pilotti vs. MVP) ja oikealla lupauksella — mitä tämä demo TODISTAA, mitä se EI todista, ja mitä seuraavaksi tapahtuu jos se onnistuu. Käytä ennen jokaista demoa tai PoC-esitystä, erityisesti kun riskinä on että asiakas ylitulkitsee demon tuotantovalmiudeksi tai automaattiseksi eteneväksi tuotantoon."
---

# Demo Framing & Expectation Setting

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin kalliisti korjattava virhe demoilussa: **väärä kehys ennen
ensimmäistä diaakaan.** Jos asiakas kävelee ulos demosta luullen, että
tuotantovalmis ratkaisu on kolmen viikon päässä, ja todellisuus on kuuden
kuukauden kehitystyö, ongelma ei ole demon laatu — ongelma on se, ettei
kukaan kehystänyt demoa oikein ennen kuin se alkoi. Tämä skilli tuottaa
sen kehyksen: mikä termi kuvaa oikein sitä mitä tänään näytetään, mitä
tämä demo todistaa ja mitä se EI todista, ja mitä konkreettisesti tapahtuu
seuraavaksi jos demo onnistuu.

Tämä on **eri kysymys** kuin
`../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`,
joka määrittää PoC:n TEKNISET reunaehdot (mitä dataa, mitä
onnistumiskriteerejä, mitä rajauksia). Tämä skilli vastaa **asiakas-
viestinnän** kysymykseen: miten sama PoC kehystetään puheessa niin, ettei
synny vääriä odotuksia. Käytä molempia yhdessä — tekninen rajaus ensin,
sitten tämä viestinnällinen kehys.

## Ankkurointi tutkimukseen

- PoC / Pilotti / MVP -erottelu (useamman 2026-lähteen synteesi, ks.
  Referenssit): kolme eri vaihetta vastaavat kolmeen eri epävarmuustyyppiin
  (tekninen toteutettavuus / operatiivinen sopivuus / tuotekehityssuunta).
- "Pilot purgatory" -tutkimus (McKinsey, BCG, IDC, MIT-synteesejä, ks.
  Referenssit): suuri osa yrityssektorin AI-piloteista ei koskaan etene
  tuotantoon, ja pullonkaula on tyypillisesti operatiivinen (johdon
  sitoutuminen, työnkulun uudelleensuunnittelu, mittakaavan investointi) —
  ei demo/PoC-vaiheen tekninen onnistuminen tai epäonnistuminen.

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. **Nimeä täsmällisesti, mitä tänään näytetään, oikealla termillä äläkä
   käytä termejä synonyymeinä** (ks. pakin `../../CLAUDE.md`):
   - **PoC**, jos kysymys on "toimiiko tämä teknisesti edustavalla
     datalla" — ei vielä oikeita käyttäjiä, ei tuotantokuormaa.
   - **Pilotti**, jos kysymys on "toimiiko tämä oikeiden ihmisten ja
     oikeiden operatiivisten olosuhteiden kanssa" — tekninen toteutettavuus
     on jo osoitettu.
   - **MVP**, jos kysymys on "mitä pitäisi rakentaa seuraavaksi oikean
     käyttäjäpalautteen perusteella" — tuotekehitysote, ei todistamisvaihe.
   Jos et ole varma kumpi, kysy itseltäsi: "mihin YHTEEN epävarmuuteen tämä
   vastaa tänään?" Jos vastauksia on useampi, olet todennäköisesti
   yhdistämässä vaiheita — erottele ne.
2. **Kirjoita yhden lauseen "todistaa/ei todista" -pari ennen demoa:**
   - "Tämä demo todistaa, että ___ [tarkka, kapea väite, esim. 'malli
     poimii toimittajan Y-tunnuksen 20/20 testilaskusta']."
   - "Tämä demo EI todista, että ___ [mitä tahansa mikä ei ollut
     testin piirissä, esim. 'toimii kaikilla laskuformaateilla',
     'on tietoturvallinen tuotantokäyttöön', 'skaalautuu 10 000
     laskuun kuukaudessa']."
   Esitä molemmat asiakkaalle ennen demoa, ei vasta jos joku kysyy.
3. **Kytke kehys `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`
   -skillin tekniseen rajaukseen** jos se on jo tehty — käytä samoja
   onnistumiskriteerejä, älä keksi uusia demo-hetkellä.
4. **Kerro etukäteen, mitä konkreettisesti tapahtuu SEURAAVAKSI jos demo
   onnistuu** — kuka päättää, millä aikataululla, mitä resursseja pilotti/
   tuotantovaihe vaatisi. Tämä on suoraan "pilot purgatory" -riskin
   torjuntaa: jos kukaan ei ole etukäteen sopinut mitä onnistunut demo
   johtaa, se ei johda mihinkään riippumatta demon laadusta.
5. **Nimeä ääneen, mitä demo EI vielä ratkaise organisatorisesti** —
   työnkulun muutos, käyttäjien koulutus, johdon sitoutuminen, budjetti
   täyteen mittakaavaan. Tekninen onnistuminen demossa ei tarkoita että
   nämä on ratkaistu.
6. **Valitse kehyksen sävy yleisön mukaan:** tekniselle yleisölle voi
   painottaa tarkkuuslukuja ja rajoituksia suoraan; johdon yleisölle
   kehys kannattaa viedä `../../../change-and-communication/skills/executive-narrative-and-storyline/SKILL.md`
   -skillin kautta ennen demoa, jotta tekninen "todistaa/ei todista"
   -pari kääntyy liiketoiminnan kielelle.
7. **Dokumentoi kehys kirjallisesti ennen demoa** (yksi kappale riittää) ja
   jaa se osallistujille — vähentää riskiä, että demon jälkeinen muistikuva
   vääristyy (ihmiset unohtavat suurimman osan demon sisällöstä nopeasti,
   mutta kirjallinen kehys jää).

## Mitä tämä skilli EI tee

- Ei tee PoC:n teknistä rajausta — se on
  `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`
  -skillin tehtävä. Tämä skilli kehystää saman rajauksen asiakasviestintään.
- Ei rakenna itse demoa tai prototyyppiä — käytä
  `../rapid-prototype-and-vibe-coding-craft/SKILL.md` ennen tätä.
- Ei takaa, että oikea kehys yksin estää "pilot purgatoryn" — vähentää
  väärinymmärryksen riskiä, mutta tuotantoon eteneminen vaatii aina
  organisatorisia päätöksiä jotka ovat tämän skillin ulkopuolella.
- Ei laske ROI:ta tai rakenna business casea — ks.
  `../demo-to-business-case-bridge/SKILL.md`.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia esimerkkejä siitä, miten olet kehystänyt demon onnistuneesti (tai
  epäonnistuneesti) tietyn asiakkaan kanssa
- oma vakiolause-/slide-mallipohja "todistaa/ei todista" -parille
  (`../../references/`-kansioon)
- nyrkkisääntöjä siitä, milloin asiakas yleensä ylitulkitsee demon —
  mitkä signaalit ennakoivat tätä

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (protoilu): `../rapid-prototype-and-vibe-coding-craft/SKILL.md`
- Ennen tätä (tekninen rajaus): `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`
- Samassa pakissa seuraavaksi: `../demo-delivery-and-storytelling/SKILL.md`
- Johdon yleisölle: `../../../change-and-communication/skills/executive-narrative-and-storyline/SKILL.md`
- Jos demo onnistuu ja seuraava askel on liiketoimintaperustelu:
  `../demo-to-business-case-bridge/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- PoC vs. Pilotti vs. MVP -erottelu — usean 2026-lähteen synteesi
  yrityssektorin AI-projektien vaihejaosta
- "Pilot purgatory" -tutkimus — McKinsey/BCG/IDC/MIT-synteesejä siitä miksi
  suuri osa AI-piloteista ei etene tuotantoon
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
