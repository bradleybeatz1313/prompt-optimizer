# Migration Guide: v1.x → v2.x

## What Changed in v2.0

### New in v2.0
- **Context Engineering (4-Layer Model)** — The most impactful addition. Evaluates whether prompts need enrichment from system context, retrieved knowledge, tool outputs, or implicit context.
- **RAG Awareness** — Explicitly flags when retrieval would improve output quality.
- **Iterative Framing** — Structures prompts for refinement rather than one-shot perfection.
- **Common Mistakes section** — Explicit anti-pattern guidance.

### Changed in v2.0
- **Activation threshold lowered** — v1 only activated on "complex" requests. v2 activates on any substantive request where even one technique would help.
- **Output format simplified** — Removed the technique list; now just shows the optimized prompt + brief "what changed" note.
- **Technique selection streamlined** — Cleaner decision tree for choosing techniques.

### Removed in v2.0
- **Complexity scoring** — Replaced by the simpler light/medium/heavy classification.
- **Technique probability matrix** — Over-engineered; replaced by judgment-based selection.

## What Changed in v2.1 (Desktop Only)

### New in v2.1
- **APE (Automatic Prompt Engineering)** — For production systems, notes when LLM-based prompt optimization would be valuable.
- **Pydantic Validation Pattern** — Structured output enforcement for production pipelines.
- **Many-shot (10-100+)** — Guidance for long-context models that benefit from large example sets.
- **Multimodal Prompting** — Explicit handling of text + image + code inputs.
- **Code Prompting patterns** — Specialized patterns for generation, explanation, translation, and debugging.

## Upgrading

1. Replace the old SKILL.md with the new version
2. No configuration changes needed — the new version is backward compatible
3. The optimizer will automatically use new techniques when applicable
