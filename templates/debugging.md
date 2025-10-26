# Debugging Template

```
<role>Act as a senior [LANGUAGE] developer debugging a production issue.</role>

<context>
What I expected: [EXPECTED BEHAVIOR]
What actually happens: [ACTUAL BEHAVIOR]
Error message: [PASTE ERROR/TRACEBACK]
Environment: [OS, runtime version, relevant dependencies]

Code:
```[LANGUAGE]
[PASTE RELEVANT CODE]
```

What I've already tried:
- [ATTEMPT 1]
- [ATTEMPT 2]
</context>

<instruction>
Debug this systematically:

1. Analyze the error message and identify the root cause
2. Explain WHY this error occurs (not just what it means)
3. Provide the exact fix with corrected code
4. Explain any related issues that might surface after this fix
5. Suggest a test case that would have caught this

Think through this step by step before providing the fix.
</instruction>
```
