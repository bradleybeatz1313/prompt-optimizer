---
name: prompt-optimizer
description: Use when receiving any substantive user request involving content creation, code, analysis, research, documents, automation, strategy, or data processing. Activates BEFORE any work begins. Skip only for casual greetings, simple factual lookups, brief follow-up confirmations, or explicit user opt-out.
---

# Prompt Optimizer

## Overview

A prompt optimization layer that analyzes and improves user prompts before execution. Runs as the FIRST step on every substantive request — analyzes the incoming prompt using a comprehensive framework, shows the user an improved version with a brief note on what changed, then executes it.

**Core principle:** Better to optimize unnecessarily than miss an opportunity to improve output quality.

## When to Activate

Activate on any substantive request — anything where the user wants Claude to produce, analyze, build, write, research, code, design, plan, or decide something. The threshold is low: if applying even one technique from the framework would improve the output, activate.

**Skip activation only when:**
- The message is a casual greeting or small talk
- It's a simple factual lookup with an obvious single answer
- It's a short follow-up in an already-optimized conversation thread ("yes", "do that", "looks good", "thanks")
- The user explicitly says to skip optimization

## The Optimization Pipeline

Run through these stages in order. Not every stage applies to every prompt — use judgment about which techniques will actually improve the specific request. The goal is a meaningfully better prompt, not a bloated one.

### Stage 1: Core Principles Check

Evaluate the original prompt against these four foundations:

**1. Clarity and Specificity**
Is the prompt unambiguous? Does it define the task, desired output format, and limitations? If vague, sharpen it. Add specifics about format, length, audience, tone, or constraints that the user likely intends but didn't state.

**2. Conciseness**
Is it specific without being wordy? Replace weak verbs with power verbs that direct precisely:

`Act, Analyze, Categorize, Classify, Compare, Create, Define, Evaluate, Extract, Generate, Identify, List, Organize, Predict, Rank, Recommend, Retrieve, Rewrite, Summarize, Translate, Write`

Choose the verb that most precisely matches what the user actually wants.

**3. Instructions Over Constraints**
Does the prompt tell the model what TO DO rather than what NOT to do? Positive instructions outperform negative constraints.

Transform: "Don't use technical jargon" -> "Explain in plain language a 10th grader would understand."

**4. Decomposition Check**
Is this actually multiple tasks crammed into one prompt? If so, break it into a sequenced plan where each step feeds the next. Factored cognition — executing sub-tasks separately and combining results — consistently outperforms monolithic prompts on complex requests.

### Stage 2: Technique Selection

Based on what the prompt is asking for, select and apply the most impactful techniques:

**Zero-Shot vs Few-Shot Decision**
- Task handled well out of the box? Leave as zero-shot.
- Specific or uncommon format needed? Add one example (one-shot).
- Accuracy on pattern-matching is critical? Add 3-5 diverse examples (few-shot). Ensure example quality is high. For classification, mix up class order across examples to prevent sequence bias.

**Role Prompting**
Assign a specific expert persona when domain expertise would improve the output. "Act as a senior SaaS pricing strategist" frames tone, depth, and communication style better than a generic request.

**Delimiters and Structure**
Add XML tags, triple backticks, or markers to separate instructions from context from input data. Claude responds particularly well to XML-style delimiters like `<instruction>`, `<context>`, `<input>`.

**Context Engineering**
The most impactful technique for complex requests. Evaluate whether the prompt would benefit from enriching any of these four context layers:
- **System-level framing:** foundational operational parameters
- **Retrieved knowledge:** information from documents, knowledge bases, or prior conversations
- **Tool/data context:** real-time data from APIs, files, or databases
- **Implicit context:** user identity, interaction history, environmental state

The quality of output depends more on the richness of provided context than on prompt phrasing alone.

**Structured Output**
If the output needs to be machine-readable or feed into another system, specify the exact format (JSON, XML, Markdown with specific headers, table structure). For programmatic data, define a schema.

**User Persona / Audience Definition**
If the prompt involves creating content for a specific audience, explicitly define that audience. "The target audience is small business owners with no technical background who want practical results they can implement in under 10 minutes" calibrates language, complexity, and examples far better than an unspecified audience.

### Stage 3: Reasoning Enhancement

For prompts involving analysis, decision-making, problem-solving, or multi-step logic:

**Chain of Thought (CoT)**
For multi-step reasoning tasks, instruct step-by-step thinking:
- *Zero-Shot CoT:* Add "Let's think step by step" or "Reason through this methodically before giving your answer."
- *Few-Shot CoT:* Show example problems with reasoning steps AND answers. More powerful for complex or domain-specific tasks.
- Place the final answer AFTER the reasoning, not before. Use low temperature for tasks with single correct answers.

**Self-Consistency**
For high-stakes decisions where accuracy matters more than speed, note that the request would benefit from exploring multiple reasoning paths and converging on the most consistent conclusion.

**Step-Back Prompting**
Before tackling a specific problem, first establish the general principles. Add a preliminary question about the broader framework, then apply it to the specific case.

Example: Before "Should I price at $99 or $149?" -> First ask "What are the key factors in SaaS pricing for SMB customers?" -> Then apply that framework.

**Tree of Thoughts (ToT)**
For decisions with multiple viable approaches, instruct the model to explore several reasoning paths simultaneously, evaluate each, and select the strongest. Useful for architecture decisions, strategy choices, and creative direction.

**ReAct Pattern (Reason + Act)**
For tasks requiring tool use or information gathering, structure as alternating Thought -> Action -> Observation loops. The model reasons about what it needs, takes an action, observes the result, then reasons again.

### Stage 4: Advanced Enhancements

Apply selectively when they'd provide clear value:

**Meta-Prompting**
If the user's prompt is about creating prompts, agents, or automation instructions, apply a meta-layer: have the optimization itself be optimized by considering what makes prompts effective for the specific downstream use case.

**Analogies and Framing**
When a complex concept needs to be made accessible, introduce an analogy that anchors the model to a familiar framework.

**Negative Examples (Use Sparingly)**
If a specific failure mode is predictable, add one targeted negative example showing what NOT to produce. Prefer positive instructions — use negative examples only as a last resort for stubborn patterns.

**RAG Awareness**
If the task would benefit from retrieving external knowledge (documents, files, web search), note this in the improved prompt so the execution step knows to gather context before generating.

**Iterative Framing**
For tasks where the first output is unlikely to be final (creative writing, design, strategy), frame the prompt to produce a strong first draft with explicit hooks for refinement rather than trying to nail perfection in one shot.

## Output Format

After optimizing, present the result in this format:

```
**Optimized Prompt:**

[The improved prompt, ready to execute]

**What changed:** [1-3 sentences explaining the key improvements]
```

Then immediately execute the optimized prompt and deliver the output.

## Important Principles

| Principle | Guideline |
|-----------|-----------|
| Don't over-optimize | A prompt that's already clear and well-structured might only need minor tweaks or none at all |
| Preserve intent | Never change WHAT the user is asking for — only improve HOW it's framed |
| Match complexity to task | Simple request = light touch. Complex request = full treatment |
| Speed matters | The optimization step should feel fast and lightweight to the user |
| Learn from conversation | Factor accumulated context into subsequent optimizations |

## Common Mistakes

- **Over-engineering simple prompts** — "write a thank you email" doesn't need Tree of Thoughts and Self-Consistency
- **Changing the user's intent** — optimization improves framing, not the request itself
- **Lengthy "what changed" notes** — keep it to 1-3 sentences max
- **Skipping execution** — always execute the optimized prompt immediately after presenting it
- **Applying every technique** — pick only the ones that genuinely move the needle for the specific request
