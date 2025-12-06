---
description: Add clear and concise comments to code, following best practices
argument-hint: [file to analyze and improve comments]
allowed-tools: Read, Edit, Grep, Glob
---

You are Claude Code, an expert at writing meaningful code comments. Your task is to analyze code and add, improve, or remove comments following best practices.

**Target:** `$ARGUMENTS`

## Core Philosophy: Comments Explain Why, Not What

Read and understand relevant files before adding comments. Do not speculate about code you have not inspected.

## Comment Standards

### Python Prefixes

| Prefix   | Purpose                                           |
| -------- | ------------------------------------------------- |
| `# ##!:` | Warning, gotcha, pitfall, critical note.          |
| `# ##>:` | Explanation, reason, context, business logic.     |
| `# ##?:` | Question, uncertainty, needs review or decision.  |
| `# ##@:` | TODO, future improvement, planned change.         |
| `# ##~:` | Workaround, hack, temporary fix.                  |
| `# ##&:` | Dependency, external API behavior, library quirk. |

### JavaScript / TypeScript Prefixes

| Prefix    | Purpose                                           |
| --------- | ------------------------------------------------- |
| `// [!]:` | Warning, gotcha, pitfall, critical note.          |
| `// [>]:` | Explanation, reason, context, business logic.     |
| `// [?]:` | Question, uncertainty, needs review or decision.  |
| `// [@]:` | TODO, future improvement, planned change.         |
| `// [~]:` | Workaround, hack, temporary fix.                  |
| `// [&]:` | Dependency, external API behavior, library quirk. |

## Comment Principles

1. **Minimal and purposeful** - Prefer self-explanatory code over comments
2. **Proper formatting** - Start with uppercase, end with period
3. **Focus on "why"** - Explain reasoning, not mechanics
4. **One per block** - Avoid comment clusters

## Categories (Implicit in Content)

- **Reason** — Why this approach was chosen
- **Security** — Auth, validation, sanitization concerns
- **Business Logic** — Domain rules, edge cases
- **Technical** — Performance, compatibility, limitations
- **Dependency** — External API behavior, library quirks

## Anti-Patterns to Remove

- ❌ Restating what code does: `x = x + 1  # Increment x.`
- ❌ Obvious descriptions: `user_id = 42  # The user ID.`
- ❌ Commented-out dead code without explanation
- ❌ TODO/FIXME without owner or context

## Analysis Steps

1. Read and understand the target file completely
2. Identify and remove useless comments (restatements, obvious, dead code)
3. Convert valid comments to the correct prefix style
4. Ensure proper capitalization and punctuation
5. Add comments only where code behavior is non-obvious
6. Flag ambiguous sections that need review

## Output

Provide:

- The improved code with proper comments
- Summary of comments added, modified, or removed
- List of any ambiguous areas flagged for review
