---
name: ai-native-opportunity-scan
description: "Käyttää agenttista/closed-loop-linssiä AI:n mahdollistamien, aidosti uusien liiketoimintamahdollisuuksien löytämiseen omassa startup-caseessa, ja pisteyttää/priorisoi löydökset toteutettavuuden ja pienimmän prototypoitavan version mukaan."
---

# AI-Native Opportunity Scan

*Tila: `validated`, `source_layer: owner` — ks. `../../../skills_index.json` ja
`../../../meta/maturity_levels.md`.*

## Tarkoitus

Löytää oman startup-casen sisältä alueita, joissa AI mahdollistaa jotain aidosti
uutta — ei vain nopeuta olemassa olevaa työtä. Skilli käyttää kaksivaiheista
promptiketjua AI-ajattelukumppanin kanssa: ensin löydetään viisi
agenttisen/closed-loop-tasoisen AI:n mahdollistamaa mahdollisuutta, sitten
pressure-testataan ja priorisoidaan ne liiketoimintapotentiaalin,
asiakasarvon ja toteutettavuuden mukaan — päätyen yhteen mahdollisuuteen,
joka viedään suunnittelun seuraaviin vaiheisiin.

## Perustuu

- Omistajan (Tommi Järvinen) AI-native Business Design -työpaja
  ([redacted] / firstkiss.co), pidetty 1.–2.6.2026, Day 1 — Session 1
  "The New AI Mindset" -harjoitus ja sitä edeltävä ydinerottelu: AI ei ole
  vain tuottavuustyökalu, joka nopeuttaa olemassa olevaa työtä — se on uusi
  kyvykkyys ja kapasiteetti, joka mahdollistaa tuotteita ja työnkulkuja, jotka
  olivat aiemmin liian hitaita, kalliita tai mahdottomia.
- Ks. `../../references/workshop-source.md` (lähdetiedot) ja
  `../../references/prompt-library.md` (promptit 1–2, tämän skillin pohjana).

## Rakenne

1. **Varmista, että AI-ajattelukumppanilla on oma liiketoimintakonteksti
   käytössä** — projekti (Claude/ChatGPT), johon on ladattu pitchi,
   business plan, asiakasmuistiinpanot tms. Ilman tätä löydökset jäävät
   geneerisiksi ("automatisoi asiakaspalvelu AI-agentilla" -tyyppisiksi).
2. **Aja löytöprompti** (`../../references/prompt-library.md` promptti 1):
   pyydä AI:ta tunnistamaan 5 aluetta, joissa AI loisi AIDOSTI UUSIA
   liiketoimintamahdollisuuksia — ei "tee X nopeammin" vaan uusia
   ominaisuuksia, tuotteita, työnkulkuja tai liiketoimintamalleja. Vaadi
   agenttista/closed-loop-tasoista ajattelua eikä perustuottavuuskäyttöä
   (ks. `../closed-loop-process-and-human-oversight-design/SKILL.md`
   tarkemmasta erottelusta).
3. Kirjaa jokaiselle viidelle löydökselle: nimi, kuvaus (2–3 lausetta),
   miksi juuri nyt mahdollista AI:n ansiosta, ja mitä pitäisi olla totta
   jotta tekisimme tämän.
4. **Kirjoita oma alustava arviosi ennen pressure-test-vaihetta.** Tämä
   pakottaa oman ajattelun ennen AI:n arviota — työpajan periaate: ajattele
   ensin itse, älä anna AI:n arvioida puolestasi ilman omaa kantaa.
5. **Aja pressure-test-/priorisointiprompti**
   (`../../references/prompt-library.md` promptti 2): pyydä arviota
   kustakin viidestä: liiketoimintapotentiaali, asiakasarvo, toteutettavuus
   pienelle tiimille nykyisillä AI-työkaluilla (matala/keskitaso/korkea), ja
   pienin tällä viikolla prototypoitava versio.
6. Pyydä ranking 1–5 perusteluineen ja suositus, mikä prototypoidaan
   ensin.
7. Valitse yksi mahdollisuus jatkokehitykseen — vie se
   `../customer-vision-to-jtbd/SKILL.md`- ja
   `../ai-buildable-prd-writing/SKILL.md`-skilleihin.

## Mitä tämä skilli EI tee

- Ei tee valintaa puolestasi — pisteytys ja ranking ovat AI:n arvio, ei
  totuus; ihminen tekee lopullisen valinnan.
- Ei korvaa `ai-opportunity-portfolio`-skilliä
  (`ai-strategy-and-governance`-pakissa) — se on tarkoitettu olemassa
  olevan yrityksen laajemman AI-portfolion systemaattiseen priorisointiin.
  Tämä skilli on kevyempi, nopea promptiketju yksittäisen pre-startup-
  founderin oman casen läpikäyntiin.
- Ei generoi liiketoimintaideoita tyhjästä ilman käyttäjän omaa
  liiketoimintakontekstia — laatu riippuu suoraan siitä, kuinka hyvin AI
  tuntee caset.

## Jatka tästä

- Seuraava skilli samassa pakissa: `../customer-vision-to-jtbd/SKILL.md`
  — valitun mahdollisuuden syventäminen asiakasymmärrykseksi.
- Liittyvä skilli samassa pakissa:
  `../closed-loop-process-and-human-oversight-design/SKILL.md` — syventää
  "agenttinen/closed-loop"-linssiä, joka tässä skillissä on vasta
  tunnistuskriteerinä.
- Liittyvä skilli toisessa pakissa:
  `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/prompt-library.md` — promptit 1–2
- `../../references/workshop-source.md` — lähdetiedot
- `../../CLAUDE.md` — pakin jaetut suojaukset
