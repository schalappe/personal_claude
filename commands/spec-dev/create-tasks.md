---
description: Create an actionable tasks breakdown from a spec and requirements for a new feature
argument-hint: [spec-name]
allowed-tools: Read, Write, Glob, Grep, Bash(ls:*, mkdir:*), Skill, TodoWrite
---

# Create Tasks

> **Workflow Step 4 of 5** — Previous: `/write-spec` | Next: `/implement-task`

Transform specifications into an actionable task list with strategic grouping, ordering, and size constraints.

## Prerequisites

- Specification at `docs/specs/[spec-name]/spec.md`
- Or requirements at `docs/specs/[spec-name]/planning/requirements.md`
- Run `/write-spec` first if neither exists

## Output

- `docs/specs/[spec-name]/tasks.md` — Grouped, ordered implementation tasks

---

## Phase 1: Load Specification

### Locate Required Files

```bash
SPEC_PATH=$(ls -dt docs/specs/*/ 2>/dev/null | head -1 | sed 's:/$::')
ls $SPEC_PATH/spec.md $SPEC_PATH/planning/requirements.md 2>/dev/null
```

If argument provided, use that spec name.

### Validate Availability

If neither spec.md nor requirements.md exists:

```markdown
I need a spec.md or requirements.md to create tasks.

Please direct me to the spec folder, or run `/shape-spec` or `/write-spec` first.
```

### Read and Analyze

1. Read `spec.md` and/or `requirements.md`
2. Note: specific requirements, architecture approach, existing code to leverage, out-of-scope items

---

## Phase 2: Create Task List

Invoke the **task-breakdown** skill before proceeding.

### Task Sizing Rules

**All tasks must be small or medium. Large tasks are NOT allowed.**

| Size                | Duration  | Lines  | Files |
| ------------------- | --------- | ------ | ----- |
| Small (preferred)   | 15-45 min | 20-80  | 1-3   |
| Medium (acceptable) | 1-2 hours | 80-200 | 3-6   |
| Large (NOT allowed) | 3+ hours  | 200+   | 7+    |

**If a task is large**, decompose it into 3-7 smaller tasks.

### Task Grouping Strategy

Group tasks by specialization (backend, API, UI, etc.) and order by dependencies.

**Common groups:**

- Database Layer (models, migrations, associations)
- API Layer (controllers, endpoints, auth)
- Frontend Components (UI, forms, pages)
- Testing (gap analysis, additional tests)

### Task Structure

Each task group follows this pattern:

```markdown
### [Layer Name]

#### Task Group N: [Group Title]
**Dependencies:** [Previous groups or "None"]

- [ ] N.0 Complete [layer] — parent task
  - [ ] N.1 Write 2-8 focused tests for [component]
  - [ ] N.2 Implement [specific item]
  - [ ] N.3 Implement [specific item]
  - [ ] N.4 Ensure tests pass (run ONLY tests from N.1)

**Acceptance Criteria:**
- [Specific, verifiable criteria]
```

### Testing Strategy

| Phase                  | Tests                                |
| ---------------------- | ------------------------------------ |
| Per task group (N.1)   | Write 2-8 focused tests              |
| Per task group (final) | Run ONLY those 2-8 tests             |
| Final testing group    | Add max 10 additional tests for gaps |
| Total expected         | ~16-34 tests per feature             |

**Do NOT** run entire test suite during development — only feature-specific tests.

### Write tasks.md

Create `[spec-path]/tasks.md`:

```markdown
# Task Breakdown: [Feature Name]

## Overview
Total Tasks: [count]

## Task List

### Database Layer

#### Task Group 1: [Title]
**Dependencies:** None

- [ ] 1.0 Complete database layer
  - [ ] 1.1 Write 2-8 focused tests for [model] functionality
  - [ ] 1.2 Create [Model] with validations
  - [ ] 1.3 Create migration for [table]
  - [ ] 1.4 Set up associations
  - [ ] 1.5 Ensure tests pass

**Acceptance Criteria:**
- Tests written in 1.1 pass
- Migrations run successfully

### API Layer

#### Task Group 2: [Title]
**Dependencies:** Task Group 1

- [ ] 2.0 Complete API layer
  - [ ] 2.1 Write 2-8 focused tests for endpoints
  - [ ] 2.2 Create [resource] controller
  - [ ] 2.3 Implement authentication/authorization
  - [ ] 2.4 Ensure tests pass

**Acceptance Criteria:**
- CRUD operations work
- Authorization enforced

### Frontend Components

#### Task Group 3: [Title]
**Dependencies:** Task Group 2

- [ ] 3.0 Complete UI components
  - [ ] 3.1 Write 2-8 focused tests for components
  - [ ] 3.2 Create [Component]
  - [ ] 3.3 Implement [form/view]
  - [ ] 3.4 Apply styling
  - [ ] 3.5 Ensure tests pass

**Acceptance Criteria:**
- Components render correctly
- Matches visual design

### Testing

#### Task Group 4: Test Review
**Dependencies:** Task Groups 1-3

- [ ] 4.0 Review and fill critical gaps
  - [ ] 4.1 Review tests from groups 1-3 (~6-24 tests)
  - [ ] 4.2 Identify critical gaps for THIS feature only
  - [ ] 4.3 Write max 10 additional tests
  - [ ] 4.4 Run feature-specific tests only

**Acceptance Criteria:**
- All feature tests pass (~16-34 total)
- Critical workflows covered

## Execution Order
1. Database Layer (Task Group 1)
2. API Layer (Task Group 2)
3. Frontend (Task Group 3)
4. Testing (Task Group 4)
```

**Adapt structure** based on actual feature requirements — this is a template, not a rigid format.

### Verify Standards Compliance

Check user's coding standards from:

- `~/.claude/CLAUDE.md`
- `CLAUDE.md` (project-level)

Ensure tasks align and do not conflict with user preferences.

---

## Completion

```markdown
✅ Tasks created at `[spec-path]/tasks.md`

**Summary:**
- Task Groups: [N]
- Total Tasks: [M]
- Testing Strategy: 2-8 tests per group, max 10 gap-fill

Review to ensure all tasks look good.

👉 Next: Run `/implement-task [spec-name] [group-number]` to start implementation.
```

---

## Constraints

- **All tasks must be small or medium** — break down any 2+ hour tasks
- **Create specific, verifiable tasks** — avoid vague descriptions
- **Group related tasks** — backend together, frontend together
- **Limit testing during development** — 2-8 tests per group
- **Use test-driven pattern** — tests first (x.1), verify last (final subtask)
- **Include acceptance criteria** per group
- **Reference visual assets** if available in planning/visuals/
- **Final size check** — review all tasks before completing
