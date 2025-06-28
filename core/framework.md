# Prompt Optimization Framework

The shared methodology powering both the Claude Desktop and Claude Code versions of the Prompt Optimizer.

## The 4-Stage Pipeline

Every prompt passes through four stages. The optimizer applies only what moves the needle for each specific request.

### Stage 1: Core Principles Check

Five foundations that every prompt must satisfy:

| Principle | Question | Action |
|-----------|----------|--------|
| Clarity | Is the prompt unambiguous? | Sharpen vague language, add format/audience/tone specifics |
| Conciseness | Is it specific without being wordy? | Replace weak verbs with power verbs, trim filler |
| Positive Framing | Does it tell the model what TO DO? | Convert "don't do X" into "do Y instead" |
| Decomposition | Is this multiple tasks in one? | Break into sequenced sub-tasks |
| Iteration Awareness | Is perfection expected in one shot? | Frame for strong first draft with refinement hooks |

### Stage 2: Technique Selection

Choose from the technique toolkit based on task type:

**Prompting Strategy**
- Zero-shot: Simple tasks the model handles well natively
- One-shot: Specific format needs one template example
- Few-shot (3-5): Pattern-matching accuracy is critical
- Many-shot (10-100+): Complex nuanced tasks with long-context models

**Structural Techniques**
- Role Prompting: Assign expert persona for domain expertise
- User Persona: Define the target audience explicitly
- Delimiters: XML tags, backticks, markers to separate sections
- Structured Output: JSON/XML/table schemas for machine-readable output
- System Prompting: Session-level behavioral framing

**Context Engineering (4-Layer Model)**
1. System prompts — foundational operational parameters
2. Retrieved knowledge — RAG, documents, prior conversations
3. Tool outputs — API results, database queries, real-time data
4. Implicit context — user identity, history, environment

### Stage 3: Reasoning Enhancement

For analysis, decision-making, and multi-step logic:

- **Chain of Thought (CoT)**: Step-by-step reasoning before final answer
- **Self-Consistency**: Multiple reasoning paths converging on best answer
- **Step-Back Prompting**: Establish general principles before specifics
- **Tree of Thoughts (ToT)**: Explore multiple approaches simultaneously
- **ReAct Pattern**: Thought → Action → Observation loops

### Stage 4: Advanced Enhancements

Applied selectively:

- Meta-Prompting: Optimizing prompts about prompts
- Analogies: Anchoring complex concepts to familiar frameworks
- Negative Examples: Last resort for stubborn failure modes
- RAG Awareness: Flag when retrieval would improve output
- Iterative Framing: Structure for refinement rather than perfection
- APE (Automatic Prompt Engineering): LLM-generated prompt candidates
- Code Prompting: Language/version/library-specific patterns

## Decision Matrix

| Task Type | Key Techniques | Reasoning | Complexity |
|-----------|---------------|-----------|------------|
| Simple Q&A | Zero-shot, clarity check | None | Light |
| Content creation | Role + persona + format | None | Medium |
| Code generation | Code prompting + decomposition | CoT | Medium |
| Data analysis | Structured output + context eng. | CoT + step-back | Heavy |
| Architecture design | Role + decomposition + context | ToT + self-consistency | Heavy |
| Research | RAG awareness + decomposition | Step-back + CoT | Heavy |
| Debugging | Code prompting + negative examples | ReAct | Medium |
| Strategy | Role + persona + context eng. | ToT + step-back | Heavy |

## Version Differences

| Feature | Desktop (v2.1) | Code (v2.0) |
|---------|---------------|-------------|
| Target environment | Claude.ai web/mobile | Claude Code terminal |
| Technique coverage | Full (14 techniques) | Streamlined (10 core) |
| System prompting | Included | Included |
| Context engineering | Full 4-layer model | Full 4-layer model |
| APE / meta-prompting | Included | Omitted (manual iteration) |
| Multimodal prompting | Included | Omitted (text-only focus) |
| Pydantic validation | Mentioned | Omitted |
| Output format | Markdown block | Markdown block |
| Activation threshold | Low (any substantive request) | Low (any substantive request) |
