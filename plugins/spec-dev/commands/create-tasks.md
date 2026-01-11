---
description: Create an actionable tasks breakdown from a spec and requirements for a new feature
argument-hint: [spec-name]
allowed-tools: Read, Write, Glob, Grep, Bash(ls:*, mkdir:*, test:*, sed:*), Skill, TodoWrite
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

Find most recent spec: ❯`ls -dt docs/specs/*/ 2>/dev/null | head -1 | sed 's:/$::'`

If argument provided, use `docs/specs/*[spec-name]*` instead.

### Validate Availability

Check for spec or requirements:
❯`test -f [spec-path]/spec.md && echo "SPEC_EXISTS"`
❯`test -f [spec-path]/planning/requirements.md && echo "REQ_EXISTS"`

**Validation:**

- If neither exists → Stop: "No spec or requirements found. Run `/shape-spec` first to gather requirements."
- If at least one exists → Proceed

### Read and Analyze

1. Read @[spec-path]/spec.md (if exists) and/or @[spec-path]/planning/requirements.md
2. Note: specific requirements, architecture approach, existing code to leverage, out-of-scope items

---

## Phase 2: Create Task List

> **Domain Knowledge:** The **task-breakdown** skill provides sizing rules, grouping strategy, task template, and testing strategy.

### Apply Skill Standards

1. Apply the task sizing rules from the skill — all tasks must be small or medium
2. Group tasks by specialization using the skill's grouping patterns
3. Follow the task template structure from the skill
4. Apply the testing strategy from the skill (2-8 tests per group)

### Write tasks.md

Create `[spec-path]/tasks.md` following the task template from the skill.

**Adapt structure** based on actual feature requirements — the skill template is guidance, not a rigid format.

### Verify Standards Compliance

Check user's coding standards from:

- @~/.claude/CLAUDE.md (global standards)
- @CLAUDE.md (project-level)

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

- Apply the **task-breakdown** skill's quality checklist before completing
- **All tasks must be small or medium** — break down any 2+ hour tasks
- **Create specific, verifiable tasks** — avoid vague descriptions
- **Group related tasks** — backend together, frontend together
- **Use test-driven pattern** — tests first (x.1), verify last (final subtask)
- **Include acceptance criteria** per group
- **Reference visual assets** if available in planning/visuals/
- **Final size check** — review all tasks before completing
