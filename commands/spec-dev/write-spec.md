---
description: Create comprehensive specification document from gathered requirements
argument-hint: [spec-name]
allowed-tools: Read, Write, Glob, Grep, Bash(ls:*), Task, Skill, TodoWrite
---

# Write Spec

> **Workflow Step 3 of 5** — Previous: `/shape-spec` | Next: `/create-tasks`

Transform gathered requirements into a comprehensive specification document by exploring the codebase and designing architecture.

## Prerequisites

- Requirements gathered at `docs/specs/[spec-name]/planning/requirements.md`
- Run `/shape-spec` first if requirements don't exist

## Output

- `docs/specs/[spec-name]/spec.md` — Complete feature specification

---

## Phase 1: Load Context

### Locate Spec Folder

```bash
SPEC_PATH=$(ls -dt docs/specs/*/ 2>/dev/null | head -1 | sed 's:/$::')
ls -la $SPEC_PATH/planning/
```

If argument provided, use that spec name instead.

### Read Requirements

1. Read `[spec-path]/planning/requirements.md`
2. Check for visual assets in `[spec-path]/planning/visuals/`
3. Parse: feature description, scope boundaries, constraints, similar features mentioned

---

## Phase 2: Codebase Exploration

Invoke the **spec-creation** skill before proceeding.

### Launch Code Explorers

Launch 2-3 `feature-dev:code-explorer` agents **in parallel** using the Task tool:

| Agent Focus         | What to Find                                    |
| ------------------- | ----------------------------------------------- |
| Similar Features    | Architecture, components, patterns to replicate |
| Reusable Components | UI components, forms, modals to reuse or extend |
| Backend Patterns    | Services, validators, models in related domain  |

**Example parallel launch:**

```markdown
Task 1: code-explorer analyzing similar feature at [path from requirements]
Task 2: code-explorer searching for reusable [component type] components
Task 3: code-explorer analyzing [domain] patterns (services, models)
```

**Wait for all explorers to complete**, then synthesize findings.

---

## Phase 3: Architecture Design

### Launch Code Architect

Launch `feature-dev:code-architect` agent with:

- Requirements from planning/requirements.md
- Reusable components identified by explorers
- Visual designs (if any in planning/visuals/)
- Existing codebase conventions

**Architect deliverables:**

- Component design with responsibilities
- Data flow and state management
- Integration points with existing code
- Implementation approach maximizing code reuse

**Wait for architect to complete.**

---

## Phase 4: Write Specification

Create `[spec-path]/spec.md`:

```markdown
# Specification: [Feature Name]

## Goal
[1-2 sentences describing the core objective]

## User Stories
- As a [user type], I want to [action] so that [benefit]
- [max 2 additional stories]

## Specific Requirements

**[Requirement Name]**
- [Up to 8 concise sub-bullets: sub-requirements, design decisions, technical approach]

[max 10 specific requirements]

## Visual Design
[If mockups provided]

**`planning/visuals/[filename]`**
- [Up to 8 bullets describing UI elements to address]

[repeat per visual file]

## Existing Code to Leverage
[From code-explorer findings]

**[Component/Service] — `path/to/file.ext`**
- What it does: [Description]
- How to reuse: [Extend, replicate pattern, import]
- Key methods: [Relevant APIs]

[max 5 existing code areas]

## Architecture Approach
[From code-architect blueprint]

**Component Design:**
- [Key components and responsibilities]

**Data Flow:**
- [Entry points → transformations → outputs]

**Integration Points:**
- [How feature connects to existing code]

## Out of Scope
- [max 10 items that should NOT be built]
```

**Constraints:**

- Do NOT write actual code in spec.md
- Keep each section short and skimmable
- Reference visual assets when available
- Focus on clarity over completeness

---

## Phase 5: Verify Quality

Before completing, verify:

| Check                 | Criteria                                  |
| --------------------- | ----------------------------------------- |
| Requirements Coverage | All user answers reflected                |
| Visual Alignment      | All visual files referenced (if any)      |
| Explorer Integration  | "Existing Code" section populated         |
| Architect Integration | "Architecture Approach" section populated |
| Scope Clarity         | In-scope and out-of-scope clearly defined |
| No Over-engineering   | No unnecessary complexity added           |
| No Code               | Specification only, no implementation     |

---

## Completion

```markdown
✅ Spec created at `[spec-path]/spec.md`

**Summary:**
- Goal: [Brief statement]
- User Stories: [X] defined
- Requirements: [Y] detailed
- Visual Design: [Z files / No visuals]
- Existing Code: [N reusable components identified]
- Architecture: Blueprint included

**Agent Analysis:**
- code-explorer agents: [X] launched
- code-architect: Design complete

👉 Next: Run `/create-tasks` to break this into implementation tasks.
```

---

## Constraints

- Launch code-explorer agents **in parallel** (single message, multiple Task calls)
- Wait for agents to complete before proceeding
- Integrate agent findings into specification
- Do NOT write actual code
- Keep sections short and skimmable
- Do NOT deviate from template structure
