# Database Patterns Reference

This reference provides advanced database modeling patterns, migration strategies, and query optimization techniques.

## Database Model Patterns

### Base Model Pattern

Create a reusable base with common fields:

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

### Soft Delete Pattern

Track deletions without removing data:

```python
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

class SoftDeleteMixin:
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None
    )

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

    def soft_delete(self) -> None:
        self.deleted_at = datetime.now(UTC)

    def restore(self) -> None:
        self.deleted_at = None

# Repository method for soft delete filtering
class UserRepository:
    async def get_active_users(self) -> list[User]:
        return await self.session.execute(
            select(User).where(User.deleted_at.is_(None))
        )
```

### Audit Trail Pattern

Track all changes with full history:

```python
from sqlalchemy import JSON, DateTime, ForeignKey, String, event
from sqlalchemy.orm import Mapped, mapped_column

class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id: Mapped[int] = mapped_column(primary_key=True)
    table_name: Mapped[str] = mapped_column(String(100))
    record_id: Mapped[str] = mapped_column(String(36))
    action: Mapped[str] = mapped_column(String(10))  # INSERT, UPDATE, DELETE
    old_values: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    new_values: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    changed_by: Mapped[str | None] = mapped_column(String(36), nullable=True)
    changed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

# Event listener for automatic auditing
@event.listens_for(Session, 'before_flush')
def audit_changes(session, flush_context, instances):
    for obj in session.new:
        if hasattr(obj, '__audit__') and obj.__audit__:
            log = AuditLog(
                table_name=obj.__tablename__,
                record_id=str(obj.id),
                action='INSERT',
                new_values=obj.to_dict()
            )
            session.add(log)
```

### Enum Field Pattern

Store enums safely with database constraints:

```python
from enum import Enum

from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

class OrderStatus(str, Enum):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

class Order(BaseModel):
    __tablename__ = 'orders'

    status: Mapped[str] = mapped_column(
        String(20),
        default=OrderStatus.PENDING.value
    )

    __table_args__ = (
        CheckConstraint(
            status.in_([s.value for s in OrderStatus]),
            name='valid_order_status'
        ),
    )
```

## Relationship Patterns

### One-to-Many with Cascade

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(255), unique=True)

    # One user has many orders
    orders: Mapped[list['Order']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',  # Delete orders when user deleted
        lazy='selectin'  # Eager load by default
    )

class Order(BaseModel):
    __tablename__ = 'orders'

    user_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        index=True  # Always index foreign keys
    )

    user: Mapped['User'] = relationship(back_populates='orders')
```

### Many-to-Many with Association Table

```python
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship

# Association table (no model class needed)
product_categories = Table(
    'product_categories',
    Base.metadata,
    Column('product_id', ForeignKey('products.id', ondelete='CASCADE'), primary_key=True),
    Column('category_id', ForeignKey('categories.id', ondelete='CASCADE'), primary_key=True)
)

class Product(BaseModel):
    __tablename__ = 'products'

    categories: Mapped[list['Category']] = relationship(
        secondary=product_categories,
        back_populates='products',
        lazy='selectin'
    )

class Category(BaseModel):
    __tablename__ = 'categories'

    products: Mapped[list['Product']] = relationship(
        secondary=product_categories,
        back_populates='categories',
        lazy='selectin'
    )
```

### Many-to-Many with Extra Fields

When the relationship itself has attributes:

```python
class OrderItem(BaseModel):
    __tablename__ = 'order_items'

    order_id: Mapped[str] = mapped_column(
        ForeignKey('orders.id', ondelete='CASCADE'),
        primary_key=True
    )
    product_id: Mapped[str] = mapped_column(
        ForeignKey('products.id', ondelete='RESTRICT'),
        primary_key=True
    )

    # Extra fields on the relationship
    quantity: Mapped[int] = mapped_column(default=1)
    unit_price: Mapped[float] = mapped_column()
    discount: Mapped[float] = mapped_column(default=0.0)

    order: Mapped['Order'] = relationship(back_populates='items')
    product: Mapped['Product'] = relationship()

class Order(BaseModel):
    __tablename__ = 'orders'

    items: Mapped[list['OrderItem']] = relationship(
        back_populates='order',
        cascade='all, delete-orphan'
    )
```

### Self-Referential Relationship

For hierarchical data:

```python
class Category(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(100))
    parent_id: Mapped[str | None] = mapped_column(
        ForeignKey('categories.id', ondelete='SET NULL'),
        nullable=True
    )

    parent: Mapped['Category | None'] = relationship(
        remote_side='Category.id',
        back_populates='children'
    )
    children: Mapped[list['Category']] = relationship(
        back_populates='parent'
    )
```

## Migration Patterns

### Safe Column Addition

Add columns without breaking existing code:

```python
# Migration: add_user_preferences.py
def upgrade():
    # Step 1: Add nullable column
    op.add_column(
        'users',
        sa.Column('preferences', sa.JSON(), nullable=True)
    )

def downgrade():
    op.drop_column('users', 'preferences')
```

### Safe Column Removal

Remove columns in multiple deployments:

```python
# Migration 1: Stop writing to column (code change, no migration)

# Migration 2: Make column nullable
def upgrade():
    op.alter_column(
        'users',
        'legacy_field',
        existing_type=sa.String(100),
        nullable=True
    )

# Migration 3: Drop column (after code deployed)
def upgrade():
    op.drop_column('users', 'legacy_field')
```

### Safe Column Rename

Rename without downtime:

```python
# Migration 1: Add new column
def upgrade():
    op.add_column(
        'users',
        sa.Column('full_name', sa.String(200), nullable=True)
    )
    # Copy data
    op.execute('UPDATE users SET full_name = name')

# Code change: Write to both columns, read from new

# Migration 2: Make old column nullable
def upgrade():
    op.alter_column('users', 'name', nullable=True)

# Migration 3: Drop old column
def upgrade():
    op.drop_column('users', 'name')
```

### Index Creation on Large Tables

Create indexes without locking:

```python
def upgrade():
    # Use CONCURRENTLY to avoid locking (PostgreSQL)
    op.execute(
        'CREATE INDEX CONCURRENTLY ix_orders_created_at '
        'ON orders (created_at)'
    )

def downgrade():
    op.execute('DROP INDEX CONCURRENTLY ix_orders_created_at')
```

### Data Migration Pattern

Separate schema from data migrations:

```python
# Schema migration: create table
def upgrade():
    op.create_table(
        'user_settings',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('user_id', sa.String(36), sa.ForeignKey('users.id')),
        sa.Column('settings', sa.JSON(), nullable=False, server_default='{}')
    )

# Data migration: migrate data (separate file)
def upgrade():
    # Use raw SQL for performance
    op.execute('''
        INSERT INTO user_settings (id, user_id, settings)
        SELECT gen_random_uuid(), id, preferences
        FROM users
        WHERE preferences IS NOT NULL
    ''')
```

## Query Optimization

### Eager Loading Strategies

```python
from sqlalchemy.orm import joinedload, selectinload, subqueryload

# joinedload: Single query with JOIN (good for one-to-one/many-to-one)
users = await session.execute(
    select(User).options(joinedload(User.profile))
)

# selectinload: Separate IN query (good for one-to-many)
users = await session.execute(
    select(User).options(selectinload(User.orders))
)

# subqueryload: Subquery (good for complex filters)
users = await session.execute(
    select(User).options(subqueryload(User.orders))
)

# Nested eager loading
users = await session.execute(
    select(User)
    .options(
        selectinload(User.orders)
        .selectinload(Order.items)
        .joinedload(OrderItem.product)
    )
)
```

### Selecting Specific Columns

```python
# Only select needed columns
result = await session.execute(
    select(User.id, User.email, User.name)
    .where(User.is_active == True)
)

# Using load_only for relationships
result = await session.execute(
    select(User)
    .options(load_only(User.id, User.email))
    .options(
        selectinload(User.orders)
        .load_only(Order.id, Order.total)
    )
)
```

### Batch Operations

```python
# Batch insert
users_data = [{'email': f'user{i}@example.com'} for i in range(1000)]

await session.execute(
    insert(User),
    users_data
)

# Batch update
await session.execute(
    update(Order)
    .where(Order.status == 'pending')
    .where(Order.created_at < cutoff_date)
    .values(status='expired')
)

# Batch delete
await session.execute(
    delete(AuditLog)
    .where(AuditLog.created_at < retention_date)
)
```

### Query Result Caching

```python
from functools import lru_cache

import redis

redis_client = redis.Redis()

async def get_product(product_id: str) -> Product | None:
    # Try cache first
    cached = redis_client.get(f'product:{product_id}')
    if cached:
        return Product.parse_raw(cached)

    # Query database
    product = await session.get(Product, product_id)

    if product:
        # Cache for 5 minutes
        redis_client.setex(
            f'product:{product_id}',
            300,
            product.json()
        )

    return product

async def invalidate_product_cache(product_id: str):
    redis_client.delete(f'product:{product_id}')
```

### Pagination with Total Count

Efficient pagination with count:

```python
from sqlalchemy import func, select

async def paginate_users(
    page: int,
    per_page: int,
    filters: dict
) -> tuple[list[User], int]:
    # Build base query
    base_query = select(User).where(User.is_active == True)

    for key, value in filters.items():
        base_query = base_query.where(getattr(User, key) == value)

    # Get total count (separate query for performance)
    count_query = select(func.count()).select_from(base_query.subquery())
    total = await session.scalar(count_query)

    # Get paginated results
    offset = (page - 1) * per_page
    users_query = (
        base_query
        .order_by(User.created_at.desc())
        .offset(offset)
        .limit(per_page)
    )
    result = await session.execute(users_query)

    return result.scalars().all(), total
```

## Index Strategies

### Composite Indexes

Order matters - put high-cardinality columns first:

```python
from sqlalchemy import Index

class Order(BaseModel):
    __tablename__ = 'orders'

    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        # For queries: WHERE user_id = ? AND status = ?
        Index('ix_orders_user_status', 'user_id', 'status'),

        # For queries: WHERE status = ? ORDER BY created_at
        Index('ix_orders_status_created', 'status', 'created_at'),
    )
```

### Partial Indexes

Index only rows that matter:

```sql
-- Only index active orders
CREATE INDEX ix_orders_active ON orders (user_id, created_at)
WHERE status NOT IN ('cancelled', 'completed');

-- Only index unprocessed items
CREATE INDEX ix_queue_pending ON job_queue (priority, created_at)
WHERE processed_at IS NULL;
```

### Expression Indexes

Index computed values:

```sql
-- Index lowercase email for case-insensitive search
CREATE INDEX ix_users_email_lower ON users (LOWER(email));

-- Index date part for date-range queries
CREATE INDEX ix_orders_date ON orders (DATE(created_at));
```

## Connection Pooling

### SQLAlchemy Async Pool Configuration

```python
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(
    'postgresql+asyncpg://user:pass@localhost/db',
    pool_size=20,           # Minimum connections
    max_overflow=10,        # Extra connections allowed
    pool_timeout=30,        # Wait time for connection
    pool_recycle=1800,      # Recycle connections after 30 min
    pool_pre_ping=True,     # Verify connections before use
    echo=False              # Set True for SQL logging
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False
)
```

### Connection Context Manager

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_session():
    session = AsyncSessionLocal()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

# Usage
async def create_user(user_data: dict):
    async with get_session() as session:
        user = User(**user_data)
        session.add(user)
        # Auto-commits on exit
        return user
```

## Transaction Patterns

### Nested Transactions (Savepoints)

```python
async def complex_operation():
    async with session.begin():
        # Main transaction
        user = await create_user(...)

        try:
            async with session.begin_nested():
                # Savepoint - can rollback without affecting main tx
                await risky_operation()
        except RiskyOperationError:
            # Savepoint rolled back, main transaction continues
            await log_failure(...)

        # Main transaction commits
```

### Read-Only Transactions

```python
from sqlalchemy import text

async def get_report():
    # Start read-only transaction for consistency
    async with session.begin():
        await session.execute(text('SET TRANSACTION READ ONLY'))

        # All queries see consistent snapshot
        users = await get_active_users()
        orders = await get_pending_orders()
        metrics = await calculate_metrics()

        return ReportData(users=users, orders=orders, metrics=metrics)
```
