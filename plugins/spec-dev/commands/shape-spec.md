---
description: Shape, spec, and plan a feature through guided discovery - combines requirements gathering, specification writing, and task breakdown into a single plan-mode workflow
argument-hint: [feature-description]
allowed-tools: Read, Write, Glob, Grep, Bash(ls:*, mkdir:*, date:*, test:*), Task, Skill, AskUserQuestion, ExitPlanMode, TodoWrite
---

# Shape Spec (Unified)

> **Unified Workflow** — Combines shape-spec, write-spec, and create-tasks into a single plan-mode flow

Shape a feature from idea to actionable implementation plan. Runs entirely in plan mode with natural approval checkpoints.

## Prerequisites

- Must be in **plan mode** — if not, stop and instruct user to enter plan mode first
- Product documentation at `docs/product/` recommended but not required

## Output

```text
docs/specs/[YYYY-MM-DD]-[feature-slug]/
├── shape.md       # Context, decisions, and requirements
├── plan.md        # Specification + tasks combined
├── references.md  # Code pointers from exploration
└── visuals/       # Mockups and screenshots
```

---

## Step 1: Verify Plan Mode

**CRITICAL:** This command must run in plan mode.

If not in plan mode, output:

```markdown
**Shape-spec requires plan mode.**

Please enter plan mode first, then run `/shape-spec` again:
1. Ask me to plan a feature
2. Or type `/shape-spec` after entering plan mode
```

**Stop execution if not in plan mode.**

---

## Step 2: Clarify Scope

### Get Feature Description

**If argument provided:** Use it as the feature description.

**Otherwise:**

1. Check for roadmap: ❯`test -f docs/product/roadmap.md && echo "EXISTS" || echo "MISSING"`

2. If roadmap exists, read @docs/product/roadmap.md and identify next unchecked feature

3. Ask using **AskUserQuestion**:

   ```markdown
   Which feature should we shape?

   Options:
   - [Next roadmap feature if found]
   - Describe a different feature
   ```

### Generate Clarifying Questions

Generate 4-6 targeted questions that:

- Start with reasonable assumptions ("I assume X, is that correct?")
- Make it easy to confirm or provide alternatives
- Include questions about similar existing features
- End with scope boundaries (what's explicitly OUT of scope)

**Format:**

```markdown
Based on your idea for [feature], I have some clarifying questions:

1. I assume [assumption]. Is that correct, or [alternative]?
2. [Continue with numbered questions...]
N. What should be explicitly OUT of scope?

**Visual Assets:**
Do you have mockups or screenshots? If yes, I'll tell you where to place them.
```

**Wait for user response using AskUserQuestion.**

---

## Step 3: Gather Visuals

### Create Spec Folder

Get today's date: ❯`date +%Y-%m-%d`

Create folder structure:
❯`mkdir -p docs/specs/[DATE]-[kebab-case-name]/visuals`

Inform user:

```markdown
Spec folder created: `docs/specs/[path]/`

If you have mockups, place them in: `docs/specs/[path]/visuals/`
Let me know when ready, or say "no visuals" to continue.
```

**Wait for user response.**

### Check for Visual Assets

**Always run this check** (users often add files without mentioning):

❯`ls -la docs/specs/[path]/visuals/ 2>/dev/null | grep -E '\.(png|jpg|jpeg|gif|svg|pdf|md)$' || echo "NO_VISUALS"`

If files found:
- Read and analyze each visual file
- Note UI elements, patterns, user flows
- Check filenames for fidelity indicators (lofi, wireframe = low-fidelity)

---

## Step 4: Explore Codebase

### Check Product Context

Read these files if they exist:

| Document                    | Extract                                 |
| --------------------------- | --------------------------------------- |
| @docs/product/mission.md    | Mission, target users, core problems    |
| @docs/product/roadmap.md    | Where this feature fits                 |
| @docs/product/tech-stack.md | Technologies, constraints               |

Note any missing files but continue.

### Launch Code Explorers

Launch 2-3 `dev-kit:code-explorer` agents **in parallel** using the Task tool:

| Agent Focus         | Goal                                           |
| ------------------- | ---------------------------------------------- |
| Similar Features    | Find architecture and patterns to replicate    |
| Reusable Components | Identify UI components, services to extend     |
| Domain Patterns     | Map relevant models, validators, API endpoints |

Each agent should return 5-10 key files to read.

**Wait for all agents to complete.**

### Read and Synthesize

1. Read all files identified by explorers
2. Note reusable patterns and components
3. Identify integration points

---

## Step 5: Design Architecture

Launch `dev-kit:code-architect` agent with:

- Requirements from user answers
- Reusable components from explorers
- Visual designs (if any)
- Codebase conventions discovered

**Architect deliverables:**

- Component design with responsibilities
- Data flow and state management
- Integration points with existing code
- Implementation approach maximizing reuse

**Wait for architect to complete.**

---

## Step 6: Surface Standards

Invoke the **spec-creation** and **task-breakdown** skills to load quality standards.

Check for applicable standards in:
- @~/.claude/CLAUDE.md (global)
- @CLAUDE.md (project)

Note any specific coding conventions that apply.

---

## Step 7: Write Documentation

### Create shape.md

Write `docs/specs/[path]/shape.md`:

```markdown
# Shape: [Feature Name]

## Feature Description
[User's original description]

## Decisions & Context

### Questions & Answers
**Q1:** [Question]
**A:** [User's exact answer]
[Continue for all Q&A]

### Scope Boundaries
**In Scope:**
- [What will be built]

**Out of Scope:**
- [What won't be built]

## Visual Assets
[Files found via bash check, analysis notes, fidelity level]
[Or "No visual assets provided."]

## Product Alignment
[How this fits mission/roadmap, or "No product docs found."]
```

### Create references.md

Write `docs/specs/[path]/references.md`:

```markdown
# Code References: [Feature Name]

## Similar Implementations
[From code-explorer findings]

**[Component/Feature] — `path/to/file.ext`**
- What it does: [Description]
- How to reuse: [Extend, replicate, import]
- Key patterns: [Relevant code patterns]

## Reusable Components
[UI components, services, utilities identified]

## Integration Points
[Where this connects to existing code]

## Standards Applied
[Relevant coding standards from CLAUDE.md]
```

### Create plan.md

Write `docs/specs/[path]/plan.md`:

```markdown
# Plan: [Feature Name]

## Goal
[1-2 sentences describing core objective]

## User Stories
- As a [user], I want to [action] so that [benefit]
[Max 3 stories]

## Architecture Approach
[From code-architect]

**Component Design:**
- [Key components and responsibilities]

**Data Flow:**
- [Entry points → transformations → outputs]

**Integration:**
- [How feature connects to existing code]

---

## Implementation Tasks

### Overview
- Total Task Groups: [N]
- Primary Stack: [e.g., TypeScript + React]

### Task Group 1: [Layer/Component Name]
**Dependencies:** None

- [ ] 1.0 Complete [component]
  - [ ] 1.1 Write 2-4 focused tests
  - [ ] 1.2 [Implementation task]
    - [Specific details]
    - Reuse: `path/to/existing.ts`
  - [ ] 1.3 [Implementation task]
  - [ ] 1.4 Verify tests pass

**Acceptance Criteria:**
- [Specific requirement]

### Task Group 2: [Layer/Component Name]
**Dependencies:** Task Group 1

[Continue pattern...]

---

## Execution Order
1. Task Group 1 — [reason]
2. Task Group 2 — [reason]
```

**Task sizing rules:**
- Small: 15-45 min, 1-3 files
- Medium: 1-2 hours, 3-6 files
- **No large tasks** — decompose into smaller ones

---

## Step 8: Present Plan Summary

Output summary:

```markdown
## Shape Complete

**Spec folder:** `docs/specs/[path]/`

**Files created:**
- `shape.md` — Context and decisions
- `references.md` — Code pointers ([N] reusable components)
- `plan.md` — Specification + [M] task groups

**Architecture:** [Brief summary from architect]

**Visual Assets:** [N files analyzed / No visuals]

**Ready for implementation approval.**
```

---

## Step 9: Exit Plan Mode

Use **ExitPlanMode** to signal the plan is ready for user approval.

After user approves, implementation can begin with:

```markdown
To implement, run: `/implement-task [spec-name] [group-number]`

Or implement task groups sequentially starting with Task Group 1.
```

---

## Constraints

- **Must run in plan mode** — stop if not active
- **Always check visuals via bash** — don't trust user statements alone
- **Launch agents in parallel** where indicated
- **Read files identified by agents** before proceeding
- **Keep documentation lightweight** — this is shaping, not exhaustive docs
- **All tasks must be small or medium** — no 3+ hour tasks
- **Wait for user responses** at each question checkpoint
