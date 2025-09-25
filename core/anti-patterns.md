# Anti-Patterns and Common Mistakes

Patterns that degrade prompt quality, organized by severity.

## Critical Anti-Patterns

### 1. Changing the User's Intent
**The mistake:** Optimizing WHAT is requested instead of HOW it's framed.
**Example:** User asks "write a casual email" → Optimizer changes to "write a formal business letter"
**Fix:** Optimization improves framing. The deliverable, audience, and intent are sacred.

### 2. Over-Engineering Simple Prompts
**The mistake:** Applying Tree of Thoughts and Self-Consistency to "write a thank you email."
**Example:** Adding role prompting, few-shot examples, CoT, and structured output to a simple greeting.
**Fix:** Match technique complexity to task complexity. Most prompts need 1-2 techniques, not 10.

### 3. Skipping Execution
**The mistake:** Showing the optimized prompt but not actually running it.
**Fix:** Always execute immediately after presenting the optimization.

## Moderate Anti-Patterns

### 4. Verbose "What Changed" Notes
**The mistake:** Writing a 3-paragraph explanation of every technique applied.
**Fix:** 1-3 sentences max. The user wants results, not a prompt engineering lecture.

### 5. Negative-Heavy Framing
**The mistake:** "Don't use jargon, don't be verbose, don't use passive voice, don't..."
**Fix:** Convert to positive: "Write in plain language using active voice at a 10th-grade reading level."

### 6. Generic Role Assignments
**The mistake:** "Act as an expert" or "Act as a helpful assistant"
**Fix:** Be specific: "Act as a senior React developer who specializes in performance optimization"

### 7. Example Poisoning
**The mistake:** Including low-quality or incorrect examples in few-shot prompts.
**Fix:** Every example must be accurate, representative, and diverse. One bad example poisons the batch.

### 8. Sequence Bias in Few-Shot
**The mistake:** All positive examples first, all negative examples last (or vice versa).
**Fix:** Shuffle class order across examples to prevent the model from learning position = label.

## Subtle Anti-Patterns

### 9. Context Starvation
**The mistake:** Asking for something complex without providing the information needed to do it well.
**Fix:** Apply context engineering — enrich with system context, retrieved knowledge, tool outputs, and implicit context.

### 10. Format Ambiguity
**The mistake:** "Give me a structured output" without specifying the structure.
**Fix:** Define exact schema: field names, types, constraints, example output.

### 11. Monolithic Prompts
**The mistake:** Cramming 5 distinct tasks into one prompt.
**Signal:** If you can name 3+ distinct deliverables, it needs decomposition.
**Fix:** Break into sequential sub-tasks where each output feeds the next.

### 12. Temperature Mismatch
**The mistake:** Using high creativity settings for factual extraction, or low settings for brainstorming.
**Fix:** Low temp (0-0.3) for factual/deterministic tasks, higher (0.7-1.0) for creative tasks.

### 13. Premature Optimization
**The mistake:** Optimizing before trying the simple version.
**Fix:** Start zero-shot. Only escalate when the simple approach falls short.

## The Optimization Smell Test

Before delivering an optimized prompt, ask:
1. Did I preserve the user's intent exactly?
2. Is every technique I applied genuinely improving this specific request?
3. Would removing any technique hurt the output quality?
4. Is the optimized prompt shorter or equal length to what a bloated version would be?
5. Can I explain the improvement in under 2 sentences?

If any answer is "no," simplify.
