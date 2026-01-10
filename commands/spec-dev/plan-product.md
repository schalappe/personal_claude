---
description: Plan and document the mission, roadmap, and tech stack for the current product
argument-hint: [product-name]
allowed-tools: Read, Write, Glob, Bash(ls:*, mkdir:*, test:*), Skill, AskUserQuestion, TodoWrite
---

# Plan Product

> **Workflow Step 1 of 5** — Next: `/shape-spec`

Create foundational product documentation: mission, roadmap, and tech stack. This is the starting point for product development.

## Prerequisites

- None (this is the first step in the workflow)

## Output

- `docs/product/mission.md` — Product vision, users, problems, differentiators
- `docs/product/roadmap.md` — Prioritized feature list with effort estimates
- `docs/product/tech-stack.md` — Technical choices and constraints

---

## Phase 1: Gather Product Information

### Check Existing Documentation

Check for existing docs: ❯`ls -la docs/product/ 2>/dev/null || echo "NO_DOCS"`

**Validation:**

- If docs exist → Ask user: "Product documentation exists. Review and update, or start fresh?"
- If `NO_DOCS` → Proceed to collect information

**Wait for user response if docs exist.**

### Collect Required Information

> **Domain Knowledge:** The **product-planning** skill provides templates and quality standards for product documents.

Gather from the user:

| Required Info | Description                                   |
| ------------- | --------------------------------------------- |
| Product Idea  | Core concept and purpose                      |
| Key Features  | Minimum 3 features with descriptions          |
| Target Users  | At least 1 user segment with use cases        |
| Tech Stack    | Confirmation or deviations from default stack |

If information is missing, prompt:

```markdown
Please provide the following to create your product plan:
1. Main idea for the product
2. List of key features (minimum 3)
3. Target users and use cases (minimum 1)
4. Will this product use your usual tech stack choices or deviate in any way?
```

### Confirm Before Proceeding

```markdown
I have all the info I need:
- Product: [PRODUCT_NAME]
- Key Features: [LIST]
- Target Users: [LIST]
- Tech Stack: [NOTES]

Ready to proceed?
```

---

## Phase 2: Create Mission Document

Create `docs/product/mission.md`:

```markdown
# Product Mission

## Pitch
[PRODUCT_NAME] is a [PRODUCT_TYPE] that helps [TARGET_USERS] [SOLVE_PROBLEM]
by providing [KEY_VALUE_PROPOSITION].

## Users

### Primary Customers
- [CUSTOMER_SEGMENT]: [DESCRIPTION]

### User Personas
**[USER_TYPE]** ([AGE_RANGE])
- **Role:** [JOB_TITLE/CONTEXT]
- **Context:** [BUSINESS/PERSONAL_CONTEXT]
- **Pain Points:** [SPECIFIC_PROBLEMS]
- **Goals:** [DESIRED_OUTCOMES]

## The Problem

### [PROBLEM_TITLE]
[PROBLEM_DESCRIPTION]. [QUANTIFIABLE_IMPACT].

**Our Solution:** [SOLUTION_APPROACH]

## Differentiators

### [DIFFERENTIATOR_TITLE]
Unlike [COMPETITOR/ALTERNATIVE], we provide [SPECIFIC_ADVANTAGE].
This results in [MEASURABLE_BENEFIT].

## Key Features

### Core Features
- **[FEATURE_NAME]:** [USER_BENEFIT_DESCRIPTION]

### Collaboration Features
- **[FEATURE_NAME]:** [USER_BENEFIT_DESCRIPTION]

### Advanced Features
- **[FEATURE_NAME]:** [USER_BENEFIT_DESCRIPTION]
```

**Constraints:**

- Focus on user benefits, not technical details
- Keep concise and scannable

Output:

```markdown
✅ Mission documented at `docs/product/mission.md`

Review to ensure it matches your vision. Ready for Phase 3?
```

---

## Phase 3: Create Roadmap

### Build the Roadmap

Read `docs/product/mission.md` to inform feature ordering.

Create `docs/product/roadmap.md`:

```markdown
# Product Roadmap

1. [ ] [FEATURE_NAME] — [1-2 sentence description] `[EFFORT]`
2. [ ] [FEATURE_NAME] — [1-2 sentence description] `[EFFORT]`
3. [ ] [FEATURE_NAME] — [1-2 sentence description] `[EFFORT]`

> **Notes**
> - Ordered by technical dependencies and product architecture
> - Each item is an end-to-end functional and testable feature
```

**Effort Scale:**

| Size | Duration |
| ---- | -------- |
| XS   | 1 day    |
| S    | 2-3 days |
| M    | 1 week   |
| L    | 2 weeks  |
| XL   | 3+ weeks |

**Ordering Criteria:**

1. Technical dependencies (foundational features first)
2. Most direct path to achieving the mission
3. Building incrementally from MVP to full product

**Constraints:**

- Do NOT include codebase initialization or bootstrapping tasks
- Each feature should be testable end-to-end

Output:

```markdown
✅ Roadmap documented at `docs/product/roadmap.md`

Review to ensure alignment. Ready for Phase 4?
```

---

## Phase 4: Document Tech Stack

### Gather Tech Stack Information

1. Note any user-provided tech stack preferences from this conversation
2. Fill gaps from these sources (in order):
   - User's global standards: @~/.claude/CLAUDE.md
   - Project documentation: @CLAUDE.md

### Create Tech Stack Document

Create `docs/product/tech-stack.md` with comprehensive technical choices.

Output:

```markdown
✅ Tech stack documented at `docs/product/tech-stack.md`

Review to ensure all details are correct.

---

**Product planning complete!**

📁 Created:
- `docs/product/mission.md`
- `docs/product/roadmap.md`
- `docs/product/tech-stack.md`

👉 Next: Run `/shape-spec` to start planning your first feature.
```

---

## Constraints

- Follow phases sequentially — do not skip ahead
- Wait for user confirmation before proceeding between phases
- Focus on user benefits over technical details in mission document
- Keep roadmap actionable with effort estimates
- Reconcile tech stack from multiple sources, prioritizing user input
