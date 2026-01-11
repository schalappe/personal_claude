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

> **Domain Knowledge:** The **product-planning** skill provides the mission template structure.

Create `docs/product/mission.md` following the mission template from the skill.

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

> **Domain Knowledge:** The **product-planning** skill provides the onion layer philosophy, feature definitions, effort scale, and ordering criteria.

### Build the Roadmap

1. Read `docs/product/mission.md` to inform feature ordering
2. Apply the onion layer philosophy from the skill
3. Use the effort scale from the skill for estimates
4. Follow the ordering criteria from the skill

Create `docs/product/roadmap.md` following the roadmap structure from the skill.

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

> **Domain Knowledge:** The **product-planning** skill provides tech stack documentation patterns.

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
- Apply the **product-planning** skill's quality checklist before completing each document
- Reconcile tech stack from multiple sources, prioritizing user input
