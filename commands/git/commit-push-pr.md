---
description: Commit changes, push branch, and open a pull request
allowed-tools: Bash(git checkout:*), Bash(git add:*), Bash(git status:*), Bash(git push:*), Bash(git commit:*), Bash(gh pr create:*)
---

# Commit, Push, and Create PR

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status`
- Changes: !`git diff HEAD`
- Recent commits (for style): !`git log --oneline -5`

## Task

Execute the complete PR workflow based on the changes above.

### Execution Steps

1. **Branch check**: If on `main`, create a descriptive feature branch
2. **Stage & commit**: Add changes and commit with conventional message format:
   - `type(scope): description` (e.g., `feat(api): add user endpoints`)
   - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
3. **Push**: Push branch to origin with `-u` flag
4. **Create PR**: Use `gh pr create` with:
   - Clear title matching commit
   - Body with Summary and Test Plan sections

### Commit Message Footer

```text
🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

Execute all steps using parallel Bash tool calls where independent. Do not output any text besides tool calls.
