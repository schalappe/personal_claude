# Git Plugin

A Claude Code plugin for git workflow automation, providing commands for committing, branch cleanup, and pull request creation.

## Features

- **Conventional Commits**: Create properly formatted commits with type, scope, and description
- **Branch Cleanup**: Remove local branches that have been deleted from remote
- **PR Workflow**: Complete flow from commit to push to pull request creation

## Commands

### /git:commit

Stage changes and create a conventional git commit.

```bash
/git:commit
```

**What it does:**
- Shows current git status and changes
- Creates a conventional commit (`type(scope): description`)
- Supports: feat, fix, docs, refactor, test, chore

### /git:clean_gone

Clean up local branches deleted from remote, including worktrees.

```bash
/git:clean_gone
```

**What it does:**
- Identifies branches marked as `[gone]`
- Removes associated worktrees if present
- Deletes the local branches

### /git:commit-push-pr

Complete workflow: commit, push, and create a pull request.

```bash
/git:commit-push-pr
```

**What it does:**
- Creates a feature branch if on main
- Stages and commits with conventional format
- Pushes to origin
- Creates a PR with summary and test plan

## Installation

Add this plugin to your Claude Code configuration:

```bash
claude --plugin-dir /path/to/plugins/git
```

Or copy to your project's `.claude/plugins/` directory.

## Usage

Simply run any command when you have git changes to process:

```bash
# Quick commit
/git:commit

# Full PR workflow
/git:commit-push-pr

# After merging PRs, clean up
/git:clean_gone
```

## Requirements

- Git installed and configured
- GitHub CLI (`gh`) for PR creation
- Valid git repository

## License

MIT
