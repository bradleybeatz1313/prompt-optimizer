# Decomposition — Deep Dive

## What It Is
Breaking a complex prompt into sequential sub-tasks where each output feeds the next. Factored cognition consistently outperforms monolithic prompts on multi-step requests.

## When to Decompose
**Signal:** If you can name 3+ distinct deliverables, decompose.

| Monolithic (Bad) | Decomposed (Good) |
|-------------------|--------------------|
| "Write a complete marketing plan" | 1. Market analysis → 2. Positioning → 3. Channel strategy → 4. Budget → 5. Timeline |
| "Build a full-stack app" | 1. Data model → 2. API endpoints → 3. Frontend components → 4. Auth → 5. Deployment |
| "Research and write a paper" | 1. Literature review → 2. Outline → 3. Draft sections → 4. Conclusion → 5. Edit |

## The Decomposition Pattern

```
Step 1: [Foundation task — produces context for later steps]
        ↓ output feeds →
Step 2: [Building task — uses Step 1 output as input]
        ↓ output feeds →
Step 3: [Refinement task — uses Step 2 output as input]
        ↓ output feeds →
Step N: [Integration task — combines all outputs]
```

## Decomposition Strategies

### Sequential (Linear Chain)
Each step depends on the previous. Best for building up complexity.

### Parallel + Merge
Independent sub-tasks executed separately, then combined.
Best when sub-tasks don't depend on each other.

### Iterative Refinement
Same task repeated with increasing specificity.
Best for creative or design tasks.

## Anti-Pattern: Over-Decomposition
Don't break a task into 15 micro-steps when 4 would suffice. Each decomposition step adds overhead. The sweet spot is usually 3-6 steps for most tasks.
