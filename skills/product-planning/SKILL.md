---
name: product-planning
description: This skill should be used when the user asks to "plan a product", "create a product plan", "define product vision", "create a mission document", "build a roadmap", "document tech stack", "plan features", or mentions needing help with product strategy, feature planning, or product documentation.
---

# Product Planning Skill

Guide systematic product planning through a structured 4-phase process: gathering information, creating mission documents, building roadmaps, and documenting tech stack.

## When to Use

Trigger this skill when users:

- Ask to plan a new product or define product vision
- Request help creating a product roadmap
- Need to document their tech stack decisions
- Want to organize features strategically
- Ask about product planning best practices

## Planning Process Overview

Execute four sequential phases, completing each fully before proceeding:

| Phase                  | Output                           | Purpose                    |
| ---------------------- | -------------------------------- | -------------------------- |
| 1. Gather Information  | User inputs                      | Collect product details    |
| 2. Create Mission      | `agent-os/product/mission.md`    | Define vision and strategy |
| 3. Build Roadmap       | `agent-os/product/roadmap.md`    | Prioritize features        |
| 4. Document Tech Stack | `agent-os/product/tech-stack.md` | Record technical choices   |

## Phase 1: Gather Product Information

Collect comprehensive details before creating documentation.

### Required Information

- **Product Idea**: Core concept and purpose
- **Key Features**: Minimum 3 features with descriptions
- **Target Users**: At least 1 user segment with use cases
- **Tech Stack**: Technology choices or confirmation of defaults

### Process

1. Check if `agent-os/product/` directory exists
2. If exists, ask whether to review existing docs or start fresh
3. Prompt for missing required information
4. Confirm all information before proceeding

### Prompt Template

```markdown
Please provide the following to create your product plan:
1. Main idea for the product
2. List of key features (minimum 3)
3. Target users and use cases (minimum 1)
4. Will this product use your usual tech stack choices or deviate in any way?
```

### Completion Message

```markdown
I have all the info I need to help you plan this product:
- Product: [NAME]
- Key Features: [LIST]
- Target Users: [LIST]
- Tech Stack: [NOTES]

Ready to proceed to creating the mission document?
```

## Phase 2: Create Mission Document

Generate `agent-os/product/mission.md` with comprehensive product definition.

### Mission Structure

| Section         | Purpose                                     |
| --------------- | ------------------------------------------- |
| Pitch           | One-sentence value proposition              |
| Users           | Primary customers and detailed personas     |
| The Problem     | Problem statement and solution approach     |
| Differentiators | Unique advantages over alternatives         |
| Key Features    | Categorized feature list with user benefits |

### Guidelines

- Focus on user benefits, not technical implementation
- Keep content concise and scannable
- Use quantifiable impacts where possible
- Emphasize strategic advantages

**Reference:** `references/mission-template.md` for complete structure and examples

### Completion Message

```markdown
I have documented the product mission at `agent-os/product/mission.md`.

Review it to ensure it matches your vision and strategic goals.

Ready to proceed to creating the roadmap?
```

## Phase 3: Build Roadmap

Generate `agent-os/product/roadmap.md` with prioritized feature checklist.

### Process

1. Review mission to understand goals and success criteria
2. Identify concrete features needed for product vision
3. Order strategically based on dependencies and mission alignment
4. Write feature descriptions in standard format

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

- **Technical Dependencies**: Foundational features first
- **Mission Alignment**: Most direct path to achieving goals
- **Incremental Building**: MVP to full product progression

### Constraints

- Each item must be end-to-end functional and testable
- Include both frontend and backend when applicable
- Do NOT include bootstrapping or initialization tasks
- Assume bare-bones application already exists

**Reference:** `references/roadmap-guide.md` for detailed guidance and examples

### Completion Message

```markdown
I have documented the product roadmap at `agent-os/product/roadmap.md`.

Review it to ensure it aligns with how you see the product roadmap.

Ready to proceed to documenting the tech stack?
```

## Phase 4: Document Tech Stack

Generate `agent-os/product/tech-stack.md` with comprehensive technical choices.

### Information Sources (Priority Order)

1. **User-provided information** (highest priority)
2. **Global standards**: `~/.claude/CLAUDE.md`
3. **Project documentation**: `CLAUDE.md`, `agents.md`

### Process

1. Note tech stack details mentioned by user
2. Read available documentation sources
3. Reconcile information from all sources
4. Create comprehensive tech stack document

**Reference:** `references/tech-stack-template.md` for structure and examples

### Completion Message

```markdown
I have documented the product's tech stack at `agent-os/product/tech-stack.md`.

Review it to ensure all tech stack details are correct.

You're ready to start planning feature specs using `/shape-spec` or `/write-spec`.
```

## Best Practices

### Sequential Execution

- Complete each phase fully before proceeding
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

## Related Commands

- `/plan-product` - User-invoked command that uses this skill
- `/shape-spec` - Next step: Shape feature specifications
- `/write-spec` - Next step: Write detailed specifications

## Reference Files

For detailed templates and guidance, consult:

- **`references/mission-template.md`** - Complete mission document structure and writing tips
- **`references/roadmap-guide.md`** - Detailed roadmap creation process and validation checklist
- **`references/tech-stack-template.md`** - Tech stack documentation template and common patterns
