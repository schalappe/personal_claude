---
description: Generate a Ralph Loop prompt for autonomous task implementation
argument-hint: [spec-name] [task-group-number]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(ls:*, test:*, mkdir:*), AskUserQuestion, TodoWrite
---

# Implement Task Loop

> **Alternative to `/implement-task`** — Generates a prompt for Ralph Loop

Generate a self-contained prompt for the Ralph Loop technique. The prompt includes everything Claude needs to iterate autonomously until tests pass.

## When to Use This vs `/implement-task`

| Aspect      | `/implement-task`                 | `/implement-task-loop`              |
| ----------- | --------------------------------- | ----------------------------------- |
| Interaction | High (7 phases with questions)    | Low (autonomous execution)          |
| Control     | Manual approval gates             | Iterative until done                |
| Best for    | Complex decisions, new patterns   | Well-defined tasks                  |
| Output      | Implemented code + reports        | Ralph Loop prompt file              |

**Use `/implement-task-loop` when:**

- Task group has clear acceptance criteria
- Tests can verify completion
- You want autonomous execution
- Architecture is already defined in spec

**Use `/implement-task` when:**

- You need to make design decisions
- Task requires human judgment
- Architecture needs discussion

## Prerequisites

- Tasks defined at `docs/specs/[spec-name]/tasks.md`
- Spec with architecture at `docs/specs/[spec-name]/spec.md`
- Run `/create-tasks` first if tasks don't exist

## Output

- `docs/specs/[spec-name]/ralph-prompt/[task-group].md` — Ready-to-use Ralph Loop prompt

---

## Phase 1: Locate and Validate

### Find Spec

Find specs with tasks: !`ls docs/specs/*/tasks.md 2>/dev/null || echo "NO_TASKS"`

**Validation:**

- If `NO_TASKS` → Stop: "No tasks.md found. Run `/create-tasks` first."
- If multiple specs and none specified → Ask which to work on
- If one spec → Use that spec

### Read Task Group

1. Read `docs/specs/[spec-name]/tasks.md`
2. If group number not specified → List available groups and ask
3. Extract the specified task group:
   - Group title
   - All subtasks with details
   - Acceptance criteria
   - Dependencies (verify they're complete)

**Validation:**

- If dependencies not complete → Stop: "Task Group [N] depends on [X, Y] which are not complete."

---

## Phase 2: Build Context

### Read Spec Context

Read `docs/specs/[spec-name]/spec.md` and extract:

- **Architecture Approach** section (if exists)
- **Existing Code to Leverage** section (if exists)

If architecture section exists, note all referenced files for the prompt.

### Read Requirements

Read `docs/specs/[spec-name]/planning/requirements.md` for additional context.

### Identify Test Command

Detect test runner from project:

- Check `package.json` for test scripts
- Check for `Makefile` with test target
- Check for `pytest`, `vitest`, `jest`, etc.

Store the test command for the prompt.

---

## Phase 3: Build Prompt

Create a self-contained prompt that includes everything Claude needs.

### Prompt Structure

Build the prompt with these sections:

```markdown
# Ralph Loop: [Task Group Title]

## Mission

Implement Task Group [N]: [Title] from the specification.
Iterate until ALL acceptance criteria are met, then output `<promise>GROUP [N] COMPLETE</promise>`

## Task Group Details

[Paste full task group from tasks.md including all subtasks]

## Acceptance Criteria

[Paste acceptance criteria from tasks.md]

## Architecture Context

[Paste architecture approach from spec.md OR note "Follow existing patterns in the codebase"]

## Existing Code to Reference

[List files from "Existing Code to Leverage" section, or key files identified]

## Test Command

Run tests with: `[detected test command]`

Focus on tests relevant to this task group.

## Implementation Rules

1. **Read before writing** — Understand existing patterns first
2. **Small iterations** — Make incremental changes, test frequently
3. **Follow conventions** — Match existing code style
4. **Update tasks.md** — Mark subtasks `[x]` as you complete them
5. **Run tests** — Verify each change passes tests

## Completion Checklist

Before outputting the promise, verify:

- [ ] All subtasks in tasks.md marked `[x]`
- [ ] All acceptance criteria met
- [ ] Tests pass for this task group
- [ ] Code follows project conventions

When ALL criteria are met, output: `<promise>GROUP [N] COMPLETE</promise>`
```

### Calculate Recommended Iterations

Based on task count:

- 1-3 subtasks → 10 iterations
- 4-6 subtasks → 15 iterations
- 7+ subtasks → 20 iterations

Add this recommendation at the top of the prompt file as a comment.

---

## Phase 4: Save Prompt

### Create Directory

Create directory if needed: `docs/specs/[spec-name]/ralph-prompt/`

### Write Prompt File

Save the generated prompt to: `docs/specs/[spec-name]/ralph-prompt/[task-group].md`

The task-group filename should be descriptive, e.g., `group-1-core-infrastructure.md` or `group-2-api-endpoints.md`

### Display Summary

```markdown
## Ralph Loop Prompt Generated

**Spec:** [spec-name]
**Task Group:** [N] - [Title]
**Saved to:** `docs/specs/[spec-name]/ralph-prompt/[task-group].md`

**Recommended settings:**
- Max iterations: [calculated]
- Completion promise: `GROUP [N] COMPLETE`

**To run:**
Copy the prompt content and start Ralph Loop with:
`/ralph-loop --max-iterations [N] --completion-promise "GROUP [N] COMPLETE"`

Or paste the prompt directly into a new Claude session.
```

---

## Constraints

- **Do not ask clarifying questions** — use spec and requirements as-is
- **Use defined architecture** — do not explore alternatives
- **Focus on one group** — generate prompt for one group at a time
- **Include all context** — the prompt must be self-contained
- **Do not execute** — only generate and save the prompt

---

## Example Output

For a task group implementing authentication:

```text
docs/specs/auth-feature/ralph-prompt/group-1-auth-core.md
```

Contents would include:

- Mission with task group details
- All subtasks and acceptance criteria
- Architecture context from spec
- Files to reference
- Test command
- Implementation rules
- Completion checklist with promise
