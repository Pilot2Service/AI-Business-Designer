---
name: shadow-ai-response-and-safe-adoption
description: "Tunnistaa organisaatiossa jo tapahtuvan luvattoman/epävirallisen AI-työkalujen käytön (Shadow AI) ja korvaa sen turvallisilla, skaalautuvilla virallisilla ratkaisuilla, joille on laskettu selkeä ROI."
---

# Shadow AI Response & Safe Adoption

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Kartoittaa työntekijöiden jo tapahtuvan, ilman virallista hyväksyntää
tapahtuvan AI-työkalujen käytön ("Shadow AI"), ymmärtää mitä aitoa tarvetta
se ratkaisee, ja rakentaa sille turvallinen, skaalautuva ja selkeällä
ROI:lla perusteltu virallinen vastine — kieltämisen sijaan tai sen ohella.

## Ankkurointi tutkimukseen

- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — Shadow AI -käsite nostettu esiin osana nopean
  AI-business case -rakentamisen menetelmää.
- Yleinen "Shadow IT" -kirjallisuus ja -käytäntö, laajennettuna
  AI-työkalujen kontekstiin.

## Rakenne (luonnos — täydennettävä)

1. Kartoita Shadow AI:n laajuus: mitä AI-työkaluja työntekijät jo
   käyttävät ilman virallista hyväksyntää tai näkyvyyttä (kyselyt,
   käyttödata, IT-lokit jos saatavilla).
2. Erittele käyttötapaukset syyn mukaan: mitä aitoa tarvetta epävirallinen
   käyttö ratkaisee — nopeus, puuttuva virallinen työkalu, byrokratian
   kiertäminen?
3. Arvioi riski jokaisessa löydetyssä käyttötapauksessa: tietoturva,
   tietosuoja (GDPR), IP-vuoto, virheellisen tiedon leviäminen,
   sääntelyriski (ks. `../responsible-ai-and-governance-check/SKILL.md`).
4. Älä lähde oletuksesta "kiellä kaikki" — arvioi kussakin tapauksessa:
   onko nopein turvallinen reitti kieltäminen, ohjeistaminen, vai
   virallisen vastineen rakentaminen?
5. Priorisoi käyttötapaukset, joissa epävirallinen käyttö on laajaa ja
   arvokasta: näille rakennetaan virallinen, turvallinen ja skaalautuva
   vastine ensin.
6. Laske jokaiselle viralliselle vastineelle selkeä ROI (säästetty
   aika/kustannus vs. käyttöönotto- ja ylläpitokustannus) — sama kuri kuin
   muissakin AI-investoinneissa (ks.
   `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`).
7. Viesti muutos työntekijöille avoimesti: miksi virallinen työkalu on
   parempi vaihtoehto, ei vain kielto (ks.
   `../../../change-and-communication/skills/stakeholder-communication-plan/SKILL.md`).
8. Rakenna kevyt jatkuva seuranta, joka tunnistaa uusia Shadow AI
   -käyttötapauksia ajan myötä — tämä ei ole kertaluonteinen projekti.

## Mitä tämä skilli EI tee

- Ei ole tietoturva-auditointi eikä korvaa IT-/tietoturvaosaston teknistä
  kartoitusta — jäsentää liiketoiminnallisen vastauksen.
- Ei oleta että kaikki epävirallinen käyttö on haitallista — monessa
  tapauksessa se paljastaa aidon, jo validoidun tarpeen jota kannattaa
  hyödyntää, ei vain tukahduttaa.
- Ei tee lopullista työkalu- tai politiikkapäätöstä puolestasi.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, milloin Shadow AI kannattaa virallistaa vs.
  milloin se pitää sulkea pois
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  Shadow AI -kartoituskysely)
- referenssitapaukset / omat caset onnistuneesta Shadow AI:n
  virallistamisesta
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa: `../responsible-ai-and-governance-check/SKILL.md`,
  `../ai-capability-roadmap/SKILL.md` (viralliset vastineet osaksi
  roadmapia).
- Liittyvä skilli toisessa pakissa:
  `../../../change-and-communication/skills/stakeholder-communication-plan/SKILL.md`,
  `../../../specialisation-packs/ai-native-startup-design/skills/ai-native-tool-stack-selection/SKILL.md`
  (mistä virallinen vastine valitaan).
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
