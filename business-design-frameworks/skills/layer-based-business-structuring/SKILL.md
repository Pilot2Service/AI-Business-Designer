---
name: layer-based-business-structuring
description: "Jäsentää liiketoiminnan, palvelukonseptin tai liiketoimintamallin erillisiin toiminnallisiin kerroksiin (OSI-mallin kaltaisesti) infrastruktuurista brändiin, jotta voidaan päättää mitkä kerrokset toteutetaan itse ja mitkä kumppanien kautta."
---

# Layer-Based Business Structuring

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Jäsentää liiketoiminta, palvelukonsepti tai liiketoimintamalli erillisiin
toiminnallisiin kerroksiin — analogisesti tietoliikenteen OSI-mallin kanssa —
fyysisestä/infrastruktuurikerroksesta ylös aina brändi-tason kerrokseen, tai
kaupankäynnin näkökulmasta esim. logistiikka-, sopimus-, maksuliikenne-,
valikoima- ja markkinointikerroksiin. Kerrosmallin ydinidea on erottaa eri
toiminnalliset kokonaisuudet omiksi, itsenäisiksi kerroksikseen, jotta
jokaisesta kerroksesta voidaan tehdä oma päätös: toteutetaanko se itse vai
kumppanin kautta.

## Ankkurointi tutkimukseen

- OSI-malli (tietoliikenne, ISO/IEC 7498-1) — kerrosperiaatteen alkuperäinen
  esikuva: kukin kerros hoitaa oman, rajatun tehtävänsä ja on vaihdettavissa
  ja testattavissa itsenäisesti ilman että muut kerrokset tietävät sen
  sisäisestä toteutuksesta.
- Hagel, J. & Singer, M. (1999), "Unbundling the Corporation", Harvard
  Business Review — kolme perusliiketoimintaa jotka useimmat yritykset
  yhdistävät yhdeksi organisaatioksi: infrastruktuurin hallinta (skaalalla
  optimoituva), tuoteinnovaatio (nopeudella optimoituva) ja asiakassuhteen
  hallinta (laajuudella/scope:lla optimoituva). Näitä kolmea ei voi
  optimoida samanaikaisesti — siksi niiden erottaminen omiksi kerroksikseen
  usein kannattaa.
- Baldwin, C. & Clark, K. (2000), *Design Rules: The Power of Modularity* —
  modulaarisuusteoria: järjestelmän jakaminen moduuleihin/kerroksiin
  selkeillä rajapinnoilla mahdollistaa osien itsenäisen kehittämisen,
  korvaamisen ja ulkoistamisen ilman että koko järjestelmä pitää suunnitella
  uudelleen.

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. Valitse kerrosnäkökulma tilanteeseen sopivaksi. Esimerkkejä: **tekninen/
   toiminnallinen pino** (infrastruktuuri → operaatiot → tuote/palvelu →
   asiakasrajapinta → brändi), tai **kaupankäynnin pino** (logistiikka →
   sopimukset → maksuliikenne → valikoima → markkinointi → asiakaskokemus).
   Kerrosnäkökulma pitää aina sovittaa kontekstiin — ei ole yhtä oikeaa
   kerrosjakoa.
2. Listaa liiketoiminnan tai konseptin kaikki toiminnalliset osat ja sijoita
   kukin sopivaan kerrokseen.
3. Määritä kunkin kerroksen rajapinta naapurikerroksiin — mitä kerros ottaa
   sisään ja mitä se tuottaa ulos — jotta kerrokset pysyvät aidosti
   vaihdettavina (kuten OSI-mallissa: kukin kerros tarjoaa palvelun
   ylemmälle kerrokselle tietämättä sen sisäisestä toteutuksesta).
4. Arvioi kerroskohtaisesti: onko tämä kerros erottava kilpailuetu (kannattaa
   rakentaa itse) vai kypsä/kommoditisoitunut toiminto (kannattaa hankkia
   kumppanilta tai alustalta)? Hagel & Singerin jaottelu (infrastruktuuri /
   tuoteinnovaatio / asiakassuhde) auttaa tunnistamaan mitkä kerrokset
   kilpailevat keskenään organisaation sisällä resursseista ja johtamishuomiosta.
5. Tee build/partner/buy-päätös kerroksittain (sama päätöslogiikka soveltuu
   myös ei-AI-konteksteissa kuin `../../../ai-strategy-and-governance/skills/build-vs-buy-vs-partner-ai/SKILL.md`).
6. Visualisoi kerrosmalli pinona (esim. alhaalta ylös) ja merkitse kuhunkin
   kerrokseen oma/kumppani-päätös sekä perustelu.
7. Tarkista kokonaisuus: tuottaako kerrosten summa yhtenäisen
   asiakaskokemuksen, vai näkyykö rajapintojen kitka asiakkaalle asti
   (esim. hidas käsittelyaika kun kaksi kerrosta on eri toimijoiden vastuulla)?

## Mitä tämä skilli EI tee

- Ei anna valmista kerrosjakoa jokaiseen tilanteeseen — kerrosnäkökulma on
  aina valittava ja sovitettava kontekstiin.
- Ei tee build/partner/buy-päätöstä puolestasi — jäsentää päätöskriteerit
  kerroksittain ihmisen päätöksenteon tueksi.
- Ei korvaa syvällistä toimittaja- tai kumppanianalyysia yksittäisen
  kerroksen ulkoistamispäätöksessä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat vakiokerrosjaot, joita käytät toistuvasti tietyissä toimialoissa/tilanteissa
- konkreettiset mallipohjat (`../../references/`-kansioon, esim. kerrospino-templatet)
- referenssitapaukset / omat caset onnistuneesta tai epäonnistuneesta kerrosjaosta
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi: `../value-chain-mapping/SKILL.md` — Jäsentää
  liiketoiminnan Porterin arvoketjumallin mukaisesti ydin- ja
  tukitoimintoihin; toinen, perinteisempi tapa jäsentää sama liiketoiminta.
- Liittyvä skilli toisessa pakissa: `../../../ai-strategy-and-governance/skills/build-vs-buy-vs-partner-ai/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
