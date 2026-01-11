# Common Testing Scenarios

This reference provides detailed guidance for testing specific scenarios. Load this reference when implementing tests for API endpoints, UI components, business logic, or database operations.

## Testing API Endpoints

### Happy Path Testing

Test valid input produces expected response:

```python
async def test_create_user_with_valid_data():
    response = await client.post("/users", json={
        "email": "test@example.com",
        "name": "Test User"
    })

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"
```

### Authentication Testing

Test protected endpoints require authentication:

```python
async def test_protected_endpoint_requires_auth():
    response = await client.get("/protected")
    assert response.status_code == 401

async def test_protected_endpoint_with_valid_token(auth_headers):
    response = await client.get("/protected", headers=auth_headers)
    assert response.status_code == 200
```

### Authorization Testing

Test role-based access:

```python
async def test_admin_endpoint_rejects_regular_user(user_token):
    response = await client.get("/admin/users", headers=user_token)
    assert response.status_code == 403

async def test_admin_endpoint_allows_admin(admin_token):
    response = await client.get("/admin/users", headers=admin_token)
    assert response.status_code == 200
```

### Critical Error Cases

Test important error scenarios:

```python
async def test_create_user_with_duplicate_email():
    # First user
    await client.post("/users", json={"email": "test@example.com", "name": "User 1"})

    # Duplicate email
    response = await client.post("/users", json={"email": "test@example.com", "name": "User 2"})

    assert response.status_code == 409
    assert "email" in response.json()["error"].lower()

async def test_get_nonexistent_user():
    response = await client.get("/users/99999")
    assert response.status_code == 404
```

### Request Validation

Test input validation for critical fields:

```python
async def test_create_user_with_invalid_email():
    response = await client.post("/users", json={
        "email": "not-an-email",
        "name": "Test User"
    })

    assert response.status_code == 422
    assert "email" in str(response.json()).lower()

async def test_create_user_with_missing_required_field():
    response = await client.post("/users", json={
        "name": "Test User"
        # Missing email
    })

    assert response.status_code == 422
```

### Pagination Testing

Test paginated endpoints:

```python
async def test_list_users_pagination(create_users):
    # Create 25 users
    await create_users(25)

    # First page
    response = await client.get("/users?page=1&per_page=10")
    assert len(response.json()["items"]) == 10
    assert response.json()["total"] == 25
    assert response.json()["page"] == 1

    # Last page
    response = await client.get("/users?page=3&per_page=10")
    assert len(response.json()["items"]) == 5
```

## Testing UI Components

### User Interaction Testing

Test main user interactions:

```typescript
// React Testing Library example
test('form submission calls onSubmit with form data', async () => {
  const onSubmit = jest.fn();
  render(<ContactForm onSubmit={onSubmit} />);

  await userEvent.type(screen.getByLabelText(/email/i), 'test@example.com');
  await userEvent.type(screen.getByLabelText(/message/i), 'Hello');
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));

  expect(onSubmit).toHaveBeenCalledWith({
    email: 'test@example.com',
    message: 'Hello'
  });
});
```

### Conditional Rendering

Test show/hide based on state:

```typescript
test('shows error message when form is invalid', async () => {
  render(<ContactForm />);

  // Submit without filling required fields
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));

  expect(screen.getByText(/email is required/i)).toBeInTheDocument();
});

test('hides error message after correction', async () => {
  render(<ContactForm />);

  await userEvent.click(screen.getByRole('button', { name: /submit/i }));
  expect(screen.getByText(/email is required/i)).toBeInTheDocument();

  await userEvent.type(screen.getByLabelText(/email/i), 'test@example.com');
  expect(screen.queryByText(/email is required/i)).not.toBeInTheDocument();
});
```

### Loading States

Test loading and loaded states:

```typescript
test('shows loading spinner while fetching data', async () => {
  render(<UserList />);

  expect(screen.getByRole('progressbar')).toBeInTheDocument();

  await waitFor(() => {
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument();
  });
});

test('renders user list after loading', async () => {
  render(<UserList />);

  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});
```

### Critical User Flows

Test end-to-end user journeys:

```typescript
test('user can complete checkout flow', async () => {
  render(<App />);

  // Add item to cart
  await userEvent.click(screen.getByRole('button', { name: /add to cart/i }));

  // Go to checkout
  await userEvent.click(screen.getByRole('link', { name: /checkout/i }));

  // Fill payment details
  await userEvent.type(screen.getByLabelText(/card number/i), '4242424242424242');

  // Complete purchase
  await userEvent.click(screen.getByRole('button', { name: /pay now/i }));

  // Verify success
  await waitFor(() => {
    expect(screen.getByText(/order confirmed/i)).toBeInTheDocument();
  });
});
```

## Testing Business Logic

### Core Calculations

Test calculations and transformations:

```python
def test_order_total_calculation():
    order = Order()
    order.add_item(Item("Widget", price=100, quantity=2))
    order.add_item(Item("Gadget", price=50, quantity=1))

    assert order.subtotal == 250
    assert order.total == 250

def test_order_total_with_discount():
    order = Order()
    order.add_item(Item("Widget", price=100, quantity=2))
    order.apply_discount(percentage=10)

    assert order.subtotal == 200
    assert order.discount == 20
    assert order.total == 180

def test_order_total_with_tax():
    order = Order()
    order.add_item(Item("Widget", price=100, quantity=1))
    order.apply_tax(rate=0.08)

    assert order.subtotal == 100
    assert order.tax == 8
    assert order.total == 108
```

### Validation Rules

Test critical validation logic:

```python
def test_password_validation_requires_minimum_length():
    result = validate_password("short")
    assert not result.is_valid
    assert "8 characters" in result.error

def test_password_validation_requires_uppercase():
    result = validate_password("alllowercase123")
    assert not result.is_valid
    assert "uppercase" in result.error.lower()

def test_password_validation_accepts_strong_password():
    result = validate_password("StrongPass123!")
    assert result.is_valid
```

### Decision Branches

Test main decision paths:

```python
def test_shipping_calculation_standard():
    order = Order(total=50, shipping_method="standard")
    assert calculate_shipping(order) == 5.99

def test_shipping_calculation_express():
    order = Order(total=50, shipping_method="express")
    assert calculate_shipping(order) == 15.99

def test_shipping_calculation_free_over_threshold():
    order = Order(total=100, shipping_method="standard")
    assert calculate_shipping(order) == 0
```

### State Transitions

Test state machine behavior:

```python
def test_order_state_transitions():
    order = Order()
    assert order.status == "pending"

    order.confirm()
    assert order.status == "confirmed"

    order.ship()
    assert order.status == "shipped"

    order.deliver()
    assert order.status == "delivered"

def test_order_cannot_ship_without_confirmation():
    order = Order()
    with pytest.raises(InvalidStateError):
        order.ship()
```

## Testing Database Operations

### CRUD Operations

Test basic database operations:

```python
async def test_create_user(db_session):
    user = User(email="test@example.com", name="Test User")
    db_session.add(user)
    await db_session.commit()

    assert user.id is not None
    assert user.created_at is not None

async def test_read_user(db_session, sample_user):
    user = await db_session.get(User, sample_user.id)

    assert user is not None
    assert user.email == sample_user.email

async def test_update_user(db_session, sample_user):
    sample_user.name = "Updated Name"
    await db_session.commit()

    user = await db_session.get(User, sample_user.id)
    assert user.name == "Updated Name"

async def test_delete_user(db_session, sample_user):
    await db_session.delete(sample_user)
    await db_session.commit()

    user = await db_session.get(User, sample_user.id)
    assert user is None
```

### Query Operations

Test critical queries:

```python
async def test_find_users_by_role(db_session, create_users):
    await create_users([
        {"email": "admin@example.com", "role": "admin"},
        {"email": "user1@example.com", "role": "user"},
        {"email": "user2@example.com", "role": "user"},
    ])

    admins = await user_repository.find_by_role("admin")
    assert len(admins) == 1
    assert admins[0].email == "admin@example.com"

async def test_search_users(db_session, create_users):
    await create_users([
        {"email": "john@example.com", "name": "John Doe"},
        {"email": "jane@example.com", "name": "Jane Smith"},
    ])

    results = await user_repository.search("john")
    assert len(results) == 1
    assert results[0].name == "John Doe"
```

### Relationship Testing

Test entity relationships:

```python
async def test_user_has_posts(db_session, sample_user):
    post1 = Post(title="First Post", author=sample_user)
    post2 = Post(title="Second Post", author=sample_user)
    db_session.add_all([post1, post2])
    await db_session.commit()

    user = await db_session.get(User, sample_user.id)
    assert len(user.posts) == 2

async def test_post_belongs_to_user(db_session, sample_user, sample_post):
    assert sample_post.author_id == sample_user.id
    assert sample_post.author.email == sample_user.email
```

### Constraint Testing

Test data integrity constraints:

```python
async def test_unique_email_constraint(db_session):
    user1 = User(email="test@example.com", name="User 1")
    db_session.add(user1)
    await db_session.commit()

    user2 = User(email="test@example.com", name="User 2")
    db_session.add(user2)

    with pytest.raises(IntegrityError):
        await db_session.commit()

async def test_foreign_key_constraint(db_session):
    post = Post(title="Orphan Post", author_id=99999)
    db_session.add(post)

    with pytest.raises(IntegrityError):
        await db_session.commit()
```

## Testing Async Code

### Async Functions

Test async operations:

```python
@pytest.mark.asyncio
async def test_async_user_creation():
    user = await create_user_async("test@example.com")
    assert user.id is not None

@pytest.mark.asyncio
async def test_concurrent_operations():
    results = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)
    )
    assert len(results) == 3
```

### Async Context Managers

Test async context managers:

```python
@pytest.mark.asyncio
async def test_database_transaction():
    async with database.transaction() as tx:
        user = await tx.create_user("test@example.com")
        await tx.commit()

    assert await database.get_user(user.id) is not None

@pytest.mark.asyncio
async def test_transaction_rollback():
    try:
        async with database.transaction() as tx:
            await tx.create_user("test@example.com")
            raise ValueError("Force rollback")
    except ValueError:
        pass

    assert await database.find_user_by_email("test@example.com") is None
```

## Testing Error Handling

### Exception Testing

Test expected exceptions:

```python
def test_division_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_invalid_input_raises_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        validate_email("not-an-email")

    assert "invalid email" in str(exc_info.value).lower()
```

### Error Recovery

Test error recovery behavior:

```python
async def test_retry_on_transient_error(mock_api):
    mock_api.side_effect = [ConnectionError(), ConnectionError(), {"data": "success"}]

    result = await fetch_with_retry(max_retries=3)

    assert result == {"data": "success"}
    assert mock_api.call_count == 3

async def test_fails_after_max_retries(mock_api):
    mock_api.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        await fetch_with_retry(max_retries=3)

    assert mock_api.call_count == 3
```

## Test Organization

### File Structure

Organize tests to mirror source structure:

```text
src/
├── services/
│   ├── user_service.py
│   └── order_service.py
└── repositories/
    └── user_repository.py

tests/
├── unit/
│   ├── services/
│   │   ├── test_user_service.py
│   │   └── test_order_service.py
│   └── repositories/
│       └── test_user_repository.py
└── integration/
    ├── test_user_flows.py
    └── test_order_flows.py
```

### Test Class Organization

Group related tests in classes:

```python
class TestUserRegistration:
    def test_valid_registration_succeeds(self):
        pass

    def test_duplicate_email_fails(self):
        pass

    def test_weak_password_fails(self):
        pass

class TestUserAuthentication:
    def test_valid_credentials_succeed(self):
        pass

    def test_invalid_password_fails(self):
        pass

    def test_locked_account_fails(self):
        pass
```

### Shared Fixtures

Centralize common fixtures:

```python
# conftest.py
@pytest.fixture
def sample_user():
    return User(id=1, email="test@example.com", name="Test User")

@pytest.fixture
async def db_session():
    async with AsyncSession(test_engine) as session:
        yield session
        await session.rollback()

@pytest.fixture
def auth_headers(sample_user):
    token = create_access_token(sample_user)
    return {"Authorization": f"Bearer {token}"}
```
