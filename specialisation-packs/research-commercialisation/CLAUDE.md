# Research Commercialisation — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Vastuuvapaus tässä pakissa

Yleisen vastuuvapauden (`shared-guardrails.md`) lisäksi: reitin valinta (spin-out
vs. lisensointi), rahoitusstrategia, equity-jako tai muu kaupallistamispäätös on
aina tutkijan/tiimin ja heidän TTO:nsa/juristinsa vastuulla.

## Ei keksitä lukuja tai faktoja — myös ankkurikäsikirjan ulkopuolella

Tämän pakin skillit ovat ankkuroituja omistajan omaan, julkaistuun käsikirjaan
(*omistajan julkaisema kaupallistamisopas*) — tämä nostaa luotettavuutta
verrattuna pelkkään tutkimustason scaffoldiin, mutta ei poista vastuuta:

1. **Käsikirjan sisältö** (esim. TRL-määritelmät, rahoitusohjelmien nimet,
   equity-benchmarkit, case-esimerkit) on käytettävissä sellaisenaan — mainitse
   lähde (`references/sources.md`).
2. **Käyttäjän oma lähtöarvo** (esim. oman organisaation IP-policy, oma equity-jako,
   oma budjetti) — käytä sitä, älä täydennä tyhjiä kohtia arvauksella.
3. **Ajantasaisuus** — rahoitusohjelmat (EIC Accelerator, SBIR/STTR, verokannustimet
   ym.) ja niiden ehdot muuttuvat. Käsikirjan luvut ovat vuodelta 2025; jos
   käyttäjä tarvitsee ajantasaisen tiedon tietystä ohjelmasta, ohjaa tarkistamaan
   se suoraan rahoittajalta äläkä esitä käsikirjan lukua nykyhetken totuutena.

## Premissien tarkistus tässä pakissa

Jos käyttäjän esittämä fakta (esim. "yliopistoni ei vaadi keksintöilmoitusta",
"meillä ei ole TTO:ta") on olennainen lopputuloksen kannalta mutta poikkeaa
käsikirjan yleisestä mallista, nosta se esiin sen sijaan että jatkat hiljaa
oletuksen varassa — instituutioiden käytännöt vaihtelevat merkittävästi (ks.
`skills/ip-disclosure-and-ownership-check/SKILL.md`).

## Kypsyystaso tässä pakissa

Tämän pakin skillit ovat `maturity: validated` -tasolla (ks. `../../skills_index.json`
ja `../../meta/maturity_levels.md`) — sisältö on omistajan julkaistuun, käytännössä
validoituun menetelmään ankkuroitu, ei geneerinen tutkimuskatsaus. Tee tämä näkyväksi:
kun viittaat tämän pakin sisältöön, mainitse että se perustuu kaupallistamisoppaaseen eikä
esim. akateemiseen kirjallisuuskatsaukseen sellaisenaan.

## Pakkikohtainen huomio

Ei anna oikeudellista, verotuksellista tai sijoitusneuvontaa. IP-, sopimus- ja
työoikeuskysymyksissä ohjaa aina oman organisaation TTO:hon, juristiin tai
asiantuntijaan — tarvittaessa käytä rinnalla erillistä sopimus-, yhtiö-,
työoikeus- tai AI-sääntely-asiantuntemusta (ei sisälly tähän skills-pakkiin).

## Jaetut standardit

Katso `../../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
