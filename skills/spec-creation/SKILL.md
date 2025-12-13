---
name: spec-creation
description: This skill should be used when the user asks to "create a spec", "write a specification", "plan a feature", "gather requirements", "shape an idea", "spec out [feature]", "document requirements", or mentions needing to prepare feature documentation before development.
---

# Specification Creation Skill

Create comprehensive, well-structured feature specifications through a proven two-phase workflow: **shaping** (requirements gathering) and **writing** (specification documentation).

## Core Philosophy

Spec-driven development ensures:

1. Clear understanding before coding begins
2. Alignment between user vision and implementation
3. Reuse of existing code and patterns
4. Explicit scope boundaries (what's in, what's out)
5. Visual design alignment when mockups exist
6. Focused, minimal testing approach

## Two-Phase Workflow Overview

### Phase 1: Shaping (Requirements Gathering)

Transform a vague idea into documented, validated requirements.

**Key Steps:**

1. Initialize spec folder structure (`YYYY-MM-DD-feature-name`)
2. Read product mission, roadmap, and tech stack for context
3. Generate 4-8 clarifying questions with sensible defaults
4. Request visual assets and ask about existing similar features
5. Check visuals folder via bash (mandatory, even if user says "no visuals")
6. Ask 1-3 focused follow-ups to resolve ambiguities
7. Document everything to `planning/requirements.md`

**Critical Practices:**

- Propose assumptions to make confirmation easy for the user
- Always run `ls -la [spec-path]/planning/visuals/` to check for files
- Document user's exact answers, not interpretations
- Keep follow-ups minimal (1-3 questions maximum)

For detailed shaping workflow, see `references/shaping-guide.md`.

### Phase 2: Writing (Specification Documentation)

Transform requirements into a clear, actionable specification with architectural guidance.

**Key Steps:**

1. Read `planning/requirements.md` and analyze gathered information
2. Launch 2-3 **code-explorer** subagents in parallel to:
   - Analyze similar features mentioned in requirements
   - Search for reusable UI components
   - Identify backend patterns and services
3. Launch **code-architect** subagent with explorer findings to:
   - Design feature architecture based on requirements
   - Create component design and data flow
4. Analyze every visual file with Read tool
5. Create `spec.md` integrating all subagent findings
6. Verify quality and alignment with requirements

**Critical Practices:**

- Launch subagents in parallel (single message with multiple Task calls)
- Wait for explorers to complete before launching architect
- Never write actual code in specifications
- Keep sections concise and skimmable
- Follow the template exactly

For detailed writing workflow, see `references/writing-guide.md`.

## Folder Structure

Every spec creates this structure:

```text
docs/specs/YYYY-MM-DD-feature-name/
├── planning/
│   ├── requirements.md       # All gathered requirements
│   └── visuals/              # Mockups, wireframes, screenshots
├── implementation/           # Implementation reports (created later)
└── spec.md                   # The final specification document
```

## Specification Template

```markdown
# Specification: [Feature Name]

## Goal
[1-2 sentences describing core objective]

## User Stories
- As a [user type], I want to [action] so that [benefit]
[Max 3 user stories]

## Specific Requirements
**[Requirement name]**
- [Up to 8 concise sub-bullets per requirement]
[Max 10 requirements]

## Visual Design
[If mockups exist]
**`planning/visuals/[filename]`**
- [Up to 8 bullets describing UI elements to build]
[One section per visual file]

## Existing Code to Leverage
[Based on code-explorer findings]
**[Component/code found] - `path/to/file`**
- What it does: [From code-explorer analysis]
- How to reuse: [Extend, replicate, import]
- Key methods: [Relevant APIs]
[Max 5 code areas from code-explorer agents]

## Architecture Approach
[Based on code-architect blueprint]
**Component Design:** [Key components and responsibilities]
**Data Flow:** [Entry points → transformations → outputs]
**Integration Points:** [How feature integrates with existing code]

## Out of Scope
- [Up to 10 specific features that MUST NOT be built]
```

## Key Principles

### 1. Context Before Questions

Always read product mission, roadmap, and tech stack before asking questions. This makes questions more relevant and informed.

### 2. Visuals Are Critical

- Always request visual assets from the user
- Always check visuals folder via bash (users often forget to mention files)
- Analyze every visual file with Read tool
- Check filenames for fidelity indicators (lofi, wireframe = low-fidelity)

### 3. Reusability First

- Launch code-explorer subagents to find reusable code
- Document existing components with file paths
- Avoid specifying new components when existing ones work
- Follow established patterns identified by subagents

### 4. Scope Clarity

- Define explicit in-scope features
- State out-of-scope items clearly
- Avoid over-engineering
- Keep it simple and focused

### 5. Limited Testing

- Specs call for focused, minimal tests
- Implementation task groups: 2-8 tests each
- Total: ~16-34 tests per feature, not hundreds

## Quality Checklist

Before completing each phase:

**Shaping Phase:**

- [ ] Spec folder created with proper YYYY-MM-DD-name format
- [ ] Product context files read (mission, roadmap, tech-stack)
- [ ] 4-8 clarifying questions asked with sensible defaults
- [ ] Reusability and visual assets questions included
- [ ] Mandatory bash visual check performed
- [ ] All visual files analyzed with Read tool
- [ ] All answers documented exactly as stated

**Writing Phase:**

- [ ] All visual files referenced and analyzed
- [ ] Code-explorer subagents launched in parallel
- [ ] Code-architect subagent received explorer findings
- [ ] Subagent findings integrated into specification
- [ ] Template structure followed exactly
- [ ] No actual code written in spec
- [ ] Out-of-scope items clearly stated

## Common Mistakes

**Avoid:**

- Skipping the visual check (always run `ls -la visuals/`)
- Writing actual code in the specification
- Adding features not requested by user
- Creating new components when existing ones work
- Interpreting user answers instead of using exact words
- Making specifications too long or detailed

**Instead:**

- Always check visuals folder via bash
- Ask about existing similar features
- Search codebase before specifying new components
- Keep specifications concise and skimmable
- Document user's exact answers

## Additional Resources

### Reference Files

For detailed workflow instructions, consult:

- **`references/shaping-guide.md`** - Step-by-step shaping workflow with examples
- **`references/writing-guide.md`** - Specification writing best practices and template details

## Example Usage Flow

```bash
User: "I want to create a spec for user authentication"

Phase 1 - Shaping:
→ Create spec folder: agent-os/specs/2025-11-16-user-authentication/
→ Read product mission, roadmap, tech stack
→ Generate 6 clarifying questions about auth approach
→ Ask about existing similar features and visual assets
→ Receive user answers
→ Run: ls -la planning/visuals/ (find login-mockup.png!)
→ Read and analyze login-mockup.png
→ Ask 2 follow-up questions about visual elements
→ Document everything to planning/requirements.md

Phase 2 - Writing:
→ Read planning/requirements.md
→ Launch 3 code-explorer agents in parallel:
  • Explorer 1: Analyze existing auth features
  • Explorer 2: Search for reusable form components
  • Explorer 3: Find validation and service patterns
→ Wait for explorers to complete
→ Launch code-architect with requirements + explorer findings
→ Read login-mockup.png and analyze design elements
→ Create spec.md integrating all findings
→ Verify alignment with requirements

Result: Comprehensive, architecture-informed spec ready for implementation
```
