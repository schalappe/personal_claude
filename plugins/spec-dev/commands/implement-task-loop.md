---
description: Generate a Ralph Loop prompt for autonomous task implementation
argument-hint: [spec-name] [task-group(s)]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(ls:*, test:*, mkdir:*), AskUserQuestion, TodoWrite
---

# Implement Task Loop

Generate a self-contained prompt for the Ralph Loop technique. The prompt includes everything Claude needs to iterate autonomously until tests pass.

## Task Group Selection

- **Single group**: `3` → Creates prompt for group 3
- **Range of groups**: `1-6` → Creates ONE combined prompt for groups 1 through 6

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

### Read Task Group(s)

1. Read `docs/specs/[spec-name]/tasks.md`
2. Parse the argument:
   - If not specified → List available groups and ask
   - If single number (e.g., `3`) → Extract group 3
   - If range (e.g., `1-6`) → Extract groups 1, 2, 3, 4, 5, and 6
3. For each group, extract:
   - Group title
   - All subtasks with details
   - Acceptance criteria
   - Dependencies (verify they're complete)

**Validation:**

- If dependencies for any group are not complete → Stop: "Task Group [N] depends on [X, Y] which are not complete."

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

Build the prompt with these sections. Adapt based on single group vs. range:

**For single group (e.g., `3`):**

```markdown
# Ralph Loop: [Task Group Title]

## Mission

Implement Task Group [N]: [Title] from the specification.
Iterate until ALL acceptance criteria are met, then output `<promise>COMPLETE</promise>`

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

When ALL criteria are met, output: `<promise>COMPLETE</promise>`
```

**For range of groups (e.g., `1-6`):**

```markdown
# Ralph Loop: Groups [START]-[END]

## Mission

Implement Task Groups [START] through [END] from the specification.
Work through groups sequentially. Iterate until ALL groups are complete, then output `<promise>COMPLETE</promise>`

## Task Groups

### Group [N1]: [Title]

[Paste full task group from tasks.md including all subtasks and acceptance criteria]

### Group [N2]: [Title]

[Paste full task group from tasks.md including all subtasks and acceptance criteria]

[... repeat for all groups in range ...]

## Architecture Context

[Paste architecture approach from spec.md OR note "Follow existing patterns in the codebase"]

## Existing Code to Reference

[List files from "Existing Code to Leverage" section, or key files identified]

## Test Command

Run tests with: `[detected test command]`

## Implementation Rules

1. **Work sequentially** — Complete each group before moving to the next
2. **Read before writing** — Understand existing patterns first
3. **Small iterations** — Make incremental changes, test frequently
4. **Follow conventions** — Match existing code style
5. **Update tasks.md** — Mark subtasks `[x]` as you complete them
6. **Run tests** — Verify each change passes tests

## Completion Checklist

Before outputting the promise, verify:

- [ ] All subtasks for ALL groups marked `[x]`
- [ ] All acceptance criteria for ALL groups met
- [ ] Tests pass
- [ ] Code follows project conventions

When ALL criteria are met, output: `<promise>COMPLETE</promise>`
```

### Calculate Recommended Iterations

Based on total subtask count (across all groups if range):

- 1-3 subtasks → 10 iterations
- 4-6 subtasks → 15 iterations
- 7-10 subtasks → 20 iterations
- 11+ subtasks → 25 iterations

Add this recommendation at the top of the prompt file as a comment.

---

## Phase 4: Save Prompt

### Create Directory

Create directory if needed: `docs/specs/[spec-name]/ralph-prompt/`

### Write Prompt File

Save the generated prompt to: `docs/specs/[spec-name]/ralph-prompt/[filename].md`

Filename conventions:
- Single group: `group-3-api-endpoints.md`
- Range: `groups-1-6.md`

### Display Summary

**For single group:**

```markdown
## Ralph Loop Prompt Generated

**Spec:** [spec-name]
**Task Group:** [N] - [Title]
**Saved to:** `docs/specs/[spec-name]/ralph-prompt/[filename].md`

**Recommended settings:**
- Max iterations: [calculated]
- Completion promise: `COMPLETE`

**To run:**
Copy the prompt content and start Ralph Loop with:
`/ralph-loop --max-iterations [N] --completion-promise "COMPLETE"`

Or paste the prompt directly into a new Claude session.
```

**For range of groups:**

```markdown
## Ralph Loop Prompt Generated

**Spec:** [spec-name]
**Task Groups:** [START] through [END]
**Saved to:** `docs/specs/[spec-name]/ralph-prompt/groups-[START]-[END].md`

**Recommended settings:**
- Max iterations: [calculated]
- Completion promise: `COMPLETE`

**To run:**
Copy the prompt content and start Ralph Loop with:
`/ralph-loop --max-iterations [N] --completion-promise "COMPLETE"`

Or paste the prompt directly into a new Claude session.
```

---

## Constraints

- **Do not ask clarifying questions** — use spec and requirements as-is
- **Use defined architecture** — do not explore alternatives
- **One prompt per invocation** — single group = one prompt, range = one combined prompt
- **Include all context** — the prompt must be self-contained
- **Do not execute** — only generate and save the prompt

---

## Example Output

**Single group:**

```text
docs/specs/auth-feature/ralph-prompt/group-1-auth-core.md
```

**Range of groups:**

```text
docs/specs/auth-feature/ralph-prompt/groups-1-6.md
```

Contents include:

- Mission with task group details (all groups if range)
- All subtasks and acceptance criteria
- Architecture context from spec
- Files to reference
- Test command
- Implementation rules
- Completion checklist with promise
