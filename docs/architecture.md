# Prompt Optimizer Architecture

## System Design

```
User Prompt
    │
    ▼
┌──────────────────┐
│  Activation Gate  │ ─── Skip: greetings, factual lookups, confirmations
└──────────────────┘
    │ Activate
    ▼
┌──────────────────┐
│ Stage 1: Core    │ ─── Clarity, Conciseness, Positive Framing,
│ Principles Check │     Decomposition, Iteration Awareness
└──────────────────┘
    │
    ▼
┌──────────────────┐
│ Stage 2: Tech    │ ─── Zero/Few-Shot, Role, Persona, Delimiters,
│ Selection        │     Context Eng., Structured Output, System Prompt
└──────────────────┘
    │
    ▼
┌──────────────────┐
│ Stage 3: Reason  │ ─── CoT, Self-Consistency, Step-Back, ToT, ReAct
│ Enhancement      │     (only for analysis/decision/multi-step logic)
└──────────────────┘
    │
    ▼
┌──────────────────┐
│ Stage 4: Advanced│ ─── Meta-Prompting, Analogies, Negative Examples,
│ Enhancements     │     RAG Awareness, Iterative Framing, APE
└──────────────────┘
    │
    ▼
┌──────────────────┐
│ Output           │ ─── Optimized prompt + "What changed" note
└──────────────────┘
    │
    ▼
┌──────────────────┐
│ Execute          │ ─── Run the optimized prompt immediately
└──────────────────┘
```

## Version Architecture

### Desktop Edition (v2.1)
Full pipeline with all 14 techniques. Optimized for Claude.ai where:
- Context windows are large (200K tokens)
- Conversations are interactive and iterative
- Multimodal inputs (images, PDFs) are supported
- Users expect visible optimization step before execution

### Code Edition (v2.0)
Streamlined pipeline with 10 core techniques. Optimized for Claude Code where:
- Speed matters more (terminal workflow)
- Tasks are predominantly code-centric
- Context comes from files and codebase
- Iteration is fast and manual

## Design Decisions

### Why Show the Optimized Prompt?
Transparency builds trust. Users learn prompt engineering by seeing what changed, and can course-correct if the optimization misinterpreted their intent.

### Why Execute Immediately?
The optimization step should feel like a natural enhancement, not a blocker. Showing the prompt AND the result in one turn keeps the workflow fast.

### Why Two Versions?
Different environments have different constraints. Desktop users benefit from the full technique library; Code users need speed and code-focused optimization. A single version would be either too heavy for Code or too limited for Desktop.
