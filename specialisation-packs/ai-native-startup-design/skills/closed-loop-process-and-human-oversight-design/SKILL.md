---
name: closed-loop-process-and-human-oversight-design
description: "Jäsentää liiketoimintaprosessit avoimiksi tai suljetuiksi silmukoiksi (open/closed loop) ja päättää ihmisen roolin (in-the-loop / on-the-loop / outside-the-loop) kussakin — mentaalimalli AI-agenttien vastuualueiden suunnitteluun."
---

# Closed-Loop Process & Human Oversight Design

*Tila: `validated`, `source_layer: owner` — ks. `../../../skills_index.json` ja
`../../../meta/maturity_levels.md`.*

## Tarkoitus

Auttaa näkemään liiketoiminnan prosessien kokoelmana, joista osa on
"avoimia silmukoita" (suoritetaan, ei opita) ja osa voisi olla "suljettuja
silmukoita" (suoritetaan, mitataan, säädetään automaattisesti seuraavalla
kierroksella). Skilli antaa kielen ja päätöskehyksen sille, mitkä prosessit
kannattaa suunnitella suljetuiksi silmukoiksi, ja missä kohtaa ihmisen
tulee pysyä mukana päätöksenteossa — kolmiportaisella
in-the-loop/on-the-loop/outside-the-loop-mallilla.

## Perustuu

- Omistajan (Tommi Järvinen) AI-native Business Design -työpaja
  ([redacted] / firstkiss.co), pidetty 1.–2.6.2026, Day 1 —
  Session 1 "AI as the operating system your company runs on": avoin
  silmukka (Input → Execution → Output, ei systemaattista palautetta) vs.
  suljettu silmukka (Input → Execution → Output → Feedback → Adjustment →
  takaisin Inputiin); ydinajatus "yrityksesi ei ole yksi suljettu silmukka
  — sen pitäisi olla joukko suljettuja silmukoita", kukin agenttien
  ajamana ja orkestroituna yhteen.
- Human-in-the-loop / human-on-the-loop / human-outside-the-loop
  -kolmijako ihmisen valvonnan tasosta AI-prosessissa.
- Agentti-, orkestrointi- ja työkalu-/agenttirekisterikäsitteet, sellaisina
  kuin työpaja ne esittää.

## Rakenne

1. **Valitse tarkasteltava prosessi.** Esim. tilausten käsittely,
   asiakastuki, sisällöntuotanto, laadunvarmistus, myynnin seuranta.
2. **Piirrä prosessi nykytilassa.** Onko se avoin silmukka — Input →
   Execution → Output ilman systemaattista palautetta, joka muuttaisi
   seuraavaa kierrosta — vai onko siinä jo osittainen palautemekanismi?
   Useimmat yritykset ja useimmat osat yrityksistä toimivat avoimina
   silmukoina: opittu tieto valuu pois joka kierroksella sen sijaan että
   se parantaisi seuraavaa.
3. **Suunnittele suljettu silmukka.** Lisää Feedback- ja Adjustment-
   vaiheet: Input → Execution → Output → Feedback → Adjustment → (takaisin
   Inputiin). Suljettu silmukka on itsesäätelevä — se tarkkailee omaa
   tulostaan ja säätää toimintaansa pitääkseen tavoitteen saavutettuna.
4. **Anna silmukalle selkeä, mitattava tavoite.** Suljettu silmukka
   toimii vain, jos se tietää mitä sen pitää saavuttaa ja pystyy
   mittaamaan edistymistä sitä kohti.
5. **Päätä ihmisen sijainti suhteessa silmukkaan** kolmesta
   vaihtoehdosta:
   - **Human-in-the-loop** — ihminen tarkistaa/hyväksyy jokaisen askeleen
     ennen etenemistä. Korkein kontrolli, hitain, sopii korkean panoksen
     tai vielä testaamattomiin prosesseihin.
   - **Human-on-the-loop** — prosessi pyörii itsenäisesti, ihminen valvoo
     ja voi puuttua tarvittaessa. Hyvä välitaso, kun silmukka on
     osoittautunut luotettavaksi.
   - **Human-outside-the-loop** — prosessi toimii täysin automaattisesti
     ilman ihmistä yksittäisessä tapauksessa. Nopein ja skaalautuvin,
     sopii vain kun silmukka on luotettu ja virheen hinta on matala.
6. **Arvioi rehellisesti, onko työnkulku aidosti closed-loop-muotoinen**
   ennen kuin lähdet automatisoimaan: onko sillä selkeä tavoite,
   koneluettavat syötteet, hyvin määritellyt työkalut joita agentti voi
   käyttää, ja mitattava onnistumissignaali? Jos työ on pääosin hiljaista
   ihmisarviointia ilman näitä, dokumentoi prosessi ensin manuaalisena
   äläkä yritä automatisoida sitä suoraan.
7. **Kun useampi silmukka on suunniteltu:** kirjaa työkalu-/
   agenttirekisteri — mitä agentteja/työkaluja on käytössä, mitä kukin
   tekee, ja miten työ reititetään oikeaan paikkaan. Mieti orkestrointia:
   miten erilliset silmukat koordinoituvat isommaksi, johdonmukaiseksi
   kokonaisuudeksi.

## Mitä tämä skilli EI tee

- Ei suosittele automatisoimaan kaikkea — pääviesti on päinvastainen:
  tavoite on poistaa ihmisen arvostelukyvyn *pullonkaula* niistä
  kohdista, joissa sitä ei aidosti tarvita, ei poistaa arvostelukykyä
  kokonaan sieltä missä sitä tarvitaan.
- Ei arvioi yksittäisen AI-työkalun teknistä toteutettavuutta — ks.
  `../ai-native-tool-stack-selection/SKILL.md` ja
  `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`.
- Ei korvaa vastuullisen tekoälyn hallintotarkistusta korkean riskin
  käyttötapauksissa — ks.
  `../../../ai-strategy-and-governance/skills/responsible-ai-and-governance-check/SKILL.md`
  ja tarvittaessa `tekoalysaantely`-pakki (EU:n tekoälyasetus).

## Jatka tästä

- Edeltävä/liittyvä skilli samassa pakissa:
  `../ai-native-opportunity-scan/SKILL.md` (agenttisuuden tunnistus-
  kriteeri, jota tämä skilli syventää).
- Liittyvä skilli toisessa pakissa:
  `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
  (Agenttisuuden aste -vaihe),
  `../../../ai-strategy-and-governance/skills/responsible-ai-and-governance-check/SKILL.md`
- Liittyvä skilli toisessa pakissa:
  `../../../business-design-frameworks/skills/value-chain-mapping/SKILL.md`
  — täydentävä tapa jäsentää samaa liiketoimintaa arvoketjuna prosessien
  sijaan.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/workshop-source.md` — lähdetiedot
- `../../CLAUDE.md` — pakin jaetut suojaukset
