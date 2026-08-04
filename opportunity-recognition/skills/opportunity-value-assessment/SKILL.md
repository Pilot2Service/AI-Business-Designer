---
name: opportunity-value-assessment
description: "Sijoittaa tunnistetun mahdollisuuden houkuttelevuus × toteutettavuus -matriisiin ja arvioi sen seitsemästä kaupallistamisnäkökulmasta — omistajan oma, tuotteistettu arviointikehys."
---

# Opportunity Value Assessment

*Tila: `validated` — omistajan (Tommi Järvinen) [redacted]-palvelun
Opportunity Value Assessment -tuotteen ytimenä toimivaan arviointikehykseen
ankkuroitu sisältö, ei tutkimustason scaffold. Ks. `../../../skills_index.json`
ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Sijoittaa tunnistetun mahdollisuuden kaksiulotteiseen houkuttelevuus ×
toteutettavuus -matriisiin ja arvioi sen seitsemästä kaupallistamisnäkökulmasta.
Tämä on omistajan oma, tuotteistettu ja asiakastyössä käytetty arviointikehys —
konkreettisempi ja tarkempi kuin yleinen `opportunity-evaluation-and-judgment`
-scaffold, joka kuvaa evaluation & judgment -osaamisen yleisellä tasolla.

## Perustuu

[redacted] — Opportunity Value Assessment -palvelu (oma tuote) ja sitä
tukeva taustatutkimus "S1 — Opportunity Package: Ehdotus yksinkertaisesta
arviointikehyksestä".

- Mullins' Seven Domains Model — kolme markkinakeskeistä + neljä
  organisaatiokeskeistä osa-aluetta mahdollisuuden elinkelpoisuuden arviointiin
  (Soren Kaplan, 2023 -yhteenveto)
- Timmons-malli: tiimi, mahdollisuus, resurssit jatkuvassa vuorovaikutuksessa
- Product Opportunity Evaluation Matrix (POEM) — feasibility × attractiveness
  (ConnectedDale, 2023)
- TRL-asteikko (DOE Tech-to-Market, 2021)

Edellyttää lähtöaineistoksi `../opportunity-intake-elicitation/SKILL.md`:n
tuottamat vastaukset (tai vastaavan tason tiedon muuta kautta).

## Rakenne

1. **Arvioi houkuttelevuus (attractiveness).** Neljä tekijää: markkinan koko ja
   kasvu (ks. `../market-sizing-tam-sam-som/SKILL.md`), asiakkaan
   ongelman/tarpeen merkittävyys, kilpailuedun vahvuus (mikä on ainutlaatuista —
   teknologia, patentti, liiketoimintamalli), kaupallinen potentiaali
   (katemarginaalit, skaalautuvuus, alustava näkemys tuotoista suhteessa
   lisensointivaihtoehtoon).
2. **Arvioi toteutettavuus/valmius (feasibility/readiness).** Neljä tekijää:
   teknologian valmiusaste (TRL, selkokielisenä: idea → PoC → prototyyppi →
   testattu prototyyppi → pilotti → markkinavalmis), resurssit ja osaaminen
   (tiimi, kumppanit, rahoitus — kyetäänkö kriittiset menestystekijät
   toteuttamaan käytännössä), strateginen yhteensopivuus (isolle yritykselle:
   linjassa strategian kanssa; startup-tiimille: linjassa tiimin vision kanssa),
   riskit ja toteutuksen esteet (tekniset epävarmuudet, regulaatio, pitkä
   kehitysaika, investointitarve).
3. **Sijoita mahdollisuus 2D-matriisiin** (3×3 tai 5×5 ruudukko, asteikko
   matala–keski–korkea kummallakin akselilla) ja kirjoita sanallinen tulkinta
   lokerosta: mitä käytännössä tarkoittaa esim. "korkea houkuttelevuus /
   keskitason valmius" tälle nimenomaiselle mahdollisuudelle.
4. **Tunnista kolme vahvistavaa ja kolme heikentävää tekijää.** Rehellisesti
   mutta rakentavasti — tarkoitus on auttaa tiedostamaan haasteet etukäteen,
   ei lannistaa.
5. **Muotoile Opportunity Hypothesis.** Muutaman lauseen tiivistys
   liiketoimintatermein, elevator pitch -muodossa: mikä tuote/palvelu, kenelle
   kohdennettuna, mikä arvo luvataan, mikä tekee siitä erinomaisen.
6. **Arvioi seitsemän kaupallistamisnäkökulmaa (evaluation lenses)** asteikolla
   1-5 + lyhyt perustelu kullekin: markkinan koko & kasvu; ongelman vahvuus &
   omaksuminen; skaalautuvuus & liiketoimintamalli; kilpailuasema; ajoitus &
   disruptio; rahoitus- ja pääomapolku; tiimi & kyvykkyydet.
7. **Anna alustava License vs. Startup -suunta** kolmen kriteerin pohjalta:
   markkinan koko/tuottopotentiaali, IPR:n suojattavuus, tiimin
   resurssit/riskinsietokyky. Tämä on suunta, ei lopullinen päätös — syvempi
   analyysi: `../../../specialisation-packs/research-commercialisation/skills/spinout-vs-licensing-pathway/SKILL.md`.
8. **Listaa 2-5 kriittistä toteutustekijää** — mitä on ratkaistava, jotta
   mahdollisuus realisoituu täyteen arvoonsa (esim. skaalautuvuuden validointi,
   jakelukumppanuudet, regulaatiohyväksynnät, kaupallisen osaamisen rekrytointi).
9. **Pidä arvio elävänä hypoteesina.** Päivitä matriisisijoitus ja pisteytys
   kun uutta evidenssiä markkinasta tai teknologiasta kertyy — älä lukitse
   arviota liian aikaisin väärien oletusten varaan.

## Mitä tämä skilli EI tee

- Ei anna lopullista sijoitus- tai go/no-go-päätöstä — tuottaa jäsennellyn,
  eri mahdollisuuksien kesken vertailukelpoisen arvion päätöksenteon tueksi.
- Ei korvaa syvällistä markkina-, kilpailija- tai kustannusanalyysia — matriisi
  ja pisteytys ovat karkeistuksia, joiden taustalla olevat analyysit on tehtävä
  huolella ennen kuin pisteytys on perusteltu.
- Ei tee lopullista license-vs-startup-päätöstä — antaa vain alustavan suunnan.
- Ei vahvista markkinakoko-, TRL- tai muita lukuja muistista — käyttää
  `opportunity-intake-elicitation`-vaiheen antamia lähtöarvoja tai merkitsee
  oletuksen selvästi.

## Jatka tästä

- Samassa pakissa seuraavaksi: `../opportunity-brief-writing/SKILL.md` —
  Kirjoittaa arvioinnin tulokset tiiviiksi Opportunity Brief -raportiksi.
- Syventävät skillit samassa pakissa: `../market-sizing-tam-sam-som/SKILL.md`,
  `../competitive-and-five-forces-mapping/SKILL.md`
- Liittyvä skilli toisessa pakissa (syvempi license-vs-startup-analyysi):
  `../../../specialisation-packs/research-commercialisation/skills/spinout-vs-licensing-pathway/SKILL.md`
- Liittyvä skilli toisessa pakissa (tutkimuspohjaisen mahdollisuuden
  tunnistaminen ennen tätä vaihetta):
  `../../../specialisation-packs/research-commercialisation/skills/research-opportunity-recognition/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/[redacted]-frameworks-review.md` — Mullins, Timmons, POEM -yhteenvedot
- `../../references/opportunity-brief-template.md` — raporttipohja tämän arvioinnin tuloksille
- `../../CLAUDE.md` — pakin jaetut suojaukset
