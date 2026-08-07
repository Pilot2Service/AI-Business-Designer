# Quickstart — yksi polku, viisi minuuttia

Tämä on lyhin reitti ensimmäisen skillin ajamiseen. Täydellinen rakenne ja kaikki
pakit: [`README.md`](README.md). Miten agentti käyttää tätä pakkia: [`AGENT_GUIDE.md`](AGENT_GUIDE.md).

## 1. Asenna marketplace

Claude Code / Cowork -ympäristössä:

```
/plugin marketplace add <tämän repon polku tai GitHub-osoite>
/plugin
```

## 2. Valitse yksi pakki

Et tarvitse kaikkia 8 ydinpakkia kerralla. Valitse yksi tehtävän mukaan:

| Tilanne | Pakki |
|---|---|
| "Onko tässä liiketoimintamahdollisuus?" | `opportunity-recognition` |
| "Tarvitsen ROI-perustelun investoinnille" | `business-case-and-analysis` |
| "Mitä AI-käyttötapauksia kannattaa priorisoida?" | `ai-strategy-and-governance` |
| "Pitää jäsentää iso, epäselvä ongelma" | `strategic-thinking` |
| "Miten esitän muutoksen johdolle?" | `change-and-communication` |

Asenna Discover-välilehdeltä valitsemasi pakki (esim. `opportunity-recognition`).

## 3. Aja yksi skilli

Esimerkki: `opportunity-recognition`-pakissa on `opportunity-value-assessment`.
Kirjoita Claudelle jotain tämän suuntaista:

```
Käytä opportunity-value-assessment-skilliä arvioimaan tämä idea: [kuvaa oma tilanteesi
2–3 lauseella — mitä ongelmaa ratkaistaan, kenelle, miksi nyt]
```

## 4. Mitä pitäisi tulla ulos

Jokainen skilli tuottaa **jäsennellyn luonnoksen**, ei valmista vastausta:

- Rakenteinen analyysi/pisteytys/kehys — ei vapaamuotoinen essee.
- Näkyvät oletukset — jos jotain ei tiedetä, se on merkitty `[oletus — tarkista]`,
  ei hiljaa täytetty.
- Näkyvä kypsyystaso — Claude kertoo onko käytetty skilli `scaffold` (rakenne
  valmis, ei vielä omaa validoitua kokemusta) vai `validated`/`canonical`
  (käytännössä testattu). Tarkista tarvittaessa `skills_index.json`.
- **Ei lopullista päätöstä.** Tuotos on aina ihmisen tarkistettavaksi ja
  hyväksyttäväksi — ks. `meta/shared-guardrails.md`.

Jos tulos ei näytä tältä (esim. Claude esittää luvun ilman merkintää tai väittää
skillin sisällön olevan sinun validoitua kokemustasi vaikka se on `scaffold`-tasolla),
jokin meni pieleen — tarkista että oikea pakin `CLAUDE.md` on luettu.

## 5. Seuraava askel

- Yhden skillin sijaan haluat valmiin ketjun? Ks. `playbooks/` (esim.
  `playbooks/idea-to-decision.md`).
- Haluat haastaa/ristiintarkistaa tuloksen ennen kuin se menee eteenpäin? Neljä
  pakkia sisältää tähän tarkoitetun delegoitavan agentin (`agents/`-kansio) — ks.
  README:n "Agentit"-taulukko.
- Haluat lisätä oman skillin tai täydentää `[OWNER INPUT]`-osion? Ks.
  `CONTRIBUTING.md`.
