"""
Example: SQLAlchemy model with relationships, constraints, and best practices.

This example demonstrates:
- Base model with common fields (id, timestamps)
- Proper relationship definitions with cascade
- Database-level constraints
- Index definitions
- Type annotations with Mapped
"""

from datetime import UTC, datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Base Classes
class Base(DeclarativeBase):
    """SQLAlchemy declarative base."""

    pass


class TimestampMixin:
    """Mixin providing created_at and updated_at timestamps."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        server_default=func.now(),
    )


class UUIDMixin:
    """Mixin providing UUID primary key."""

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )


class BaseModel(Base, UUIDMixin, TimestampMixin):
    """Abstract base model with id and timestamps."""

    __abstract__ = True


# Enums
class OrderStatus(str, Enum):
    """Order status enumeration."""

    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'


# Models
class User(BaseModel):
    """User account model."""

    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    # ##>: Soft delete support - nullable means not deleted.
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None,
    )

    # Relationships
    orders: Mapped[list['Order']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='selectin',
    )
    addresses: Mapped[list['Address']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='selectin',
    )

    __table_args__ = (
        Index('ix_users_email_lower', func.lower(email)),
        Index('ix_users_active', 'is_active', 'created_at'),
    )


class Address(BaseModel):
    """User address model."""

    __tablename__ = 'addresses'

    user_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    label: Mapped[str] = mapped_column(String(50), nullable=False)
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False)
    country: Mapped[str] = mapped_column(String(2), nullable=False)
    is_default: Mapped[bool] = mapped_column(default=False)

    # Relationships
    user: Mapped['User'] = relationship(back_populates='addresses')

    __table_args__ = (
        # ##>: Ensure only one default address per user.
        UniqueConstraint(
            'user_id',
            'is_default',
            name='uq_user_default_address',
            postgresql_where='is_default = true',
        ),
        CheckConstraint(
            "country ~ '^[A-Z]{2}$'",
            name='ck_address_country_iso',
        ),
    )


class Product(BaseModel):
    """Product model."""

    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(220), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    stock_quantity: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(default=True)

    __table_args__ = (
        CheckConstraint('price >= 0', name='ck_product_price_positive'),
        CheckConstraint('stock_quantity >= 0', name='ck_product_stock_positive'),
        Index('ix_products_active_price', 'is_active', 'price'),
    )


class Order(BaseModel):
    """Order model with relationships and constraints."""

    __tablename__ = 'orders'

    user_id: Mapped[str] = mapped_column(
        ForeignKey('users.id', ondelete='RESTRICT'),
        nullable=False,
        index=True,
    )
    shipping_address_id: Mapped[str | None] = mapped_column(
        ForeignKey('addresses.id', ondelete='SET NULL'),
        nullable=True,
    )
    status: Mapped[str] = mapped_column(
        String(20),
        default=OrderStatus.PENDING.value,
        nullable=False,
    )
    subtotal: Mapped[float] = mapped_column(default=0.0)
    tax: Mapped[float] = mapped_column(default=0.0)
    shipping: Mapped[float] = mapped_column(default=0.0)
    total: Mapped[float] = mapped_column(default=0.0)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    user: Mapped['User'] = relationship(back_populates='orders')
    shipping_address: Mapped['Address | None'] = relationship()
    items: Mapped[list['OrderItem']] = relationship(
        back_populates='order',
        cascade='all, delete-orphan',
        lazy='selectin',
    )

    __table_args__ = (
        # ##>: Validate status against enum values.
        CheckConstraint(
            f"status IN ({', '.join(repr(s.value) for s in OrderStatus)})",
            name='ck_order_valid_status',
        ),
        CheckConstraint('total >= 0', name='ck_order_total_positive'),
        Index('ix_orders_user_status', 'user_id', 'status'),
        Index('ix_orders_status_created', 'status', 'created_at'),
    )


class OrderItem(BaseModel):
    """Order line item model (many-to-many with extra fields)."""

    __tablename__ = 'order_items'

    order_id: Mapped[str] = mapped_column(
        ForeignKey('orders.id', ondelete='CASCADE'),
        nullable=False,
        index=True,
    )
    product_id: Mapped[str] = mapped_column(
        ForeignKey('products.id', ondelete='RESTRICT'),
        nullable=False,
        index=True,
    )
    quantity: Mapped[int] = mapped_column(default=1)
    unit_price: Mapped[float] = mapped_column(nullable=False)
    discount: Mapped[float] = mapped_column(default=0.0)

    # Relationships
    order: Mapped['Order'] = relationship(back_populates='items')
    product: Mapped['Product'] = relationship()

    __table_args__ = (
        UniqueConstraint('order_id', 'product_id', name='uq_order_product'),
        CheckConstraint('quantity > 0', name='ck_item_quantity_positive'),
        CheckConstraint('unit_price >= 0', name='ck_item_price_positive'),
        CheckConstraint('discount >= 0', name='ck_item_discount_positive'),
    )
