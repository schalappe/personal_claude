# Academic Plugin

A Claude Code plugin for academic writing support, focusing on research paper creation with IEEE and ACM formatting standards.

## Features

- **Research Paper Writer Skill**: Comprehensive guidance for writing formal academic papers
- IEEE and ACM formatting specifications
- Academic writing style conventions
- Paper structure templates for survey and experimental papers

## Skills

### research-paper-writer

Helps create formal academic research papers meeting publication standards.

**Triggers when you ask to:**
- "write a research paper"
- "create an academic paper"
- "write a conference paper"
- "draft a journal article"
- "write a survey paper"
- "draft the methodology section"
- "write an abstract"
- "structure my findings as a paper"

**Includes:**
- Paper structure guidance (Abstract, Introduction, Methodology, Results, etc.)
- IEEE formatting specifications
- ACM formatting specifications
- Academic writing style guide
- Example outlines for survey and experimental papers

## Installation

Add this plugin to your Claude Code configuration:

```bash
claude --plugin-dir /path/to/plugins/academic
```

Or copy to your project's `.claude/plugins/` directory.

## Usage

Simply ask Claude to help with academic writing tasks. The skill activates automatically based on your request.

**Example prompts:**
- "Help me write the introduction section for my machine learning paper"
- "Create an outline for a survey paper on context-aware systems"
- "What's the correct IEEE citation format for conference papers?"
- "Draft an abstract for my experimental study on vision-language models"

## References

The plugin includes detailed reference materials:

| File | Content |
|------|---------|
| `references/ieee_formatting_specs.md` | Complete IEEE page setup, typography, figures, tables, citations |
| `references/acm_formatting_specs.md` | Complete ACM formatting including CCS Concepts, keywords, DOI requirements |
| `references/writing_style_guide.md` | Academic writing conventions, paragraph construction, common phrases |

## Examples

Working examples in `skills/research-paper-writer/examples/`:

- `survey_paper_outline.md` - Complete outline for a survey/review paper
- `experimental_paper_outline.md` - Outline for an experimental/empirical paper

## Requirements

- Claude Code CLI
- No external dependencies

## License

MIT
