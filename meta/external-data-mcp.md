# External data MCPs — optional, not a dependency

## Principle

This repo is designed to work **fully standalone**: no skill or agent
requires an external MCP server to function. Every skill works on
user-supplied input data and transparent assumptions (`[assumption —
verify]`, see `shared-guardrails.md`). This file lists **optional**
external data MCPs that relevant skills and agents can use *if* one happens
to be connected in the user's environment — never as a requirement.

The model is the same as in the `claude-for-legal-finland` repo (which
connects to Finlex and a legal-source MCP), with one key difference: there,
the source is a single authoritative, legally binding register. The sources
suggested here are public economic/market data sources — useful for
cross-checking, but never the sole truth behind a business decision.

## Candidates

**These have not been audited for production use, and their maintenance is
not guaranteed.** They were identified from a public MCP directory
(mcpservers.org) in August 2026 as relevant candidates — before using one,
verify the project is still maintained and that its license and privacy
practices fit your intended use.

### Primary: Market Sizing MCP Server (TAM-MCP-Server)

- **What:** an open-source (MIT) MCP server with 28 tools and 15 ready-made
  business prompts. Connects to eight public economic data sources: Alpha
  Vantage, BLS, Census, FRED, IMF, Nasdaq Data Link, OECD, World Bank.
- **Relevant skills/agents:**
  `opportunity-recognition/skills/market-sizing-tam-sam-som`,
  `opportunity-recognition/agents/market-sizing-cross-validator`.
- **What it's good for:** pulling baseline data for a TAM/SAM/SOM
  calculation and cross-checking it across several independent sources
  (the `data_validation` tool), instead of a number resting on a bare
  assumption.
- **Maintenance:** a single-developer project
  (github.com/gvaibhav/TAM-MCP-Server), not institutional — assess its
  reliability yourself before using it.

### Other candidates (not evaluated in depth)

| Candidate | What it would suit |
|---|---|
| `company-mcp` (company/LEI/SEC lookup) | Competitor and company data for the `business-design-frameworks` and `business-case-and-analysis` packs |
| `secedgar-mcp-server` (SEC EDGAR filings) | Benchmarking US public companies in the `business-case-and-analysis` pack |

## How a skill/agent uses this if an MCP is connected

1. Treat a number returned by an MCP **the same way as a user-supplied
   baseline** — state the source (which MCP/data source) and the retrieval
   date; don't present it without a source note (see `shared-guardrails.md`
   item 2).
2. If the MCP returns conflicting figures from multiple sources, surface
   the conflict rather than silently averaging it away.
3. MCP data never replaces the human review and approval required by item 1
   of `shared-guardrails.md` — it's a better baseline, not a finished
   decision.

## How to connect (if you want to try it)

This repo doesn't ship a ready-made `.mcp.json` configuration — connecting
one is done in your own Claude Code / Cowork environment via the normal MCP
setup process (see each server's own documentation). Once an MCP is
connected in the same environment where this skills pack is installed,
relevant skills and agents will recognize its availability from context and
require no separate configuration in this repo.
