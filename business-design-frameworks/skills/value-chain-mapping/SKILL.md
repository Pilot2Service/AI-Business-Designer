---
name: value-chain-mapping
description: "Jäsentää liiketoiminnan toiminnot Porterin arvoketjumallin mukaisesti ydin- ja tukitoimintoihin, jotta nähdään mistä arvo ja marginaali syntyvät ja missä kilpailuetu voidaan rakentaa."
---

# Value Chain Mapping

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Jäsentää liiketoiminnan toiminnot Michael Porterin arvoketjumallin
mukaisesti ydin- ja tukitoimintoihin, jotta nähdään mistä arvo ja marginaali
syntyvät organisaatiossa ja missä toiminnossa kilpailuetu — kustannusjohtajuus
tai differointi — todella rakentuu.

## Ankkurointi tutkimukseen

- Porter, M. (1985), *Competitive Advantage: Creating and Sustaining
  Superior Performance* — arvoketjumalli (Value Chain). Ydintoiminnot:
  tulologistiikka, operaatiot, lähtölogistiikka, markkinointi & myynti,
  palvelu. Tukitoiminnot: yrityksen infrastruktuuri, henkilöstöhallinto,
  teknologiakehitys, hankinta.
- Laajennettu näkemys: arvoketju ei pääty organisaation rajalle vaan
  ulottuu **arvojärjestelmäksi** (value system) toimittajista aina
  asiakkaan omiin asiakkaisiin — kilpailuetu voi syntyä myös oman ketjun
  ulkopuolella olevien linkkien optimoinnista.
- Sama teoreettinen perhe: Porter's Five Forces, ks.
  `../../../opportunity-recognition/skills/competitive-and-five-forces-mapping/SKILL.md`.

## Rakenne (luonnos — täydennettävä)

1. Listaa organisaation ydintoiminnot Porterin viiteen kategoriaan:
   **tulologistiikka** (panosten/raaka-aineiden vastaanotto ja varastointi),
   **operaatiot** (panosten muuttaminen lopputuotteeksi tai palveluksi),
   **lähtölogistiikka** (tuotteen/palvelun toimitus asiakkaalle),
   **markkinointi & myynti**, **palvelu** (myynnin jälkeinen tuki ja huolto).
2. Listaa tukitoiminnot: **yrityksen infrastruktuuri** (johto, talous,
   laatu, lakiasiat), **henkilöstöhallinto**, **teknologiakehitys** (T&K,
   IT, tuotekehitys), **hankinta**.
3. Arvioi kunkin toiminnon kustannus ja sen tuottama koettu arvo/erottautuminen
   asiakkaalle — mikä toiminto tuo eniten arvoa asiakkaan silmissä, mikä on
   pelkkä välttämätön kustannus ilman erottautumista?
4. Tunnista marginaalin lähde: missä toiminnossa syntyy suurin osa katteesta,
   ja missä toiminnossa kilpailuetu todella rakentuu — kustannusjohtajuus
   (halvin toteutus) vai differointi (paras koettu arvo) Porterin geneeristen
   strategioiden mukaisesti?
5. Kartoita toimintojen väliset linkit (linkages) — miten yhden toiminnon
   tehostaminen vaikuttaa toiseen (esim. parempi laatuvalvonta operaatioissa
   voi vähentää palvelukustannuksia myöhemmin).
6. Laajenna tarvittaessa arvojärjestelmäksi: miten oma arvoketju kytkeytyy
   toimittajien arvoketjuihin ylävirtaan ja jakelukanavan/asiakkaan
   arvoketjuihin alavirtaan.
7. Käytä tulosta kilpailuetuanalyysin pohjana: mitkä toiminnot kannattaa
   optimoida ja investoida, mitkä ulkoistaa, ja mitkä lopettaa kokonaan.

## Mitä tämä skilli EI tee

- Ei laske tarkkoja kustannus- tai katelukuja puolestasi — jäsentää mihin
  toimintoihin ne pitäisi kohdistaa ja mistä ne pitäisi hankkia.
- Ei tee lopullista kilpailustrategiavalintaa (kustannusjohtajuus vs.
  differointi) — tuottaa jäsennellyn pohjan päätökselle.
- Ei korvaa toimialakohtaista syväanalyysia — yleinen malli vaatii aina
  kontekstiin sovittamista.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, mistä arvoketjun kohdista useimmiten löytyy
  piilevä kilpailuetu eri toimialoilla
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  arvoketjukartta-template)
- referenssitapaukset / omat caset
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../layer-based-business-structuring/SKILL.md`
  — vaihtoehtoinen, kerrospohjainen tapa jäsentää sama liiketoiminta.
- Samassa pakissa seuraavaksi: `../category-definition-and-modeling/SKILL.md`
  — Mallintaa tuotteen tai liiketoiminnan suhteessa markkinakategorioihin.
- Liittyvä skilli toisessa pakissa (sama teoreettinen perhe):
  `../../../opportunity-recognition/skills/competitive-and-five-forces-mapping/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
