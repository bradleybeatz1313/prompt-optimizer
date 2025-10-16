# Code Review Template

```
<role>Act as a senior [LANGUAGE] developer conducting a thorough code review.</role>

<context>
[Paste the code to review here]
</context>

<instruction>
Review this code and provide feedback organized as:

1. **Critical Issues** — Bugs, security vulnerabilities, or logic errors that must be fixed
2. **Performance** — Bottlenecks, unnecessary allocations, or algorithmic improvements
3. **Readability** — Naming, structure, documentation, and code organization
4. **Best Practices** — Patterns, anti-patterns, and idiomatic usage for [LANGUAGE]
5. **Testing** — Missing test coverage, edge cases, or testability concerns

For each issue, provide:
- The specific line or section
- What the problem is
- A concrete fix with code

End with a 1-paragraph summary assessment.
</instruction>
```
