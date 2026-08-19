# Task starter: Task-Level Automation Fit — Automate / Augment / Human-Only

**When to use:** You're looking at a role, team, or process and want to know
specifically which parts of it actually suit AI — not "could AI handle
customer service?" as a whole question, but task by task. This is the step
that usually gets skipped, and skipping it is the single most common
mistake in AI-opportunity work.

**What to provide:** A description of the role, team, or process — a job
description, a weekly task list, or a walkthrough of how the work actually
gets done. The more concrete the task list, the better the classification; a
log of "every system switch and every moment of uncertainty for one day"
works well if nothing more formal exists.

**Start with this:**

1. *Full decomposition* — "Use the
   task-level-decomposition-and-automation-fit skill to break this down into
   individual tasks and classify each one as Automate, Augment, or
   Human-Only using the four SML criteria (input/output clarity, cognitive
   nature, error tolerance, time scale): [paste the role, team, or process
   description]."
2. *Start top-down instead* — "Before we go task by task, run
   ai-capability-pattern-matching on our situation first — which of the
   known AI capability patterns show up here, before we do the detailed
   task-level pass?"
3. *Sanity-check one surprising call* — "I'd have assumed [specific task] is
   Human-Only. Double-check that against the four SML criteria — is that
   actually right, or is it Augment-eligible?"

**What you get:** A structured task list — task / SML assessment in brief /
classification + justification — not a blanket verdict on the whole role.
The output actively flags the two most common mistakes: calling an entire
role "Automate" because some of its tasks are, and ruling a task
"Human-Only" just because it's complex.

**What happens next:** Feed the Automate- and Augment-classified tasks
straight into `ai-opportunity-portfolio` (the AI Idea Portfolio Scoring
starter) for 5-dimension scoring and prioritization — this skill produces
exactly the raw, classified list that one scores.

## Skills used

1. `ai-strategy-and-governance/skills/task-level-decomposition-and-automation-fit`
2. `ai-strategy-and-governance/skills/ai-capability-pattern-matching`
3. `ai-strategy-and-governance/skills/ai-opportunity-portfolio`
