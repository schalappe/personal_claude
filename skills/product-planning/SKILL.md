---
name: product-planning
description: This skill should be used when the user asks to "plan a product", "create a product plan", "define product vision", "create a mission document", "build a roadmap", "document tech stack", "plan features", or mentions needing help with product strategy, feature planning, or product documentation. Provides templates and standards for product documentation.
---

# Product Planning Skill

Domain knowledge for systematic product planning and documentation. This skill provides the templates, structures, and quality standards—the `/plan-product` command provides the step-by-step procedure.

## Output Structure

Product planning creates three documents:

```text
docs/product/
├── mission.md      # Product vision, users, problems, differentiators
├── roadmap.md      # Prioritized feature list with effort estimates
└── tech-stack.md   # Technical choices and constraints
```

## Mission Document Structure

`docs/product/mission.md` defines the product strategy:

| Section         | Purpose                                     |
| --------------- | ------------------------------------------- |
| Pitch           | One-sentence value proposition              |
| Users           | Primary customers and detailed personas     |
| The Problem     | Problem statement and solution approach     |
| Differentiators | Unique advantages over alternatives         |
| Key Features    | Categorized feature list with user benefits |

### Mission Template

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

**Guidelines:**
- Focus on user benefits, not technical implementation
- Keep content concise and scannable
- Use quantifiable impacts where possible

## Roadmap Structure

`docs/product/roadmap.md` prioritizes features using the **Onion Layer Philosophy**.

### Onion Layer Philosophy

The roadmap follows a layered approach where each feature adds a new "ring" around the product core:

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

1. **Features deliver user value** — A feature provides a service, possibility, or function to the user
2. **Always functional** — After completing any feature, the product works; new features add capabilities, never break existing ones
3. **Standalone completeness** — Each feature is end-to-end (frontend + backend + tests) and independently testable
4. **Layered building** — Start with foundation, then build around previous features until complete

### What IS a Feature

A feature delivers tangible user value:

- ✅ "Generate API keys" — User gains a new capability
- ✅ "Export data to CSV" — User can accomplish a task
- ✅ "User authentication" — User can access the product
- ✅ "Dashboard with analytics" — User sees valuable information

### What is NOT a Feature

Technical setup tasks are NOT features:

- ❌ "Add a database" — Infrastructure, not user value
- ❌ "Set up CI/CD" — Developer tooling
- ❌ "Configure logging" — Operational concern
- ❌ "Install dependencies" — Bootstrapping

These technical needs are embedded WITHIN features that require them.

### Feature Format

```markdown
[#]. [ ] [FEATURE_NAME] — [1-2 sentence description of user value] `[EFFORT]`
```

### Effort Scale

| Tag  | Duration |
| ---- | -------- |
| `XS` | 1 day    |
| `S`  | 2-3 days |
| `M`  | 1 week   |
| `L`  | 2 weeks  |
| `XL` | 3+ weeks |

### Ordering Criteria

1. **Foundation First** — Features that other features depend on
2. **Core Value Next** — Primary user capabilities that fulfill the mission
3. **Extended Capabilities** — Features that enhance but aren't essential
4. **Polish Last** — Advanced features, optimizations, nice-to-haves

### Roadmap Constraints

- Each item must deliver user value (not just technical setup)
- Each item must be end-to-end functional and testable
- Product must work after completing each feature
- Include both frontend and backend when applicable
- Do NOT include bootstrapping or initialization tasks
- Assume bare-bones application already exists

## Tech Stack Document

`docs/product/tech-stack.md` records technical choices.

### Information Sources (Priority Order)

1. **User-provided information** (highest priority)
2. **Global standards**: `~/.claude/CLAUDE.md`
3. **Project documentation**: `CLAUDE.md`

## Required Information

Before creating documents, gather:

| Required Info | Description                                   |
| ------------- | --------------------------------------------- |
| Product Idea  | Core concept and purpose                      |
| Key Features  | Minimum 3 features with descriptions          |
| Target Users  | At least 1 user segment with use cases        |
| Tech Stack    | Confirmation or deviations from default stack |

## Best Practices

### Sequential Execution

- Complete each document fully before proceeding
- Wait for user confirmation between phases
- Do not skip ahead or combine phases

### User Alignment

- Ensure documents align with user's standards
- Reference user's CLAUDE.md for preferences
- Ask clarifying questions when needed

### Document Quality

- Keep content concise and scannable
- Focus on "why" over "what"
- Use clear, actionable language
- Include quantifiable metrics where possible

## Quality Checklist

Before completing each document:

**Mission:**
- [ ] Pitch clearly states value proposition
- [ ] User personas are specific and actionable
- [ ] Problems include quantifiable impacts
- [ ] Differentiators show competitive advantage
- [ ] Features focus on user benefits

**Roadmap:**
- [ ] Each feature delivers user value (not technical setup)
- [ ] Features follow onion layer order (foundation → core → extended → polish)
- [ ] Product remains functional after completing each feature
- [ ] Each item is end-to-end (frontend + backend + tests)
- [ ] Effort estimates are realistic
- [ ] No bootstrapping or infrastructure-only tasks

**Tech Stack:**
- [ ] User preferences prioritized
- [ ] All major technology choices documented
- [ ] Constraints and trade-offs noted

## Additional Resources

### Reference Files

For detailed templates and guidance, consult:

- **`references/mission-template.md`** - Complete mission document examples
- **`references/roadmap-guide.md`** - Detailed roadmap creation guidance
- **`references/tech-stack-template.md`** - Tech stack documentation patterns

## Workflow Command

This skill provides domain knowledge for:

- **`/plan-product`** - Creates product documentation (procedure)

The command contains the step-by-step procedure; this skill provides the templates and quality standards.
