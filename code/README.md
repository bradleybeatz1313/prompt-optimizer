# Prompt Optimizer — Claude Code Edition

Streamlined prompt optimization skill for Claude Code terminal workflows.

## Overview

This version is optimized for the Claude Code environment — faster activation, focused on code-centric tasks, and trimmed of techniques that don't apply in terminal contexts (multimodal, APE). The core 4-stage pipeline and context engineering model are preserved.

## Features

- Streamlined 4-stage optimization pipeline
- 10 core techniques focused on code and technical tasks
- Context engineering with the 4-layer model
- RAG awareness for file/codebase context
- Iterative framing for development workflows

## Installation

### Claude Code Skills
```bash
# Copy into your skills directory
cp code/SKILL.md ~/.claude/skills/prompt-optimizer/SKILL.md
```

### Manual
Add to your Claude Code configuration:
```bash
claude config set skillsDir /path/to/skills
```

## Differences from Desktop Edition

The Code edition omits techniques that are less relevant in terminal contexts:
- APE / meta-prompting (manual iteration is faster in Code)
- Multimodal prompting (Code is text-only)
- Pydantic validation (implementation detail, not prompting)
- Many-shot beyond few-shot (context window management in Code)

All core optimization power is preserved.

## Examples

See `examples/` for code-specific optimization examples including generation, refactoring, debugging, and architecture tasks.
