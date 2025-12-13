---
name: backend-standards
version: "1.0.0"
description: This skill should be used when the user asks to "create an API endpoint", "design a REST API", "write a database model", "create a migration", "optimize a query", "implement a repository", "add database constraints", "repository pattern", "unit of work", "service layer", "dependency injection", "JWT authentication", "FastAPI structure", or mentions backend architecture, server-side logic, ORM code, or database operations.
---

# Backend Development Standards

This skill provides standards for backend development including API design, database modeling, migration management, and query optimization. Apply these principles when implementing server-side logic, data access layers, or API endpoints.

## When to Apply This Skill

Activate when:

- Creating or modifying API endpoints
- Designing database models or schemas
- Writing database migrations
- Implementing repository or service patterns
- Optimizing queries or database performance
- Working with database relationships and constraints

## Core API Design Principles

### RESTful Resource Design

Design APIs around resources using these conventions:

| Method | Purpose              | Example             | Success Code |
| ------ | -------------------- | ------------------- | ------------ |
| GET    | Retrieve resource(s) | `GET /users/123`    | 200          |
| POST   | Create resource      | `POST /users`       | 201          |
| PUT    | Replace resource     | `PUT /users/123`    | 200          |
| PATCH  | Partial update       | `PATCH /users/123`  | 200          |
| DELETE | Remove resource      | `DELETE /users/123` | 204          |

### URL Structure Rules

1. Use plural nouns for collections: `/users`, `/products`, `/orders`
2. Use lowercase with hyphens: `/user-profiles`, `/order-items`
3. Limit nesting to 2-3 levels: `/users/123/orders` (not deeper)
4. Use query parameters for filtering: `/products?category=electronics&sort=price`

### Response Conventions

Return consistent response structures:

```json
// Success response
{
  "data": { ... },
  "meta": { "page": 1, "total": 100 }
}

// Error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [...]
  }
}
```

## Database Model Standards

### Required Fields

Include on every table:

- `id` - Primary key (UUID or auto-increment)
- `created_at` - Timestamp with timezone
- `updated_at` - Timestamp with timezone (auto-update)

### Constraint Rules

Enforce data integrity at the database level:

1. **NOT NULL** - Apply to all required fields
2. **UNIQUE** - Apply to natural keys (email, username, slug)
3. **Foreign Keys** - Always define with appropriate CASCADE behavior
4. **Check Constraints** - Validate enums and value ranges

### Indexing Strategy

Index these columns:

- Foreign key columns (always)
- Columns in WHERE clauses
- Columns in ORDER BY clauses
- Columns in JOIN conditions
- Composite indexes for multi-column queries

## Migration Best Practices

### Migration Rules

1. **One change per migration** - Single logical change only
2. **Always reversible** - Implement both up and down methods
3. **Never modify deployed** - Create new migrations instead
4. **Separate schema from data** - Keep DDL and DML separate

### Zero-Downtime Patterns

For production deployments:

1. Add new columns as nullable first
2. Deploy code that handles both states
3. Backfill data in batches
4. Add NOT NULL constraint after backfill
5. Remove old code paths

## Query Optimization

### Prevent N+1 Queries

Always eager load related data:

```python
# Bad: N+1 queries
users = User.query.all()
for user in users:
    print(user.orders)  # Separate query per user

# Good: Eager loading
users = User.query.options(selectinload(User.orders)).all()
```

### Query Efficiency Rules

1. **Select specific columns** - Never use `SELECT *` in production
2. **Use parameterized queries** - Prevent SQL injection
3. **Set query timeouts** - Prevent runaway queries
4. **Paginate large results** - Use LIMIT/OFFSET or cursor pagination

## Architecture Patterns

### Repository Pattern

Isolate data access in repository classes:

```text
Service Layer (business logic)
    ↓
Repository Layer (data access)
    ↓
Database
```

### Service Layer Responsibilities

- Orchestrate repository calls
- Implement business logic
- Handle transactions
- Call external services

### Repository Responsibilities

- Execute queries
- Map data to models
- Handle database-specific logic
- Provide clean interfaces

## Error Handling

### Database Errors

Handle these categories:

| Error Type           | HTTP Code | Action               |
| -------------------- | --------- | -------------------- |
| Not Found            | 404       | Return clear message |
| Constraint Violation | 400/409   | Parse and explain    |
| Connection Error     | 503       | Retry with backoff   |
| Timeout              | 504       | Log and notify       |

### Transaction Safety

Wrap related operations:

```python
async with session.begin():
    await repo.create(order)
    await repo.update_inventory(items)
    await repo.create_payment(payment)
```

## Performance Checklist

Before deploying backend code:

- [ ] Indexes exist for query patterns
- [ ] N+1 queries eliminated
- [ ] Queries use parameterized values
- [ ] Transactions wrap related operations
- [ ] Error handling covers all cases
- [ ] Timeouts configured appropriately
- [ ] Large results paginated

## Integration with Other Skills

Apply in conjunction with:

- **Global Standards** - Foundation for coding style and error handling
- **Testing Standards** - Guide for testing backend code

## Additional Resources

### Reference Files

For detailed patterns and examples, consult:

- **`references/api-patterns.md`** - Comprehensive API design patterns, versioning strategies, and response structures
- **`references/database-patterns.md`** - Advanced database modeling, migration patterns, and query optimization techniques

### Example Files

Working examples in `examples/`:

- **`examples/fastapi-endpoint.py`** - Complete FastAPI endpoint with validation
- **`examples/sqlalchemy-model.py`** - SQLAlchemy model with relationships
- **`examples/alembic-migration.py`** - Reversible Alembic migration
