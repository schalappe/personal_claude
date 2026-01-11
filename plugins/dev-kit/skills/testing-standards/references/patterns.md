# Testing Patterns Reference

This reference provides detailed guidance on testing patterns to avoid and prefer. Load this reference when deeper pattern guidance is needed beyond the core SKILL.md content.

## Testing Anti-Patterns

### Patterns to Avoid

#### Testing Implementation Details

Tests that break when refactoring without changing behavior:

```python
# Anti-pattern: Testing internal implementation
def test_user_service_calls_repository():
    service = UserService()
    service.get_user(1)
    # Brittle: Breaks if implementation changes
    service.repository.find_by_id.assert_called_once_with(1)

# Better: Test the outcome
def test_get_user_returns_user_data():
    service = UserService()
    result = service.get_user(1)
    assert result.id == 1
    assert result.name is not None
```

#### Excessive Mocking

Mocking so much that tests do not verify real behavior:

```python
# Anti-pattern: Everything is mocked
def test_checkout_with_all_mocks():
    cart = Mock()
    payment = Mock()
    inventory = Mock()
    shipping = Mock()
    # Test verifies mocks, not real behavior
    checkout(cart, payment, inventory, shipping)

# Better: Mock only external dependencies
def test_checkout_with_real_logic():
    cart = Cart([Item("widget", 10)])
    payment = Mock()  # External service
    result = checkout(cart, payment)
    assert result.total == 10
```

#### Brittle Assertions

Tests that depend on exact string matches or fragile selectors:

```python
# Anti-pattern: Exact string matching
def test_error_message():
    result = validate_email("invalid")
    assert result.error == "The email address 'invalid' is not valid. Please enter a valid email address in the format user@domain.com"

# Better: Check essential parts
def test_error_message():
    result = validate_email("invalid")
    assert "not valid" in result.error.lower()
    assert "email" in result.error.lower()
```

#### Slow Tests

Tests that take seconds instead of milliseconds:

```python
# Anti-pattern: Real network calls
def test_api_integration():
    response = requests.get("https://api.example.com/users")  # Slow, flaky
    assert response.status_code == 200

# Better: Mock external calls
def test_api_integration(mock_requests):
    mock_requests.get.return_value = Mock(status_code=200)
    response = fetch_users()
    assert response.status_code == 200
```

#### Testing Frameworks

Testing library code instead of application code:

```python
# Anti-pattern: Testing SQLAlchemy behavior
def test_sqlalchemy_relationship():
    user = User()
    user.posts.append(Post())
    assert len(user.posts) == 1  # Tests SQLAlchemy, not app logic

# Better: Test business logic
def test_user_can_create_post():
    user = User()
    post = user.create_post("Title", "Content")
    assert post.author == user
    assert post.title == "Title"
```

#### Duplicate Coverage

Multiple tests covering the same scenario:

```python
# Anti-pattern: Same test with different names
def test_login_with_valid_credentials():
    result = login("user", "pass")
    assert result.success

def test_user_can_login():  # Duplicate
    result = login("user", "pass")
    assert result.success

def test_authentication_works():  # Another duplicate
    result = login("user", "pass")
    assert result.success
```

#### Test-First Everything

Writing tests before understanding requirements:

```python
# Anti-pattern: Tests written before feature is understood
def test_user_flow_step_1():
    pass  # Will change when requirements clarify

def test_user_flow_step_2():
    pass  # Premature abstraction

# Better: Implement feature first, then add strategic tests
```

## Preferred Patterns

### Behavior-Focused Tests

Tests that verify outcomes, not implementation:

```python
# Verify what the code does, not how
def test_order_total_includes_tax():
    order = Order([Item("widget", 100)])
    order.apply_tax(rate=0.1)
    assert order.total == 110  # Outcome, not implementation
```

### Minimal Mocking

Mock only external dependencies, not internal code:

```python
# Mock external services, use real internal logic
def test_payment_processing():
    payment_gateway = Mock()  # External service
    payment_gateway.charge.return_value = PaymentResult(success=True)

    order = Order([Item("widget", 100)])  # Real order logic
    result = process_payment(order, payment_gateway)

    assert result.success
    assert order.status == "paid"
```

### Resilient Assertions

Tests that verify core behavior, not presentation details:

```python
# Check essential properties, not exact format
def test_user_creation_response():
    response = create_user("john@example.com")

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "john@example.com"
    # Do not assert exact response structure
```

### Fast Feedback

Tests that run in milliseconds for rapid iteration:

```python
# Keep unit tests fast
def test_calculate_discount():
    # No I/O, no network, no database
    result = calculate_discount(100, percentage=10)
    assert result == 90
```

### Integration Tests

Tests that verify real component interactions:

```python
# Test real component interactions for critical flows
async def test_user_registration_flow(test_db):
    # Use real database (in-memory or test instance)
    user = await register_user(
        email="test@example.com",
        password="secure123"
    )

    # Verify in database
    stored_user = await get_user_by_email("test@example.com")
    assert stored_user.id == user.id
```

### Unique Coverage

Each test verifies a distinct scenario:

```python
# Each test has a unique purpose
def test_login_with_valid_credentials_succeeds():
    # Happy path
    pass

def test_login_with_invalid_password_fails():
    # Specific error case
    pass

def test_login_with_locked_account_shows_locked_message():
    # Different error scenario
    pass
```

### Feature-First Development

Implement features, then add strategic tests:

```python
# After feature is complete and stable:

def test_checkout_happy_path():
    """Core user flow - always test this."""
    cart = Cart([Item("widget", 100)])
    result = checkout(cart, valid_payment)
    assert result.success
    assert result.order_id is not None

def test_checkout_with_invalid_payment():
    """Critical error case - test this."""
    cart = Cart([Item("widget", 100)])
    result = checkout(cart, invalid_payment)
    assert not result.success
    assert "payment" in result.error.lower()
```

## Test Structure Patterns

### Arrange-Act-Assert

Standard test structure for clarity:

```python
def test_user_registration():
    # Arrange: Set up test data and conditions
    email = "test@example.com"
    password = "secure123"

    # Act: Execute the code being tested
    result = register_user(email, password)

    # Assert: Verify the expected outcome
    assert result.success
    assert result.user.email == email
```

### Given-When-Then (BDD Style)

Alternative structure for behavior-driven tests:

```python
def test_user_receives_welcome_email_after_registration():
    # Given: A new user with valid credentials
    user_data = {"email": "test@example.com", "password": "secure123"}

    # When: The user registers
    result = register_user(**user_data)

    # Then: A welcome email is sent
    assert email_service.sent_emails[-1].to == user_data["email"]
    assert "welcome" in email_service.sent_emails[-1].subject.lower()
```

### Test Fixtures

Reusable test setup:

```python
@pytest.fixture
def sample_user():
    """Reusable user fixture."""
    return User(
        id=1,
        email="test@example.com",
        name="Test User"
    )

@pytest.fixture
def authenticated_client(sample_user):
    """Client with authentication."""
    client = TestClient(app)
    client.login(sample_user)
    return client

def test_user_profile(authenticated_client, sample_user):
    response = authenticated_client.get("/profile")
    assert response.json()["email"] == sample_user.email
```

### Parameterized Tests

Test multiple inputs efficiently:

```python
@pytest.mark.parametrize("email,is_valid", [
    ("user@example.com", True),
    ("user@subdomain.example.com", True),
    ("invalid", False),
    ("@example.com", False),
    ("user@", False),
])
def test_email_validation(email, is_valid):
    result = validate_email(email)
    assert result.is_valid == is_valid
```

## Mocking Patterns

### Mock External Services

```python
@pytest.fixture
def mock_payment_gateway():
    with patch("app.services.payment_gateway") as mock:
        mock.charge.return_value = PaymentResult(success=True)
        yield mock

def test_checkout_charges_payment(mock_payment_gateway):
    order = Order(total=100)
    checkout(order)
    mock_payment_gateway.charge.assert_called_once_with(amount=100)
```

### Mock Time/Dates

```python
from freezegun import freeze_time

@freeze_time("2024-01-15 10:00:00")
def test_subscription_expires_after_30_days():
    subscription = create_subscription()
    assert subscription.expires_at == datetime(2024, 2, 14, 10, 0, 0)
```

### Mock File System

```python
def test_config_loading(tmp_path):
    # Create test config file
    config_file = tmp_path / "config.yaml"
    config_file.write_text("setting: value")

    # Test with real file operations
    config = load_config(config_file)
    assert config["setting"] == "value"
```

### Mock Database

```python
@pytest.fixture
async def test_db():
    """In-memory database for testing."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        yield session
```

## Coverage Guidance

### What to Cover

| Priority | Scenario | Coverage Target |
|----------|----------|-----------------|
| High | Core user flows | 100% |
| High | Critical business logic | 100% |
| Medium | Public APIs | 80%+ |
| Medium | Error handling for critical paths | 80%+ |
| Low | Edge cases | As needed |
| Low | Internal utilities | Minimal |

### What to Skip

- Trivial getters/setters
- Framework/library behavior
- Generated code
- Configuration files
- Simple data classes without logic
