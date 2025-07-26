# Role Prompting — Deep Dive

## What It Is
Assigning a specific expert persona to the model to frame tone, depth, and domain expertise. Changes how the model approaches the entire task.

## Effective Role Specifications

### Bad (Too Generic)
- "Act as an expert"
- "Be a helpful assistant"
- "You are smart"

### Good (Specific + Qualified)
- "Act as a senior DevOps engineer with 10 years of AWS experience"
- "Act as a tech journalist who covers enterprise AI for CIO Magazine"
- "Act as a seed-stage startup advisor who has evaluated 500+ pitch decks"

### Great (Specific + Qualified + Styled)
- "Act as a senior DevOps engineer with 10 years of AWS experience. Communicate in clear, direct language. When suggesting solutions, always include the tradeoffs and cost implications."

## The Formula
```
Role = [Seniority] + [Domain] + [Specialization] + [Communication Style]
```

## Common Roles by Task Type

| Task | Effective Role |
|------|---------------|
| Code review | Senior [language] developer at a FAANG company |
| Content writing | [Industry] journalist writing for [publication] |
| Strategy | Management consultant specializing in [domain] |
| Data analysis | Senior data scientist at a [type] company |
| API design | API architect who has designed systems at scale |
| Debugging | Staff engineer who debugs production issues |
| UX/UI | Senior product designer focused on [platform] |

## Role vs Persona
- **Role prompting** assigns an identity to the MODEL (who's writing)
- **Persona/audience** describes the TARGET READER (who's reading)
- Both can and should be used together when applicable
