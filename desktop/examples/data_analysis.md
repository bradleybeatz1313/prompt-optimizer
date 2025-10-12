# Data Analysis Example

## Original Prompt
> "analyze this data and tell me what you find"

## Optimized Prompt
> Analyze the attached dataset and identify the top 3 actionable insights.
>
> <context>
> This is our Q4 2025 customer churn data. Columns include: customer_id, signup_date, plan_tier, monthly_usage, support_tickets, churn_date (null if still active).
> </context>
>
> <instruction>
> 1. Calculate the overall churn rate and break down by plan tier
> 2. Identify the strongest predictors of churn (correlations between usage, support tickets, tenure, and churn)
> 3. Find any notable patterns or segments (e.g., "customers who filed 3+ tickets in their first month churn at 4x the base rate")
>
> Present findings as:
> - Executive summary (3 sentences)
> - Key metrics table
> - Top 3 insights with supporting data
> - Recommended actions for each insight
> </instruction>
>
> Think through the analysis step by step before presenting conclusions.

## What Changed
Added context engineering (dataset description), specified output structure (exec summary + table + insights), applied CoT for systematic analysis, and framed deliverables around actionable recommendations rather than raw findings.

## Techniques Applied
- Context Engineering → Dataset description
- Structured Output → 4-section format
- Chain of Thought → Step-by-step analysis
- Specificity → Exact deliverables defined
- Delimiters → XML tags separating context from instruction
