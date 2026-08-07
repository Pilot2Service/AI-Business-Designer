# AI Strategy & Governance — jaetut suojaukset

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

Ei korvaa juridista EU AI Act -compliance-arviota — syvempään analyysiin tarvitaan
erillinen sääntely-asiantuntemus.

Tässä pakissa on useita samankaltaisia kolmi-/nelijaotteluja, jotka
vastaavat ERI kysymyksiin — älä sekoita niitä keskenään:

- **Automate/Augment/Human-Only** (`task-level-decomposition-and-
  automation-fit`) — vastaa "sopiiko TÄMÄ TEHTÄVÄ AI:lle ja millä
  tasolla".
- **Quick Wins/Strategic Bets/Hard-Low Value/Deprioritize**
  (`ai-opportunity-portfolio`) — vastaa "kannattaako TÄMÄ MAHDOLLISUUS
  ja onko se helppo toteuttaa".
- **Deploy/Reshape/Invent** (`ai-opportunity-portfolio`) — vastaa
  "kuinka SYVÄLLE organisaatiota tämän toteutus koskettaa".
- **Horisontti 1/2/3** (`ai-capability-roadmap`) — vastaa "MILLOIN tämä
  toteutetaan".

Kun viittaat johonkin näistä, käytä oikeaa termiä äläkä käytä niitä
toistensa synonyymeinä — ne korreloivat mutta eivät ole sama luokitus.

Raakalistan kokoamiseen on kaksi täydentävää, EI kilpailevaa, lähestymistapaa
— älä esitä toista "parempana" ilman kontekstia:

- **Bottom-up** (`task-level-decomposition-and-automation-fit`) — käydään
  olemassa oleva prosessi läpi tehtävä kerrallaan. Vahva kun prosessi on jo
  tarkasti kuvattu.
- **Top-down** (`ai-capability-pattern-matching`) — esitetään valmiin
  kyvykkyyspatternikirjaston (`references/ai-capability-pattern-library.md`)
  diagnostiset kysymykset ennen tarkkaa prosessikuvausta. Nopeampi
  ensimmäinen kartoitus, vaatii validoinnin ennen pisteytystä.

Tämän pakin `ai-initiative-readiness-auditor`-agentti (ks. `agents/`) auditoi
`ai-opportunity-portfolio`-skillin 5 ulottuvuutta ja `responsible-ai-and-
governance-check`-tarkistuslistaa vasten ennen kuin aloite viedään hyväksyntään —
se ei korvaa yllä mainittua juridista compliance-arviota.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
