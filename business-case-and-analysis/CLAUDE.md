# Business Case & Analysis — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Kypsyystaso tässä pakissa

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia, mutta omaa validoitua kokemusta ei vielä ole liitetty.

## Pakkikohtainen huomio

Ei korvaa talousosaston/controllerin virallista laskentaa — ROI/NPV-luvut ovat
päätöksenteon tukena, viralliseen käyttöön tarvitaan vahvistus.

Tämän pakin `assumption-stress-tester`-agentti (ks. `agents/`) on tarkoitettu
käytettäväksi ennen kuin business case viedään päätöksentekoon — se haastaa
oletukset adversariaalisesti, mutta ei korvaa kohdan 1 (`shared-guardrails.md`)
ihmisen hyväksyntää.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
