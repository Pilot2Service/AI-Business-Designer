# Business Design Frameworks — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Tämä pakki on avoin kokoelma — ei suljettu lista

Toisin kuin muut ydinpakit, tämä pakki on suunniteltu **kasvamaan jatkuvasti**.
Se kokoaa yhteen erilaisia tapoja jäsentää ja mallintaa liiketoimintaa, arvonluontia,
arvoketjuja ja asemointia — kerrosmallit, arvoketjuanalyysi, kategoriamallinnus ja
myöhemmin lisättävät uudet jäsentämistavat. Kun uusi skilli lisätään tähän pakkiin:

- Se saa oman `skills/<skill-id>/SKILL.md`-tiedoston samaa minimifrontmatter-mallia
  noudattaen (`name` + `description`, ei muuta).
- Se lisätään tämän pakin `README.md`:n skillitaulukkoon ja tarvittaessa
  ristiinlinkitetään muihin saman pakin skilleihin ("Jatka tästä").
- Sen kypsyys (`maturity`) alkaa oletuksena `scaffold`-tasolta, ellei kyseessä ole
  käyttäjän oma validoitu menetelmä (kuten esim. research-commercialisation-pakin
  tai opportunity-recognition-pakin owner-skillit).

## Vastuuvapaus tässä pakissa — jäsennystapa, ei valmis analyysi

Yleisen vastuuvapauden (`shared-guardrails.md`) lisäksi: nämä ovat ajattelun
apuvälineitä (mental models). Älä esitä mallinnuksen tulosta lopullisena totuutena
tai ainoana oikeana jäsennyksenä — useampi malli voi tuottaa erilaisia, yhtä
valideja näkökulmia samaan liiketoimintaan.

## Kypsyystaso tässä pakissa

Tämän pakin kypsyystaso on **sekoitettu** (ks. `../skills_index.json` ja
`../meta/maturity_levels.md`):

- `layer-based-business-structuring`, `value-chain-mapping`,
  `category-definition-and-modeling` ovat `maturity: scaffold` — rakenne ja
  ankkurointi ovat tutkimuspohjaisia (klassisia liiketoiminnan
  viitekehyksiä), mutta omaa validoitua kokemusta ei vielä ole liitetty.
- `strategy-canvas-and-value-curve` on `maturity: validated`,
  `source_layer: owner` — Blue Ocean Strategy -teoria yhdistettynä
  omistajan tuotteistettuun 360 Comparison Factors -vertailutyökaluun.

## Pakkikohtainen huomio

Nämä ovat yleisiä, toimialariippumattomia jäsentämismalleja — ne pitää aina sovittaa
kontekstiin. Älä pakota liiketoimintaa väkisin johonkin malliin, jos se ei tuota
oivallusta; kokeile toista mallia samasta kokoelmasta tai yhdistä useampaa.

Tämän pakin `competitive-blind-spot-scanner`-agentti (ks. `agents/`) etsii minkä
tahansa kilpailu-/asemointianalyysin katvealueet — toimii sekä tämän pakin
`strategy-canvas-and-value-curve`-tuotoksen että esim. `opportunity-recognition`-pakin
`competitive-and-five-forces-mapping`-tuotoksen päällä. Käytä sitä ennen kuin
kilpailutilanne-analyysi esitetään valmiina kuvana toimialasta.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
