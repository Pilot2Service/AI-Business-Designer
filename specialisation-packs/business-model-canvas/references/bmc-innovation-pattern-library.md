# BMC Innovation Pattern Library — 159 patternia

Lähde: julkinen liiketoimintamallin innovaatiopatternien kirjasto (159 patternia,
JSON-muodossa). Jäsennetty omistajan omalla nelijakoisella taksonomialla
(Financial / Operating / Value / Experience Model). Käytetään skillissä
`../skills/bmc-innovation-pattern-matching/SKILL.md`.

**Huom laskentaan:** alkuperäisen `Business-model-patterns-README.md`:n mukaan
patterneja pitäisi olla 168; JSON:sta laskettu todellinen määrä on **159** —
todennäköisesti README on kirjoitettu Revenue Modelin aiemmasta kaksiosaisesta
versiosta (12+11=23), kun taas nykyisessä JSON:ssa Revenue Model on yksi 22
patternin kokonaisuus. Käytä tätä (159) ajantasaisena totuutena; alkuperäinen
README säilytetty sellaisenaan `bmc-source-material-notes.md`:ssä.

## 1. Financial Business Model Innovations (Financial Model)

### Financial Model > Cost Model

*Optimize cost structure by combining standardization, variable cost conversion, and scale advantages. Key metrics: cost per unit, fixed-to-variable ratio, modularity index.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `financial.cost.asset_standardization` | Asset Standardization | Reduce operating costs and increase modularity by standardizing assets. Track time-to-deploy and interoperability success rate. |
| `financial.cost.cost_leadership` | Cost Leadership (No Frills) | Maintain lowest possible variable costs to offer high volumes at low prices, measuring margin-per-unit and market penetration. |
| `financial.cost.costs_per_unit` | Costs per Unit | Decrease costs per unit via process improvements and automation. Monitor unit-cost trajectory and ROI on automation investments. |
| `financial.cost.decrease_service_level` | Decrease Service Level | Lower service support costs through self-service interfaces and AI bots. Metrics: deflection rate, customer satisfaction. |
| `financial.cost.economies_of_scale` | Economies of Scale | Leverage increased volume to spread fixed costs. Monitor throughput, utilization rate, and marginal cost decline. |
| `financial.cost.economies_of_scope` | Economies of Scope | Share capabilities across product lines to reduce incremental cost. Metrics: cross-product cost savings, resource utilization. |
| `financial.cost.fixed_to_variable` | Fixed to Variable Costs | Convert fixed costs into variable via leasing/cloud services. Track CapEx/Opex ratio and elasticity. |
| `financial.cost.fractional_ownership` | Fractional Ownership | Distribute asset ownership across multiple users to maximize utilization. Monitor occupancy rate and cost per user. |
| `financial.cost.location` | Location | Optimize location to minimize labor and overhead costs. Metrics: local wage differential, logistics cost. |
| `financial.cost.outsourcing` | Outsourcing | Delegate non-core activities to specialized providers. Track service-level agreements, cost savings, and risk. |
| `financial.cost.physical_to_digital` | Physical > Digital Assets | Migrate physical services to digital formats (e.g., e-commerce, virtual experiences). Metrics: digital adoption rate. |
| `financial.cost.pool_purchasing_power` | Pool Purchasing Power | Collaborate with partners for bulk procurement. Track discount rate and partner network size. |
| `financial.cost.shared_incentives` | Shared Incentives | Align incentives across stakeholders to drive cost reductions. Metrics: incentive redemption, cost performance. |
| `financial.cost.virtual_office` | Virtual Office | Reduce facility costs by enabling remote work. Monitor remote productivity and overhead savings. |
| `financial.cost.ai_as_a_service` | AI-as-a-Service | Expose AI models via APIs/SaaS. Charge per call or tier. Key metrics: requests/sec, latency ≤200ms, uptime ≥99.9%. |

### Financial Model > Revenue Model

*Innovate revenue streams through dynamic pricing, subscriptions, and AI-driven monetization.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `financial.rev.add_on_services` | Add On Financial Services | Offer core products with minimal margin, monetize adjunct services. Track attach rate and service ARPU. |
| `financial.rev.ad_based_auction` | Advertising-Based Auction | Provide free or low-cost services funded by auction-based ads. Metrics: eCPM, fill rate, user engagement. |
| `financial.rev.broker_bundled_pricing` | Broker Bundled Pricing | Facilitate marketplace pricing mechanisms. Monitor take rate, transaction volume, and liquidity. |
| `financial.rev.cash_up_front` | Cash Up Front | Collect prepayment to fund operations. Track working capital benefits and churn rate. |
| `financial.rev.disaggregated_pricing` | Disaggregated Pricing | Enable peer-to-peer or marketplace transactions. Metrics: GMV, take rate, transaction frequency. |
| `financial.rev.flat_rate` | Flat Rate | Fixed fee regardless of usage. Monitor average usage vs. fee and margin stability. |
| `financial.rev.dynamic_pricing` | Dynamic Pricing | Adjust prices in real time based on demand signals. Metrics: yield improvement, price elasticity. |
| `financial.rev.forced_scarcity` | Forced Scarcity | Limit availability to boost price. Track sell-through rate and secondary-market effects. |
| `financial.rev.freemium` | Freemium | Free basic tier with paid premium features. Monitor conversion rate and feature uptake. |
| `financial.rev.bait_and_hook` | Bait & Hook | Sell low-margin core with high-margin consumables. Metrics: refill rate, attach rate. |
| `financial.rev.licensing` | Licensing | License IP to third parties. Track royalty revenue and licensee uptake. |
| `financial.rev.membership` | Membership | Charge for privileged access. Metrics: membership growth, retention rate, CLV. |
| `financial.rev.metered_use` | Metered Use | Bill per unit consumed. Monitor usage patterns and revenue predictability. |
| `financial.rev.on_demand` | On-Demand | Premium pricing for instant delivery. Metrics: delivery time SLA and premium uptake. |
| `financial.rev.pay_per_use` | Pay per Use | Charge per actual usage or consumables. Track usage variability and average revenue. |
| `financial.rev.pay_what_you_want` | Pay What You Want | Customer sets price. Monitor average payment and participation rate. |
| `financial.rev.performance_based` | Performance-Based | Fees tied to outcome metrics, with rebates if targets miss. Track SLA compliance. |
| `financial.rev.premium_pricing` | Premium Pricing | Higher margin for superior offerings. Metrics: price premium and segment uptake. |
| `financial.rev.revenue_sharing` | Revenue Sharing | Share transaction revenue with partners. Monitor partner performance and split. |
| `financial.rev.data_monetization` | Data Monetization | Sell raw or processed data/insights to third parties. Metrics: data unit price, volume sold. |
| `financial.rev.outcome_based_ai_services` | Outcome-Based AI Services | Charge based on measurable AI-delivered outcomes (e.g. % efficiency gain). Requires baseline instrumentation and SLA with guaranteed uplift. |
| `financial.rev.continuous_learning_subscription` | Continuous Learning Subscription | Subscription includes periodic ML model retraining, feature updates, and custom fine-tuning. Performance thresholds govern renewal. |

## 2. Operative Business Model Innovations (Operating Model)

### Operating Model > Value Chain

*Orchestrate processes to maximize throughput, quality, and adaptability. Incorporate AI-driven optimization where possible.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `operating.chain.crowdsourcing` | Crowdsourcing | Distribute tasks to a large crowd via digital platforms. Monitor task completion rate and quality score. |
| `operating.chain.flexible_manufacturing` | Flexible Manufacturing | Rapidly reconfigure production lines. Metrics: changeover time and capacity utilization. |
| `operating.chain.intellectual_property` | Intellectual Property | Leverage proprietary processes or patents. Track licensing revenue and enforcement cost. |
| `operating.chain.lean_production` | Lean Production | Minimize waste via continuous improvement cycles. Monitor defect rate and cycle time. |
| `operating.chain.localization` | Localization | Adapt offerings/processes to local markets. Metrics: local adoption rate and customization cost. |
| `operating.chain.lock_in` | Lock In | Increase switching costs via technical or contractual means. Track retention rate and churn drivers. |
| `operating.chain.logistic_systems` | Logistic Systems | Optimize flow of goods with AI-powered routing. Metrics: delivery accuracy and transit time. |
| `operating.chain.on_demand_production` | On-Demand Production | Produce items post-order to reduce inventory. Track lead time and fill rate. |
| `operating.chain.process_standardisation` | Process Standardisation | Uniform procedures reduce variability. Monitor compliance rate and error frequency. |
| `operating.chain.predictive_analysis` | Predictive Analysis | Use ML to forecast demand and failures. Metrics: forecast accuracy and cost avoidance. |
| `operating.chain.process_automation` | Process Automation | Automate routine workflows using RPA or AI. Monitor throughput and human-in-the-loop exceptions. |
| `operating.chain.process_efficiency` | Process Efficiency | Enhance output per input via optimization. Metrics: OEE (overall equipment efficiency). |
| `operating.chain.vertical_integration` | Vertical Integration | Own multiple supply chain stages to capture margin. Track integration cost vs. margin gain. |
| `operating.chain.human_in_the_loop` | Human-in-the-Loop | Hybrid human+AI workflows to balance scale with oversight. Monitor exception rate and human review time. |

### Operating Model > Key Resources

*Leverage talent, data, and technology assets. Integrate AI models as strategic resources.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `operating.resources.competency_center` | Competency Center | Centralize expertise in shared hubs. Monitor utilization and knowledge transfer. |
| `operating.resources.corporate_university` | Corporate University | Train staff continuously. Metrics: skill adoption and learning ROI. |
| `operating.resources.decentralized_management` | Decentralized Management | Distribute decision rights closer to execution. Track decision latency and outcome quality. |
| `operating.resources.incentive_systems` | Incentive Systems | Align rewards with goals. Metrics: incentive impact on performance. |
| `operating.resources.innovation_teams` | Innovation Teams | Cross-functional AI squads to prototype. Monitor prototype velocity and success rate. |
| `operating.resources.it_integration` | IT Integration | Unify data and systems. Metrics: integration coverage and data latency. |
| `operating._resources.knowledge_management` | Knowledge Management | Capture and share insights. Monitor usage and contribution rates. |
| `operating.resources.leverage_customer_data` | Leverage Customer Data | Analyze and act on customer data. Metrics: model performance and data freshness. |
| `operating.resources.reverse_innovation` | Reverse Innovation | Deploy emerging-market solutions in developed markets. Track adaptation cost and market response. |

### Operating Model > Key Partners

*Build ecosystems of strategic alliances, co-innovation and AI-data-sharing partners.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `operating.partners.affiliation` | Affiliation | Revenue share with referral partners. Monitor partner referral volume. |
| `operating.partners.alliances` | Alliances | Joint ventures for shared R&D. Metrics: joint project ROI. |
| `operating.partners.competition` | Competition | Coopetition agreements to expand markets. Monitor combined market share. |
| `operating.partners.consolidation` | Consolidation | Merge assets with peers to scale. Track synergy capture. |
| `operating.partners.coopetition` | Coopetition | Collaborate with competitors. Metrics: mutual revenue gain. |
| `operating.partners.crowdfunding` | Crowdfunding | Source capital from communities. Monitor funding success rate. |
| `operating.partners.franchising` | Franchising | License business model to operators. Metrics: franchisee performance. |
| `operating.partners.open_innovation` | Open Innovation | In-license/out-license tech. Track patent transactions. |
| `operating.partners.supply_chain_integration` | Supply Chain Integration | Share data and processes across suppliers. Metrics: lead time reduction. |
| `operating.partners.horizontal_integration` | Horizontal Integration | Acquire peers to grow scale. Track market consolidation. |
| `operating.partners.m_a` | Merger & Acquisition (M&A) | Combine entities for capability gain. Metrics: post-merger integration KPI. |
| `operating.partners.open_business` | Open Business | Ecosystem collaboration. Monitor partner API usage. |
| `operating.partners.secondary_markets` | Secondary Markets | Monetize by-products. Metrics: secondary-market revenue. |

## 3. Value-based Innovations (Value Model)

### Value Model > Value Proposition

*Define the core promise of value, tailored by AI-driven insights.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `value.prop.added_functionality` | Added Functionality | Integrate new features identified by usage analytics. Metrics: feature adoption and satisfaction. |
| `value.prop.adjacent_jobs` | Adjacent Jobs to be Done | Expand into related tasks using AI-based job mapping. Monitor cross-sell revenue. |
| `value.prop.bespoke` | Bespoke | Fully tailor offerings via AI-driven configuration engines. Metrics: customization depth and margin. |
| `value.prop.conservation` | Conservation | Enable customers to reduce waste via AI optimization. Track resource savings. |
| `value.prop.demand_driven` | Demand-Driven | Real-time usage adjustment by AI. Metrics: demand-forecast accuracy. |
| `value.prop.ease_of_use` | Ease of Use | Leverage UX analytics to streamline interfaces. Metrics: task completion time. |
| `value.prop.engaging_functionality` | Engaging Functionality | Add unexpected, AI-personalized features. Monitor engagement uplift. |
| `value.prop.environmental_sensitivity` | Environmental Sensitivity | Optimize environmental footprint via AI. Metrics: emissions reduction. |
| `value.prop.mass_customization` | Mass Customization | AI-driven configuration at scale. Monitor units customized and margin. |
| `value.prop.safety` | Safety | Use AI to detect and mitigate risks. Metrics: incident rate. |
| `value.prop.superior_product` | Superior Product | Differentiate via AI-enhanced quality controls. Metrics: defect rate improvement. |
| `value.prop.feature_aggregation` | Feature Aggregation | Combine best-in-class AI modules. Monitor integration success. |
| `value.prop.focus` | Focus | Narrow scope using AI segmentation. Metrics: segment-target fit. |
| `value.prop.market_agnostic_specialization` | Market-Agnostic Specialization | Provide specialized AI services across sectors. Track vertical expansion. |
| `value.prop.opposites_attract` | Opposites Attract | Create novel contrasts via AI-generated differentiation. Monitor novelty score. |
| `value.prop.simplification` | Simplification | Strip down to essentials guided by AI usage data. Metrics: feature reduction impact. |

### Value Model > Product System

*Create ecosystems of products and services with AI-enabled interoperability.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `value.product.complements` | Complements | Cross-sell AI-driven adjunct products. Track bundle attach rate. |
| `value.product.ecosystem_play` | Ecosystem Play | Build AI-platform APIs to attract partners. Metrics: developer adoption. |
| `value.product.extensions` | Extensions or Plug-Ins | Enable third-party AI modules. Monitor plugin downloads. |
| `value.product.integrated_offering` | Integrated Offering | Seamless AI + physical/digital integration. Track end-to-end usage. |
| `value.product.long_tail` | Long Tail | Offer niche AI models on demand. Monitor tail model usage. |
| `value.product.modular_systems` | Modular Systems | Configurable AI components. Metrics: module reuse. |
| `value.product.product_bundling` | Product Bundling | Bundle AI services with hardware. Monitor bundle penetration. |
| `value.product.productize_services` | Productize Services | Package AI consulting as off-the-shelf products. Metrics: time-to-market. |
| `value.product.product_line` | Product Line | Tier AI offerings by capability. Track migration between tiers. |
| `value.product.platforms` | Product/Service Platforms | Create AI-enabled platform with extensibility. Metrics: platform MAU. |
| `value.product.smartification` | Product Smartification | Add AI sensors/agents to existing products. Track feature activation. |

### Value Model > Service Model

*Deliver services augmented by AI, ensuring scalability and personalization.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `value.service.added_value` | Added Value | Offer AI-based analytics as a service. Metrics: uptake and insight accuracy. |
| `value.service.automatic_adjustment` | Automatic Adjustment | AI dynamically adjusts service parameters. Track adjustment frequency and success. |
| `value.service.concierge` | Concierge | Premium AI-driven task automation. Metrics: tasks completed and customer satisfaction. |
| `value.service.customization` | Customization | Personalized services via AI profiles. Monitor customization depth. |
| `value.service.guarantee` | Guarantee | SLA-backed AI performance guarantees. Metrics: SLA compliance and penalty incidence. |
| `value.service.lease_or_loan` | Lease or Loan | Spread AI solution cost over time. Track financing uptake. |
| `value.service.loyalty_programs` | Loyalty Programs | Reward usage and referrals. Monitor program engagement. |
| `value.service.managed_service` | Managed Service | Fully managed AI operations. Metrics: uptime and incident response. |
| `value.service.self_service` | Self-Service | AI chatbots and portals for self-help. Track deflection rate. |
| `value.service.supplementary_service` | Supplementary Service | Ancillary AI tools. Monitor usage and cross-sell. |
| `value.service.try_before_you_buy` | Try Before You Buy | Free AI trial environments. Track trial-to-paid conversion. |
| `value.service.user_support` | User Support Systems | Community Q&A with AI moderation. Metrics: resolution time. |
| `value.service.ai_as_a_service` | AI-as-a-Service | Duplicate of Financial Model pattern – available under Service Model for API provision scenarios. |

## 4. Experience Model Innovations (Experience Model)

### Experience Model > Channels

*Leverage AI to personalize and optimize delivery channels.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `experience.channels.context_specific` | Context-Specific | AI selects optimal delivery context (time/place). Track context-match accuracy. |
| `experience.channels.cross_selling` | Cross Selling | AI-driven upsell recommendations. Monitor attach rate lift. |
| `experience.channels.digitization` | Digitization | Convert to digital channels with AI personalization. Metrics: digital engagement. |
| `experience.channels.diversification` | Diversification | Add new digital/physical channels via AI insights. Monitor channel ROI. |
| `experience.channels.e_commerce` | E-Commerce | Online sales with AI merchandizing. Metrics: online conversion. |
| `experience.channels.flagship_store` | Flagship Store | AI-enhanced experiential retail. Monitor footfall and engagement. |
| `experience.channels.go_direct` | Go Direct | Direct-to-consumer with AI CRM. Track CAC and LTV. |
| `experience.channels.indirect_distribution` | Indirect Distribution | Partner channels with AI-supported training. Monitor partner sales. |
| `experience.channels.on_demand` | On-Demand | AI-powered real-time delivery. Metrics: SLA compliance. |
| `experience.channels.premium_experience` | Premium Experience | High-end AI-curated experiences. Track NPS. |
| `experience.channels.low_cost_center` | Low Cost Center | High-volume AI-assisted kiosks. Monitor cost per interaction. |
| `experience.channels.outsourced_sales` | Outsourced Sales | Third-party sales with AI lead scoring. Track lead conversion. |
| `experience.channels.non_traditional` | Non-Traditional Channels | Novel channels enabled by AI (e.g., VR). Monitor adoption. |
| `experience.channels.pop_up_presence` | Pop-Up Presence | Temporary AI-driven activations. Track event ROI. |

### Experience Model > Customer Engagement

*Deepen engagement via AI-personalized experiences.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `experience.engagement.augmented_reality` | Augmented Reality | AR overlays powered by AI. Monitor engagement duration. |
| `experience.engagement.community_belonging` | Community & Belonging | AI-moderated social platforms. Track community growth. |
| `experience.engagement.customer_autonomy` | Customer Autonomy | Empower users with AI configurators. Monitor self-service adoption. |
| `experience.engagement.customer_sourcing` | Customer Sourcing | AI-driven feedback loops. Monitor insight volume. |
| `experience.engagement.direct_marketing_automation` | Direct Marketing Automation | AI-targeted campaigns. Metrics: conversion lift. |
| `experience.engagement.experience_automation` | Experience Automation | End-to-end automated journeys. Track completion rate. |
| `experience.engagement.experience_enabling` | Experience Enabling | Simplify via AI orchestration. Monitor friction points. |
| `experience.engagement.experience_simplification` | Experience Simplification | Remove unnecessary steps with AI analysis. Metrics: step reduction. |
| `experience.engagement.reward_engagement` | Reward Engagement | AI-driven gamification and rewards. Track participation. |
| `experience.engagement.use_data` | Use Data | Leverage customer data for personalization. Metrics: data coverage. |
| `experience.engagement.gamification` | Gamification | AI-powered game mechanics. Monitor engagement uplift. |
| `experience.engagement.mastery` | Mastery | Guided learning via AI tutors. Metrics: skill acquisition. |
| `experience.engagement.personalization` | Personalization | Real-time content personalization. Track relevance score. |
| `experience.engagement.status_recognition` | Status & Recognition | AI-driven recognition programs. Monitor award redemption. |

### Experience Model > Customer Relationships

*Shape relationships with AI-enabled automation and personalization.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `experience.relationships.automated_services` | Automated Services | Combine self-service with AI. Metrics: automation ratio. |
| `experience.relationships.co_creation` | Co-creation | AI-facilitated joint design. Track co-creation sessions. |
| `experience.relationships.communities` | Communities | AI-curated user groups. Monitor engagement and churn. |
| `experience.relationships.long_term` | Long-Term | Focus on CLV using AI lifetime models. Metrics: predicted vs. actual CLV. |
| `experience.relationships.personal_assistance` | Personal Assistance | AI plus human support at key moments. Monitor resolution time. |
| `experience.relationships.self_service` | Self Service | AI portals for troubleshooting. Metrics: deflection rate. |
| `experience.relationships.spoc` | Single Point of Contact (SPOC) | AI-managed ticketing to one agent. Track handoff rate. |
| `experience.relationships.switching_costs` | Switching Costs | AI locks in via data portability friction. Metrics: churn drivers. |
| `experience.relationships.transactional` | Transactional | Make interactions pay-per-use. Metrics: transaction frequency. |

### Experience Model > Brand

*Amplify brand via AI-driven content and experiences.*

| ID | Nimi | Kuvaus |
|---|---|---|
| `experience.brand.architecture` | Brand Architecture | Structure brand ecosystem with AI coherence checks. Metrics: brand equity. |
| `experience.brand.leverage` | Brand Leverage | Extend brand via AI-curated sub-labels. Track sub-brand uptake. |
| `experience.brand.co_branding` | Co-Branding | Joint brand campaigns aided by AI. Metrics: campaign reach. |
| `experience.brand.component_branding` | Component Branding | Highlight parts via AI storytelling. Track component recognition. |
| `experience.brand.employer_of_choice` | Employer of Choice | AI-driven talent branding. Monitor candidate quality. |
| `experience.brand.increased_loyalty` | Increased Loyalty | AI-tailored loyalty initiatives. Metrics: repeat purchase rate. |
| `experience.brand.ingredient_branding` | Ingredient Branding | AI-selected ingredient highlights. Monitor co-brand sales. |
| `experience.brand.private_label` | Private Label | AI-driven private label development. Metrics: margin improvement. |
| `experience.brand.umbrella` | Umbrella Brand | Leverage single brand for multiple offerings. Track brand coherence. |

---

**Yhteensä: 159 patternia.**

## Käyttösäännöt

- Select 3–5 patterns per scenario, output full JSON path per pattern
- Avoid conflicting patterns (e.g. Cost Leadership vs. Premium Pricing)
- Ensure ethical compliance (data privacy, non‐exploitative)
- Validate feasibility against scale and resources

Tulostusskeema (`aiUsage.outputSchema`):

```json
{
  "recommendations": [
    {
      "pattern_id": "string",
      "pattern_name": "string",
      "sub_model": "string",
      "rationale": "string"
    }
  ]
}
```