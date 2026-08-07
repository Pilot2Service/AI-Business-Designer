# Opportunity Recognition — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Kypsyystaso tässä pakissa

Tämän pakin kypsyystaso on **sekoitettu** (ks. `../skills_index.json` ja
`../meta/maturity_levels.md`):

- `market-and-signal-scanning`, `pattern-and-analogy-connector`,
  `opportunity-evaluation-and-judgment`, `market-sizing-tam-sam-som`,
  `competitive-and-five-forces-mapping` ovat `maturity: scaffold` — rakenne ja
  ankkurointi ovat tutkimuspohjaisia, mutta omaa validoitua kokemusta ei vielä
  ole liitetty.
- `opportunity-intake-elicitation`, `opportunity-value-assessment` ja
  `opportunity-brief-writing` ovat `maturity: validated`, `source_layer: owner`
  — konvertoitu suoraan omistajan oman palvelun tuotteistetusta
  Opportunity Value Assessment -metodologiasta.

## Pakkikohtainen huomio

Ei korvaa toimialan syvällistä asiantuntemusta — nostaa esiin mahdollisuuksia
arvioitavaksi, ei takaa niiden toteutuskelpoisuutta.

Tämän pakin `market-sizing-cross-validator`-agentti (ks. `agents/`) ristiintarkistaa
`market-sizing-tam-sam-som`-skillin tuottaman laskelman ennen kuin lukua käytetään
business casessa tai esitetään johdolle — ks. myös `../meta/external-data-mcp.md`
valinnaisista ulkoisista datalähteistä joita agentti voi hyödyntää jos ne on
kytketty.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
