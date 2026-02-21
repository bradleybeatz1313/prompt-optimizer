# Code Generation Example

## Original Prompt
> "build me a REST API for a todo app"

## Optimized Prompt
> Build a REST API for a todo application using Node.js with Express and PostgreSQL.
>
> Requirements:
> - CRUD endpoints for todos: GET /todos, GET /todos/:id, POST /todos, PUT /todos/:id, DELETE /todos/:id
> - Todo model: id (uuid), title (string, required), description (text, optional), completed (boolean, default false), created_at, updated_at
> - Input validation with Joi or Zod
> - Error handling middleware with consistent JSON error responses
> - Database migrations using Knex
>
> Structure the project as:
> ```
> src/
>   routes/todos.js
>   controllers/todosController.js
>   models/todo.js
>   middleware/errorHandler.js
>   db/migrations/
>   app.js
> ```
>
> Start with the database migration, then model, then routes. Include a sample .env and README with setup instructions.

## What Changed
Specified tech stack (Node/Express/PostgreSQL), defined the data model with field types, listed exact endpoints, added project structure, and sequenced the implementation order. Decomposed into migration → model → routes.

## Techniques Applied
- Specificity → Tech stack, model fields, endpoint paths
- Structured Output → Project directory structure
- Decomposition → Build order (migration → model → routes)
- Code Prompting → Language, framework, and library specifics
