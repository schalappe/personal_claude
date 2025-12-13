---
name: task-breakdown
description: This skill should be used when the user asks to "break down a spec into tasks", "create a task list", "plan implementation tasks", "organize development work", "structure feature development", "create implementation phases", or mentions task planning, task organization, or implementation ordering. Transforms feature specifications into actionable, ordered implementation tasks.
---

# Task Breakdown Skill

This skill transforms feature specifications and requirements into actionable implementation tasks. It produces structured task lists organized by layer, with clear dependencies and acceptance criteria.

## When to Use This Skill

Activate this skill when users:

- Ask to break down a spec into implementation tasks
- Request a task list or implementation plan
- Need help organizing development work
- Want to know the order to implement features
- Ask about implementation strategy or approach
- Need to plan development phases for a feature
- Want to group related tasks together

## Core Philosophy

Transform high-level specifications into concrete, actionable tasks that:

1. **Are small to medium in size** - Prefer multiple small tasks over one large task
2. **Are specific and verifiable** - Each task has clear completion criteria
3. **Follow natural dependencies** - Tasks ordered so prerequisites come first
4. **Group by specialization** - Related work grouped together (backend, frontend, testing)
5. **Support focused testing** - Each phase includes targeted tests, not exhaustive coverage

### Critical Rule: Task Sizing

**All tasks must be small or medium sized. Large tasks are not acceptable.**

| Size   | Duration  | Files | Lines of Code |
| ------ | --------- | ----- | ------------- |
| Small  | 15-45 min | 1-3   | 20-80         |
| Medium | 1-2 hours | 3-6   | 80-200        |
| Large  | 3+ hours  | 7+    | 200+          |

When encountering a large task, decompose it into 3-7 smaller tasks. See `references/task-sizing.md` for detailed guidance and examples.

## Task Breakdown Process

### Phase 1: Analyze Inputs

**Required Files** (need at least one):

- `agent-os/specs/[spec-name]/spec.md` - Full feature specification
- `agent-os/specs/[spec-name]/planning/requirements.md` - Detailed requirements

**Analysis Steps:**

1. Read the complete spec and/or requirements
2. Identify major functional areas (database, API, UI, integrations)
3. Understand dependencies between components
4. Note any visual assets or design references
5. Review project coding standards for alignment

### Phase 2: Identify Task Groups

Organize tasks by architectural layer. Common groupings:

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

### Phase 3: Create Task Structure

For each task group:

1. **Start with focused tests** (2-8 tests maximum)
   - Test only critical behaviors for this group
   - Skip exhaustive coverage

2. **Implementation tasks**
   - Break work into logical sub-tasks
   - Reference existing patterns to follow
   - Include specific technical details

3. **Verification tasks**
   - Run ONLY the tests from this group
   - Do NOT run entire test suite

4. **Acceptance criteria**
   - Define clear completion criteria
   - Specify what "done" looks like

### Phase 4: Order and Dependencies

**Ordering Principles:**

1. **Foundation first**: Database models before API before UI
2. **Dependencies**: Required tasks before dependent tasks
3. **Logical flow**: Follow natural development progression
4. **Parallel potential**: Note tasks that can be done concurrently

**Dependency Notation:**

```markdown
#### Task Group 2: API Endpoints
**Dependencies:** Task Group 1
```

## Task Template

Use this structure for task breakdowns:

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

For the complete template with all sections, see `references/task-template.md`.

## Testing Strategy

- **Each development phase**: Write 2-8 focused tests maximum
- **Test scope**: Cover only critical behaviors, not edge cases
- **Test execution**: Run ONLY new tests, not entire suite
- **Final testing phase**: Add maximum of 10 additional strategic tests
- **Total feature tests**: Approximately 16-34 tests for the entire feature

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

## Standards Alignment

Before finalizing tasks, ensure alignment with:

- **Global Standards** (`~/.claude/CLAUDE.md`): Coding conventions, testing requirements
- **Project Standards** (`CLAUDE.md`): Project-specific patterns, architecture preferences

## Visual Asset References

If the spec includes visual designs, reference them in tasks:

```markdown
- [ ] 3.4 Build Dashboard page
  - Layout: Two-column grid
  - Match mockup: `planning/visuals/dashboard-mockup.png`
  - Use design system: `styles/design-system.css`
```

## Output Format

After creating tasks, output:

```markdown
The tasks list has been created at `agent-os/specs/[spec-name]/tasks.md`.

Review it closely to make sure it all looks good.

NEXT STEP: Implement these tasks manually, or use implementation commands if available.
```

## Additional Resources

### Reference Files

For detailed guidance, consult:

- **`references/task-sizing.md`** - Detailed task sizing guidelines, decomposition examples, verification checklist
- **`references/task-template.md`** - Complete template structure with all sections and customization guidelines
- **`references/common-patterns.md`** - Patterns for CRUD features, integrations, UI enhancements, real-time features

### Example Files

Working examples in `examples/`:

- **`examples/examples.md`** - Four complete task breakdown examples:
  - Simple CRUD Feature (12 tasks, Rails + React)
  - Integration Feature (20 tasks, Stripe Payment)
  - Frontend-Only Feature (8 tasks, Dark Mode)
  - Complex Multi-Layer Feature (35 tasks, Real-Time Notifications)

## Quick Reference

### Task Size Limits

- Maximum: Medium (1-2 hours)
- Preferred: Small (15-45 minutes)
- Break large tasks into 3-7 smaller ones

### Tests Per Phase

- Development phases: 2-8 tests each
- Final gap analysis: Up to 10 additional tests
- Total per feature: 16-34 tests

### Feature Complexity Scale

| Complexity | Task Groups | Total Tasks |
| ---------- | ----------- | ----------- |
| Low        | 1-3         | 5-15        |
| Medium     | 3-5         | 15-25       |
| High       | 6+          | 25+         |

### Common Mistakes to Avoid

1. Creating large tasks (3+ hours)
2. Mixing unrelated work in same group
3. Skipping dependency notation
4. Writing vague task descriptions
5. Running full test suite per phase
6. Forgetting acceptance criteria
