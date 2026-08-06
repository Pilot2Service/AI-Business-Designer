# Business Model Canvas — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi.

---

## Tämä pakki on kaksikerroksinen — tee kerros näkyväksi joka kerta

Tämän pakin seitsemästä skillistä **kolme on `validated`/`owner`-tasoa** (suoraan
omistajan huhtikuun 2026 konsultointihaastattelusta, omistajan tutkimuskerroksen
asiantuntijakerros) ja **neljä on `scaffold`/`research`-tasoa** (tunnettujen BMC-
lähteiden — Jeffries, Williams, van der Linden, Blank/Strategyzer, Ash Maurya —
esitäytetty synteesi, jota omistaja ei ole vielä validoinut omalla kokemuksellaan).

| Skilli | Taso |
|---|---|
| `bmc-innovation-pattern-matching` | `validated` / `owner` |
| `bmc-canvas-clarity-and-iteration` | `validated` / `owner` |
| `bmc-antipattern-and-misunderstanding-correction` | `validated` / `owner` |
| `bmc-session-facilitation-design` | `scaffold` / `research` |
| `bmc-canvas-diagnostic-reading` | `scaffold` / `research` |
| `bmc-tool-switching-decisions` | `scaffold` / `research` |
| `bmc-client-language-translation` | `scaffold` / `research` |

**Kun käytät `scaffold`-tason skilliä, sano se ääneen.** Älä esitä
tutkimuskerroksen sisältöä ("van der Linden suosittelee...") omistajan omana,
käytännössä testattuna näkemyksenä. Kun kaksi skilliä käsittelevät samaa aihetta eri
tasoilta (esim. canvasin valmiuskriteerit: `bmc-canvas-clarity-and-iteration` omistajan
oma vs. `bmc-canvas-diagnostic-reading` tutkimuskerroksen laajempi rubriikki),
priorisoi `validated`/`owner`-skilliä ja käytä `scaffold`-skilliä täydentävänä, et
korvaavana lähteenä — ks. `../../meta/maturity_levels.md`: "canonical > validated >
draft > scaffold".

## Ristiriitatilanteessa asiantuntijakerros voittaa

omistajan tutkimuskerroksen oma sääntö (`AGENT_GUIDE.md`): kun tutkimuskerros ja
asiantuntijakerros ovat eri linjoilla samasta aiheesta, asiantuntijakerros voittaa.
Tämä pakki noudattaa samaa periaatetta: jos `scaffold`-skillin tutkimuspohjainen
ohje on ristiriidassa `validated`-skillin omistajan oman näkemyksen kanssa, käytä
`validated`-skilliä.

## Vastuuvapaus — canvas on ajattelutyökalu, ei valmis liiketoimintasuunnitelma

Tämän koko pakin ydinviesti (`bmc-antipattern-and-misunderstanding-correction`) on
että BMC EI korvaa liiketoimintasuunnitelmaa, tuotespesifikaatiota tai taloudellista
mallinnusta. Älä esitä minkään tämän pakin skillin tuottamaa canvasia, pattern­
suositusta tai diagnoosia valmiina liiketoimintapäätöksenä — se on aina päätöksen­
teon tukena oleva luonnos, jonka ihminen tarkistaa.

## Ei keksitä patterneja tai lähteitä

`bmc-innovation-pattern-matching`-skilli rajoittuu 159 patternin julkiseen
kirjastoon (`references/bmc-innovation-pattern-library.md`). Jos konteksti vaatisi
patternia jota kirjastossa ei ole, tunnista puute eksplisiittisesti — älä keksi
uutta patternia kirjaston nimissä äläkä anna sille valeteknistä `pattern_id`-polkua.

## Jaetut standardit

Katso `../../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
