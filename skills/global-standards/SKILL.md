---
name: global-standards
version: "1.0.0"
description: This skill should be used when the user asks to "format this code", "what naming convention should I use", "how should I handle errors", "add comments to code", "organize this file", "validate input", "structure this project", "SOLID principles", "DRY principle", "clean architecture", "code quality rules", or mentions coding style, code conventions, error handling patterns, validation logic, or development best practices.
---

# Global Development Standards

Apply consistent development standards across all code changes. These principles ensure code quality, maintainability, and consistency regardless of domain (frontend, backend, testing).

## When to Apply This Skill

Activate when:

- Implementing any code changes (features, fixes, refactoring)
- Writing new functions, modules, or components
- Making architectural or structural decisions
- Handling errors or validation logic
- Adding comments or documentation to code
- Defining project conventions or configuration

## Core Principles

### Coding Style

| Principle  | Guideline                                                  |
| ---------- | ---------------------------------------------------------- |
| Naming     | Descriptive names revealing intent; avoid abbreviations    |
| Functions  | Small, focused on single task; <50 lines ideal             |
| Formatting | Consistent automated style (indentation, line breaks)      |
| Dead Code  | Delete unused code, commented blocks, imports              |
| DRY        | Extract common logic into reusable functions               |
| Simplicity | No backward compatibility hacks unless explicitly required |

### Error Handling

| Principle      | Guideline                                                |
| -------------- | -------------------------------------------------------- |
| Fail Fast      | Validate input early; reject invalid state immediately   |
| Specific Types | Use specific exception types, not generic                |
| User Messages  | Clear, actionable; no technical details or security info |
| Centralized    | Handle at boundaries (controllers, API layers)           |
| Graceful       | Degrade gracefully for non-critical failures             |
| Cleanup        | Always release resources in finally blocks               |
| Retry          | Exponential backoff for transient external failures      |

### Validation

| Principle       | Guideline                                             |
| --------------- | ----------------------------------------------------- |
| Server-Side     | Always validate server-side; never trust client alone |
| Client-Side     | Use for UX feedback; duplicate checks server-side     |
| Fail Early      | Reject invalid data before processing                 |
| Specific Errors | Field-specific messages helping users correct input   |
| Allowlists      | Define what is allowed, not what is blocked           |
| Sanitization    | Prevent injection attacks (SQL, XSS, command)         |
| Consistency     | Apply uniformly across all entry points               |

### Code Commenting

Follow this hierarchy:

1. **Self-documenting code first** - Clear structure and naming
2. **Minimal comments** - Explain large sections of logic only
3. **Evergreen only** - No comments about recent changes or fixes
4. **Focus on "why"** - Not "what" the code does

## Project Conventions

### Structure

- Organize files in predictable, logical structure
- Maintain up-to-date README with setup and architecture
- Use environment variables for configuration
- Never commit secrets or API keys

### Version Control

- Clear commit messages with type prefixes
- Feature branches for development
- Meaningful pull requests with descriptions
- Changelog for significant changes

### Dependencies

- Keep dependencies minimal and up-to-date
- Document why major dependencies exist
- Use feature flags for incomplete features

### Code Review

- Establish consistent review process
- Define testing requirements before merge
- Clear expectations for reviewers and authors

## Tech Stack Alignment

Ensure code aligns with the project's defined tech stack.

## Implementation Checklist

When implementing any code change:

1. **Naming** - Choose clear, descriptive names
2. **Size** - Write small, focused functions
3. **Validation** - Check inputs at entry points
4. **Errors** - Handle gracefully with clear messages
5. **Cleanup** - Delete dead code and unused imports
6. **Documentation** - Minimal comments; self-documenting code
7. **Conventions** - Align with project structure and team standards
8. **Testing** - Define appropriate testing requirements

## Related Skills

This skill provides foundation standards. Apply specialized skills for domain-specific guidance:

- **Backend Standards** - Server-side code patterns
- **Testing Standards** - Test writing practices

## Additional Resources

### Reference Files

For detailed patterns and examples, consult:

- **`references/patterns.md`** - Detailed coding patterns with examples for naming, error handling, validation, and commenting across languages
