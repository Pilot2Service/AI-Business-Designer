# Business Model Canvas — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

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

## Vastuuvapaus tässä pakissa — canvas on ajattelutyökalu

Yleisen vastuuvapauden (`shared-guardrails.md`) lisäksi, tämän koko pakin ydinviesti
(`bmc-antipattern-and-misunderstanding-correction`) on että BMC EI korvaa
liiketoimintasuunnitelmaa, tuotespesifikaatiota tai taloudellista mallinnusta. Älä
esitä minkään tämän pakin skillin tuottamaa canvasia, patternsuositusta tai
diagnoosia valmiina liiketoimintapäätöksenä.

## Ei keksitä patterneja tai lähteitä

`bmc-innovation-pattern-matching`-skilli rajoittuu 159 patternin julkiseen
kirjastoon (`references/bmc-innovation-pattern-library.md`). Jos konteksti vaatisi
patternia jota kirjastossa ei ole, tunnista puute eksplisiittisesti — älä keksi
uutta patternia kirjaston nimissä äläkä anna sille valeteknistä `pattern_id`-polkua.

## Jaetut standardit

Katso `../../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
