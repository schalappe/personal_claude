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

### Onion Layer Philosophy

The roadmap follows a layered approach where each feature adds a new "ring" around the product:

```text
        ┌────────────────────────────────────┐
        │      Advanced Features             │  ← Layer 4: Polish & power features
        │   ┌────────────────────────────┐   │
        │   │   Extended Features        │   │  ← Layer 3: Enhanced capabilities
        │   │   ┌────────────────────┐   │   │
        │   │   │  Core Features     │   │   │  ← Layer 2: Primary user value
        │   │   │   ┌────────────┐   │   │   │
        │   │   │   │ Foundation │   │   │   │  ← Layer 1: Essential infrastructure
        │   │   │   └────────────┘   │   │   │
        │   │   └────────────────────┘   │   │
        │   └────────────────────────────┘   │
        └────────────────────────────────────┘
```

**Key Principles:**

1. **Features deliver user value** — A feature provides a service, possibility, or function
2. **Always functional** — After each feature, the product works; new features never break existing ones
3. **Standalone completeness** — Each feature is end-to-end (frontend + backend + tests)
4. **Layered building** — Start with foundation, then build around previous features

### What IS a Feature

- ✅ "Generate API keys" — User gains a capability
- ✅ "Export data to CSV" — User accomplishes a task
- ✅ "User authentication" — User can access the product

### What is NOT a Feature

- ❌ "Add a database" — Infrastructure, not user value
- ❌ "Set up CI/CD" — Developer tooling
- ❌ "Configure logging" — Operational concern

Technical needs are embedded WITHIN features that require them.

### Build the Roadmap

Read `docs/product/mission.md` to inform feature ordering.

Create `docs/product/roadmap.md`:

```markdown
# Product Roadmap

> **Onion Layer Approach:** Each feature adds a layer of capability. The product remains functional after completing any feature.

## Foundation Layer
1. [ ] [FEATURE_NAME] — [User value description] `[EFFORT]`

## Core Features Layer
2. [ ] [FEATURE_NAME] — [User value description] `[EFFORT]`
3. [ ] [FEATURE_NAME] — [User value description] `[EFFORT]`

## Extended Features Layer
4. [ ] [FEATURE_NAME] — [User value description] `[EFFORT]`

## Advanced Features Layer
5. [ ] [FEATURE_NAME] — [User value description] `[EFFORT]`
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

1. **Foundation First** — Features that other features depend on
2. **Core Value Next** — Primary user capabilities that fulfill the mission
3. **Extended Capabilities** — Features that enhance but aren't essential
4. **Polish Last** — Advanced features, optimizations, nice-to-haves

**Constraints:**

- Each feature must deliver user value (not just technical setup)
- Product must work after completing each feature
- Do NOT include codebase initialization or bootstrapping tasks
- Each feature should be end-to-end (frontend + backend + tests)

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
- **Roadmap follows onion layer philosophy** — each feature adds a layer of capability
- **Features deliver user value** — no infrastructure-only items
- **Product stays functional** — completing any feature leaves product working
- Keep roadmap actionable with effort estimates
- Reconcile tech stack from multiple sources, prioritizing user input
