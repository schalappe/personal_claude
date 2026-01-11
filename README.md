# Personal Claude Plugins

A Claude Code plugin marketplace for software engineering workflows. Install individual plugins to extend Claude Code with specialized skills, agents, and commands.

## Installation

### Via Claude Code CLI

```bash
# Install from this marketplace
/install-plugin plugin-name@github:schalappe/personal_claude
```

### Via Settings

1. Open Claude Code settings
2. Navigate to Plugins > Discover
3. Add this marketplace URL: `github:schalappe/personal_claude`
4. Browse and install desired plugins

## Available Plugins

### dev-kit

Development toolkit with coding standards, specialized agents, and mode-based commands.

| Component | Count | Description |
|-----------|-------|-------------|
| Commands | 6 | `/code-mode`, `/debug-mode`, `/docs-mode`, `/test-mode`, `/ask-mode`, `/architect-mode` |
| Agents | 3 | code-explorer, code-architect, code-reviewer |
| Skills | 5 | global-standards, backend-design, frontend-design, codebase-documenter, testing-standards |

**Use cases:** Writing code, debugging, documentation, testing, architecture design

---

### spec-dev

Specification-driven development workflow from idea to implementation.

| Component | Count | Description |
|-----------|-------|-------------|
| Commands | 6 | `/plan-product`, `/shape-spec`, `/write-spec`, `/create-tasks`, `/implement-task`, `/implement-task-loop` |
| Skills | 3 | product-planning, spec-creation, task-breakdown |

**Use cases:** Product planning, feature specifications, task breakdown, structured implementation

---

### git

Git workflow automation with conventional commit support.

| Component | Count | Description |
|-----------|-------|-------------|
| Commands | 3 | `/commit`, `/clean_gone`, `/commit-push-pr` |

**Use cases:** Staging changes, creating commits, branch cleanup, pull request creation

---

### academic

Academic writing support for research papers.

| Component | Count | Description |
|-----------|-------|-------------|
| Skills | 1 | research-paper-writer (IEEE/ACM formatting) |

**Use cases:** Research papers, conference submissions, academic writing

## Workflows

### Spec-First Development

```text
/plan-product -> /shape-spec -> /write-spec -> /create-tasks -> /implement-task
```

1. Define mission and roadmap
2. Gather requirements
3. Write detailed specification
4. Break into actionable tasks
5. Implement each task

### Direct Development

```text
/code-mode or /debug-mode
```

Quick fixes and small changes without full specification workflow.

## Agent Models

| Agent | Model | Purpose |
|-------|-------|---------|
| code-explorer | haiku | Fast codebase analysis |
| code-architect | opus | Complex architectural decisions |
| code-reviewer | sonnet | Code quality and pattern matching |

## Contributing

See [CLAUDE.md](CLAUDE.md) for development guidelines.

## License

MIT
