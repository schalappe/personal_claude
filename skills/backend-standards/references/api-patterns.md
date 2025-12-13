# API Design Patterns Reference

This reference provides comprehensive API design patterns, versioning strategies, and response structures for building robust REST APIs.

## API Versioning Strategies

### URL Path Versioning (Recommended)

Include version in the URL path for explicit versioning:

```text
/api/v1/users
/api/v2/users
```

**Advantages:**

- Explicit and visible
- Easy to route at load balancer level
- Clear in documentation and logs

**Implementation:**

```python
# FastAPI router with versioning
from fastapi import APIRouter

v1_router = APIRouter(prefix='/api/v1')
v2_router = APIRouter(prefix='/api/v2')

@v1_router.get('/users')
async def get_users_v1():
    return {'version': 1, 'users': [...]}

@v2_router.get('/users')
async def get_users_v2():
    return {'data': [...], 'meta': {...}}
```

### Header-Based Versioning

Use custom headers for version selection:

```text
Accept: application/vnd.api+json;version=2
X-API-Version: 2
```

**When to use:** Internal APIs where URL aesthetics matter.

### Query Parameter Versioning

Pass version as query parameter:

```text
/api/users?version=2
```

**When to use:** Quick prototyping only; avoid in production.

## Response Envelope Patterns

### Standard Success Response

```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

### Collection Response with Pagination

```json
{
  "data": [
    {"id": "1", "name": "Item 1"},
    {"id": "2", "name": "Item 2"}
  ],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total_pages": 5,
    "total_count": 100
  },
  "links": {
    "self": "/api/v1/items?page=1",
    "next": "/api/v1/items?page=2",
    "prev": null,
    "first": "/api/v1/items?page=1",
    "last": "/api/v1/items?page=5"
  }
}
```

### Error Response Structure

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
      },
      {
        "field": "age",
        "code": "OUT_OF_RANGE",
        "message": "Must be between 18 and 120"
      }
    ],
    "request_id": "req_abc123",
    "documentation_url": "https://api.example.com/docs/errors#VALIDATION_ERROR"
  }
}
```

### Error Code Taxonomy

Define consistent error codes:

| Code                      | HTTP Status | Description                      |
| ------------------------- | ----------- | -------------------------------- |
| `VALIDATION_ERROR`        | 400         | Input validation failed          |
| `AUTHENTICATION_REQUIRED` | 401         | Missing or invalid credentials   |
| `PERMISSION_DENIED`       | 403         | Insufficient permissions         |
| `RESOURCE_NOT_FOUND`      | 404         | Requested resource doesn't exist |
| `CONFLICT`                | 409         | Resource state conflict          |
| `RATE_LIMITED`            | 429         | Too many requests                |
| `INTERNAL_ERROR`          | 500         | Unexpected server error          |
| `SERVICE_UNAVAILABLE`     | 503         | Temporary unavailability         |

## Pagination Patterns

### Offset-Based Pagination

Simple but has performance issues with large datasets:

```text
GET /api/v1/users?page=5&per_page=20
```

**Implementation:**

```python
@router.get('/users')
async def list_users(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100)
):
    offset = (page - 1) * per_page
    users = await repo.get_users(offset=offset, limit=per_page)
    total = await repo.count_users()

    return {
        'data': users,
        'meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': ceil(total / per_page),
            'total_count': total
        }
    }
```

### Cursor-Based Pagination (Recommended for Large Datasets)

Use encoded cursors for consistent pagination:

```text
GET /api/v1/users?cursor=eyJpZCI6MTAwfQ&limit=20
```

**Implementation:**

```python
import base64
import json

def encode_cursor(data: dict) -> str:
    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.urlsafe_b64decode(cursor.encode()).decode())

@router.get('/users')
async def list_users(
    cursor: str | None = None,
    limit: int = Query(20, ge=1, le=100)
):
    if cursor:
        cursor_data = decode_cursor(cursor)
        users = await repo.get_users_after(cursor_data['id'], limit=limit + 1)
    else:
        users = await repo.get_users(limit=limit + 1)

    has_next = len(users) > limit
    users = users[:limit]

    next_cursor = None
    if has_next and users:
        next_cursor = encode_cursor({'id': users[-1].id})

    return {
        'data': users,
        'meta': {
            'has_next': has_next,
            'next_cursor': next_cursor
        }
    }
```

## Filtering and Sorting

### Query Parameter Filtering

```text
GET /api/v1/products?category=electronics&price_min=100&price_max=500&in_stock=true
```

**Implementation:**

```python
@router.get('/products')
async def list_products(
    category: str | None = None,
    price_min: float | None = Query(None, ge=0),
    price_max: float | None = Query(None, ge=0),
    in_stock: bool | None = None
):
    filters = ProductFilters(
        category=category,
        price_min=price_min,
        price_max=price_max,
        in_stock=in_stock
    )
    return await repo.get_products(filters)
```

### Sorting Parameters

```text
GET /api/v1/products?sort=price&order=desc
GET /api/v1/products?sort=-price,+name  # Shorthand notation
```

**Implementation:**

```python
from enum import Enum

class SortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'

@router.get('/products')
async def list_products(
    sort: str = 'created_at',
    order: SortOrder = SortOrder.DESC
):
    allowed_sorts = {'name', 'price', 'created_at', 'rating'}
    if sort not in allowed_sorts:
        raise HTTPException(400, f'Sort must be one of: {allowed_sorts}')

    return await repo.get_products(sort_by=sort, sort_order=order)
```

## Rate Limiting

### Response Headers

Include rate limit information in every response:

```text
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
Retry-After: 60  # Only on 429 responses
```

### Rate Limit Response

```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Rate limit exceeded",
    "details": {
      "limit": 1000,
      "remaining": 0,
      "reset_at": "2024-01-01T00:00:00Z",
      "retry_after_seconds": 60
    }
  }
}
```

## Bulk Operations

### Batch Create

```text
POST /api/v1/users/batch
```

```json
{
  "items": [
    {"email": "user1@example.com", "name": "User 1"},
    {"email": "user2@example.com", "name": "User 2"}
  ]
}
```

**Response with partial success:**

```json
{
  "data": {
    "created": [
      {"id": "1", "email": "user1@example.com"}
    ],
    "failed": [
      {
        "index": 1,
        "error": {
          "code": "DUPLICATE_EMAIL",
          "message": "Email already exists"
        }
      }
    ]
  },
  "meta": {
    "total": 2,
    "created_count": 1,
    "failed_count": 1
  }
}
```

### Batch Update/Delete

```text
PATCH /api/v1/users/batch
DELETE /api/v1/users/batch
```

```json
{
  "ids": ["1", "2", "3"],
  "updates": {
    "status": "inactive"
  }
}
```

## Content Negotiation

### Request Content-Type

```text
Content-Type: application/json
Content-Type: multipart/form-data  # For file uploads
```

### Response Accept Header

```text
Accept: application/json
Accept: text/csv
Accept: application/pdf
```

**Implementation:**

```python
from fastapi import Request
from fastapi.responses import JSONResponse, StreamingResponse

@router.get('/reports/{id}')
async def get_report(id: str, request: Request):
    report = await repo.get_report(id)

    accept = request.headers.get('accept', 'application/json')

    if 'text/csv' in accept:
        return StreamingResponse(
            generate_csv(report),
            media_type='text/csv',
            headers={'Content-Disposition': f'attachment; filename=report-{id}.csv'}
        )

    return JSONResponse(report.dict())
```

## Idempotency

### Idempotency Keys

For non-idempotent operations, accept client-provided keys:

```text
POST /api/v1/payments
Idempotency-Key: unique-request-id-123
```

**Implementation:**

```python
@router.post('/payments')
async def create_payment(
    payment: PaymentCreate,
    idempotency_key: str = Header(None, alias='Idempotency-Key')
):
    if idempotency_key:
        existing = await cache.get(f'idempotency:{idempotency_key}')
        if existing:
            return JSONResponse(existing, status_code=200)

    result = await payment_service.create(payment)

    if idempotency_key:
        await cache.set(
            f'idempotency:{idempotency_key}',
            result.dict(),
            ttl=86400  # 24 hours
        )

    return JSONResponse(result.dict(), status_code=201)
```

## HATEOAS Links

Include navigational links in responses:

```json
{
  "data": {
    "id": "123",
    "status": "pending"
  },
  "links": {
    "self": "/api/v1/orders/123",
    "cancel": "/api/v1/orders/123/cancel",
    "items": "/api/v1/orders/123/items",
    "customer": "/api/v1/customers/456"
  }
}
```

## API Documentation Standards

### OpenAPI/Swagger

Document every endpoint with:

- Summary and description
- Request/response schemas
- Example values
- Error responses
- Authentication requirements

```python
@router.post(
    '/users',
    response_model=UserResponse,
    status_code=201,
    summary='Create a new user',
    description='Creates a new user account with the provided details.',
    responses={
        201: {'description': 'User created successfully'},
        400: {'description': 'Invalid input data'},
        409: {'description': 'Email already exists'}
    }
)
async def create_user(user: UserCreate):
    """
    Create a new user with the following fields:

    - **email**: Valid email address (required)
    - **name**: Full name (required)
    - **password**: Minimum 8 characters (required)
    """
    pass
```

## Health Check Endpoints

### Liveness Probe

```text
GET /health/live
```

```json
{"status": "ok"}
```

### Readiness Probe

```text
GET /health/ready
```

```json
{
  "status": "ok",
  "checks": {
    "database": {"status": "ok", "latency_ms": 5},
    "cache": {"status": "ok", "latency_ms": 1},
    "external_api": {"status": "degraded", "latency_ms": 500}
  }
}
```
