# Ulkoiset data-MCP:t — valinnainen, ei riippuvuus

## Periaate

Tämä repo on suunniteltu toimimaan **täysin itsenäisesti**: mikään skilli tai agentti
ei vaadi ulkoista MCP-palvelinta toimiakseen. Jokainen skilli toimii käyttäjän antamalla
lähtödatalla ja läpinäkyvillä oletuksilla (`[oletus — tarkista]`, ks.
`shared-guardrails.md`). Tämä tiedosto listaa **valinnaisia** ulkoisia data-MCP:tä,
joita relevantit skillit ja agentit voivat käyttää *jos* käyttäjän ympäristössä sellainen
on kytkettynä — ei koskaan edellytyksenä.

Malli on sama kuin `claude-for-legal-finland`-repossa (joka kytkeytyy Finlexiin ja
oikeuslähde-MCP:hen), mutta yhdellä keskeisellä erolla: siellä lähde on yksi
auktoritatiivinen, oikeudellisesti sitova rekisteri. Tässä repossa ehdotetut lähteet
ovat julkisia talous-/markkinadatalähteitä — hyödyllisiä ristiintarkistukseen, mutta
eivät koskaan ainoa totuus liiketoimintapäätöksen taustalla.

## Kandidaatit

**Näitä ei ole auditoitu tuotantokäyttöön eikä niiden ylläpitoa taata.** Ne on
tunnistettu julkisesta MCP-hakemistosta (mcpservers.org) elokuussa 2026 relevantteina
kandidaatteina — tarkista ennen käyttöä että projekti on yhä ylläpidetty ja että sen
lisenssi ja tietosuojakäytäntö sopivat omaan käyttötarkoitukseesi.

### Ensisijainen: Market Sizing MCP Server (TAM-MCP-Server)

- **Mitä:** avoimen lähdekoodin (MIT) MCP-palvelin, 28 työkalua, 15 valmista
  business-promptia. Kytkeytyy kahdeksaan julkiseen talousdatalähteeseen: Alpha
  Vantage, BLS, Census, FRED, IMF, Nasdaq Data Link, OECD, World Bank.
- **Relevantit skillit/agentit:** `opportunity-recognition/skills/market-sizing-tam-sam-som`,
  `opportunity-recognition/agents/market-sizing-cross-validator`.
- **Mihin sopii:** TAM/SAM/SOM-laskelman pohjadatan haku ja usean riippumattoman
  lähteen ristiintarkistus (`data_validation`-työkalu) sen sijaan että luku
  perustuisi pelkkään oletukseen.
- **Ylläpito:** yksittäisen kehittäjän projekti (github.com/gvaibhav/TAM-MCP-Server),
  ei institutionaalinen — arvioi luotettavuus itse ennen käyttöä.

### Muita kandidaatteja (ei syvemmin arvioitu)

| Kandidaatti | Mihin sopisi |
|---|---|
| `company-mcp` (yritys-/LEI-/SEC-haku) | Kilpailija- ja yritysdata `business-design-frameworks`- ja `business-case-and-analysis`-pakkeihin |
| `secedgar-mcp-server` (SEC EDGAR -tilinpäätökset) | Amerikkalaisten pörssiyhtiöiden benchmarkkaus `business-case-and-analysis`-pakissa |

## Miten skilli/agentti käyttää tätä jos MCP on kytketty

1. Käytä MCP:n palauttamaa lukua **samoin kuin käyttäjän antamaa lähtöarvoa** —
   merkitse lähde (mikä MCP/data-source) ja hakuajankohta, älä esitä ilman
   lähdemerkintää (ks. `shared-guardrails.md` kohta 2).
2. Jos MCP palauttaa useamman lähteen ristiriitaisia lukuja, tee ristiriita
   näkyväksi äläkä keskiarvoista sitä hiljaa.
3. MCP:n data ei koskaan korvaa kohdan 1 (`shared-guardrails.md`) ihmisen
   tarkistusta ja hyväksyntää — se on parempi lähtöarvo, ei valmis päätös.

## Miten kytket (jos haluat kokeilla)

Tämä repo ei sisällä valmista `.mcp.json`-konfiguraatiota — kytkentä tehdään omassa
Claude Code / Cowork -ympäristössäsi normaalin MCP-asennusprosessin kautta (ks.
kunkin palvelimen oma dokumentaatio). Kun MCP on kytketty samaan ympäristöön jossa
tämä skills-pack on asennettuna, relevantit skillit ja agentit tunnistavat sen
saatavuuden kontekstista eivätkä vaadi erillistä konfigurointia tässä repossa.
