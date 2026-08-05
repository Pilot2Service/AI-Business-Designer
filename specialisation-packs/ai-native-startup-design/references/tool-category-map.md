# Työkalukategoriakartta — AI-natiivi pino

Tilannekuva **kesäkuulta 2026** (`workshop-source.md`, `tools.md`). Kategoriat
ovat pysyvämpiä kuin tuotenimet — tarkista aina työkalun senhetkinen tila
ennen sitoutumista. Käytetään skillissä `ai-native-tool-stack-selection`.

| # | Kategori | Mihin tarkoitukseen | Esimerkkejä (kesäkuu 2026 — tarkista ajantasaisuus) |
|---|---|---|---|
| 1 | AI-ajattelukumppani | Yleinen suunnittelu, kirjoittaminen, päättely; projektissa säilyy liiketoimintakonteksti | Claude, ChatGPT, Gemini |
| 2 | Tutkimus ja tiedonhaku | Lähteistetty tiedonhaku, syväluotaava tutkimus omista dokumenteista | Perplexity, NotebookLM, deep research -tilat |
| 3 | Design-luonnostelu | Tekstistä käyttöliittymäluonnos, komponenttien visualisointi | Figma (+Figma Make), Google Stitch, Claude Artifacts |
| 4 | Sovelluksen rakentaja | Promptista toimiva web-prototyyppi ilman koodia | Lovable, Bolt.new, v0, Replit, Firebase Studio |
| 5 | Koodausagentti | Prototyypistä tuotantoon, todellisen koodikannan muokkaus | Claude Code, Codex, Cursor, Windsurf, GitHub Copilot |
| 6 | Versionhallinta / koodin säilytys | Koodin tallennus, versiointi, jako, siirrettävyys | GitHub, GitLab |
| 7 | Hosting ja julkaisu | Prototyypin/tuotteen julkaisu verkkoon | Vercel, Netlify, Cloudflare Pages |
| 8 | Backend ja tietokanta | Käyttäjät, data, tiedostot, autentikointi | Supabase, Firebase, Neon |
| 9 | Skillit | Agentin kykyjen paketointi ja uudelleenkäyttö | Anthropic Skills Marketplace, skills.sh, SkillsMP |
| 10 | Projektinhallinta | Työn jakaminen ja seuranta tiimin kasvaessa | Linear, Notion |
| 11 | Kokous-/muistiinpanotyökalu | Keskustelujen muuttaminen koneluettavaksi tekstiksi | Granola, Fathom, Fireflies, Otter |
| 12 | Työnkulkujen automaatio / agenttien rakentaminen | Työkalujen ketjutus, autonomiset agentit | Zapier, n8n, Make; agenttialustat: Lindy, Sintra, Relevance AI |

## Minimipino pre-startup-founderille

Ensimmäiset viisi kategoriaa (1, 2, 3, 4, 6) riittävät useimmiten
toimivan, validoidun prototyypin rakentamiseen kahdessa päivässä:
ajattelukumppani + tutkimus + design-luonnos + sovelluksen rakentaja +
koodin säilytys. Loput lisätään vasta kun aito tarve syntyy (ks.
`../skills/ai-native-tool-stack-selection/SKILL.md`).

## Agenttityökalujen kolmiportainen kypsyyspolku

1. **No-code-agenttialustat** — ei-tekniselle founderille tuotantoagenttien
   rakentamiseen visuaalisella käyttöliittymällä (esim. Lindy, Sintra AI,
   Relevance AI, Gumloop).
2. **Avoimen lähdekoodin ajonajat** — teknisesti kiinnostuneille, jotka
   haluavat autonomisen agentin omalle koneelleen, paikallisella datalla
   (esim. OpenClaw-tyyppiset local-first-runtimet).
3. **Kehittäjäkehykset** — kun mukana on tai tulee kehittäjä (esim. Claude
   Agent SDK, OpenAI Agents SDK, LangGraph, CrewAI, Mastra, AutoGen,
   LlamaIndex).

## Muistutus

Tämä taulukko vanhenee nopeasti — hinnoittelu, ilmaiskiintiöt ja
ominaisuudet muuttuvat viikoittain tällä markkinalla. Käytä sitä
kategoriakarttana, älä ajantasaisena tuotevertailuna.
