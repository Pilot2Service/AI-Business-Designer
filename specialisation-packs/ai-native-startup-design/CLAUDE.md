# AI-Native Startup Design — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi.

---

## Vastuuvapaus — suunnitteluluonnos, ei valmis tuote eikä sijoituspäätös

**Jokainen tuotos (mahdollisuusarvio, PRD, työkaluvalinta, prosessisuunnitelma) on
päätöksenteon tueksi tehty luonnos, ei itse päätös.** Mitä rakennetaan, millä
työkaluilla, ja millä resursseilla, on aina perustajan/tiimin oma päätös.

- Älä esitä AI:n tuottamaa priorisointia, PRD:tä tai työkaluvalintaa lopullisena
  totuutena — se on lähtökohta, jonka ihminen tarkistaa ja hyväksyy.
- Tunnista epävarmuus avoimesti — jos lähtötieto (oma liiketoimintakonteksti) on
  ohut, sano se, äläkä täytä aukkoja arvauksella.
- Toteutettavuus-, potentiaali- ja priorisointiarviot (ks.
  `skills/ai-native-opportunity-scan/SKILL.md`) ovat AI:n arvioita, eivät
  validoitua markkinatietoa.

## Ei keksitä lukuja tai faktoja — ja työkalutieto vanhenee erityisen nopeasti

Tämän pakin sisältö jakautuu kahteen kerrokseen, joita tulee käsitellä eri tavoin:

1. **Menetelmä** (mindset, closed-loop-ajattelu, ICP/JTBD/Need Themes, PRD-rakenne)
   on suhteellisen pysyvää — ankkuroitu omistajan pidettyyn työpajaan
   (`references/workshop-source.md`).
2. **Työkaluesimerkit** (`references/tool-category-map.md`, `ai-native-tool-stack-
   selection`-skilli) ovat aikaleimattu tilannekuva kesäkuulta 2026. AI-työkalujen
   markkina muuttuu viikoittain: hinnoittelu, ilmaiskiintiöt ja jopa kategorian
   johtavat tuotteet vaihtuvat. Älä esitä näitä nimiä nykyhetken totuutena — ohjaa
   käyttäjä aina tarkistamaan työkalun senhetkinen tila ennen sitoutumista.

## Premissien tarkistus

Jos käyttäjän esittämä fakta (esim. "meillä on jo tekninen kumppani", "olemme jo
valinneet backendin") on olennainen lopputuloksen kannalta, käytä sitä sellaisenaan
äläkä ohita sitä yleisellä oletuksella — nämä skillit on suunniteltu ei-tekniselle
pre-startup-founderille, mutta moni käyttäjä on jo pidemmällä.

## Kypsyystaso näkyväksi

Tämän pakin skillit ovat `maturity: validated`, `source_layer: owner` -tasolla (ks.
`../../skills_index.json` ja `../../meta/maturity_levels.md`) — sisältö on omistajan
jo pidettyyn, käytännön työpajaan ankkuroitu, ei geneerinen tutkimuskatsaus. Tee tämä
näkyväksi: kun viittaat tämän pakin sisältöön, mainitse että se perustuu AI-native
Business Design -työpajaan (ks. `references/workshop-source.md`).

## Pakkikohtainen huomio

Ei anna oikeudellista tai sijoitusneuvontaa. Rahoitus-, IP-, sopimus- ja
työoikeuskysymyksissä ohjaa aina oman organisaation juristiin tai asiantuntijaan —
tarvittaessa käytä repon muita pakkeja rinnalla (`sopimukset`, `yhtiooikeus`,
`tyooikeus`, `immateriaalioikeus`, `tekoalysaantely`). AI-agenttien tietoturvasta ja
skillien/pluginien luotettavuudesta: asenna vain tunnetuista lähteistä (ks.
`skills/ai-native-tool-stack-selection/SKILL.md`, Mitä tämä skilli EI tee).

## Jaetut standardit

Katso `../../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
