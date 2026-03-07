# Refactoring Example

## Original Prompt
> "refactor this code to be better"

## Optimized Prompt
> Refactor this Express route handler to follow separation of concerns.
>
> Current issues:
> - Business logic mixed with HTTP handling
> - Database queries inline with validation
> - No error handling
> - Hardcoded values
>
> ```javascript
> app.post('/users', async (req, res) => {
>   const { name, email } = req.body;
>   if (!name || !email) {
>     return res.status(400).json({ error: 'Missing fields' });
>   }
>   if (!email.includes('@')) {
>     return res.status(400).json({ error: 'Invalid email' });
>   }
>   const existing = await db.query('SELECT * FROM users WHERE email = $1', [email]);
>   if (existing.rows.length > 0) {
>     return res.status(409).json({ error: 'Email exists' });
>   }
>   const result = await db.query(
>     'INSERT INTO users (name, email, role) VALUES ($1, $2, $3) RETURNING *',
>     [name, email, 'user']
>   );
>   res.status(201).json(result.rows[0]);
> });
> ```
>
> Refactor into: controller (HTTP), service (business logic), and validation (input checking) layers. Keep Express as the framework. Show the refactored file structure.

## Techniques Applied
- Specificity → Named the exact issues and target architecture
- Code Prompting → Language, framework, current code
- Decomposition → Three-layer target structure
- Structured Output → File structure requested
