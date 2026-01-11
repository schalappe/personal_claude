# Spec Dev Plugin

A Claude Code plugin for specification-driven development. Provides a complete workflow from product planning through implementation.

## Workflow Overview

The plugin provides a 5-step development workflow:

```text
/plan-product → /shape-spec → /write-spec → /create-tasks → /implement-task
     ↓              ↓             ↓              ↓               ↓
  Mission      Requirements   Specification    Tasks         Code
  Roadmap      Visuals        Architecture     Acceptance    Tests
  Tech Stack   Scope          Code Reuse       Order         Reports
```

## Commands

### /spec-dev:plan-product

Create foundational product documentation: mission, roadmap, and tech stack.

```bash
/spec-dev:plan-product [product-name]
```

**Output**: `docs/product/mission.md`, `roadmap.md`, `tech-stack.md`

### /spec-dev:shape-spec

Gather and document requirements for a new feature through structured questioning.

```bash
/spec-dev:shape-spec [feature-description]
```

**Output**: `docs/specs/[date]-[name]/planning/requirements.md`

### /spec-dev:write-spec

Transform gathered requirements into a comprehensive specification document.

```bash
/spec-dev:write-spec [spec-name]
```

**Output**: `docs/specs/[date]-[name]/spec.md`

### /spec-dev:create-tasks

Transform specifications into an actionable task list with strategic grouping.

```bash
/spec-dev:create-tasks [spec-name]
```

**Output**: `docs/specs/[date]-[name]/tasks.md`

### /spec-dev:implement-task

Implement a single task group with deep codebase understanding and quality review.

```bash
/spec-dev:implement-task [spec-name] [task-group-number]
```

**Output**: Implemented code, implementation report, verification report

### /spec-dev:implement-task-loop

Implement a task group autonomously using Ralph Loop for iterative development.

```bash
/spec-dev:implement-task-loop [spec-name] [task-group-number]
```

**Output**: Implemented code with tests passing

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
│   ├── shape-spec.md         # Step 2: Requirements gathering
│   ├── write-spec.md         # Step 3: Specification writing
│   ├── create-tasks.md       # Step 4: Task breakdown
│   ├── implement-task.md     # Step 5: Implementation
│   └── implement-task-loop.md # Step 5 (alt): Autonomous implementation
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
        ├── planning/
        │   ├── requirements.md   # Gathered requirements
        │   └── visuals/          # Mockups, wireframes
        ├── implementation/       # Implementation reports
        ├── verification/         # Verification reports
        ├── spec.md               # Feature specification
        └── tasks.md              # Implementation tasks
```

## License

MIT
