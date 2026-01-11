---
description: Implement a task group autonomously using Ralph Loop for iterative development until tests pass
argument-hint: [spec-name] [task-group-number]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git:*, npm:*, bun:*, pnpm:*, yarn:*, make:*, ls:*, test:*, mkdir:*), Task, Skill, TodoWrite
---

# Implement Task Loop

> **Alternative to `/implement-task`** — Uses Ralph Loop for autonomous iteration

Implement a task group using the Ralph Loop technique: Claude iterates on the implementation until all tests pass and acceptance criteria are met.

## When to Use This vs `/implement-task`

| Aspect | `/implement-task` | `/implement-task-loop` |
| ------ | ----------------- | ---------------------- |
| Interaction | High (7 phases with questions) | Low (autonomous) |
| Control | Manual approval gates | Iterative until done |
| Best for | Complex decisions, new patterns | Well-defined tasks |
| Completion | User confirms | Tests pass + promise |

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

- Implemented code changes
- Updated `tasks.md` with completed checkboxes
- Tests passing for the task group

---

## Phase 1: Locate and Validate

### Find Spec

Find specs with tasks: `ls docs/specs/*/tasks.md 2>/dev/null || echo "NO_TASKS"`

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

If architecture section exists, read all referenced files.

### Read Requirements

Read `docs/specs/[spec-name]/planning/requirements.md` for additional context.

### Identify Test Command

Detect test runner from project:
- Check `package.json` for test scripts
- Check for `Makefile` with test target
- Check for `pytest`, `vitest`, `jest`, etc.

Store the test command for the loop prompt.

---

## Phase 3: Build Loop Prompt

Create a self-contained prompt that includes everything Claude needs.

### Prompt Template

Build the prompt with these sections:

**Header:**
> # Ralph Loop: [Task Group Title]

**Mission:**
> Implement Task Group [N]: [Title] from the specification.
> Iterate until ALL acceptance criteria are met, then output `<promise>GROUP [N] COMPLETE</promise>`

**Task Group Details:**
> [Paste full task group from tasks.md including all subtasks]

**Acceptance Criteria:**
> [Paste acceptance criteria from tasks.md]

**Architecture Context:**
> [Paste architecture approach from spec.md OR note "Follow existing patterns"]

**Existing Code to Reference:**
> [List files from "Existing Code to Leverage" section]

**Test Command:**
> Run tests with: `[detected test command]`
> Only run tests for this task group, not the full suite.

**Implementation Rules:**
> 1. Read before writing — Understand existing patterns first
> 2. Small iterations — Make incremental changes, test frequently
> 3. Follow conventions — Match existing code style
> 4. Update tasks.md — Mark subtasks `[x]` as you complete them
> 5. Run tests — Verify each change passes tests

**Completion Checklist:**
> Before outputting the promise, verify:
> - All subtasks in tasks.md marked `[x]`
> - All acceptance criteria met
> - Tests pass for this task group
> - Code follows project conventions
>
> When ALL criteria are met, output: `<promise>GROUP [N] COMPLETE</promise>`

---

## Phase 4: Start Ralph Loop

### Calculate Iterations

Based on task count:
- 1-3 subtasks → `--max-iterations 10`
- 4-6 subtasks → `--max-iterations 15`
- 7+ subtasks → `--max-iterations 20`

### Invoke Ralph Loop

Use the Skill tool to invoke ralph-loop with:
- The built prompt
- `--max-iterations [calculated]`
- `--completion-promise "GROUP [N] COMPLETE"`

Example invocation:

    /ralph-loop "[built prompt]" --max-iterations [N] --completion-promise "GROUP [N] COMPLETE"

---

## Phase 5: Post-Loop Verification

After ralph-loop completes (via promise or max iterations):

### Check Completion Status

1. Read `docs/specs/[spec-name]/tasks.md`
2. Verify all subtasks for this group are marked `[x]`
3. Run tests one final time

### Report Results

```markdown
## Ralph Loop Complete

**Task Group:** [N] - [Title]
**Iterations:** [count]
**Status:** ✅ Complete | ⚠️ Partial | ❌ Incomplete

**Completed Tasks:**
- [x] N.1 [task]
- [x] N.2 [task]
...

**Test Results:**
- Passing: [N]
- Failing: [N]

**Next Steps:**
[If incomplete: suggest running /implement-task for manual completion]
[If complete: suggest next task group]
```

---

## Constraints

- **Do not ask clarifying questions** — use spec and requirements as-is
- **Use defined architecture** — do not explore alternatives
- **Focus on one group** — complete it fully before moving on
- **Trust the loop** — let Ralph iterate until done
- **Max iterations prevent infinite loops** — if stuck, manual intervention needed

---

## Troubleshooting

### Tests keep failing

Check if:
- Test command is correct
- Dependencies are properly installed
- Task dependencies are actually complete
- Acceptance criteria are achievable

### Loop completes but tasks not marked

The prompt may need adjustment. Verify:
- tasks.md path is correct
- Checkbox syntax is correct (`- [ ]` → `- [x]`)
