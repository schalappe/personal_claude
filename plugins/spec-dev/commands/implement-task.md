---
description: Implement a single task group from tasks.md using a multi-phase workflow that ensures deep codebase understanding, thoughtful architecture design, and high-quality implementation
argument-hint: [spec-name] [task-group-number]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git:*, npm:*, bun:*, pnpm:*, yarn:*, make:*, ls:*, test:*, mkdir:*), Task, Skill, AskUserQuestion, TodoWrite
---

# Implement Task

> **Workflow Step 5 of 5** — Previous: `/create-tasks`

Implement a single task group with deep codebase understanding, clarifying questions, architecture design, and quality review.

## Prerequisites

- Tasks defined at `docs/specs/[spec-name]/tasks.md`
- Run `/create-tasks` first if tasks don't exist

## Output

- Implemented code changes
- `docs/specs/[spec-name]/implementation/[task-group].md` — Implementation report
- `docs/specs/[spec-name]/verification/[task-group]-verification.md` — Verification report
- Updated `tasks.md` with completed checkboxes

---

## Core Principles

| Principle                | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| Ask First                | Identify ambiguities before implementing — don't assume |
| Understand Before Acting | Read existing code patterns first                       |
| Read Agent Findings      | After agents complete, read the files they identify     |
| Simple & Elegant         | Prioritize readable, maintainable code                  |
| Track Progress           | Use TodoWrite throughout                                |

---

## Phase 1: Discovery & Task Selection

### Create Todo List

Initialize todos for all phases.

### Locate Spec and Tasks

Find specs with tasks: ❯`ls docs/specs/*/tasks.md 2>/dev/null || echo "NO_TASKS"`

**Validation:**

- If `NO_TASKS` → Stop: "No tasks.md found. Run `/create-tasks` first to generate implementation tasks."
- If multiple specs → Ask which to work on
- If one spec → Use that spec

### Validate Tasks File

Check tasks exist: ❯`test -f [spec-path]/tasks.md && echo "EXISTS" || echo "MISSING"`

**Validation:**

- If `MISSING` → Stop: "No tasks.md at `[spec-path]`. Run `/create-tasks [spec-name]` first."
- If `EXISTS` → Read @[spec-path]/tasks.md

### Select Task Group

**If group specified:** Use that group.

**Otherwise:**

```markdown
Which task group should we implement?

Available task groups:
[List groups with titles and brief descriptions]
```

**Wait for user response.**

---

## Phase 2: Load Codebase Context

### Analyze Task Requirements

1. Read the selected task group from @[spec-path]/tasks.md
2. Read @[spec-path]/planning/requirements.md for context
3. Identify key codebase areas that will be affected

### Check Spec Coverage

Read @[spec-path]/spec.md and check for these sections:

- "Existing Code to Leverage"
- "Architecture Approach"

**If spec has both sections with content:**

1. Extract all file paths mentioned in "Existing Code to Leverage"
2. Read each referenced file to build understanding
3. Note the architecture approach for Phase 4
4. Skip to Phase 3 (Clarifying Questions)

Output:

```markdown
✅ Loaded context from spec.md
- Referenced files: [N] read
- Architecture approach: Defined
```

**If spec is missing or lacks these sections:**

1. Launch 2-3 `dev-kit:code-explorer` agents **in parallel**:

| Agent Focus      | Goal                                       |
| ---------------- | ------------------------------------------ |
| Similar Features | Trace implementation patterns to replicate |
| Architecture     | Map abstractions and flow of control       |
| Extension Points | Identify testing approaches, UI patterns   |

Each agent should return 5-10 key files to read.

2. **Wait for agents to complete**
3. Read all files they identified
4. Summarize findings

Output:

```markdown
ℹ️ Spec lacked exploration data — ran fresh analysis
- Agents launched: [N]
- Key files identified: [M]
```

---

## Phase 3: Clarifying Questions

**This phase is critical — do not skip.**

### Identify Ambiguities

Review task group and codebase findings. Identify:

- Edge cases and error handling
- Integration points
- Scope boundaries
- Design preferences
- Backward compatibility needs
- Performance requirements

### Ask Questions

Use **AskUserQuestion** to present all questions in an organized list.

**Wait for answers before proceeding.**

If user says "whatever you think is best", provide your recommendation and get explicit confirmation.

---

## Phase 4: Architecture Approach

### Check Existing Architecture

**If spec.md has "Architecture Approach" section (from Phase 2 check):**

Present to user:

```markdown
The spec already defines an architecture approach:

**Component Design:**
[Summary from spec]

**Data Flow:**
[Summary from spec]

**Integration Points:**
[Summary from spec]

Options:
1. Use this approach (Recommended)
2. Explore alternative approaches
```

Use **AskUserQuestion** to confirm.

- If user selects option 1 → Proceed to Phase 5
- If user selects option 2 → Continue to "Generate Alternatives" below

**If spec lacks architecture OR user wants alternatives:**

### Generate Alternatives

Launch 2-3 `dev-kit:code-architect` agents **in parallel** with different focuses:

| Focus              | Approach                              |
| ------------------ | ------------------------------------- |
| Minimal Changes    | Smallest change, maximum reuse        |
| Clean Architecture | Maintainability, elegant abstractions |
| Pragmatic Balance  | Speed + quality                       |

### Present Options

For each approach, present:

- Brief summary
- Trade-offs
- Concrete implementation differences

**Provide your recommendation with reasoning.**

### Get User Decision

Use **AskUserQuestion** to ask which approach to use.

**Wait for response.**

---

## Phase 5: Implementation

**Requires explicit user approval before proceeding.**

### Invoke Relevant Skills

Check available skills and invoke all that are appropriate for this task.

### Implement

1. Read all relevant files from previous phases
2. Follow chosen architecture
3. Follow codebase conventions strictly
4. Write clean, well-documented code
5. Update todos as you progress

### Update tasks.md

Mark task group and all subtasks as complete:

```markdown
- [x] N.0 Complete [layer]
  - [x] N.1 [subtask]
  - [x] N.2 [subtask]
```

### Create Implementation Report

Create `docs/specs/[spec-name]/implementation/[task-group].md`:

```markdown
# Implementation: [Task Group Title]

**Date:** [Date]
**Task Group:** [Number and title]

## Summary
[Brief overview]

## Architecture Approach
[Which approach was selected and why]

## Files Modified
- `path/to/file.ext` — [What changed]

## Files Created
- `path/to/file.ext` — [Purpose]

## Key Details
[Important implementation notes]

## Integration Points
[How this integrates with existing code]

## Testing Notes
[Tests written or considerations]
```

---

## Phase 6: Quality Review

### Launch Reviewers

Launch 3 `dev-kit:code-reviewer` agents **in parallel**:

| Focus          | What to Check                  |
| -------------- | ------------------------------ |
| Simplicity/DRY | Code elegance, duplication     |
| Correctness    | Bugs, functional issues        |
| Conventions    | Project patterns, abstractions |

### Present Findings

Consolidate issues by severity. Recommend which to fix.

### Get User Answer

Use **AskUserQuestion**: fix now, fix later, or proceed as-is?

### Address Issues

If fixing, apply changes and re-run affected tests.

### Simplify and Refine Code

After addressing review issues, launch `dev-kit:code-simplifier` agent to:

- Simplify recently modified code for clarity and consistency
- Apply project-specific coding standards
- Remove unnecessary complexity while preserving functionality

**Wait for simplifier to complete.** Review any changes it suggests.

---

## Phase 7: Verification

### Verify tasks.md Updated

Confirm all checkboxes for this task group are marked `[x]`.

### Run Tests

1. Identify test command (package.json, Makefile, etc.)
2. Run full test suite
3. Capture results — do NOT attempt to fix failures

### Create Verification Report

Create `docs/specs/[spec-name]/verification/[task-group]-verification.md`:

```markdown
# Verification Report: [Task Group Title]

**Spec:** [spec-name]
**Task Group:** [Number and title]
**Date:** [Date]
**Status:** ✅ Passed | ⚠️ Issues | ❌ Failed

## Executive Summary
[2-3 sentences on results]

## Task Completion
- [x] [Task group and subtasks listed]

## Implementation Documentation
- [x] Report: `implementation/[task-group].md`
- [x] tasks.md updated

## Code Quality
- Simplicity/DRY: [Summary]
- Correctness: [Summary]
- Conventions: [Summary]
- Issues: [List or "None"]

## Test Results
- Total: [N]
- Passing: [N]
- Failing: [N]

### Failed Tests
[List or "None"]

## Next Steps
[Recommendations]
```

### Display Summary

```markdown
🎉 Implementation Complete!

**Task Group:** [Title]
**Status:** [Status]

**Documentation:**
- Implementation: docs/specs/[spec]/implementation/[group].md
- Verification: docs/specs/[spec]/verification/[group]-verification.md

**Tests:** [Passing]/[Total]

**Remaining Tasks:**
[List or "All complete!"]

Would you like to implement another task group?
```

---

## Constraints

- **Ask questions early** — after exploration, before architecture
- **Wait for user approval** before implementation
- **Launch agents in parallel** where indicated
- **Read files identified by agents** before proceeding
- **Invoke all relevant skills** during implementation
- **Do not fix failing tests** — document them only
- **Update tasks.md** as work completes
