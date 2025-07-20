# Technique Reference Card

Quick-reference for all prompt optimization techniques supported by the framework.

## Prompting Strategy Spectrum

```
Zero-Shot ─── One-Shot ─── Few-Shot (3-5) ─── Many-Shot (10-100+)
  Simple         Format        Accuracy          Complex
  tasks          template      critical          nuanced
```

### When to Escalate

| Signal | Action |
|--------|--------|
| Model handles it fine natively | Stay zero-shot |
| Output format is wrong but content is right | Add one example (one-shot) |
| Pattern accuracy inconsistent | Add 3-5 diverse examples |
| Classification with bias toward recent examples | Shuffle class order across examples |
| Nuanced task with long-context model | Consider many-shot (10-100+) |

## Technique Catalog

### Role Prompting
**When:** Domain expertise would improve depth, tone, or accuracy.
**Pattern:** "Act as a [specific role with qualifications]"
**Example:** "Act as a senior DevOps engineer with 10 years of AWS experience"
**Pitfall:** Overly generic roles ("Act as an expert") add no value.

### User Persona / Audience Definition
**When:** Output needs to be calibrated for a specific reader.
**Pattern:** "The target audience is [specific description with context]"
**Example:** "The target audience is CTOs evaluating build-vs-buy for auth systems"
**Pitfall:** Don't confuse with role prompting — persona describes the reader, not the writer.

### Chain of Thought (CoT)
**When:** Multi-step reasoning, math, logic, causal analysis.
**Zero-shot CoT:** Append "Let's think step by step" or "Reason through this methodically."
**Few-shot CoT:** Provide example problems with full reasoning chains AND answers.
**Rule:** Place final answer AFTER reasoning, never before.

### Step-Back Prompting
**When:** Specific problem would benefit from general principles first.
**Pattern:** Ask about the general framework → Apply to the specific case.
**Example:** "What factors drive SaaS pricing for SMB?" → "Given those factors, should I price at $99 or $149?"

### Tree of Thoughts (ToT)
**When:** Multiple viable approaches exist and the best one isn't obvious.
**Pattern:** "Explore 3 different approaches to this problem. For each, outline the reasoning, identify tradeoffs, and recommend the strongest option."
**Best for:** Architecture decisions, strategy, creative direction.

### ReAct Pattern
**When:** Task requires tool use or iterative information gathering.
**Pattern:** Thought → Action → Observation → Thought → ...
**Example:** "I need to find the user's timezone → Check their profile settings → They're in PST → Calculate meeting time in their local zone"

### Self-Consistency
**When:** High-stakes decisions where accuracy matters more than speed.
**Pattern:** Generate multiple independent reasoning paths and converge on the most common conclusion.
**Best for:** Critical calculations, legal/medical reasoning, architectural decisions.

### Context Engineering (4-Layer Model)
**When:** Complex tasks where output quality depends on available information.
**Layers:**
1. System prompts — behavioral rules and constraints
2. Retrieved knowledge — documents, RAG, conversation history
3. Tool outputs — API responses, database results
4. Implicit context — user identity, preferences, environment

### Structured Output
**When:** Output feeds into another system or needs machine-readable format.
**Formats:** JSON, XML, CSV, Markdown tables, YAML
**Pattern:** Define the exact schema including field names, types, and constraints.

### Delimiters and Structure
**When:** Prompt contains mixed content (instructions + context + data).
**Pattern:** Use XML tags for Claude: `<instruction>`, `<context>`, `<input>`, `<output>`
**Rule:** Never rely on the model to figure out where instructions end and data begins.

### Decomposition
**When:** The prompt is actually 3+ tasks pretending to be one.
**Pattern:** Break into sequential sub-tasks where each output feeds the next.
**Signal:** If you can name 3+ distinct deliverables, decompose.

### Negative Examples (Last Resort)
**When:** Model keeps making a specific predictable mistake.
**Pattern:** Show one example of the wrong output with explanation of why it's wrong.
**Rule:** Always prefer positive instruction. Use this only for stubborn failure modes.
