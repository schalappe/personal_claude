---
name: testing-standards
version: "1.0.0"
description: This skill should be used when the user asks to "write tests", "add test coverage", "create unit tests", "write integration tests", "test this feature", "add tests for", "pytest patterns", "unittest patterns", "vitest setup", "AAA pattern", "mock vs stub", "test fixtures", "test file structure", or mentions testing strategies, test quality, test patterns, or code coverage. Provides strategic testing guidance emphasizing minimal, behavior-focused testing.
---

# Testing Standards

This skill provides focused testing standards that emphasize strategic, minimal testing during development. Apply these principles when writing tests to ensure code quality without over-testing or creating brittle test suites.

## Core Testing Philosophy

Follow a **minimal, strategic testing approach**:

- Complete features first, then add strategic tests
- Test only core user flows and critical paths
- Defer edge case testing until dedicated testing phases
- Write tests that verify behavior, not implementation
- Prioritize developer velocity while maintaining adequate quality assurance

## When to Write Tests

### Write Tests For

| Category                | Examples                                   |
| ----------------------- | ------------------------------------------ |
| Core user flows         | Login, checkout, registration              |
| Critical business logic | Revenue calculations, data transformations |
| Public APIs             | External interfaces others depend on       |
| Complex algorithms      | Non-trivial logic hard to verify manually  |
| Bug fixes               | Regression tests for confirmed bugs        |

### Skip Tests For

| Category                       | Reason                                |
| ------------------------------ | ------------------------------------- |
| Intermediate development steps | Code will change before completion    |
| Non-critical utilities         | Internal helper functions             |
| Edge cases                     | Unless business-critical or requested |
| Trivial getters/setters        | No logic to test                      |
| Framework behavior             | Test application code, not libraries  |

## Test Coverage Targets

During feature development:

| Level       | Coverage              | When to Use                              |
| ----------- | --------------------- | ---------------------------------------- |
| Minimum     | 1-2 integration tests | Core user flow only                      |
| Recommended | 3-5 tests total       | Main scenarios + 1-2 error cases         |
| Maximum     | 5-10 tests            | Add edge cases only if business-critical |

**Do not aim for high percentage coverage during development** - focus on critical path testing.

## Test Structure

Follow the **Arrange-Act-Assert** pattern:

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

## Test Naming Convention

Use descriptive names that explain:

- What is being tested
- Under what conditions
- Expected outcome

```python
# Good names
test_user_login_with_valid_credentials_succeeds
test_checkout_with_empty_cart_shows_error
test_search_returns_results_sorted_by_relevance

# Bad names
test_login
test_checkout
test_search
```

## Test Independence

Each test must:

- Run independently without depending on other tests
- Clean up after itself (reset state, clear mocks)
- Produce the same result every run (deterministic)
- Run in any order without affecting others

## Mocking Strategy

Mock external dependencies only:

| Dependency           | Mocking Approach                     |
| -------------------- | ------------------------------------ |
| Database calls       | In-memory DB or mocks                |
| API requests         | Mock HTTP responses                  |
| File system          | Mock file operations or use tmp_path |
| Third-party services | Mock service responses               |
| Time/dates           | Mock clock for predictable tests     |

Keep mocks simple and focused. Avoid excessive mocking that prevents testing real behavior.

## Testing Levels

### Unit Tests

Test individual functions or components:

- Fast execution (milliseconds)
- Isolated from external dependencies
- Focus on single units of code
- Mock all external calls

### Integration Tests

Test component interactions:

- Slower than unit tests (but still fast)
- Use real or realistic dependencies
- Verify data flow between components
- Test critical user flows end-to-end

### When to Use Each

| Test Type         | Use For                                               |
| ----------------- | ----------------------------------------------------- |
| Unit tests        | Complex algorithms, business logic, utility functions |
| Integration tests | User flows, API endpoints, database operations        |

Prefer integration tests for user-facing features and unit tests for isolated logic.

## Quick Reference: Patterns

### Prefer These Patterns

- **Behavior-focused tests** - Verify outcomes, not implementation
- **Minimal mocking** - Mock only external dependencies
- **Resilient assertions** - Verify core behavior, not presentation details
- **Fast feedback** - Tests run in milliseconds
- **Unique coverage** - Each test verifies a distinct scenario

### Avoid These Patterns

- **Testing implementation details** - Breaks on refactor
- **Excessive mocking** - Tests do not verify real behavior
- **Brittle assertions** - Depend on exact strings or fragile selectors
- **Slow tests** - Take seconds instead of milliseconds
- **Duplicate coverage** - Multiple tests for same scenario

For detailed pattern examples and anti-patterns, consult `references/patterns.md`.

## Testing Workflow

Recommended workflow when implementing features:

1. **Implement the feature** - Focus on getting it working first
2. **Identify critical paths** - Determine what must be tested
3. **Write minimal tests** - Cover core user flows only
4. **Verify tests pass** - Ensure tests are reliable and fast
5. **Move forward** - Do not add more tests unless requested

## Best Practices Summary

When writing tests:

1. **Complete features first** - Do not write tests for incomplete code
2. **Test behavior, not implementation** - Verify outcomes, not internal details
3. **Focus on critical paths** - Test main user flows, skip edge cases initially
4. **Keep tests fast** - Unit tests in milliseconds, integration tests in seconds
5. **Mock external dependencies** - Isolate code from databases, APIs, file systems
6. **Use clear test names** - Describe what is tested, conditions, and expected outcome
7. **Ensure test independence** - Tests must not depend on each other
8. **Avoid over-testing** - More tests ≠ better quality; strategic tests matter

## Additional Resources

### Reference Files

For detailed guidance, consult:

- **`references/patterns.md`** - Comprehensive anti-patterns and preferred patterns with code examples
- **`references/scenarios.md`** - Common testing scenarios for APIs, UI components, business logic, and database operations

### Integration with Other Skills

This skill works in conjunction with:

- **Global Standards** - Foundation for code quality and validation approaches
- **Backend Standards** - Testing strategies for API endpoints, database code
