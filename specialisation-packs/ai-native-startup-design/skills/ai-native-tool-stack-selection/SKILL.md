---
name: ai-native-tool-stack-selection
description: "Valitsee pienimmän toimivan AI-natiivin työkalupinon 12 kategorian päätöspuulla (ajattelukumppani, tutkimus, design, sovelluksen rakentaja, koodausagentti, hosting, backend, skillit, projektinhallinta, muistiinpanot, automaatio, agenttien rakentaminen) — kategoriapohjainen, ei tuotenimiin sidottu."
---

# AI-Native Tool Stack Selection

*Tila: `validated`, `source_layer: owner` — ks. `../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Auttaa pre-startup-founderia tai pientä tiimiä valitsemaan pienimmän
toimivan AI-natiivin työkalupinon ilman että hukkuu satojen työkalujen
markkinaan. Skilli jäsentää valinnan kategorioiden — ei tuotenimien —
kautta, koska kategoriat (mihin tarkoitukseen työkalua tarvitaan) kestävät
ajassa, mutta yksittäiset tuotteet ja niiden ominaisuudet vanhenevat
nopeasti tällä markkinalla.

## Perustuu

- Omistajan (Tommi Järvinen) AI-native Business Design -työpaja
  ([redacted] / firstkiss.co), `tools.md` — "2026 AI-Native Stack":
  12 kategorian jaottelu sen mukaan *mitä yrität tehdä*, ei valmistajan
  mukaan; "minimum viable stack" -periaate ("3–6 työkalua, ei 30");
  agenttityökalujen kolmiportainen kypsyyspolku (no-code-alustat →
  avoimen lähdekoodin ajonajat → kehittäjäkehykset).
- Ks. `../../references/tool-category-map.md` (12 kategoriaa esimerkein,
  aikaleimattu tilannekuva) ja `../../references/workshop-source.md`.

## Rakenne

1. **Käy läpi 12 kategoriaa** (ks. `../../references/tool-category-map.md`)
   ja tunnista, mitkä ovat OMAN casen kannalta tarpeellisia juuri nyt — ei
   kaikkia kerralla:
   1. AI-ajattelukumppani (yleinen chat/projekti-AI)
   2. Tutkimus ja tiedonhaku
   3. Design-luonnostelu
   4. Sovelluksen rakentaja (prompt → toimiva app)
   5. Koodausagentti (kun prototyypistä siirrytään tuotantoon)
   6. Versionhallinta / koodin säilytys
   7. Hosting ja julkaisu
   8. Backend ja tietokanta
   9. Skillit (agentin kykyjen paketointi ja uudelleenkäyttö)
   10. Projektinhallinta
   11. Kokous-/muistiinpanotyökalu (koneluettavaksi muuttaminen)
   12. Työnkulkujen automaatio ja agenttien rakentaminen
2. **Valitse kussakin tarpeellisessa kategoriassa yksi oletustyökalu.**
   Vastusta houkutusta ottaa montaa työkalua samaan kategoriaan
   samanaikaisesti — se hajottaa kontekstin ja hidastaa, ei nopeuta.
3. **Sovella minimipino-nyrkkisääntöä.** Tyypillinen toimiva pre-startup-
   pino on 3–6 työkalua, ei 30. Aloita minimillä: ajattelukumppani +
   tutkimus + design-luonnos + sovelluksen rakentaja + koodin säilytys.
   Lisää kategorioita vasta kun aito tarve syntyy, ei ennakoivasti.
4. **Kun tiimi tai tarve kasvaa:** lisää projektinhallinta ja
   kokousmuistiinpanotyökalu vasta kun useampi ihminen työskentelee
   samassa asiassa säännöllisesti — ei heti alussa.
5. **Kun ensimmäinen työnkulku on todistetusti arvokas ja aidosti
   closed-loop-muotoinen** (ks.
   `../closed-loop-process-and-human-oversight-design/SKILL.md`): harkitse
   sen kääriimistä agentiksi. Aloita no-code-agenttialustalla; siirry
   avoimen lähdekoodin ajonaikaan tai kehittäjäkehykseen vasta kun
   tekninen osaaminen ja aito tarve sitä vaativat — ei oletuksena.
6. **Tarkista lock-in ennen sitoutumista.** Mihin infraan (tietokanta,
   hosting) työkalu sitoo sinut, ja onko koodi/data vietävissä pois
   tarvittaessa? Prototyypille tämä ei useinkaan merkitse paljon;
   skaalattavaksi tarkoitetulle tuotteelle se merkitsee paljon.
7. **Muista, että tämä on tilannekuva.** Työkalulistat, hinnoittelu ja
   ilmaiskiintiöt muuttuvat viikoittain tällä markkinalla. Tarkista aina
   työkalun senhetkinen tila ennen sitoutumista — älä nojaa
   `../../references/tool-category-map.md`:n esimerkkeihin nimiltä
   ajan tasalla olevana totuutena.

## Mitä tämä skilli EI tee

- Ei suosittele tiettyjä tuotenimiä pysyvänä totuutena — kategoriat ja
  valintaperiaate kestävät, yksittäiset tuotteet vanhenevat nopeasti (ks.
  `../../references/tool-category-map.md` aikaleima).
- Ei tee teknistä due diligenceä työkalun tietoturvasta, sopimusehdoista
  tai skillien/agenttien turvallisuudesta — tarkista erikseen ennen
  liiketoimintakriittistä käyttöä; asenna skillejä/agentteja vain
  luotetuista lähteistä.
- Ei arvioi, mitä kehittäjäkehystä (LangGraph, CrewAI, Claude Agent SDK
  jne.) kehittäjätiimin kannattaa valita tuotantokoodiin — se on
  kehittäjätiimin päätös; tämä skilli vain kontekstoi founderille mistä
  on kyse ennen sitä keskustelua.

## Jatka tästä

- Liittyvä skilli samassa pakissa: `../ai-buildable-prd-writing/SKILL.md`
  (kenelle PRD annetaan rakennettavaksi),
  `../closed-loop-process-and-human-oversight-design/SKILL.md` (milloin
  kannattaa siirtyä agentteihin).
- Liittyvä skilli toisessa pakissa:
  `../../../../ai-strategy-and-governance/skills/build-vs-buy-vs-partner-ai/SKILL.md`
  — isomman mittakaavan build/buy/partner-päätös; tämä skilli on
  kevyempi, taktinen valinta pre-startup-vaiheeseen.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/tool-category-map.md` — 12 kategoriaa esimerkein
  (aikaleimattu tilannekuva)
- `../../references/workshop-source.md` — lähdetiedot
- `../../CLAUDE.md` — pakin jaetut suojaukset
