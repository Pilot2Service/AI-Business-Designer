# AI Capability Pattern Library

This is a concrete application, to AI solutions, of the **Capability
Pattern Mapping** method from
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`.
Instead of asking "is there an AI example from our industry," this
library offers **13 named, industry-agnostic AI capability patterns**,
each of which works as a diagnostic question in any new client
situation. For usage instructions and workflow, see
`../skills/ai-capability-pattern-matching/SKILL.md`.

## How this library was built — transparency on sources

The patterns are abstracted from two independent, broad industry AI
use-case reports. This isn't an exhaustive listing of every case in the
sources, but a **curated abstraction** of a representative sample — for
the rationale on why curation is a better approach than a raw case list,
see the Purpose section of
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`.

1. **Primary source** — a broad industry report (2026 edition), 130 use
   cases across six industries (Consumer; Energy, Resources &
   Industrials; Financial Services; Government & Public Services; Life
   Sciences & Health Care; Technology, Media & Telecommunications). The
   report applies a six-dimensional responsible-AI risk framework (fair
   and impartial, robust and reliable, transparent and explainable,
   safe and secure, responsible and accountable, private) to the risk
   assessment of every case. **81 cases** across five of the six
   industries were text-extracted and verified from this report (title,
   industry, primary business function, Agentic AI / Physical AI tag)
   — the sixth industry (Technology, Media & Telecommunications) is
   included only at the theme level, due to technical extraction
   constraints, not with individual cases. Every example mentioned in
   this library is drawn directly from that extraction, not produced
   from memory.
2. **Second, independent source** — an industry AI use-case digest, 63
   use cases across 16 business functions; its own analysis shows
   roughly 75% of estimated value concentrated in four functions:
   **customer operations, marketing & sales, software development, and
   R&D**. This is used in this library as a **cross-check** on the
   patterns' weighting — not as a source for individual cases, since
   the exact content of individual cases wasn't reliably available
   during extraction.

**What this means in practice:** every reference under "Examples from
industry" below is a real, correctly titled use case from the primary
source. **Don't expand these examples with details not listed here** —
if you need more detail, go back to the original source rather than
filling in from memory.

## Industry and function coverage in the extraction (81 cases)

| Industry | Cases in extraction |
|---|---|
| Energy, Resources & Industrials | 28 |
| Consumer | 26 |
| Financial Services | 17 |
| Government & Public Services | 8 |
| Life Sciences & Health Care | 2 |
| Technology, Media & Telecommunications | 0 (theme level only) |

The source's own function categories (appearing as "Tags"): Sales,
Marketing, Operations, R&D/Product Development, Customer Service,
Customer Experience, Compliance & Risk, Procurement/Sourcing & Supply
Chain, Manufacturing & Quality, Field Services, Information Technology,
Learning & Development, Cross-functional, Distribution & Logistics. AI
type tags: **Agentic AI** (multi-agent, autonomous decision-making),
**Physical AI** (robotics/physical execution), and untagged (more
traditional predictive/generative AI without an agentic or physical
component).

---

## Patterns

### 1. Multi-agent real-time trade-off optimization

**Definition:** Two or more interdependent decisions (pricing +
inventory, cash + risk, routing + demand) are made today in separate
teams/systems on different cycles. Specialized agents coordinate the
decisions in real time based on a shared situational picture.

**Diagnostic question:** *"Where do you have two or more decisions that
affect each other, made today separately and on different timelines?"*

**AI type:** Agentic AI

**Examples from industry:**
- [Consumer] *Dynamic pricing and inventory optimization* — pricing,
  promotion, and inventory agents coordinating in real time.
- [Consumer] *Autonomous supply chain operations* — demand forecasting,
  planning, and disruption detection as a single agent network.
- [Consumer] *Integrated business planning* — combining sales, demand,
  and supply-chain data into a single decision base.
- [Energy, Resources & Industrials] *Intelligent commercial
  operations* — bid pricing, bid preparation, and customer interaction
  on the same agent network.
- [Financial Services] *AI agents for algorithmic trading and market
  simulation* — trading strategies and market simulation, multi-agent.
- [Financial Services] *Intraday liquidity optimization* — real-time
  balancing of cash and risk.

**Risk lens (responsible-AI dimensions):** *Fair and impartial* and
*Responsible and accountable* stand out — fast, coordinated decisions
(e.g. pricing) can look arbitrary to a customer if the decision logic
isn't clearly bounded and final accountability rests with a human.

---

### 2. Unstructured document validation and anomaly detection

**Definition:** A highly paid expert reads free-form text or PDF
documents looking for anomalies, gaps, or signs of fraud before an
approve/reject/escalate decision. (This is the user's own example
pattern — see
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`.)

**Diagnostic question:** *"Where in your process does a highly paid
expert have to search for anomalies in free-form text or a PDF document
before a decision?"*

**AI type:** Agentic AI / untagged (document analysis)

**Examples from industry:**
- [Consumer] *Autonomous warranty adjudication* — flagging warranty-
  claim anomalies and documentation support for a human expert.
- [Financial Services] *AI agents for credit underwriting* — applicant
  data analysis, market-context monitoring, and compliance checking
  together.
- [Financial Services] *Research-based report generation* ("Getting to
  know your customer") — compiling new-customer reports to support
  onboarding decisions.
- [Government & Public Services] *AI-supported regulatory examinations
  and inspections* — reviewing large volumes of documents during
  inspections.
- [Government & Public Services] *AI-driven permitting* — application
  scanning, information extraction, compliance checking, real-time
  feedback.
- [Government & Public Services] *AI-enhanced benefits eligibility* —
  streamlining benefits-application processing and decisions.

**Risk lens:** *Robust and reliable* is most critical — poor data leads
to poor decisions (e.g. misinterpreted signals). Strong data validation
and filtering are needed before anomaly flags are used in
decision-making.

---

### 3. Persistent personal advisor/concierge agent

**Definition:** A customer faces a complex, high-stakes, recurring
decision (what to buy, how to invest, how to manage their health) for
which they get generic, one-off advice today. A persistent agent tracks
the customer's situation continuously and updates the recommendation
over time.

**Diagnostic question:** *"Where does your customer face a recurring,
complex decision for which they get only one-off, generic advice
today?"*

**AI type:** Agentic AI

**Examples from industry:**
- [Consumer] *AI assistant for vehicle buying and leasing* — hyper-
  personalized recommendations to support the purchase decision.
- [Financial Services] *Ultra-personalized financial advice and wealth
  management* — automated, continuously adapting wealth-management
  advice.
- [Financial Services] *Enhanced AI support for customers* ("Financial
  guardian") — a personal virtual assistant for daily needs.
- [Life Sciences & Health Care] *Hyper-personalized health care* —
  24/7 virtual care team tracking patient data and coordinating care.
- [Consumer] *Product recommendations* ("A virtual shopping
  assistant") — personalized product recommendations based on
  behavioral data.

**Risk lens:** *Private* and *Transparent and explainable* — continuous,
personal tracking requires a clear data-protection basis and the
ability to explain why a recommendation changed.

---

### 4. Predictive equipment alerting and autonomous intervention

**Definition:** Equipment/infrastructure condition is monitored
continuously with sensor data instead of scheduled/manual inspection;
failure is predicted and addressed before an outage.

**Diagnostic question:** *"Where do you rely on scheduled or manual
inspection instead of continuous measurement, and what would an
unplanned outage there cost?"*

**AI type:** Agentic AI / Physical AI

**Examples from industry:**
- [Energy, Resources & Industrials] *AI-driven predictive maintenance*
  — equipment-condition monitoring, root-cause diagnosis, predictive
  maintenance.
- [Energy, Resources & Industrials] *Autonomous drone-based
  infrastructure inspection* — unmanned, AI-guided inspections of
  power lines, pipelines, transmission towers.
- [Energy, Resources & Industrials] *Predictive monitoring for
  environment health & safety* — visual monitoring by drones, robots,
  and fixed infrastructure for early risk detection.
- [Energy, Resources & Industrials] *Inspection of network and utility
  infrastructure* — using satellite, LiDAR, and drone data to detect
  degradation.
- [Financial Services] *Predictive maintenance and autonomous
  operations for IT infrastructure & ATMs* — using edge computing to
  ensure uptime.

**Risk lens:** *Safe and secure* — an automated function that intervenes
in physical infrastructure needs to be safeguarded against failure
conditions (e.g. human confirmation before a physical intervention).

---

### 5. Frontline task and workforce orchestration

**Definition:** Frontline workers (retail staff, service technicians,
city infrastructure crews) get their day's priorities from a static
schedule or a supervisor's judgment, instead of real-time,
signal-driven reprioritization.

**Diagnostic question:** *"Where do frontline workers get their day's
priorities from a static schedule instead of adapting to real-time
signals?"*

**AI type:** Agentic AI

**Examples from industry:**
- [Consumer] *Next-generation store operations* — autonomous
  coordination of in-store operations based on real-time conditions.
- [Energy, Resources & Industrials] *Autonomous field operations
  management* — task coordination and automated frontline
  decision-making.
- [Energy, Resources & Industrials] *Workforce scheduling and
  dispatch* — scheduling service staff based on failure forecasts.
- [Government & Public Services] *Smart city operations and urban
  infrastructure modernization* — monitoring city infrastructure and
  directing tasks in real time.

**Risk lens:** *Responsible and accountable* — when a system directs
people's daily work, it must be clear who's accountable if the
prioritization goes wrong.

---

### 6. Vision-guided physical handling and quality control

**Definition:** A human visually inspects or handles physical items in
a repetitive, high-volume task with defined tolerances — machine vision
+ robotics does the same.

**Diagnostic question:** *"Where does a human visually inspect or
handle physical items in a repetitive, high-volume task with clear
tolerance limits?"*

**AI type:** Physical AI

**Examples from industry:**
- [Consumer] *Vision-enabled store operations* — monitoring shelf
  execution and planogram compliance with machine vision.
- [Consumer] *Robotic stowing and picking system* — robotic warehouse
  shelf handling using machine vision.
- [Consumer] *Vision-enabled robotic induction* — handling SKU
  variation at industrial throughput speed.
- [Energy, Resources & Industrials] *Autonomous self-calibrating
  quality and process control* — defect detection and self-calibrating
  process control.
- [Energy, Resources & Industrials] *Defect detection for industrial
  machinery* — machine-vision-assisted inspection with human
  confirmation.
- [Energy, Resources & Industrials] *Precision-critical high-value
  manufacturing* — precision-critical assembly under human oversight.

**Risk lens:** *Robust and reliable* and *Safe and secure* — a machine-
vision misdetection in a physical environment can cause a safety risk,
not just a quality defect.

---

### 7. Autonomous mobile physical operation (logistics/transport)

**Definition:** Material or people are physically moved along a
predetermined fixed route/schedule; autonomous vehicles/robots detect
conditions in real time and adapt the route, speed, and execution on
the move.

**Diagnostic question:** *"Where do material or people move along a
fixed route/schedule instead of the route adapting to real-time
conditions?"*

**AI type:** Physical AI

**Examples from industry:**
- [Consumer] *Autonomous transport for urban mobility services* —
  driverless vehicles for passenger and goods transport.
- [Consumer] *Fleet telemetry and route optimization* — edge computing
  in vehicles to adapt routing on the move.
- [Consumer] *Autonomous material movement in consumer fulfillment
  environments* — AMR robots sharing space with human workers.
- [Energy, Resources & Industrials] *Autonomous haulage systems for
  safe & intelligent mining operations* — autonomous mining trucks and
  their safe, sensor-based coordination.
- [Energy, Resources & Industrials] *Autonomous agriculture and
  precision farming* — a network of drones and ground robots for
  field operations.

**Risk lens:** *Safe and secure* dominates — shared physical space
between humans and machines requires a validated safety architecture
before deployment.

---

### 8. Continuous multi-format content production

**Definition:** Content production (text, image, video) is bottlenecked
by a small creative team; on-brand drafts could instead be produced
continuously and with trend awareness.

**Diagnostic question:** *"Where is content production bottlenecked by a
small team, and could on-brand drafts be produced continuously
instead?"*

**AI type:** untagged (generative AI)

**Examples from industry:**
- [Consumer] *Marketing content assistant* — efficient, consistent,
  personalized content production across formats.
- [Consumer] *Social media content generation* — autonomous,
  trend-aware multi-format content production.
- [Consumer] *Planning for promotions* — preparing promotion plans,
  negotiation materials, and pitch decks.
- Also at the theme level in Technology, Media & Telecommunications:
  media organizations using generative AI for hyper-personalized
  content and automating editorial workflows (a theme from the report,
  not an individually extracted case).

**Risk lens:** *Transparent and explainable* — the origin and copyright
status of automatically produced content must be traceable.

---

### 9. Natural-language access to enterprise knowledge

**Definition:** A decision-maker expects an analyst or specialist to
turn a question into a report, even though the data already exists. A
natural-language interface opens direct access instead.

**Diagnostic question:** *"Where does a decision-maker expect an analyst
to turn a question into a report, even though the data already
exists?"*

**AI type:** untagged

**Examples from industry:**
- [Consumer] *Data access for all* — guiding business users to
  consumer-data insights with natural-language queries.
- [Financial Services] *Business intelligence at your fingertips* —
  enterprise-wide data search with a natural-language interface.
- [Government & Public Services] *Digitizing policymaking* — searching
  policy documents and giving natural-language answers in complex
  policy environments.
- [Government & Public Services] *Global policy tracking* — real-time
  tracking and analysis of public-policy developments across hundreds
  of countries.
- [Consumer] *Next-level market intelligence* ("Market research") —
  speeding up market research by summarizing large volumes of
  material.

**Risk lens:** *Robust and reliable* — a natural-language answer can
look confident even when the underlying data is incomplete; source
traceability from the answer is important.

---

### 10. Continuous compliance and risk monitoring

**Definition:** Compliance/risk/fraud is checked today on a periodic
cycle (quarterly audit, spot check); continuous, multi-signal
monitoring replaces the periodic check.

**Diagnostic question:** *"Where do you check compliance, risk, or fraud
on a periodic cycle instead of continuous monitoring?"*

**AI type:** Agentic AI / untagged

**Examples from industry:**
- [Financial Services] *AI-powered risk management and regulatory
  compliance* — an always-on compliance team with specialized agents.
- [Financial Services] *Focused cyber* — filtering, analyzing, and
  prioritizing security alerts by real threat level.
- [Government & Public Services] *Global policy tracking* — (see also
  pattern 9 — this case sits in two patterns: information retrieval
  AND continuous monitoring, depending on how it's used).

**Risk lens:** *Responsible and accountable* — continuous automated
monitoring must not obscure who makes the final escalation decision.

---

### 11. AI-accelerated design and research loop

**Definition:** An R&D/design process proceeds as a slow, gate-staged
cycle in which only a few of the possible alternatives are ever
explored. Simulation/generation enables faster iteration across a
wider option space.

**Diagnostic question:** *"Where does your R&D/design process proceed as
a slow, gate-staged cycle in which only a few of the possible
alternatives are ever explored?"*

**AI type:** Agentic AI / Physical AI (simulation)

**Examples from industry:**
- [Consumer] *AI-orchestrated product design* — orchestrating the
  entire product-design lifecycle from market sensing to iteration.
- [Energy, Resources & Industrials] *Materials design* — a wider
  materials design space and accelerated property optimization.
- [Energy, Resources & Industrials] *Site design generation* —
  automating site design and cutting time/cost.
- [Energy, Resources & Industrials] *Hydrocarbon reservoir
  exploration* — optimizing discovery rates and reducing risk in site
  characterization.
- [Energy, Resources & Industrials] *Simulation-first development &
  digital twins* — validating physical systems virtually before
  deployment.

**Risk lens:** *Robust and reliable* — a simulation-based model's
accuracy needs to be validated against the real world before its
resulting designs are fully relied upon.

---

### 12. Simulation-based expertise scaling

**Definition:** Expert know-how is bottlenecked in a small number of
people who can't be everywhere; a digital twin or simulation lets more
people practice safely or get remote expert support.

**Diagnostic question:** *"Where is expert know-how bottlenecked in a
small number of people who can't be everywhere?"*

**AI type:** Physical AI (simulation/AR-VR)

**Examples from industry:**
- [Energy, Resources & Industrials] *Personalized OHS training* —
  personalized, immersive occupational-safety training with realistic
  scenarios.
- [Energy, Resources & Industrials] *Simulation-driven remote
  operations and training* — AR/VR digital twins of offshore
  facilities for remote expert support.

**Risk lens:** *Safe and secure* — simulation training needs to match
the real environment closely enough that the learned behavior transfers
safely to the real situation.

---

### 13. AI-assisted software development

**Definition:** Developers write, test, document, and debug code
manually; AI-assisted tools speed up the same work without the
developer's role disappearing.

**Diagnostic question:** *"Where does your development team spend most
of its time on routine code writing, testing, or documentation that
could be AI-assisted?"*

**AI type:** untagged / Agentic AI

**Examples from industry:**
- [Consumer] *Code assist for developers* ("Augmented developer") —
  support for developing and maintaining applications and platforms.
- [Financial Services] *Transformation with speed and confidence*
  ("Code assistant for digital transformation") — accelerating banks'
  digital transformation with code assistants.
- Also at the theme level in Technology, Media & Telecommunications:
  developers using AI tools to write, test, document, and debug code
  faster, and IT-operations teams deploying agents for system
  monitoring, outage prediction, and automated resolution (a theme
  from the report, not an individually extracted case).

**Risk lens:** *Robust and reliable* — AI-generated code needs the same
or tighter testing discipline as human-written code, not looser.

---

## Cross-check against the second source

A second, independent industry AI use-case digest (63 use cases, 16
functions) shows roughly 75% of estimated value concentrated in four
functions: **customer operations, marketing & sales, software
development, R&D.** The 13-pattern library above covers all four:
patterns 3 and 2 (customer operations/document validation), patterns 8
and 1 (marketing & sales), pattern 13 (software development), patterns
11–12 (R&D). This isn't a coincidence — it's a reasonable cross-check
that the curation hasn't left out the areas producing the most value.

## How to use and extend this library

See `../skills/ai-capability-pattern-matching/SKILL.md` for usage
instructions. When adding new patterns: follow the same four-question
abstraction described in
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`,
require at least three genuinely different examples before naming a new
pattern, and always mark the source clearly (which report/case the
example was drawn from) — never add an example from memory.
