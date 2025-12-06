---
description: Add clear and concise comments to code, following best practices
---

/code-refactor Read and understand relevant files before adding comments; do not speculate about code you have not inspected.

This is my comment policy:

**Core Principles:**

- Comments must be minimal and purposeful; prefer self-explanatory code.
- Start with an uppercase letter and end with a period.
- Focus on the "why" or non-obvious "how"; never restate what the code already says.
- One comment per logical block; avoid comment clusters.

**Syntax:**

**Python:**

| Prefix   | Purpose                                           |
| -------- | ------------------------------------------------- |
| `# ##!:` | Warning, gotcha, pitfall, critical note.          |
| `# ##>:` | Explanation, reason, context, business logic.     |
| `# ##?:` | Question, uncertainty, needs review or decision.  |
| `# ##@:` | TODO, future improvement, planned change.         |
| `# ##~:` | Workaround, hack, temporary fix.                  |
| `# ##&:` | Dependency, external API behavior, library quirk. |

**JavaScript / TypeScript:**

| Prefix    | Purpose                                           |
| --------- | ------------------------------------------------- |
| `// [!]:` | Warning, gotcha, pitfall, critical note.          |
| `// [>]:` | Explanation, reason, context, business logic.     |
| `// [?]:` | Question, uncertainty, needs review or decision.  |
| `// [@]:` | TODO, future improvement, planned change.         |
| `// [~]:` | Workaround, hack, temporary fix.                  |
| `// [&]:` | Dependency, external API behavior, library quirk. |

**Categories (implicit in comment content):**

- **Reason** — Why this approach was chosen.
- **Security** — Auth, validation, sanitization concerns.
- **Business Logic** — Domain rules, edge cases.
- **Technical** — Performance, compatibility, limitations.
- **Dependency** — External API behavior, library quirks.

**Anti-patterns (to remove):**

- Restating what the code does: `x = x + 1  # Increment x.`
- Obvious variable descriptions: `user_id = 42  # The user ID.`
- Commented-out dead code without explanation.
- TODO/FIXME without owner or context.

Analyze files (Python, JavaScript, or TypeScript):

1. Remove useless comments (restatements, obvious, dead code).
2. Convert valid comments to the correct prefix style.
3. Ensure proper capitalization and punctuation.
4. Flag ambiguous comments for review.
