---
name: ai-native-conversational-os-design
description: "Suunnittelee AI-natiivin tuotteen keskusteleva käyttöliittymäarkkitehtuuri kuudella vaiheella — Intent, Strategy Cards, Clarification, Output Cards, Mission, Agent Execution — soveltaen viittä AI-first-tuoteperiaatetta (klikkaus>kysymys, valikot>promptit, dashboardit>dialogi, manuaaliset toiminnot>agentit, ruudut>chat+kortit)."
---

# AI-Native Conversational OS Design

*Tila: `draft`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Antaa konkreettinen, uudelleenkäytettävä arkkitehtuurimalli sille, miten
AI-natiivi tuote rakennetaan käyttöliittymänä, joka EI ole perinteinen
näyttöjen/valikoiden/dashboardien kokoelma vaan keskusteleva
käyttöjärjestelmä: käyttäjän aikomus tunnistetaan, oikea sisäinen
"strategia" valitaan, tarvittaessa kysytään täsmentäviä kysymyksiä,
tuotetaan strukturoidut output-kortit, annetaan yksi selkeä missio, ja
agentti voi jatkaa työtä autonomisesti. Ydinviesti: "tuotteesi ei ole enää
joukko ruutuja. Se on ajattelukumppani."

## Perustuu

- [redacted]n "AI-first SaaS Product" -työpajan menetelmä, sovellettu
  omistajan (Tommi Järvinen) toimesta [redacted]-caseen
  ("Decision Coach" MVP) — ks. `../../references/[redacted]-workshop-
  source.md` ja worked example `../../cases/[redacted]-decision-coach-mvp.md`
  kohta 8. **Huom:** sovellettu toistaiseksi vain kerran — ei laajasti
  validoitu useammalla eri tuotteella.
- Työpajan "5 shifts" -periaatteet AI-first-tuotteen suunnittelulle
  (ks. Rakenne-osion alku).

## Rakenne (luonnos — täydennettävä)

### A. Viisi AI-first-tuoteperiaatetta (mindset ennen arkkitehtuuria)

Ennen kuin suunnittelet OS-flown, sisäistä nämä viisi siirtymää vanhasta
SaaS-ajattelusta AI-natiiviin ajatteluun:

1. **Klikkaus → kysymys.** Käyttäjä ei navigoi valikoissa löytääkseen
   oikean toiminnon — hän kysyy mitä haluaa, ja järjestelmä löytää oikean
   toiminnon.
2. **Valikot → promptit.** Kiinteiden valikkorakenteiden sijaan
   käyttäjä ilmaisee aikomuksensa luonnollisella kielellä.
3. **Dashboardit → dialogi.** Tiedon selaamisen sijaan tieto tuodaan
   käyttäjälle keskustelun kautta, oikeaan aikaan, oikeassa kontekstissa.
4. **Manuaaliset toiminnot → agentit.** Käyttäjä ei suorita jokaista
   askelta itse — agentti suorittaa, käyttäjä ohjaa ja hyväksyy (ks.
   `../closed-loop-process-and-human-oversight-design/SKILL.md` ihmisen
   valvontatason valintaan).
5. **Ruudut → chat + kortit.** Käyttöliittymä ei ole pysyvä ruutujen
   kokoelma vaan dynaaminen yhdistelmä keskustelua ja strukturoituja
   informaatiokortteja, jotka ilmestyvät tarpeen mukaan.

Näiden viiden siirtymän yhteinen johtopäätös: tuote ei ole enää joukko
ruutuja, se on ajattelukumppani.

### B. Kuusivaiheinen OS-flow

1. **Intent (käyttäjä → järjestelmä).** Tunnista MIKSI käyttäjä on
   täällä ja mihin hän haluaa selkeyttä. Listaa tuotteesi tukemat
   pääasialliset intentit eksplisiittisesti (tyypillisesti 3-6) —
   älä yritä tukea rajatonta määrää vapaamuotoisia pyyntöjä MVP:ssä.
   Tunnista hallitseva intentti ja välitä se strategiakerrokselle.
2. **Strategy Cards (järjestelmä → sisäinen päättelykerros).**
   Määrittele "pelikirjat" (strategy cards), joista AI voi valita
   käyttäjän intentin mukaan. Jokainen kortti on itsenäinen päättely-
   moduuli: mitä se tulkitsee, mitä se tuottaa (esim. pistemäärä 0-100,
   luokittelu, uudelleenmuotoiltu teksti). Suunnittele niin monta korttia
   kuin MVP:n differentiaattori- ja table-stake-tarpeet vaativat (ks.
   `../customer-vision-to-jtbd/SKILL.md`) — ei enempää.
3. **Clarification (interaktiiviset mikrokysymykset).** Kysy KORKEINTAAN
   2-4 täsmentävää kysymystä, vain kun (a) syöte on liian epämääräinen
   tulkittavaksi, tai (b) väärä strategiakortti on aktivoitunut. Pidä
   kysymykset kevyinä ja nopeina — tämä ei ole lomake, se on tarkennus.
4. **Output Cards (ydin-MVP-tulokset).** Suunnittele standardoidut,
   strukturoidut korttimuodot joina käyttäjä saa tuloksen jokaisesta
   strategiakortin suorituksesta (esim. pistemäärä + "miksi tämä
   pistemäärä" -perustelu + "mikä parantaisi sitä"). Jokaisen output-
   kortin tulisi täyttää yksi MVP:n differentiaattori- tai table-stake-
   tarpeista suoraan.
5. **Mission (AI tiivistää suunnitelman + seuraavan askeleen).** Yksi
   lyhyt missiolause session lopuksi, joka kehystää seuraavat askeleet
   luottamuksen rakentamisen ja epävarmuuden vähentämisen ympärille —
   ei pitkä yhteenveto, vaan yksi konkreettinen, toimintaan johtava lause.
6. **Agent Execution (järjestelmä → autonominen toiminto).** Missio-
   lauseen jälkeen agentti voi jatkaa itsenäisesti: pisteiden
   päivittäminen uuden tiedon myötä, materiaalin uudelleenkirjoitus,
   olemassa olevien työkalujen/resurssien suosittelu. Agentin tehtävä on
   luoda eteenpäin vievää liikevoimaa — ei vain vastata kysymykseen ja
   pysähtyä.

### C. Suunnittelun tarkistuslista

7. **Testaa flow päästä päähän ennen rakentamista.** Kirjoita auki
   yksi konkreettinen käyttäjäpolku Intent-vaiheesta Agent Execution
   -vaiheeseen asti sanallisesti (ei koodia) — jos jokin vaihe tuntuu
   pakotetulta tai keinotekoiselta, yksinkertaista rakennetta ennen
   rakennusvaihetta.
8. **Vie flow `../ai-buildable-prd-writing/SKILL.md`-skillin "Core-
   ominaisuudet"-osioon** — jokainen OS-flown vaihe (Strategy Card,
   Output Card) on yksi PRD:n ominaisuusrivi, kuvattuna lopputuloksena
   ("käyttäjä saa...") teknisen toteutuksen sijaan.

## Mitä tämä skilli EI tee

- Ei sisällä teknistä orkestrointitoteutusta (promptien ketjutus, tila,
  API-rajapinnat) — tuottaa konseptuaalisen arkkitehtuurin, joka viedään
  rakennusagentille `../ai-native-tool-stack-selection/SKILL.md`-skillin
  kautta valittua työkalua käyttäen.
- Ei korvaa `../closed-loop-process-and-human-oversight-design/SKILL.md`
  -skilliä ihmisen valvontatason päättämisessä Agent Execution -vaiheelle
  — käytä sitä rinnalla päättämään in/on/outside-the-loop-taso jokaiselle
  agenttitoiminnolle.
- Ei sovi jokaiselle tuotteelle — jos tuote on aidosti työkalu-/
  dashboard-tyyppinen (esim. datan visualisointi, jatkuva monitorointi
  ilman keskustelevaa päätöksentekoa), tämä malli pakottaa väärän
  muodon. Käytä vain kun ydinarvo on AI:n tulkinta/päättely, ei datan
  näyttäminen.

## [OWNER INPUT — täydennettävä]

Tämä skilli on sovellettu toistaiseksi yhteen caseen ([redacted] Decision
Coach). Kun sovellat sitä useampaan eri tuotteeseen, täydennä:

- omia havaintoja siitä, milloin 6-vaiheinen malli pitää yksinkertaistaa
  (esim. jos Strategy Cards -kerros osoittautuu ylimitoitetuksi pienelle
  MVP:lle)
- konkreettisia esimerkkejä muista OS-flow-suunnitelmista
  `../../cases/`-kansioon
- havaintoja siitä miten flow toimi käytännössä ensimmäisen
  rakennusiteraation jälkeen (mikä vaihe tuotti eniten käyttäjäarvoa,
  mikä osoittautui tarpeettomaksi)

Kun tämä osio on täytetty useammalla caseella, nosta
`skills_index.json`:n `maturity`-kenttä arvoon `validated`
(ks. `../../../../meta/maturity_levels.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa:
  `../rice-scoring-and-mvp-synthesis/SKILL.md` — tuottaa valitun MVP:n
  jolle OS-flow suunnitellaan.
- Seuraava skilli samassa pakissa: `../ai-buildable-prd-writing/SKILL.md`
  — vie OS-flown PRD:n Core-ominaisuudet-osioon.
- Liittyvä skilli samassa pakissa:
  `../closed-loop-process-and-human-oversight-design/SKILL.md` —
  ihmisen valvontatason valinta Agent Execution -vaiheelle.
- Liittyvä skilli toisessa pakissa:
  `../../../business-design-frameworks/skills/customer-journey-and-ai-touchpoint-mapping/SKILL.md`
  — täydentävä tapa jäsentää samaa tuotetta asiakaspolkuna OS-arkkitehtuurin
  sijaan.
- Worked example: `../../cases/[redacted]-decision-coach-mvp.md` kohta 8.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/[redacted]-workshop-source.md` — lähdetiedot
- `../../cases/[redacted]-decision-coach-mvp.md` — worked example
- `../../CLAUDE.md` — pakin jaetut suojaukset
