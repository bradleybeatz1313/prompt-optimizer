# API Design Template

```
<role>Act as a senior API architect designing a RESTful API.</role>

<context>
Service: [SERVICE NAME AND PURPOSE]
Consumers: [WHO WILL USE THIS API]
Existing systems: [SYSTEMS THIS INTEGRATES WITH]
Scale expectations: [EXPECTED TRAFFIC/DATA VOLUMES]
</context>

<instruction>
Design the API with:

1. **Resource model** — Core resources and their relationships
2. **Endpoints** — Full list with HTTP methods, paths, and descriptions
3. **Request/Response schemas** — JSON schemas for each endpoint
4. **Authentication** — Auth strategy and token flow
5. **Error handling** — Standard error response format with codes
6. **Pagination** — Strategy for list endpoints
7. **Versioning** — API versioning approach
8. **Rate limiting** — Limits and headers

For each endpoint, provide:
- Method + Path
- Description
- Request body (if applicable)
- Success response with example JSON
- Error responses

Follow REST best practices: proper HTTP methods, plural nouns, consistent naming.
</instruction>
```
