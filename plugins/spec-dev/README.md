# Spec Dev Plugin

A Claude Code plugin for specification-driven development. Provides a streamlined workflow from product planning through implementation.

## Workflow Overview

The plugin provides a 3-step development workflow:

```text
/plan-product → /shape-spec → /implement-task
     ↓              ↓               ↓
  Mission      Shape + Spec      Code
  Roadmap      + Tasks           Tests
  Tech Stack   (plan mode)       Reports
```

## Commands

### /spec-dev:plan-product

Create foundational product documentation: mission, roadmap, and tech stack.

```bash
/spec-dev:plan-product [product-name]
```

**Output**: `docs/product/mission.md`, `roadmap.md`, `tech-stack.md`

### /spec-dev:shape-spec

Shape a feature from idea to actionable implementation plan. Runs in plan mode and combines requirements gathering, specification writing, and task breakdown into a single flow.

```bash
# Must be in plan mode first
/spec-dev:shape-spec [feature-description]
```

**Requires**: Plan mode active

**Output**:
- `docs/specs/[date]-[name]/shape.md` — Context and decisions
- `docs/specs/[date]-[name]/plan.md` — Specification + tasks
- `docs/specs/[date]-[name]/references.md` — Code pointers
- `docs/specs/[date]-[name]/visuals/` — Mockups if provided

### /spec-dev:implement-task

Implement a single task group with deep codebase understanding and quality review.

```bash
/spec-dev:implement-task [spec-name] [task-group-number]
```

**Output**: Implemented code, implementation report, verification report

## Skills

| Skill | Purpose |
|-------|---------|
| `product-planning` | Templates for mission, roadmap, and tech stack documents |
| `spec-creation` | Philosophy and templates for specification documents |
| `task-breakdown` | Sizing rules, grouping patterns, and task templates |

Skills are automatically activated when relevant queries are detected.

## Installation

Add this plugin to your Claude Code configuration:

```bash
claude --plugin-dir /path/to/plugins/spec-dev
```

Or copy to your project's `.claude/plugins/` directory.

## Structure

```text
spec-dev/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── commands/
│   ├── plan-product.md       # Step 1: Product planning
│   ├── shape-spec.md         # Step 2: Shape, spec, and tasks (unified)
│   └── implement-task.md     # Step 3: Implementation
├── skills/
│   ├── product-planning/     # Product documentation skill
│   │   ├── SKILL.md
│   │   └── references/
│   ├── spec-creation/        # Specification skill
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── examples/
│   └── task-breakdown/       # Task breakdown skill
│       ├── SKILL.md
│       ├── references/
│       └── examples/
└── README.md
```

## Output Structure

The workflow creates this directory structure in your project:

```text
docs/
├── product/
│   ├── mission.md      # Product vision and strategy
│   ├── roadmap.md      # Feature prioritization
│   └── tech-stack.md   # Technical decisions
└── specs/
    └── YYYY-MM-DD-feature-name/
        ├── shape.md          # Context, decisions, scope
        ├── plan.md           # Specification + implementation tasks
        ├── references.md     # Code pointers from exploration
        ├── visuals/          # Mockups, wireframes
        ├── implementation/   # Implementation reports
        └── verification/     # Verification reports
```

## License

MIT
