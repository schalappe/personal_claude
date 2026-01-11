# Architecture Patterns Reference

This reference provides detailed implementation patterns for clean architecture, repository pattern, and service layer design.

## Clean Architecture Implementation

### Directory Structure

```text
src/
├── presentation/       # UI/API layer
│   ├── routes/         # API endpoints
│   ├── schemas/        # Request/response schemas
│   └── middleware/     # Request processing
├── application/        # Use cases
│   └── services/       # Business logic orchestration
├── domain/             # Business logic
│   ├── models/         # Domain entities
│   ├── exceptions/     # Domain-specific errors
│   └── interfaces/     # Repository contracts
└── infrastructure/     # External
    ├── repositories/   # Data access implementations
    ├── clients/        # External service clients
    └── config/         # Configuration management
```

### Layer Responsibilities

**Presentation Layer:**

- Handle HTTP requests and responses
- Validate request format (not business rules)
- Transform data between external format and application format
- No business logic

**Application Layer:**

- Orchestrate use cases
- Coordinate between domain and infrastructure
- Handle transactions
- No direct database access

**Domain Layer:**

- Core business logic and rules
- Entity definitions and behavior
- Domain events
- No framework dependencies

**Infrastructure Layer:**

- Database operations
- External API clients
- File system operations
- Framework-specific implementations

## Repository Pattern

### Interface Definition

Define repository contracts in the domain layer:

```python
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass

    @abstractmethod
    async def delete(self, user_id: str) -> bool:
        pass
```

### Implementation

Implement in the infrastructure layer:

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, user_id: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        row = result.scalar_one_or_none()
        return self._to_entity(row) if row else None

    async def get_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        row = result.scalar_one_or_none()
        return self._to_entity(row) if row else None

    async def create(self, user: User) -> User:
        model = self._to_model(user)
        self._session.add(model)
        await self._session.flush()
        return self._to_entity(model)

    def _to_entity(self, model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            name=model.name,
            created_at=model.created_at
        )

    def _to_model(self, entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            email=entity.email,
            name=entity.name
        )
```

### Query Methods

Add specialized query methods as needed:

```python
class UserRepository(ABC):
    # ... basic CRUD methods

    @abstractmethod
    async def find_active_users(
        self,
        limit: int = 100,
        offset: int = 0
    ) -> list[User]:
        pass

    @abstractmethod
    async def count_by_status(self, status: UserStatus) -> int:
        pass

    @abstractmethod
    async def exists_with_email(self, email: str) -> bool:
        pass
```

## Service Layer Pattern

### Service Structure

```python
from dataclasses import dataclass

@dataclass
class UserService:
    user_repo: UserRepository
    email_client: EmailClient
    event_bus: EventBus

    async def register_user(
        self,
        email: str,
        name: str,
        password: str
    ) -> User:
        # Business rule: Check for existing user
        existing = await self.user_repo.get_by_email(email)
        if existing:
            raise BusinessRuleError('Email already registered')

        # Create user entity
        user = User.create(
            email=email,
            name=name,
            password_hash=hash_password(password)
        )

        # Persist
        created_user = await self.user_repo.create(user)

        # Side effects
        await self.email_client.send_welcome(created_user.email)
        await self.event_bus.publish(UserRegisteredEvent(created_user.id))

        return created_user
```

### Transaction Management

Handle transactions at service layer:

```python
class OrderService:
    def __init__(
        self,
        session: AsyncSession,
        order_repo: OrderRepository,
        inventory_repo: InventoryRepository,
        payment_service: PaymentService
    ):
        self._session = session
        self._order_repo = order_repo
        self._inventory_repo = inventory_repo
        self._payment_service = payment_service

    async def place_order(self, order: Order) -> OrderResult:
        async with self._session.begin():
            # Reserve inventory
            for item in order.items:
                await self._inventory_repo.reserve(
                    item.product_id,
                    item.quantity
                )

            # Process payment
            payment = await self._payment_service.charge(
                order.customer_id,
                order.total
            )

            # Create order
            order.payment_id = payment.id
            created_order = await self._order_repo.create(order)

            return OrderResult(
                order_id=created_order.id,
                payment_id=payment.id
            )
```

### Service Composition

Compose services for complex operations:

```python
class CheckoutService:
    def __init__(
        self,
        cart_service: CartService,
        order_service: OrderService,
        notification_service: NotificationService
    ):
        self._cart_service = cart_service
        self._order_service = order_service
        self._notification_service = notification_service

    async def checkout(self, customer_id: str) -> CheckoutResult:
        # Get cart
        cart = await self._cart_service.get_cart(customer_id)
        if cart.is_empty:
            raise BusinessRuleError('Cart is empty')

        # Create order
        order = cart.to_order()
        result = await self._order_service.place_order(order)

        # Clear cart
        await self._cart_service.clear_cart(customer_id)

        # Send confirmation
        await self._notification_service.send_order_confirmation(
            customer_id,
            result.order_id
        )

        return CheckoutResult(order_id=result.order_id)
```

## Dependency Injection

### Container Setup

```python
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Database
    db_engine = providers.Singleton(
        create_async_engine,
        config.database.url
    )

    db_session = providers.Factory(
        AsyncSession,
        bind=db_engine
    )

    # Repositories
    user_repository = providers.Factory(
        SQLAlchemyUserRepository,
        session=db_session
    )

    order_repository = providers.Factory(
        SQLAlchemyOrderRepository,
        session=db_session
    )

    # Services
    user_service = providers.Factory(
        UserService,
        user_repo=user_repository,
        email_client=email_client
    )
```

### FastAPI Integration

```python
from fastapi import Depends, FastAPI

app = FastAPI()
container = Container()

def get_user_service() -> UserService:
    return container.user_service()

@app.post('/users')
async def create_user(
    request: CreateUserRequest,
    service: UserService = Depends(get_user_service)
):
    user = await service.register_user(
        email=request.email,
        name=request.name,
        password=request.password
    )
    return UserResponse.from_entity(user)
```

## Error Handling Hierarchy

### Domain Exceptions

```python
class DomainError(Exception):
    """Base for all domain exceptions."""

class ValidationError(DomainError):
    """Input validation failures."""

class BusinessRuleError(DomainError):
    """Business rule violations."""

class EntityNotFoundError(DomainError):
    """Requested entity does not exist."""

class ConflictError(DomainError):
    """State conflict (duplicate, concurrent modification)."""
```

### Exception Mapping

Map domain exceptions to HTTP responses:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(EntityNotFoundError)
async def not_found_handler(request: Request, exc: EntityNotFoundError):
    return JSONResponse(
        status_code=404,
        content={'error': {'code': 'NOT_FOUND', 'message': str(exc)}}
    )

@app.exception_handler(BusinessRuleError)
async def business_rule_handler(request: Request, exc: BusinessRuleError):
    return JSONResponse(
        status_code=422,
        content={'error': {'code': 'BUSINESS_RULE', 'message': str(exc)}}
    )

@app.exception_handler(ConflictError)
async def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(
        status_code=409,
        content={'error': {'code': 'CONFLICT', 'message': str(exc)}}
    )
```

## Database Patterns

### Base Model

```python
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        server_default=func.now()
    )

class UUIDMixin:
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4())
    )

class BaseModel(Base, UUIDMixin, TimestampMixin):
    __abstract__ = True
```

### Query Optimization

Prevent N+1 queries with eager loading:

```python
from sqlalchemy.orm import selectinload

async def get_orders_with_items(user_id: str) -> list[Order]:
    result = await session.execute(
        select(Order)
        .where(Order.user_id == user_id)
        .options(selectinload(Order.items))
    )
    return result.scalars().all()
```

### Migration Best Practices

1. **One change per migration** - Single logical change only
2. **Always reversible** - Implement both up and down methods
3. **Never modify deployed** - Create new migrations instead
4. **Separate schema from data** - Keep DDL and DML separate

```python
# Safe column addition
def upgrade():
    op.add_column(
        'users',
        sa.Column('preferences', sa.JSON(), nullable=True)
    )

def downgrade():
    op.drop_column('users', 'preferences')
```
