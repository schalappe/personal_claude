---
name: backend-design
version: "1.0.0"
description: Design distinctive, well-structured REST APIs with intentional architecture. Use this skill when the user asks to "design an API", "create API endpoints", "structure an API", "design a REST API", "plan API resources", or mentions API architecture, endpoint design, or resource modeling.
---

# Backend Design

This skill guides creation of distinctive, well-structured REST APIs that avoid generic patterns. Design APIs with exceptional attention to resource modeling, response structures, and developer experience.

The user provides API requirements: endpoints to design, resources to model, or an API to architect. They may include context about consumers, constraints, or integration needs.

## Design Thinking

Before designing endpoints, understand the context and commit to a CLEAR design direction:

- **Purpose**: What problem does this API solve? Who consumes it?
- **Consumers**: Internal services, mobile apps, third-party developers, or all of these?
- **Constraints**: Performance requirements, authentication needs, versioning strategy.
- **Differentiation**: What makes this API a pleasure to use? What will developers remember?

**CRITICAL**: Choose a clear design philosophy and execute it consistently. Pragmatic simplicity and comprehensive completeness both work - the key is intentionality, not intensity.

Then design API specifications that are:

- Resource-centric and intuitive
- Consistent in naming, structure, and behavior
- Developer-friendly with clear error messages
- Future-proof with thoughtful versioning

## Core Design Principles

### Resource-First Thinking

Design around resources, not operations:

```text
# Good: Resource-centric
GET    /users/{id}
POST   /users
PATCH  /users/{id}
DELETE /users/{id}

# Bad: Operation-centric
POST   /getUser
POST   /createUser
POST   /updateUser
POST   /deleteUser
```

### URL Design Rules

| Rule              | Example                          | Rationale                        |
| ----------------- | -------------------------------- | -------------------------------- |
| Plural nouns      | `/users`, `/orders`              | Collections are plural           |
| Lowercase hyphens | `/user-profiles`, `/order-items` | Readable and URL-safe            |
| Shallow nesting   | `/users/{id}/orders`             | Max 2-3 levels deep              |
| Query for filters | `/products?category=electronics` | Resources in path, filters in QS |

### HTTP Methods

| Method | Purpose           | Request Body | Idempotent | Safe |
| ------ | ----------------- | ------------ | ---------- | ---- |
| GET    | Retrieve resource | No           | Yes        | Yes  |
| POST   | Create resource   | Yes          | No         | No   |
| PUT    | Replace resource  | Yes          | Yes        | No   |
| PATCH  | Partial update    | Yes          | Yes        | No   |
| DELETE | Remove resource   | No           | Yes        | No   |

### Status Codes

Design with appropriate status codes:

| Code | When to Use                              |
| ---- | ---------------------------------------- |
| 200  | Successful GET, PUT, PATCH               |
| 201  | Successful POST (resource created)       |
| 204  | Successful DELETE (no content)           |
| 400  | Invalid request format or validation     |
| 401  | Missing or invalid authentication        |
| 403  | Authenticated but not authorized         |
| 404  | Resource not found                       |
| 409  | Conflict (duplicate, state conflict)     |
| 422  | Valid format but business rule violation |
| 429  | Rate limit exceeded                      |
| 500  | Server error (never expose internals)    |

## Response Design

### Success Response Structure

```json
{
  "data": {
    "id": "usr_abc123",
    "type": "user",
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

### Collection Response with Pagination

```json
{
  "data": [
    {"id": "usr_abc123", "name": "John Doe"},
    {"id": "usr_def456", "name": "Jane Smith"}
  ],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total_pages": 5,
    "total_count": 100
  },
  "links": {
    "self": "/api/v1/users?page=1",
    "next": "/api/v1/users?page=2",
    "last": "/api/v1/users?page=5"
  }
}
```

### Error Response Structure

Design errors that help developers debug:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Must be a valid email address"
      }
    ],
    "request_id": "req_abc123",
    "documentation_url": "https://api.example.com/docs/errors"
  }
}
```

## API Design Guidelines

### Naming Conventions

- Use nouns for resources, never verbs
- Use consistent pluralization
- Avoid abbreviations: `/transactions` not `/txns`
- Use predictable patterns across all endpoints

### ID Design

Choose a consistent ID strategy:

| Type          | Example              | When to Use                  |
| ------------- | -------------------- | ---------------------------- |
| Prefixed UUID | `usr_abc123def456`   | Public APIs, debugging ease  |
| UUID          | `550e8400-e29b-41d4` | Standard uniqueness          |
| Sequential    | `12345`              | Internal only, never public  |

### Versioning Strategy

Use URL path versioning for explicit control:

```text
/api/v1/users
/api/v2/users
```

### Filtering and Sorting

Design consistent query patterns:

```text
# Filtering
GET /products?category=electronics&price_min=100&price_max=500

# Sorting
GET /products?sort=price&order=desc
GET /products?sort=-price,+name  # Shorthand notation

# Field selection
GET /users?fields=id,email,name
```

## Anti-Patterns to Avoid

NEVER design APIs with these patterns:

- **Verb-based URLs**: `/api/getUsers`, `/api/createOrder`
- **Inconsistent naming**: `/user` vs `/products` (mixed singular/plural)
- **Deep nesting**: `/users/{id}/orders/{id}/items/{id}/reviews`
- **Exposing internals**: Database IDs, table names, implementation details
- **Generic errors**: "Something went wrong" without context
- **Inconsistent response formats**: Different structures for similar resources

## Design Checklist

Before finalizing API design:

1. **Resources** - Clearly modeled around domain concepts
2. **URLs** - Consistent, predictable, and intuitive
3. **Methods** - Correct HTTP verbs for operations
4. **Status Codes** - Appropriate codes for all scenarios
5. **Responses** - Consistent envelope structure
6. **Errors** - Helpful, specific, and actionable
7. **Pagination** - Designed for large collections
8. **Versioning** - Strategy defined upfront

## Related Skills

Apply in conjunction with:

- **Global Standards** - Foundation for coding style and architecture patterns
- **Testing Standards** - Guide for testing API implementations

## Additional Resources

### Reference Files

For detailed patterns and examples, consult:

- **`references/api-patterns.md`** - Comprehensive API patterns including pagination, rate limiting, bulk operations, and content negotiation
- **`references/database-patterns.md`** - Database modeling patterns for API implementations

### Example Files

Working examples in `examples/`:

- **`examples/fastapi-endpoint.py`** - Complete FastAPI endpoint with validation
- **`examples/sqlalchemy-model.py`** - SQLAlchemy model with relationships
