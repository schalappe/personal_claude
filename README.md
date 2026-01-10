# Personal Claude

A Claude Code configuration repository that extends Claude's capabilities with specialized skills, agents, and slash commands.

## What's Included

### Skills

Domain-specific modules that provide structured guidance for common development tasks:

- **backend-standards** - API design, database patterns, service layers
- **frontend-design** - Production-grade UI components and interfaces
- **global-standards** - Code formatting, naming conventions, error handling
- **testing-standards** - Test patterns, coverage strategies, mocking
- **codebase-documenter** - README generation, architecture docs
- **product-planning** - Mission docs, roadmaps, tech stack decisions
- **spec-creation** - Feature specifications and requirements
- **task-breakdown** - Breaking specs into implementation tasks
- **research-paper-writer** - Academic paper structure and formatting

### Agents

Specialized analysis agents for targeted tasks:

- **code-explorer** - Deep codebase analysis and architecture mapping
- **code-architect** - Feature design and implementation blueprints
- **code-reviewer** - Bug detection and code quality review

### Commands

Slash commands organized by category:

**Git** (`/commit`, `/clean_gone`, `/commit-push-pr`)
- Streamlined git workflows with conventional commits

**Dev Kit** (`/code-mode`, `/debug-mode`, `/docs-mode`, `/test-mode`, `/ask-mode`, `/architect-mode`)
- Development workflow modes

**Spec Dev** (`/write-spec`, `/shape-spec`, `/plan-product`, `/create-tasks`, `/implement-task`)
- Specification-first development workflow

## Installation

Copy the contents of this repository to your Claude Code settings directory:

```bash
# Copy to global Claude settings
cp -r skills agents commands ~/.claude/
```

Or symlink for easier updates:

```bash
ln -s /path/to/personal_claude/skills ~/.claude/skills
ln -s /path/to/personal_claude/agents ~/.claude/agents
ln -s /path/to/personal_claude/commands ~/.claude/commands
```

## Usage

Skills are automatically triggered based on context. Commands are invoked with `/`:

```bash
/commit          # Create a conventional commit
/code-mode       # Enter focused coding mode
/shape-spec      # Start shaping a new feature spec
```

## License

Personal configuration - use as inspiration for your own setup.
