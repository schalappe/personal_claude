---
name: task-breakdown
description: This skill should be used when the user asks to "break down a spec into tasks", "create a task list", "plan implementation tasks", "organize development work", "structure feature development", "create implementation phases", or mentions task planning, task organization, or implementation ordering. Provides task sizing rules, templates, and testing strategy for implementation planning.
version: 0.1.0
---

# Task Breakdown Skill

Domain knowledge for transforming feature specifications into actionable implementation tasks. This skill provides the sizing rules, templates, and quality standards—the `/create-tasks` command provides the step-by-step procedure.

## Core Philosophy

Transform high-level specifications into concrete, actionable tasks that:

1. **Are small to medium in size** — Prefer multiple small tasks over one large task
2. **Are specific and verifiable** — Each task has clear completion criteria
3. **Follow natural dependencies** — Tasks ordered so prerequisites come first
4. **Group by specialization** — Related work grouped together (backend, frontend, testing)
5. **Support focused testing** — Each phase includes targeted tests, not exhaustive coverage

## Task Sizing Rules

**Critical Rule: All tasks must be small or medium sized. Large tasks are NOT acceptable.**

| Size   | Duration  | Files | Lines of Code |
| ------ | --------- | ----- | ------------- |
| Small  | 15-45 min | 1-3   | 20-80         |
| Medium | 1-2 hours | 3-6   | 80-200        |
| Large  | 3+ hours  | 7+    | 200+          |

**When encountering a large task**: Decompose it into 3-7 smaller tasks. See `references/task-sizing.md` for detailed guidance.

## Task Grouping

Organize tasks by architectural layer:

**Database Layer:**
- Data models and validations
- Database migrations
- Model associations and indexes

**API Layer:**
- Controller/route creation
- Business logic services
- Authentication and authorization
- Error handling

**Frontend Layer:**
- Component creation
- Form implementation
- Page layouts and styling
- Interactions and animations

**Integration Layer:**
- Third-party API integration
- Webhook handling
- Background job processing

**Testing Layer:**
- Review existing tests from other phases
- Identify critical coverage gaps
- Add strategic integration tests

For detailed patterns, see `references/common-patterns.md`.

## Testing Strategy

| Phase                  | Tests                                |
| ---------------------- | ------------------------------------ |
| Per task group         | Write 2-8 focused tests              |
| Per task group (final) | Run ONLY those 2-8 tests             |
| Final testing group    | Add max 10 additional tests for gaps |
| Total expected         | ~16-34 tests per feature             |

**Do NOT** run entire test suite during development—only feature-specific tests.

## Task Template

Use this structure for `tasks.md`:

```markdown
# Task Breakdown: [Feature Name]

## Overview
Total Tasks: [count]
Estimated Complexity: [Low/Medium/High]
Primary Stack: [e.g., Rails + React]

## Task List

### [Layer Name]

#### Task Group N: [Group Name]
**Dependencies:** [None | Task Group X, Y]

- [ ] N.0 Complete [layer name]
  - [ ] N.1 Write 2-8 focused tests for [functionality]
    - Test critical behavior 1
    - Test critical behavior 2
  - [ ] N.2 [Implementation task 1]
    - Detail A
    - Detail B
    - Reuse pattern from: [existing file]
  - [ ] N.3 [Implementation task 2]
  - [ ] N.4 Ensure tests pass
    - Run ONLY tests from N.1
    - Do NOT run entire test suite

**Acceptance Criteria:**
- All N.1 tests pass
- [Specific technical requirement]
- [Specific functional requirement]

## Execution Order
1. [Task Group 1] - [reason]
2. [Task Group 2] - [reason]
```

For the complete template, see `references/task-template.md`.

## Task Specificity

**Good tasks** include specific details:

```markdown
- [ ] Create User model with email validation
  - Fields: email (string, required), name (string), created_at (timestamp)
  - Validations: email format, email uniqueness
  - Reuse pattern from: app/models/account.rb
```

**Bad tasks** are vague:

```markdown
- [ ] Set up the database
- [ ] Make the backend work
```

## Feature Complexity Scale

| Complexity | Task Groups | Total Tasks |
| ---------- | ----------- | ----------- |
| Low        | 1-3         | 5-15        |
| Medium     | 3-5         | 15-25       |
| High       | 6+          | 25+         |

## Quality Checklist

Before finalizing tasks:

- [ ] All tasks are small or medium sized (no 3+ hour tasks)
- [ ] Tasks include specific, verifiable details
- [ ] Dependencies clearly noted between groups
- [ ] Each group has 2-8 focused tests defined
- [ ] Acceptance criteria included per group
- [ ] Visual assets referenced if available
- [ ] Execution order documented with reasons

## Common Mistakes

**Avoid:**

1. Creating large tasks (3+ hours)
2. Mixing unrelated work in same group
3. Skipping dependency notation
4. Writing vague task descriptions
5. Running full test suite per phase
6. Forgetting acceptance criteria

**Instead:**

- Break large tasks into 3-7 smaller ones
- Group related work by layer/specialization
- Note dependencies: "Dependencies: Task Group 1, 2"
- Include specific details: fields, validations, file paths
- Run only feature-specific tests per phase
- Define clear acceptance criteria per group

## Additional Resources

### Reference Files

For detailed guidance, consult:

- **`references/task-sizing.md`** - Decomposition examples, verification checklist
- **`references/task-template.md`** - Complete template structure with customization
- **`references/common-patterns.md`** - Patterns for CRUD, integrations, UI, real-time

### Example Files

Working examples in `examples/`:

- **`examples/examples.md`** - Four complete task breakdown examples:
  - Simple CRUD Feature (12 tasks, Rails + React)
  - Integration Feature (20 tasks, Stripe Payment)
  - Frontend-Only Feature (8 tasks, Dark Mode)
  - Complex Multi-Layer Feature (35 tasks, Real-Time Notifications)

## Workflow Command

This skill provides domain knowledge for:

- **`/create-tasks`** - Creates task breakdown from specification (procedure)

The command contains the step-by-step procedure; this skill provides the sizing rules, templates, and quality standards.
