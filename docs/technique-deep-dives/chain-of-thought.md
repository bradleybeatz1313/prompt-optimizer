# Chain of Thought (CoT) — Deep Dive

## What It Is
Instructing the model to show its reasoning steps before providing a final answer. This dramatically improves accuracy on multi-step reasoning, math, logic, and causal analysis tasks.

## When to Apply
- Math or calculation problems
- Multi-step logical reasoning
- Causal analysis ("why did X happen?")
- Debugging (systematic elimination)
- Any task where the answer depends on intermediate steps

## When NOT to Apply
- Simple factual lookups
- Creative writing (kills the flow)
- Translation (reasoning steps don't help)
- Simple formatting tasks

## Two Variants

### Zero-Shot CoT
Just append a reasoning trigger. No examples needed.

**Triggers that work:**
- "Let's think step by step."
- "Reason through this methodically before giving your answer."
- "Walk through your reasoning, then provide the final answer."

### Few-Shot CoT
Provide example problems with full reasoning chains AND answers.

```
Q: A store has 45 apples. They sell 1/3 on Monday and 1/2 of the remaining on Tuesday. How many are left?

A: Let me work through this step by step.
- Start: 45 apples
- Monday: Sold 1/3 of 45 = 15. Remaining: 45 - 15 = 30
- Tuesday: Sold 1/2 of 30 = 15. Remaining: 30 - 15 = 15
- Answer: 15 apples remain.
```

## Critical Rule
**Place the final answer AFTER the reasoning, never before.** When the answer comes first, the reasoning becomes post-hoc rationalization rather than genuine problem-solving.

## Temperature Guidance
- Tasks with a single correct answer → Temperature 0 (deterministic)
- Tasks with multiple valid approaches → Temperature 0.3-0.5
