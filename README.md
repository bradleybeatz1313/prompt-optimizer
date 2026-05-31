# ⚡ Prompt Optimizer

**Automatic prompt engineering for Claude — Desktop and Code editions**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Desktop%20%2B%20Code-DA8B45)
![License](https://img.shields.io/badge/License-MIT-blue)
![Techniques](https://img.shields.io/badge/Techniques-14-green)

![Hero Banner](assets/hero_banner.png)

A prompt optimization layer that analyzes and improves every substantive prompt before execution. Runs as the first step on any request involving content creation, code, analysis, research, or strategy, applies the most impactful techniques from a 14-technique framework, shows you what changed, then executes immediately.

**Two editions for two environments:**

| Edition | Environment | Techniques | Focus |
|---------|-------------|------------|-------|
| **Desktop** (v2.1) | Claude.ai web/mobile/desktop | 14 | Full framework with APE, multimodal, meta-prompting |
| **Code** (v2.0) | Claude Code terminal | 10 | Streamlined for speed, code-centric tasks |

---

## 🧠 How It Works

Every prompt passes through a 4-stage pipeline:

```
User Prompt
    ↓
Stage 1: Core Principles ─── Clarity, conciseness, positive framing, decomposition
    ↓
Stage 2: Technique Selection ─── Role, persona, delimiters, context engineering, structured output
    ↓
Stage 3: Reasoning Enhancement ─── CoT, step-back, Tree of Thoughts, ReAct (when applicable)
    ↓
Stage 4: Advanced ─── Meta-prompting, analogies, RAG awareness, iterative framing
    ↓
Output: Optimized prompt + "What changed" note → Immediate execution
```

The optimizer applies only what moves the needle. A simple email gets a light touch; a system architecture decision gets the full treatment.

## 📦 Quick Start

### Claude Code (recommended — 2 commands)

Install it as a plugin straight from this repo. Open Claude Code and run these two slash commands:

```text
/plugin marketplace add bradleybeatz1313/prompt-optimizer
/plugin install prompt-optimizer@prompt-optimizer
```

That's it. ✅ The optimizer activates automatically on your next substantive prompt.

**What each command does:**
1. `/plugin marketplace add bradleybeatz1313/prompt-optimizer` — registers this GitHub repo as a plugin marketplace.
2. `/plugin install prompt-optimizer@prompt-optimizer` — installs the `prompt-optimizer` plugin from that marketplace.

**Verify / manage:**
- `/plugin` — open the plugin manager UI to see it listed as installed
- `/prompt-optimizer:prompt-optimizer` — invoke the skill manually any time
- `/plugin marketplace update prompt-optimizer` — pull the latest version later

<details>
<summary>Other install methods for Claude Code (no plugin system)</summary>

```bash
# Install script
bash scripts/install_code.sh

# Or copy the skill file manually
cp code/SKILL.md ~/.claude/skills/prompt-optimizer/SKILL.md
```
</details>

### Claude Desktop / Claude.ai

```bash
# Option 1: Install script (copies to clipboard)
bash scripts/install_desktop.sh

# Option 2: Manual
# Copy contents of desktop/SKILL.md → Claude.ai Project → Custom Instructions
```

## 🎯 Before & After

**Before:** "write a blog post about AI"

**After:**
> Act as a technology journalist covering AI for a business audience.
>
> Write a 1,200-word blog post about how small businesses are using AI tools to automate customer service in 2026.
>
> Target audience: Small business owners (10-50 employees) with no technical background.
>
> Structure: Hook with a success story → 3-4 tools with pricing → Implementation steps → Common pitfalls → CTA
>
> Tone: Practical, encouraging, jargon-free. Use "you" directly.

**What changed:** Added role (tech journalist), specified audience (SMB owners), defined structure (5 sections), set word count (1,200), and narrowed the topic from "AI" to "customer service automation."

## 📁 Project Structure

```
prompt-optimizer/
├── .claude-plugin/          # Claude Code plugin system
│   ├── plugin.json          # Plugin manifest
│   └── marketplace.json     # Marketplace catalog (install via /plugin)
├── skills/                  # Plugin-shipped skills (auto-discovered)
│   └── prompt-optimizer/
│       └── SKILL.md         # Claude Code edition skill
├── desktop/                 # Claude Desktop edition
│   ├── SKILL.md             # Full 14-technique framework (v2.1)
│   ├── README.md            # Desktop-specific documentation
│   └── examples/            # Content creation, data analysis examples
├── code/                    # Claude Code edition
│   ├── SKILL.md             # Streamlined 10-technique framework (v2.0)
│   ├── README.md            # Code-specific documentation
│   └── examples/            # Code generation, debugging, refactoring examples
├── core/                    # Shared framework reference
│   ├── framework.md         # 4-stage pipeline documentation
│   ├── techniques.md        # Complete technique catalog
│   ├── power-verbs.md       # Verb replacement toolkit
│   └── anti-patterns.md     # Common mistakes and how to avoid them
├── benchmarks/              # Automated quality evaluation
│   ├── benchmark_runner.py  # Benchmark execution engine
│   ├── scoring.py           # Heuristic prompt scoring
│   └── datasets/            # Test datasets (code, writing, analysis)
├── evals/                   # Evaluation framework
│   ├── eval_framework.py    # Test case runner
│   └── test_cases.json      # Evaluation test cases
├── templates/               # Reusable prompt templates
│   ├── code_review.md       # Code review template
│   ├── research_analysis.md # Research analysis template
│   ├── content_brief.md     # Content brief template
│   ├── api_design.md        # API design template
│   ├── debugging.md         # Debugging template
│   └── strategy_decision.md # Strategic decision template
├── docs/                    # Extended documentation
│   ├── architecture.md      # System architecture
│   ├── migration-guide.md   # v1.x → v2.x migration
│   └── technique-deep-dives/
│       ├── chain-of-thought.md
│       ├── context-engineering.md
│       ├── role-prompting.md
│       └── decomposition.md
├── tests/                   # Unit tests
│   └── test_scoring.py
├── scripts/                 # Installation scripts
│   ├── install_desktop.sh
│   └── install_code.sh
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## 🧪 Benchmarks & Testing

```bash
# Run all benchmarks
cd benchmarks && python benchmark_runner.py --all

# Run unit tests
python -m pytest tests/ -v

# Run evals
cd evals && python eval_framework.py
```

## 🔧 The Technique Toolkit

| Technique | Stage | When to Use |
|-----------|-------|-------------|
| Clarity & Specificity | 1 | Always — sharpen vague prompts |
| Power Verbs | 1 | Replace weak verbs with precise action words |
| Positive Framing | 1 | Convert "don't do X" → "do Y instead" |
| Decomposition | 1 | 3+ deliverables crammed into one prompt |
| Role Prompting | 2 | Domain expertise would improve output |
| User Persona | 2 | Content calibrated for specific audience |
| Delimiters (XML) | 2 | Mixed content (instructions + context + data) |
| Context Engineering | 2 | Complex tasks needing rich background info |
| Structured Output | 2 | Machine-readable or schema-defined output |
| Chain of Thought | 3 | Multi-step reasoning, math, logic |
| Step-Back | 3 | Specific problem needs general principles first |
| Tree of Thoughts | 3 | Multiple viable approaches to evaluate |
| ReAct | 3 | Tool use or iterative information gathering |
| Self-Consistency | 3 | High-stakes decisions (Desktop only) |
| APE | 4 | Production prompt optimization (Desktop only) |
| Meta-Prompting | 4 | Prompts about prompts (Desktop only) |
| Multimodal | 4 | Text + image/code inputs (Desktop only) |

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
