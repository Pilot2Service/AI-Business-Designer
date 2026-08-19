# Task starter: Business Case Review & Stress-Test

**When to use:** You already have a draft business case — yours or someone
else's — and need a second pass before it goes to a decision-maker: is the
logic sound, are the risks visible, would the numbers survive a challenge?

**What to provide:** The draft business case (paste the text or attach the
document) and roughly what decision it's supporting (budget approval,
go/no-go, etc.).

**Start with this:**

1. *Full review* — "Review the attached business case using the
   business-case-builder skill. Check whether the problem statement, options
   considered (including 'do nothing'), economics, risks, and recommendation
   are all present and internally consistent. Flag anything that's missing
   or unclear before this goes to a decision-maker."
2. *Stress-test the assumptions* — "Use the assumption-stress-tester agent
   to adversarially challenge this business case's assumptions before I take
   it forward. Tell me which numbers are most likely to be wrong and what
   evidence would change the recommendation."
3. *Challenge the recommendation* — "Assume the recommendation in this
   business case may be wrong. Stress-test it against the alternative
   options, including 'do nothing' — what would have to be true for one of
   them to actually be the better choice?"

**What you get:** A structured read against a BABOK/PMI-style business case
structure, plus (if you use variant 2) a separate findings table naming the
assumptions most likely to break under scrutiny. No invented numbers —
anything unverifiable is marked `[assumption — verify]`.

**What happens next:** If the case holds up, continue into
`roi-npv-sensitivity-model` for a deeper financial pass, or
`executive-narrative-and-storyline` to prepare the pitch itself.

## Skills used

1. `business-case-and-analysis/skills/business-case-builder`
2. `business-case-and-analysis/agents/assumption-stress-tester`
3. `business-case-and-analysis/skills/roi-npv-sensitivity-model`
4. `change-and-communication/skills/executive-narrative-and-storyline`
