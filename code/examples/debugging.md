# Debugging Example

## Original Prompt
> "my code doesn't work can you fix it"

## Optimized Prompt
> Debug this Python function that should calculate compound interest but returns incorrect results for periods > 12 months.
>
> ```python
> def compound_interest(principal, rate, periods):
>     return principal * (1 + rate) ** periods
> ```
>
> Expected: compound_interest(1000, 0.05, 24) should return ~2653.30
> Actual: returns ~3225.10
>
> The rate parameter is annual (5% = 0.05) and periods is in months. I think the issue is that the rate isn't being converted to monthly, but I'm not sure if that's the only problem.
>
> Identify the root cause, provide the corrected function, and add a test case that validates the fix.

## What Changed
Added the actual code, specified expected vs actual behavior, included the error hypothesis, and requested both the fix and a validation test. Applied code prompting patterns (language, function signature, test case).

## Techniques Applied
- Clarity → Expected vs actual behavior
- Code Prompting → Language, code, error description
- Specificity → Exact input/output values
- Iterative → Requested test case for validation
