# Task Sizing Guidelines

This document provides detailed guidance on sizing tasks appropriately. The core principle: **always prefer small and medium tasks over large tasks**.

## Task Size Definitions

### Small Task (15-45 minutes)

- 1-3 file changes
- 20-80 lines of code
- Single responsibility focus
- Clear, immediate completion criteria

**Examples:**

- Create User model with email/password fields
- Add password hashing with bcrypt
- Create login endpoint
- Add JWT token generation
- Create Dashboard layout component
- Build StatsCard widget

### Medium Task (1-2 hours)

- 3-6 file changes
- 80-200 lines of code
- Cohesive functionality unit
- Testable in isolation

**Examples:**

- Implement payment intent endpoint with Stripe
- Create authentication middleware with error handling
- Build PaymentForm component with validation
- Add webhook handler for payment events

### Large Task (3+ hours) - AVOID

- 7+ file changes
- 200+ lines of code
- Multiple responsibilities
- Difficult to test in isolation

**Signs a task is too large:**

- Requires changes to 7+ files
- Involves 200+ lines of code
- Takes more than 2 hours to complete
- Has vague or multiple responsibilities
- Cannot be tested in isolation

## Why Small/Medium Tasks Are Better

1. **Easier to estimate** - More predictable completion time
2. **Faster feedback loops** - See progress quickly
3. **Simpler to test** - Each task has focused test scope
4. **Better for tracking** - Clear checkpoints show real progress
5. **Easier to debug** - Smaller scope when issues arise
6. **Less overwhelming** - Builds momentum and confidence
7. **Clearer acceptance criteria** - Simpler to verify completion

## Breaking Down Large Tasks

When a large task is identified, decompose it using this process:

### Step 1: Stop

Do not include the large task in the task list.

### Step 2: Decompose

Break it into 3-7 smaller tasks by:

- Separating by layer (model, controller, view)
- Splitting by functionality (create, read, update, delete)
- Dividing by component (form, list, detail)
- Breaking by integration point (API setup, webhook, UI)

### Step 3: Sequence

Order the smaller tasks logically:

- Foundation tasks first (models before controllers)
- Dependencies before dependents
- Shared code before consuming code

### Step 4: Verify

Ensure each smaller task is small or medium. If any resulting task is still large, repeat the decomposition.

## Decomposition Examples

### Example 1: Authentication System

**Before (Large Task):**

```markdown
- [ ] Build entire user authentication system
```

**After (Small/Medium Tasks):**

```markdown
- [ ] Create User model with email/password fields (SMALL)
- [ ] Add password hashing with bcrypt (SMALL)
- [ ] Create login endpoint (SMALL)
- [ ] Create registration endpoint (SMALL)
- [ ] Add JWT token generation (SMALL)
- [ ] Create authentication middleware (MEDIUM)
- [ ] Add password reset flow (MEDIUM)
```

### Example 2: Dashboard Feature

**Before (Large Task):**

```markdown
- [ ] Implement complete dashboard with all widgets
```

**After (Small/Medium Tasks):**

```markdown
- [ ] Create Dashboard layout component (SMALL)
- [ ] Build StatsCard widget (SMALL)
- [ ] Build RecentActivity widget (SMALL)
- [ ] Build UserProfile widget (SMALL)
- [ ] Add dashboard data fetching (MEDIUM)
- [ ] Connect widgets to data (MEDIUM)
- [ ] Add dashboard responsive styling (SMALL)
```

### Example 3: Payment Integration

**Before (Large Task):**

```markdown
- [ ] Build payment system
```

**After (Small/Medium Tasks):**

```markdown
- [ ] Add Stripe API credentials to environment (SMALL - 30 min)
- [ ] Create Payment model and migration (SMALL - 45 min)
- [ ] Create payment intent endpoint (MEDIUM - 90 min)
- [ ] Create payment confirmation endpoint (MEDIUM - 90 min)
- [ ] Add Stripe webhook handler (MEDIUM - 2 hours)
- [ ] Create PaymentForm component (MEDIUM - 90 min)
- [ ] Add payment success/failure pages (SMALL - 45 min)
```

### Example 4: Search Feature

**Before (Large Task):**

```markdown
- [ ] Add search functionality to the application
```

**After (Small/Medium Tasks):**

```markdown
- [ ] Add search index to database tables (SMALL)
- [ ] Create SearchService with query logic (MEDIUM)
- [ ] Create search API endpoint (SMALL)
- [ ] Build SearchInput component (SMALL)
- [ ] Build SearchResults component (MEDIUM)
- [ ] Add search results highlighting (SMALL)
- [ ] Implement search pagination (MEDIUM)
```

## Task Verification Checklist

Before finalizing any task, verify:

- [ ] Can be completed in under 2 hours
- [ ] Involves fewer than 7 files
- [ ] Under 200 lines of code
- [ ] Has single, clear responsibility
- [ ] Can be tested in isolation
- [ ] Has clear acceptance criteria

If any item fails, decompose the task further.
