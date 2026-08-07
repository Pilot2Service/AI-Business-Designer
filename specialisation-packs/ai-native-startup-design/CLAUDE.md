# AI-Native Startup Design — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Vastuuvapaus tässä pakissa — ei sijoituspäätöstä

Yleisen vastuuvapauden (`shared-guardrails.md`) lisäksi: mitä rakennetaan, millä
työkaluilla, ja millä resursseilla, on aina perustajan/tiimin oma päätös.
Toteutettavuus-, potentiaali- ja priorisointiarviot (ks.
`skills/ai-native-opportunity-scan/SKILL.md`) ovat AI:n arvioita, eivät validoitua
markkinatietoa.

## Ei keksitä lukuja tai faktoja — ja työkalutieto vanhenee erityisen nopeasti

Yleisen periaatteen lisäksi, tämän pakin sisältö jakautuu kahteen kerrokseen, joita
tulee käsitellä eri tavoin:

1. **Menetelmä** (mindset, closed-loop-ajattelu, ICP/JTBD/Need Themes, PRD-rakenne)
   on suhteellisen pysyvää — ankkuroitu omistajan pidettyyn työpajaan
   (`references/workshop-source.md`).
2. **Työkaluesimerkit** (`references/tool-category-map.md`, `ai-native-tool-stack-
   selection`-skilli) ovat aikaleimattu tilannekuva kesäkuulta 2026. AI-työkalujen
   markkina muuttuu viikoittain: hinnoittelu, ilmaiskiintiöt ja jopa kategorian
   johtavat tuotteet vaihtuvat. Älä esitä näitä nimiä nykyhetken totuutena — ohjaa
   käyttäjä aina tarkistamaan työkalun senhetkinen tila ennen sitoutumista.

## Premissien tarkistus tässä pakissa

Jos käyttäjän esittämä fakta (esim. "meillä on jo tekninen kumppani", "olemme jo
valinneet backendin") on olennainen lopputuloksen kannalta, käytä sitä sellaisenaan
äläkä ohita sitä yleisellä oletuksella — nämä skillit on suunniteltu ei-tekniselle
pre-startup-founderille, mutta moni käyttäjä on jo pidemmällä.

## Kypsyystaso tässä pakissa — kaksitasoinen

Kaikki tämän pakin skillit ovat `source_layer: owner` (ks.
`../../skills_index.json` ja `../../meta/maturity_levels.md`), mutta pakissa on
KAKSI eri kypsyystasoa riippuen siitä kumpaan lähteeseen skilli perustuu:

- **`maturity: validated`** — `ai-native-opportunity-scan`,
  `customer-vision-to-jtbd`, `ai-buildable-prd-writing`,
  `closed-loop-process-and-human-oversight-design`,
  `ai-native-tool-stack-selection`. Perustuvat omistajan USEALLE
  OSALLISTUJALLE pitämään AI-native Business Design -työpajaan
  (ks. `references/workshop-source.md`).
- **`maturity: draft`** — `ai-differentiator-solution-ideation`,
  `rice-scoring-and-mvp-synthesis`, `ai-native-conversational-os-design`.
  Perustuvat ulkopuolisen työpajan menetelmään, jonka omistaja on toistaiseksi
  soveltanut vain KERRAN, yhteen omaan caseen (omistajan Decision Coach — ks.
  `references/ai-first-saas-workshop-source.md` ja
  `cases/ai-decision-coach-mvp-case.md`). Ei vielä laajasti validoitu.

Tee tämä näkyväksi käytössä: kun viittaat `draft`-tason skilliin, mainitse
että menetelmä on sovellettu vain kerran eikä vielä yhtä laajasti
testattu kuin pakin `validated`-skillit. Kun viittaat mihin tahansa tämän
pakin sisältöön, mainitse mihin työpajaan/lähteeseen se perustuu.

## Pakkikohtainen huomio

Ei anna oikeudellista tai sijoitusneuvontaa. Rahoitus-, IP-, sopimus- ja
työoikeuskysymyksissä ohjaa aina oman organisaation juristiin tai asiantuntijaan —
tarvittaessa käytä rinnalla erillistä juridista, yhtiöoikeudellista, työ-
oikeudellista, immateriaalioikeudellista tai AI-sääntely-asiantuntemusta
(näitä ei sisälly tähän skills-pakkiin). AI-agenttien tietoturvasta ja
skillien/pluginien luotettavuudesta: asenna vain tunnetuista lähteistä (ks.
`skills/ai-native-tool-stack-selection/SKILL.md`, Mitä tämä skilli EI tee).

## Jaetut standardit

Katso `../../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
