# Common Task Breakdown Patterns

This document provides patterns for breaking down different types of features into implementation tasks.

## Full-Stack CRUD Feature

A standard pattern for features that create, read, update, and delete data.

### Structure

1. **Database Layer** (models + migrations + associations)
2. **API Layer** (controllers + routes + auth + validation)
3. **Frontend Layer** (components + pages + styling)
4. **Testing Layer** (integration tests for critical workflows)

### Task Group Organization

#### Database Layer Tasks

```markdown
- [ ] Write 3-5 focused tests for model validations and associations
- [ ] Create model with fields and validations
- [ ] Create migration with indexes and foreign keys
- [ ] Set up model associations
- [ ] Run database layer tests
```

#### API Layer Tasks

```markdown
- [ ] Write 4-6 focused tests for controller actions
- [ ] Create controller with CRUD actions
- [ ] Add authentication and authorization
- [ ] Implement request validation
- [ ] Add response formatting
- [ ] Run API layer tests
```

#### Frontend Layer Tasks

```markdown
- [ ] Write 3-4 focused tests for components
- [ ] Create list view component
- [ ] Create detail view component
- [ ] Create form component with validation
- [ ] Add styling and responsive design
- [ ] Run UI tests
```

## Integration Feature

A pattern for features that connect to external services (Stripe, SendGrid, etc.).

### Structure

1. **Configuration** (API credentials + environment setup)
2. **Integration Layer** (API client + webhook handlers)
3. **Business Logic** (service layer + data transformations)
4. **Error Handling** (retry logic + failure notifications)
5. **Testing** (integration tests with mocked external calls)

### Task Group Organization

#### Configuration Tasks

```markdown
- [ ] Add API credentials to environment variables
- [ ] Install SDK packages
- [ ] Create client wrapper service
- [ ] Verify connection to external service
```

#### Integration Layer Tasks

```markdown
- [ ] Write 3-4 focused tests for API client
- [ ] Create API client with core methods
- [ ] Implement webhook endpoint
- [ ] Add webhook signature verification
- [ ] Handle webhook events
- [ ] Run integration tests
```

#### Business Logic Tasks

```markdown
- [ ] Write 4-5 focused tests for service layer
- [ ] Create service with business operations
- [ ] Implement data transformations
- [ ] Add error handling and logging
- [ ] Run service tests
```

## UI Enhancement Feature

A pattern for frontend-only features (theming, animations, responsive design).

### Structure

1. **Foundation** (CSS variables + context providers)
2. **Components** (UI components + interactions)
3. **Integration** (connect to existing components)
4. **Polish** (animations + transitions + accessibility)

### Task Group Organization

#### Foundation Tasks

```markdown
- [ ] Define CSS variables or theme tokens
- [ ] Create context provider for state management
- [ ] Set up persistence (localStorage, etc.)
```

#### Component Tasks

```markdown
- [ ] Write 2-3 focused tests for components
- [ ] Create primary UI component
- [ ] Create supporting components
- [ ] Add interactions and state handling
- [ ] Run component tests
```

#### Integration Tasks

```markdown
- [ ] Update existing components to use new system
- [ ] Apply changes across affected pages
- [ ] Test integration with existing features
```

## Real-Time Feature

A pattern for features requiring live updates (notifications, chat, collaboration).

### Structure

1. **Database Layer** (models for persistent data)
2. **API Layer** (REST endpoints for CRUD)
3. **WebSocket Layer** (channels + broadcasting)
4. **Service Layer** (business logic + event handling)
5. **Frontend Layer** (components + WebSocket connection)

### Task Group Organization

#### WebSocket Layer Tasks

```markdown
- [ ] Write 3-4 focused tests for channel
- [ ] Create WebSocket channel with authorization
- [ ] Implement broadcast job
- [ ] Configure WebSocket infrastructure (Redis, etc.)
- [ ] Add connection lifecycle handling
- [ ] Run WebSocket tests
```

#### Frontend Real-Time Tasks

```markdown
- [ ] Write 2-3 focused tests for WebSocket hook
- [ ] Create WebSocket connection hook
- [ ] Integrate with UI components
- [ ] Add connection state handling (loading, error, retry)
- [ ] Run real-time UI tests
```

## Background Job Feature

A pattern for features with async processing (imports, exports, reports).

### Structure

1. **Job Definition** (job class + queue configuration)
2. **Processing Logic** (service layer for actual work)
3. **Status Tracking** (model for job status)
4. **UI** (components for triggering and monitoring)

### Task Group Organization

#### Job Definition Tasks

```markdown
- [ ] Create job class with queue configuration
- [ ] Set up queue infrastructure
- [ ] Add job scheduling logic
```

#### Processing Logic Tasks

```markdown
- [ ] Write 3-4 focused tests for processing service
- [ ] Create service with processing logic
- [ ] Add chunked processing for large datasets
- [ ] Implement error handling and retries
- [ ] Run processing tests
```

#### Status Tracking Tasks

```markdown
- [ ] Create status model and migration
- [ ] Add status update callbacks in job
- [ ] Create API endpoint for status queries
```

## Multi-Tenant Feature

A pattern for features that vary by tenant/organization.

### Structure

1. **Database Layer** (tenant scoping + associations)
2. **Middleware Layer** (tenant resolution + scoping)
3. **API Layer** (tenant-aware endpoints)
4. **Testing** (multi-tenant scenarios)

### Task Group Organization

#### Database Layer Tasks

```markdown
- [ ] Add tenant_id to relevant models
- [ ] Create migration for tenant foreign key
- [ ] Add default scope for tenant filtering
- [ ] Create tenant model if needed
```

#### Middleware Layer Tasks

```markdown
- [ ] Write 2-3 focused tests for tenant middleware
- [ ] Create tenant resolution middleware
- [ ] Add tenant context to request
- [ ] Handle missing tenant scenarios
- [ ] Run middleware tests
```

## Dependency Patterns

### Linear Dependencies

When each layer depends on the previous:

```text
Database → API → Frontend → Testing
```

### Parallel Branches

When some work can happen concurrently:

```text
Database ─┬─→ API ─────┬─→ Integration Tests
          │           │
          └─→ Frontend─┘
```

### Integration Points

When external services need setup first:

```text
Configuration → Integration → [API + Frontend] → Testing
```

## Task Group Template

Use this template for each task group:

```markdown
#### Task Group N: [Name]
**Dependencies:** [None | Task Group X, Y]

- [ ] N.0 Complete [layer/feature name]
  - [ ] N.1 Write 2-8 focused tests for [functionality]
    - Test critical behavior 1
    - Test critical behavior 2
    - Test critical behavior 3
  - [ ] N.2 [Implementation task 1]
    - Detail A
    - Detail B
    - Reuse pattern from: [existing file]
  - [ ] N.3 [Implementation task 2]
  - [ ] N.4 Ensure tests pass
    - Run ONLY tests from N.1
    - Verify [specific functionality]

**Acceptance Criteria:**
- All N.1 tests pass
- [Specific technical requirement]
- [Specific functional requirement]
```

## Scaling Guidelines

### Small Feature (5-10 tasks)

- 1-3 task groups
- Focus on core functionality
- Minimal testing overhead

### Medium Feature (15-25 tasks)

- 3-5 task groups
- Standard layers (database, API, frontend)
- Focused testing per layer

### Large Feature (30+ tasks)

- 6+ task groups
- Split layers into sub-groups
- May have parallel work streams
- Comprehensive testing phase at end
