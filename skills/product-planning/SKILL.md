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

`docs/product/roadmap.md` prioritizes features:

### Feature Format

```markdown
[#]. [ ] [FEATURE_NAME] — [1-2 sentence description] `[EFFORT]`
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

1. **Technical Dependencies** — Foundational features first
2. **Mission Alignment** — Most direct path to achieving goals
3. **Incremental Building** — MVP to full product progression

### Roadmap Constraints

- Each item must be end-to-end functional and testable
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
- [ ] Features ordered by dependencies
- [ ] Each item is end-to-end functional
- [ ] Effort estimates are realistic
- [ ] No bootstrapping tasks included

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
