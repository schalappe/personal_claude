---
name: spec-creation
version: 1.0.0
description: This skill should be used when the user asks to "create a spec", "write a specification", "plan a feature", "gather requirements", "shape an idea", "spec out [feature]", "document requirements", or mentions needing to prepare feature documentation before development. Provides philosophy, templates, and quality standards for specification creation.
---

# Specification Creation Skill

Domain knowledge for creating comprehensive, well-structured feature specifications. This skill provides the philosophy, templates, and quality standards—the `/shape-spec` and `/write-spec` commands provide the step-by-step procedures.

## Core Philosophy

Spec-driven development ensures:

1. **Clear understanding before coding** — Prevents wasted effort and rework
2. **Alignment between vision and implementation** — User goals translate to technical specs
3. **Reuse of existing patterns** — Search codebase before specifying new components
4. **Explicit scope boundaries** — Define what's in AND what's out
5. **Focused testing** — Minimal, behavior-focused tests (not exhaustive coverage)

## Key Principles

### Context Before Questions

Always read product mission, roadmap, and tech stack before asking questions. This makes questions more relevant and informed.

### Visuals Are Critical

- Always request visual assets from the user
- Always check visuals folder via bash (users often forget to mention files they added)
- Analyze every visual file with Read tool
- Check filenames for fidelity indicators (lofi, wireframe = low-fidelity)

### Reusability First

- Launch dev-kit:code-explorer subagents to find reusable code
- Document existing components with file paths
- Avoid specifying new components when existing ones work
- Follow established patterns identified by subagents

### Scope Clarity

- Define explicit in-scope features
- State out-of-scope items clearly
- Avoid over-engineering
- Keep specifications simple and focused

### Limited Testing

- Specs call for focused, minimal tests
- Each implementation task group: 2-8 tests
- Total per feature: ~16-34 tests, not hundreds

## Folder Structure

Every spec creates this structure:

```text
docs/specs/YYYY-MM-DD-feature-name/
├── shape.md          # Context, decisions, scope
├── plan.md           # Specification + implementation tasks
├── references.md     # Code pointers from exploration
├── visuals/          # Mockups, wireframes, screenshots
├── implementation/   # Implementation reports (created during implementation)
└── verification/     # Verification reports
```

## Specification Template

Use this exact structure for the specification section of `plan.md`:

```markdown
# Specification: [Feature Name]

## Goal
[1-2 sentences describing core objective and user value]

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
[Based on dev-kit:code-explorer findings]
**[Component/code found] - `path/to/file`**
- What it does: [Description]
- How to reuse: [Extend, replicate, import]
- Key methods: [Relevant APIs]
[Max 5 code areas]

## Architecture Approach
[Based on dev-kit:code-architect blueprint]
**Component Design:** [Key components and responsibilities]
**Data Flow:** [Entry points → transformations → outputs]
**Integration Points:** [How feature integrates with existing code]

## Out of Scope
- [Up to 10 specific features that MUST NOT be built]
```

## Shape Template

Use this structure for `shape.md`:

```markdown
# Spec Requirements: [Spec Name]

## Initial Description
[User's original description verbatim]

## Requirements Discussion

### Questions & Answers
**Q1:** [Question asked]
**A:** [User's exact answer]
[Continue for all Q&A]

### Existing Code References
[Similar features/paths identified by user, or "None identified"]

### Follow-up Questions
[If any were asked]

## Visual Assets

### Files Found
[Based on bash check, not user statement]
- `filename.png`: [Description from analysis]

### Visual Insights
- [Design patterns identified]
- [Fidelity level: high-fidelity mockup / low-fidelity wireframe]

## Requirements Summary

### Functional Requirements
- [Core functionality]
- [User actions enabled]
- [Data to be managed]

### Reusability Opportunities
- [Components that might exist]
- [Backend patterns to investigate]

### Scope Boundaries
**In Scope:**
- [What will be built]

**Out of Scope:**
- [What won't be built]

### Technical Considerations
- [Integration points]
- [Existing constraints]
```

## Quality Checklists

### Shaping Phase Checklist

- [ ] Spec folder created with YYYY-MM-DD-name format
- [ ] Product context files read (mission, roadmap, tech-stack)
- [ ] 4-8 clarifying questions asked with sensible defaults
- [ ] Reusability and visual assets questions included
- [ ] Mandatory bash visual check performed
- [ ] All visual files analyzed with Read tool
- [ ] All answers documented exactly as stated
- [ ] Follow-ups limited to 1-3 questions

### Writing Phase Checklist

- [ ] Requirements.md read and analyzed
- [ ] Code-explorer subagents launched in parallel
- [ ] Code-architect received explorer findings
- [ ] All visual files referenced and analyzed
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

### Example Files

Working examples demonstrating expected output format:

- **`examples/sample-requirements.md`** - Complete requirements document
- **`examples/sample-spec.md`** - Final specification document

## Workflow Commands

This skill provides domain knowledge for:

- **`/shape-spec`** - Unified command that gathers requirements, creates specification, and breaks down tasks (runs in plan mode)

The command contains the step-by-step procedure; this skill provides the philosophy, templates, and quality standards.
