# Global Standards - Detailed Patterns

This reference provides detailed patterns and examples for applying global development standards.

## Naming Patterns

### Variable and Function Naming

**Descriptive over concise:**

```text
# Good: Clear intent
user_authentication_service
calculate_monthly_revenue
is_valid_email_address

# Bad: Cryptic abbreviations
auth_svc
calc_rev
valid_em
```

### Python Naming

```python
# Variables/Functions: snake_case (descriptive > short)
verification_session = create_session()  # Good
vs = create_session()                    # Bad

# Classes: PascalCase (noun-based)
class VerificationSession:
    pass

# Constants: UPPERCASE
API_VERSION = "v1"
DEFAULT_TTL = 3600

# Enums: PascalCase class, UPPERCASE values
class VerificationDecision(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
```

### JavaScript/TypeScript Naming

```javascript
// Variables/Functions: camelCase
const userAccount = createAccount()

// Classes/Types: PascalCase
class UserAccount {}

// Constants: UPPERCASE
const MAX_RETRIES = 3
```

## Error Handling Patterns

### Python Exception Hierarchy

```python
class BaseError(Exception):
    """Base for all exceptions."""

class ValidationError(BaseError):
    """Input validation failures."""

class BusinessRuleError(BaseError):
    """Business rule violations."""

# Always chain exceptions
try:
    risky_operation()
except Exception as error:
    raise BusinessRuleError("Context about failure") from error
```

### Fail Fast Pattern

```python
def process_order(order: Order) -> Result:
    # Validate early, fail fast
    if not order.items:
        raise ValidationError("Order must contain at least one item")

    if order.total < 0:
        raise ValidationError("Order total cannot be negative")

    # Processing only happens after validation passes
    return _execute_order(order)
```

### Centralized Error Handling

```python
# Handle at boundaries, not scattered throughout code
@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "type": "validation"}
    )
```

### Retry with Exponential Backoff

```python
import asyncio
from typing import TypeVar, Callable

T = TypeVar('T')

async def with_retry(
    operation: Callable[[], T],
    max_attempts: int = 3,
    base_delay: float = 1.0
) -> T:
    for attempt in range(max_attempts):
        try:
            return await operation()
        except TransientError:
            if attempt == max_attempts - 1:
                raise
            delay = base_delay * (2 ** attempt)
            await asyncio.sleep(delay)
```

## Validation Patterns

### Server-Side Validation (Always Required)

```python
from pydantic import BaseModel, validator

class CreateUserRequest(BaseModel):
    email: str
    password: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v
```

### Allowlist Pattern

```python
# Good: Define what is allowed
ALLOWED_FILE_TYPES = {'pdf', 'png', 'jpg', 'jpeg'}

def validate_file_type(filename: str) -> bool:
    ext = filename.split('.')[-1].lower()
    return ext in ALLOWED_FILE_TYPES

# Bad: Try to block what is not allowed
BLOCKED_FILE_TYPES = {'exe', 'bat', 'sh', ...}  # Never complete
```

### Input Sanitization

```python
import html
from typing import Any

def sanitize_user_input(value: Any) -> str:
    """Sanitize user input to prevent XSS."""
    if value is None:
        return ''
    return html.escape(str(value))
```

### Business Rule Validation

```python
class OrderService:
    async def place_order(self, user_id: str, order: Order) -> OrderResult:
        # Business rule: Check sufficient balance
        user = await self.user_repo.get(user_id)
        if user.balance < order.total:
            raise BusinessRuleError("Insufficient balance")

        # Business rule: Check inventory
        for item in order.items:
            if not await self.inventory.is_available(item.product_id, item.quantity):
                raise BusinessRuleError(f"Product {item.product_id} not available")

        return await self._process_order(user, order)
```

## Code Commenting Patterns

### Comment Prefixes by Language

**Python:**

| Prefix    | Purpose                                           |
|-----------|---------------------------------------------------|
| `# ##!:`  | Warning, gotcha, pitfall, critical note           |
| `# ##>:`  | Explanation, reason, context, business logic      |
| `# ##?:`  | Question, uncertainty, needs review               |
| `# ##@:`  | TODO, future improvement, planned change          |
| `# ##~:`  | Workaround, hack, temporary fix                   |
| `# ##&:`  | Dependency, external API behavior, library quirk  |

**JavaScript/TypeScript:**

| Prefix     | Purpose                                           |
|------------|---------------------------------------------------|
| `// [!]:`  | Warning, gotcha, pitfall, critical note           |
| `// [>]:`  | Explanation, reason, context, business logic      |
| `// [?]:`  | Question, uncertainty, needs review               |
| `// [@]:`  | TODO, future improvement, planned change          |
| `// [~]:`  | Workaround, hack, temporary fix                   |
| `// [&]:`  | Dependency, external API behavior, library quirk  |

### Good vs Bad Comments

```python
# Bad: Restates what code does
x = x + 1  # Increment x

# Bad: Obvious variable description
user_id = 42  # The user ID

# Good: Explains why
# ##>: Use ceiling division to ensure partial pages still count as full page.
page_count = -(-total_items // page_size)

# Good: Documents non-obvious behavior
# ##&: Stripe API returns amounts in cents, must convert to dollars.
amount_dollars = stripe_response.amount / 100
```

### Documentation Style (Python NumPy)

```python
def process_payment(
    amount: Decimal,
    currency: str,
    idempotency_key: str
) -> PaymentResult:
    """
    Process a payment through the payment gateway.

    Parameters
    ----------
    amount : Decimal
        Payment amount in the specified currency.
    currency : str
        ISO 4217 currency code (e.g., 'USD', 'EUR').
    idempotency_key : str
        Unique key to prevent duplicate payments.

    Returns
    -------
    PaymentResult
        Contains transaction_id and status.

    Raises
    ------
    PaymentError
        If payment processing fails.
    """
```

## File Organization Patterns

### Size Limits

- **Files**: < 500 lines (split when larger)
- **Functions**: < 50 lines (extract when larger)
- **Classes**: > 100 lines should live in own module

### Import Organization (Python)

```python
# Standard library first
import os
from datetime import UTC, datetime

# Third-party packages second
from fastapi import FastAPI
from sqlalchemy import String

# Local application imports last
from app.config.settings import Settings
from app.models.base import BaseModel
```

### Clean Architecture Directory Structure

```text
src/
├── presentation/       # UI/API layer
│   ├── routes/
│   └── schemas/
├── application/        # Use cases
│   └── services/
├── domain/             # Business logic
│   ├── models/
│   └── exceptions/
└── infrastructure/     # External
    ├── repositories/
    └── clients/
```

## Anti-Patterns to Avoid

### Dead Code

```python
# Bad: Commented-out code
# def old_process():
#     pass

# Good: Delete it. Git has history if needed.
```

### Magic Numbers

```python
# Bad: Magic number
if user.age > 18:
    allow_access()

# Good: Named constant
MINIMUM_AGE = 18
if user.age > MINIMUM_AGE:
    allow_access()
```

### Deep Nesting

```python
# Bad: Deep nesting
def process(data):
    if data:
        if data.valid:
            if data.complete:
                return handle(data)
    return None

# Good: Early returns
def process(data):
    if not data:
        return None
    if not data.valid:
        return None
    if not data.complete:
        return None
    return handle(data)
```

### God Functions

```python
# Bad: Function doing too much
def process_order(order):
    # Validate order (20 lines)
    # Calculate totals (30 lines)
    # Apply discounts (25 lines)
    # Process payment (40 lines)
    # Send notification (15 lines)
    pass

# Good: Split into focused functions
def process_order(order):
    validated = validate_order(order)
    totals = calculate_totals(validated)
    discounted = apply_discounts(totals)
    payment = process_payment(discounted)
    send_notification(payment)
    return payment
```

## String Formatting

### Default to Single Quotes

```python
# Standard strings: single quotes
name = 'John'
message = 'Hello, world'

# Interpolation: double quotes with f-string
greeting = f"Hello, {name}"

# Multi-line: triple quotes
description = '''
This is a multi-line
string description.
'''
```

### JavaScript Template Literals

```javascript
// Simple strings: single quotes
const name = 'John'

// Interpolation: template literals
const greeting = `Hello, ${name}`

// Complex interpolation
const message = `User ${user.name} (${user.id}) logged in at ${timestamp}`
```
