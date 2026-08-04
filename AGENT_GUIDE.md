---
id: meta.agent_guide.001
title: Agent Guide
status: canonical
---

# Agent Guide — AI Business Designer Skills

Tämä tiedosto on kirjoitettu **agenteille** (Claude Code, Cowork, muut skill-yhteensopivat
agentit), jotka käyttävät tätä pakkia kontekstina liiketoiminta-analyysi-, strategia- tai
AI-strategiatehtävässä. Pakkikohtaiset `CLAUDE.md`-tiedostot täydentävät tätä
skillikohtaisilla suojauksilla — lue molemmat.

## 1. Mikä tämä on

Skills-pack, ei valmis vastaus. Jokainen SKILL.md opettaa yhden tarkkarajaisen
tekniikan ja kertoo, mihin akateemiseen tai ammatilliseen kehykseen se ankkuroituu.

## 2. Kaksi ohjaustasoa

1. **`<pack>/skills/<skilli>/SKILL.md`** — mitä tehdään, vaihe vaiheelta. Kapea,
   tehtäväkohtainen.
2. **`<pack>/CLAUDE.md`** — pakin jaetut suojaukset: vastuuvapaus, ei keksittyjä lukuja,
   premissien tarkistus, kypsyystason näkyväksi tekeminen. Luetaan aina ennen skilliä.

## 3. Kypsyys ja luotettavuus — lue skills_index.json, ei frontmatteria

SKILL.md-frontmatter sisältää **vain** `name` ja `description` (Claude Skill -formaatin
vakiokentät). Kypsyys, lähdekerros ja se, tarvitaanko vielä omistajan omaa syötettä, ovat
`skills_index.json`:ssa:

| Kenttä | Arvot | Merkitys agentille |
|---|---|---|
| `maturity` | `scaffold` / `draft` / `validated` / `canonical` | Kuinka paljon tähän kannattaa nojata itsenäisenä totuutena |
| `source_layer` | `research` / `owner` / `derived` | `research` = julkinen kehys. `owner` = omistajan validoitu kokemus, arvokkain. |
| `owner_input_needed` | `true` / `false` | Jos `true`, tekniikka on vasta runko |

**Luottamushierarkia:** `canonical` > `validated` > `draft` > `scaffold`.

## 4. Mitä tehdä kun skilli on `maturity: scaffold`

Suurin osa tämän pakin skilleistä on scaffold-tasolla: rakenne ja ankkurointi ovat
luotettavia, mutta `[OWNER INPUT]`-osio ei vielä sisällä omistajan omaa kokemusta.

1. Käytä rakennetta ja ankkurointia normaalisti.
2. Älä kuvittele omistajan henkilökohtaista kokemusta, heuristiikkaa tai case-esimerkkiä.
   Sano ääneen, että tämä osa puuttuu.
3. Jatka sillä mitä on saatavilla, mutta tee epävarmuus näkyväksi.

## 5. Miten pakkia haetaan (retrieval)

Älä lataa koko repoa kerralla. Käytä `skills_index.json`-tiedostoa valitaksesi 2–5
relevanteinta skilliä. Lue kyseisen pakin `CLAUDE.md` samalla.

## 6. Tehtäväpohjainen navigointi

| Tehtävätyyppi | Ensisijainen pakki |
|---|---|
| Liiketoimintamahdollisuuden tunnistus/arviointi | `opportunity-recognition` |
| ROI/riskiperustelu investoinnille | `business-case-and-analysis` |
| AI-käyttötapausten priorisointi | `ai-strategy-and-governance` |
| Johdon esitys / muutosviestintä | `change-and-communication` |
| Isomman ongelman jäsentäminen | `strategic-thinking` |
| Monivaiheinen tehtävä | `playbooks/` — valmis skilliketju |

## 7. Mitä agentti ei saa tehdä

- Ei täytä `[OWNER INPUT]`-osioita geneerisellä tai kuvitellulla sisällöllä
- Ei lisää uusia kenttiä SKILL.md-frontmatteriin (vain `name`+`description` sallittu)
- Ei kohtele `scaffold`-tason sisältöä yhtä auktoritatiivisena kuin `validated`/`canonical`
- Ei sekoita tätä pakkia valmiiksi vastaukseksi — se on konteksti oman osaamisen päälle
