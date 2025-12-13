---
name: codebase-documenter
version: "1.0.0"
description: This skill should be used when the user asks to "create a README", "document the codebase", "write architecture documentation", "add code comments", "create API documentation", "explain project structure", "make a getting-started guide", "document this code", or mentions needing help with codebase documentation, technical writing, or making code accessible to new developers.
---

# Codebase Documenter

## Overview

This skill enables creating comprehensive, beginner-friendly documentation for codebases. It provides structured templates and best practices for writing READMEs, architecture guides, code comments, and API documentation.

## Core Principles

Apply these principles when creating documentation:

1. **Start with "Why"** - Explain purpose before implementation details
2. **Progressive Disclosure** - Layer information from simple to complex
3. **Provide Context** - Explain not just what code does, but why it exists
4. **Include Examples** - Show concrete usage for every concept
5. **Define Terms** - Avoid jargon; assume no prior knowledge
6. **Visual Aids** - Use diagrams, flowcharts, and file trees
7. **Five-Minute Rule** - Enable users to get something running quickly

## Documentation Workflow

### Step 1: Analyze the Codebase

Before writing documentation:

1. Identify entry points (main files, index files, app initialization)
2. Map module dependencies and relationships
3. Find core concepts and key abstractions
4. Locate configuration files and environment setup
5. Review existing documentation to avoid duplication

### Step 2: Choose Documentation Type

Select based on user request and codebase analysis:

| Request Type                  | Documentation to Create                                  |
| ----------------------------- | -------------------------------------------------------- |
| New project or missing README | README documentation                                     |
| Complex architecture          | Architecture documentation                               |
| Confusing code sections       | Inline code comments                                     |
| HTTP endpoints or SDKs        | API documentation                                        |
| Multiple needs                | Address in order: README → Architecture → API → Comments |

### Step 3: Generate Documentation

Use templates from `assets/templates/` as starting points:

1. Read the appropriate template
2. Replace placeholders with project-specific content
3. Add concrete examples using real code
4. Create visual aids (file trees, diagrams)
5. Test all setup instructions
6. Link related documentation together
7. Remove irrelevant sections

### Step 4: Review for Clarity

Before finalizing:

1. Read as a beginner—does it make sense without context?
2. Check for gaps in explanation
3. Verify code examples actually work
4. Test setup instructions end-to-end
5. Ensure information is easy to find

## Documentation Types

### README Documentation

**Create for:** Project root directories, major feature modules, standalone components.

**Essential sections:**

- What this does (1-2 sentences, plain English)
- Quick start (< 5 minutes to running)
- Project structure (visual file tree)
- Key concepts (core abstractions)
- Common tasks (step-by-step guides)
- Troubleshooting (common issues and solutions)

**Template:** `assets/templates/README.template.md`

### Architecture Documentation

**Create for:** Projects with multiple modules, complex data flows, or non-obvious design decisions.

**Essential sections:**

- System design (high-level diagram)
- Directory structure (detailed breakdown)
- Data flow (how data moves through system)
- Key design decisions (why choices were made)
- Module dependencies (how parts interact)
- Extension points (where to add features)

**Template:** `assets/templates/ARCHITECTURE.template.md`

### API Documentation

**Create for:** HTTP endpoints, SDK methods, public interfaces.

**Essential sections:**

- What it does (plain-English explanation)
- Endpoint and method
- Authentication requirements
- Request format (parameters, body)
- Response format (success and errors)
- Working example (curl or SDK)
- Common errors and solutions

**Template:** `assets/templates/API.template.md`

### Code Comments

**Create for:** Complex logic, non-obvious algorithms, code requiring context.

**Principles:**

- Explain "why" not "what"—code shows what it does
- Document edge cases and business logic
- Add examples for complex functions
- Note gotchas and counterintuitive behavior
- Keep comments current with code changes

**Examples:** `assets/templates/CODE_COMMENTS.template.md`

## Visual Aids Quick Reference

### File Tree Structures

```text
project-root/
├── src/                    # Source code
│   ├── components/        # Reusable UI components
│   ├── services/          # Business logic and API calls
│   └── utils/             # Helper functions
├── tests/                 # Test files
└── package.json           # Dependencies and scripts
```

### Data Flow Diagrams

```text
User Request Flow:
[1] components/Form.tsx → [2] services/validation.ts → [3] services/api.ts
                                                            ↓
[5] components/Form.tsx ← [4] Database (PostgreSQL)
```

For comprehensive visual aid patterns, consult `references/visual_aids_guide.md`.

## Output Guidelines

When generating documentation:

1. **Target the audience** - Adjust complexity for beginners vs advanced users
2. **Use consistent formatting** - Follow markdown conventions
3. **Test everything** - Verify code snippets and commands work
4. **Link documents** - Create navigation between related docs
5. **Keep maintainable** - Documentation should be easy to update
6. **Add metadata** - Include last updated dates and version info

## Additional Resources

### Templates

| Template                                     | Purpose                                        |
| -------------------------------------------- | ---------------------------------------------- |
| `assets/templates/README.template.md`        | Project READMEs with quick start and structure |
| `assets/templates/ARCHITECTURE.template.md`  | System design and data flow documentation      |
| `assets/templates/API.template.md`           | API endpoints with examples and error handling |
| `assets/templates/CODE_COMMENTS.template.md` | Inline documentation patterns                  |

### Reference Files

For detailed guidance, consult:

- **`references/documentation_guidelines.md`** - Comprehensive style guide, writing conventions, testing documentation, accessibility, and maintenance practices
- **`references/visual_aids_guide.md`** - Detailed patterns for file trees, architecture diagrams, sequence diagrams, state machines, and comparison tables
- **`references/workflow_procedures.md`** - Step-by-step procedures for codebase analysis, detailed examples for each documentation type, comment patterns by language, and review checklists

Load references when:

- Creating enterprise-level documentation
- Standardizing across large projects
- Needing advanced patterns or accessibility guidance
- Following detailed step-by-step procedures with examples

## Integration with Other Skills

This skill works in conjunction with:

- **Global Standards** - Foundation for code commenting conventions and documentation style
- **Backend Standards** - API documentation patterns and endpoint documentation
- **Research Paper Writer** - Academic-style technical documentation when formality is required
