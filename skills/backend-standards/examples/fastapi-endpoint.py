"""
Example: Complete FastAPI endpoint with validation, error handling, and documentation.

This example demonstrates:
- Pydantic models for request/response validation
- Proper HTTP status codes
- Consistent error responses
- OpenAPI documentation
- Repository pattern integration
"""

from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, EmailStr, Field

router = APIRouter(prefix='/api/v1/users', tags=['users'])


# Request/Response Models
class UserCreate(BaseModel):
    """Request model for creating a user."""

    email: EmailStr = Field(..., description='User email address')
    name: str = Field(..., min_length=1, max_length=100, description='Full name')
    password: str = Field(..., min_length=8, description='Password (min 8 chars)')


class UserResponse(BaseModel):
    """Response model for user data."""

    id: str
    email: str
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    """Response model for paginated user list."""

    data: list[UserResponse]
    meta: dict


class ErrorDetail(BaseModel):
    """Error detail model."""

    code: str
    message: str
    field: str | None = None


class ErrorResponse(BaseModel):
    """Standard error response."""

    error: ErrorDetail


# Endpoints
@router.post(
    '',
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {'description': 'User created successfully'},
        400: {'model': ErrorResponse, 'description': 'Invalid input'},
        409: {'model': ErrorResponse, 'description': 'Email already exists'},
    },
    summary='Create a new user',
    description='Creates a new user account with email verification pending.',
)
async def create_user(
    user_data: UserCreate,
    repo: 'UserRepository' = Depends(get_user_repository),
):
    """
    Create a new user with the provided details.

    - **email**: Must be a valid, unique email address
    - **name**: User's full name (1-100 characters)
    - **password**: Minimum 8 characters
    """
    # ##>: Check for existing user before attempting insert.
    existing = await repo.get_by_email(user_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                'code': 'EMAIL_EXISTS',
                'message': 'A user with this email already exists',
                'field': 'email',
            },
        )

    user = await repo.create(
        id=str(uuid4()),
        email=user_data.email,
        name=user_data.name,
        password_hash=hash_password(user_data.password),
        created_at=datetime.now(UTC),
    )

    return user


@router.get(
    '',
    response_model=UserListResponse,
    summary='List users',
    description='Retrieve a paginated list of users.',
)
async def list_users(
    page: int = Query(1, ge=1, description='Page number'),
    per_page: int = Query(20, ge=1, le=100, description='Items per page'),
    is_active: bool | None = Query(None, description='Filter by active status'),
    repo: 'UserRepository' = Depends(get_user_repository),
):
    """
    List users with pagination and optional filtering.

    - **page**: Page number (starts at 1)
    - **per_page**: Number of items per page (1-100)
    - **is_active**: Optional filter for active/inactive users
    """
    filters = {}
    if is_active is not None:
        filters['is_active'] = is_active

    users, total = await repo.list_paginated(
        page=page,
        per_page=per_page,
        filters=filters,
    )

    return {
        'data': users,
        'meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': (total + per_page - 1) // per_page,
            'total_count': total,
        },
    }


@router.get(
    '/{user_id}',
    response_model=UserResponse,
    responses={404: {'model': ErrorResponse, 'description': 'User not found'}},
    summary='Get user by ID',
)
async def get_user(
    user_id: str,
    repo: 'UserRepository' = Depends(get_user_repository),
):
    """Retrieve a specific user by their ID."""
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'code': 'USER_NOT_FOUND',
                'message': f'User with ID {user_id} not found',
            },
        )
    return user


@router.patch(
    '/{user_id}',
    response_model=UserResponse,
    responses={
        404: {'model': ErrorResponse, 'description': 'User not found'},
        400: {'model': ErrorResponse, 'description': 'Invalid input'},
    },
    summary='Update user',
)
async def update_user(
    user_id: str,
    updates: dict,
    repo: 'UserRepository' = Depends(get_user_repository),
):
    """
    Partially update a user's information.

    Only provided fields will be updated.
    """
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'code': 'USER_NOT_FOUND',
                'message': f'User with ID {user_id} not found',
            },
        )

    # ##>: Validate allowed fields for update.
    allowed_fields = {'name', 'email'}
    invalid_fields = set(updates.keys()) - allowed_fields
    if invalid_fields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'code': 'INVALID_FIELDS',
                'message': f'Cannot update fields: {invalid_fields}',
            },
        )

    updated_user = await repo.update(user_id, updates)
    return updated_user


@router.delete(
    '/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'model': ErrorResponse, 'description': 'User not found'}},
    summary='Delete user',
)
async def delete_user(
    user_id: str,
    repo: 'UserRepository' = Depends(get_user_repository),
):
    """Delete a user by their ID."""
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'code': 'USER_NOT_FOUND',
                'message': f'User with ID {user_id} not found',
            },
        )

    await repo.delete(user_id)
    return None


# Placeholder functions (implement in actual application)
def get_user_repository():
    """Dependency injection for user repository."""
    raise NotImplementedError('Implement repository dependency')


def hash_password(password: str) -> str:
    """Hash password securely."""
    raise NotImplementedError('Implement password hashing')
