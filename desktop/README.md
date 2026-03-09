# Prompt Optimizer — Claude Desktop Edition

The full-featured prompt optimization skill for Claude.ai (web/mobile/desktop).

## Overview

This version includes the complete 14-technique framework with all four optimization stages. Designed for the interactive Claude.ai experience where conversations are longer, context windows are larger, and multimodal inputs are supported.

## Features

- Full 4-stage optimization pipeline
- 14 techniques including APE, meta-prompting, and multimodal
- Context engineering with the 4-layer model
- System prompting guidance
- Pydantic validation pattern for structured output
- Many-shot prompting support (10-100+ examples)

## Installation

### Claude.ai Projects
1. Open a Claude.ai Project
2. Go to Project Settings → Custom Instructions
3. Paste the contents of `SKILL.md`

### Claude Desktop App
1. Open Settings → Custom Instructions
2. Paste the contents of `SKILL.md`

## Differences from Code Edition

| Feature | Desktop | Code |
|---------|---------|------|
| Technique count | 14 | 10 |
| APE / Meta-prompting | ✅ | ❌ |
| Multimodal prompting | ✅ | ❌ |
| Pydantic validation | ✅ | ❌ |
| Many-shot (100+) | ✅ | ❌ |
| Context engineering | Full 4-layer | Full 4-layer |
| Output format | Markdown block | Markdown block |

## Examples

See `examples/` for worked examples across content creation, code generation, data analysis, and research tasks.
