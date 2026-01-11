# Dev Kit Plugin

A Claude Code plugin providing development standards, specialized analysis agents, and mode-based commands for software engineering workflows.

## Features

- **Skills**: Coding standards and design patterns (global, backend, frontend, testing, documentation)
- **Agents**: Specialized autonomous agents for code exploration, architecture design, and code review
- **Commands**: Mode-based commands for focused development tasks

## Skills

| Skill | Purpose |
|-------|---------|
| `global-standards` | Coding style, error handling, validation, SOLID principles, clean architecture |
| `backend-design` | REST API design patterns, resource modeling, response structures |
| `frontend-design` | UI/UX implementation with distinctive aesthetics using shadcn/ui |
| `testing-standards` | Strategic testing approach with minimal, behavior-focused tests |
| `codebase-documenter` | README, architecture docs, API documentation, code comments |
| `logging-standards` | Wide events, structured logging, observability, production debugging |

Skills are automatically activated when relevant queries are detected.

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `code-explorer` | haiku | Traces execution paths, maps architecture, documents dependencies |
| `code-architect` | opus | Designs feature architectures with implementation blueprints |
| `code-reviewer` | sonnet | Reviews code for bugs, security issues, and convention adherence |

Agents run autonomously on specialized tasks and return comprehensive reports.

## Commands

### /dev-kit:code-mode

Write code, implement features, and fix bugs.

```bash
/dev-kit:code-mode [feature or bug to implement/fix]
```

Orchestrates the code-explorer, code-architect, and code-reviewer agents.

### /dev-kit:debug-mode

Debug software, identify and fix issues.

```bash
/dev-kit:debug-mode [issue to debug]
```

### /dev-kit:docs-mode

Write clear and comprehensive documentation.

```bash
/dev-kit:docs-mode [what to document]
```

### /dev-kit:test-mode

Write tests for code, verify functionality.

```bash
/dev-kit:test-mode [what to test]
```

### /dev-kit:ask-mode

Answer questions about code, architecture, or technical topics.

```bash
/dev-kit:ask-mode [question]
```

### /dev-kit:architect-mode

Review and improve application architecture.

```bash
/dev-kit:architect-mode [architecture concern]
```

### /dev-kit:logging-mode

Add or improve logging with wide events and structured logging.

```bash
/dev-kit:logging-mode [file or module to add/improve logging]
```

Transforms scattered log statements into queryable wide events.

## Installation

Add this plugin to your Claude Code configuration:

```bash
claude --plugin-dir /path/to/plugins/dev-kit
```

Or copy to your project's `.claude/plugins/` directory.

## Structure

```text
dev-kit/
├── .claude-plugin/
│   └── plugin.json        # Plugin manifest
├── agents/
│   ├── code-architect.md  # Architecture design agent
│   ├── code-explorer.md   # Code analysis agent
│   └── code-reviewer.md   # Code review agent
├── commands/
│   ├── architect-mode.md  # Architecture command
│   ├── ask-mode.md        # Q&A command
│   ├── code-mode.md       # Coding command
│   ├── debug-mode.md      # Debugging command
│   ├── docs-mode.md       # Documentation command
│   ├── logging-mode.md    # Logging command
│   └── test-mode.md       # Testing command
├── skills/
│   ├── backend-design/    # API design patterns
│   ├── codebase-documenter/ # Documentation skill
│   ├── frontend-design/   # UI/UX patterns
│   ├── global-standards/  # Coding standards
│   ├── logging-standards/ # Structured logging patterns
│   └── testing-standards/ # Testing patterns
└── README.md
```

## License

MIT
