---
name: research-paper-writer
version: "1.0.0"
description: This skill should be used when the user asks to "write a research paper", "create an academic paper", "write a conference paper", "draft a journal article", "write a survey paper", "create a technical paper", "help me draft my paper", "draft the methodology section", "write an abstract", "structure my findings as a paper", "write the introduction section", "write related work", or mentions IEEE/ACM formatting for scholarly writing.
---

# Research Paper Writer

## Overview

This skill guides creation of formal academic research papers meeting IEEE and ACM publication standards. It ensures proper structure, formatting, and scholarly writing style.

## Workflow

### 1. Gather Requirements

Before starting, clarify the following with the user:

- **Topic and scope**: Main research question or contribution
- **Target venue**: Conference, journal, or general academic audience
- **Length**: Page count or word count target
- **Format**: IEEE (default) or ACM
- **Materials**: Any provided research data, references, or prior work

### 2. Paper Structure

Apply this standard academic paper structure:

| Section              | Purpose                                                                       |
| -------------------- | ----------------------------------------------------------------------------- |
| **Title & Abstract** | Concise title; 150-250 word summary of purpose, methods, results              |
| **Introduction**     | Motivation, problem statement, research gap, 3-5 contributions, paper roadmap |
| **Related Work**     | Literature review, comparison with existing approaches, positioning           |
| **Methodology**      | Proposed method/system, architecture, algorithms, design rationale            |
| **Implementation**   | Technical details, tools, challenges (if applicable)                          |
| **Evaluation**       | Experimental setup, datasets, metrics, results with tables/graphs             |
| **Discussion**       | Implications, limitations, lessons learned                                    |
| **Conclusion**       | Summary of contributions, future directions                                   |
| **References**       | Comprehensive bibliography (15-20+ references)                                |

### 3. Drafting Order

Draft sections in this order for coherence:

1. **Methodology** - Core contribution first
2. **Introduction** - Frame the contribution
3. **Related Work** - Position against literature
4. **Results/Evaluation** - Validate claims
5. **Discussion & Conclusion** - Interpret and summarize
6. **Abstract** - Write last (summary of complete paper)

### 4. Academic Writing Conventions

**Tone:**

- Formal, objective, precise language
- Third-person perspective (reserve "we" for contributions)
- Present tense for facts; past tense for specific studies

**Technical precision:**

- Define acronyms on first use: "Large Vision-Language Models (LVLMs)"
- Quantify claims with metrics or evidence
- Avoid vague terms ("significant", "many") without data

**Argumentation:**

- State claims, then support with evidence
- Compare explicitly with related work: "Unlike [X] which..., our approach..."
- Address limitations and counterarguments

**Section-specific patterns:**

*Abstract:* Broad context → specific problem → approach → key results (self-contained)

*Introduction:* Real-world motivation → problem statement → contributions list → paper roadmap

*Related Work:* Group by theme, compare explicitly, identify gaps, position current work

*Results:* Present data objectively, compare with baselines, acknowledge negative results

### 5. Citations

**In-text format:**

- Numbered: "Recent work [1, 2] has shown..."
- Multiple citations in order: [3, 7, 12]
- Reference specific sections: "As in [5, Section 3]..."

**Reference list:**

- Order by citation number or alphabetically
- Include DOI/URL when available
- Mix recent (last 5 years) and foundational works
- For detailed formatting, consult `references/ieee_formatting_specs.md` or `references/acm_formatting_specs.md`

### 6. Review Checklist

Before finalizing:

- [ ] Logical flow between sections
- [ ] Consistent terminology throughout
- [ ] All figures/tables referenced in text
- [ ] Abstract matches actual content
- [ ] Citations complete and properly formatted
- [ ] Contributions clearly stated and validated

## Paper Types

### Survey/Review Paper

- Emphasize taxonomy and classification
- Extensive related work coverage
- Identify trends and research gaps
- Typically 20-30 pages

### Experimental Paper

- Strong methodology section
- Rigorous evaluation with baselines
- Ablation studies and error analysis
- Reproducibility details

### Position/Vision Paper

- Compelling motivation
- Novel perspective or framework
- Future research directions
- Shorter, more argumentative

## Resources

### Reference Files

Consult these for detailed specifications:

| File                                  | Content                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------- |
| `references/writing_style_guide.md`   | Academic writing conventions, paragraph construction, common phrases       |
| `references/ieee_formatting_specs.md` | Complete IEEE page setup, typography, figures, tables, citations           |
| `references/acm_formatting_specs.md`  | Complete ACM formatting including CCS Concepts, keywords, DOI requirements |

### Assets

| File                             | Usage                                        |
| -------------------------------- | -------------------------------------------- |
| `assets/full_paper_template.pdf` | IEEE paper template with formatting examples |
| `assets/interim-layout.pdf`      | ACM paper template                           |

### Examples

Working examples in `examples/`:

| File                                     | Description                                 |
| ---------------------------------------- | ------------------------------------------- |
| `examples/survey_paper_outline.md`       | Complete outline for a survey paper         |
| `examples/experimental_paper_outline.md` | Outline for an experimental/empirical paper |

## Critical Notes

- **Clarify scope first**: Always ask about topic, length, and format before starting
- **User provides content**: This skill structures and writes; the user provides technical contributions and findings
- **Academic integrity**: Proper attribution is essential
- **Acknowledge limitations**: Honest discussion of constraints and threats to validity
- **Consistency**: Maintain uniform terminology, notation, and style throughout

## Integration with Other Skills

This skill works in conjunction with:

- **Global Standards** - Foundation for code examples and technical writing clarity
- **Codebase Documenter** - For code documentation sections within papers
- **Testing Standards** - For methodology and evaluation sections involving software testing
