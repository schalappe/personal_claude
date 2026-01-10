# Personal Claude

A Claude Code configuration repository that extends Claude's capabilities with specialized skills, agents, and slash commands.

## What's Included

### Skills

Domain-specific modules that provide structured guidance for common development tasks:

- **global-standards** - Coding standards, naming conventions, error handling, architecture patterns (SOLID, repository, service layer)
- **backend-design** - REST API design patterns, resource modeling, response structures
- **frontend-design** - Production-grade UI components and interfaces
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

## Architecture

### Component Relationships

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                              COMMANDS                                       │
│                                                                             │
│   ┌─────────────────┐  ┌─────────────────────┐  ┌──────────────────────┐    │
│   │     Git (3)     │  │    Dev Kit (6)      │  │    Spec Dev (5)      │    │
│   │                 │  │                     │  │                      │    │
│   │ • commit        │  │ • code-mode    ─────┼──┼─→ implement-task     │    │
│   │ • clean_gone    │  │ • debug-mode        │  │ • create-tasks       │    │
│   │ • commit-push-pr│  │ • test-mode         │  │ • write-spec         │    │
│   │                 │  │ • docs-mode         │  │ • shape-spec         │    │
│   │                 │  │ • ask-mode          │  │ • plan-product       │    │
│   │                 │  │ • architect-mode    │  │                      │    │
│   └─────────────────┘  └──────────┬──────────┘  └──────────┬───────────┘    │
│                                   │                        │                │
└───────────────────────────────────┼────────────────────────┼────────────────┘
                                    │                        │
                    ┌───────────────┴────────────────────────┴───────────────┐
                    │                                                        │
                    ▼                                                        ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                               AGENTS                                        │
│                                                                             │
│   ┌───────────────────┐  ┌────────────────────┐  ┌───────────────────┐      │
│   │   code-explorer   │  │   code-architect   │  │   code-reviewer   │      │
│   │     (haiku)       │  │     (opus)         │  │     (sonnet)      │      │
│   │                   │  │                    │  │                   │      │
│   │ • Trace paths     │  │ • Design features  │  │ • Find bugs       │      │
│   │ • Map layers      │  │ • Create blueprints│  │ • Quality review  │      │
│   │ • Find patterns   │  │ • Plan data flows  │  │ • Security audit  │      │
│   └───────────────────┘  └────────────────────┘  └───────────────────┘      │
│                                                                             │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                               SKILLS                                        │
│                                                                             │
│   Foundation:          Design:                     Workflow:                │
│   ┌────────────────┐   ┌────────────────────┐    ┌────────────────────┐     │
│   │global-standards│   │ backend-design     │    │ product-planning   │     │
│   │(all commands)  │   │ frontend-design    │    │ spec-creation      │     │
│   └────────────────┘   └────────────────────┘    │ task-breakdown     │     │
│                                                  └────────────────────┘     │
│                        Domain:                                              │
│                        ┌────────────────────┐                               │
│                        │ testing-standards  │                               │
│                        │ codebase-documenter│                               │
│                        │ research-paper-    │                               │
│                        │   writer           │                               │
│                        └────────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Command → Agent → Skill Dependencies

| Command | Agents Used | Skills Used |
|---------|-------------|-------------|
| `/code-mode` | explorer, architect, reviewer | global-standards |
| `/debug-mode` | explorer, reviewer | global-standards |
| `/test-mode` | explorer, reviewer | testing-standards |
| `/docs-mode` | explorer | codebase-documenter |
| `/ask-mode` | explorer | — |
| `/architect-mode` | explorer, architect | global-standards |
| `/plan-product` | — | product-planning |
| `/shape-spec` | — | spec-creation |
| `/write-spec` | explorer ×2-3, architect | spec-creation |
| `/create-tasks` | — | task-breakdown |
| `/implement-task` | explorer ×2-3, architect ×2-3, reviewer ×3 | all relevant |

### Development Workflows

**Spec-First Development** (recommended for features):

```text
/plan-product → /shape-spec → /write-spec → /create-tasks → /implement-task
     │              │              │              │               │
     ▼              ▼              ▼              ▼               ▼
  Mission       Requirements   Detailed       Actionable      Code with
  & Roadmap     Gathered       Spec           Tasks           QA Review
```

**Direct Development** (quick fixes, small changes):

```text
/code-mode or /debug-mode
       │
       ▼
  ┌─────────┐    ┌───────────┐    ┌──────────┐
  │ Explore │ →  │ Implement │ →  │ Review   │
  └─────────┘    └───────────┘    └──────────┘
```

### Agent Model Selection

| Agent | Model | Why |
|-------|-------|-----|
| code-explorer | haiku | Fast, cost-effective for read-heavy analysis |
| code-architect | opus | Complex reasoning for architectural decisions |
| code-reviewer | sonnet | Balanced for pattern matching and quality checks |

## License

Personal configuration - use as inspiration for your own setup.
