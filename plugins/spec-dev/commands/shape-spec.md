---
description: Shape and plan a new feature specification through guided requirements gathering
argument-hint: [feature-description]
allowed-tools: Read, Write, Glob, Bash(ls:*, mkdir:*, date:*, test:*, grep:*), Task, Skill, AskUserQuestion, TodoWrite
---

# Shape Spec

> **Workflow Step 2 of 5** — Previous: `/plan-product` | Next: `/write-spec`

Gather and document requirements for a new feature through structured questioning. Creates the foundation for specification writing.

## Prerequisites

- Product documentation should exist at `docs/product/` (run `/plan-product` first)

## Output

- `docs/specs/[YYYY-MM-DD]-[spec-name]/` — Spec folder structure
- `docs/specs/[...]/planning/requirements.md` — Documented requirements
- `docs/specs/[...]/planning/visuals/` — Place for mockups/wireframes

---

## Phase 1: Initialize Spec Structure

### Get Feature Description

**If argument provided:** Use the feature description to initiate the spec.

**Otherwise:**

1. Check roadmap exists: ❯`test -f docs/product/roadmap.md && echo "EXISTS" || echo "MISSING"`

2. **Validation:**
   - If `MISSING` → Warn: "No roadmap found. Run `/plan-product` first, or describe the feature you want to spec."
   - If `EXISTS` → Read @docs/product/roadmap.md and identify the next unchecked feature

3. Ask the user:

   ```markdown
   Which feature would you like to spec?

   - The roadmap shows "[feature]" is next. Go with that?
   - Or describe a different feature.
   ```

4. **Wait for user response before proceeding**

### Create Folder Structure

Get today's date: ❯`date +%Y-%m-%d`

Create spec folder structure:
❯`mkdir -p docs/specs/[DATE]-[kebab-case-name]/planning/visuals`
❯`mkdir -p docs/specs/[DATE]-[kebab-case-name]/implementation`

Replace `[DATE]` with the date output and `[kebab-case-name]` with the feature name.

Output:

```markdown
✅ Spec folder initialized: `[spec-path]`

Structure:
- `planning/` — Requirements and specifications
- `planning/visuals/` — Mockups and screenshots
- `implementation/` — Implementation documentation

Proceeding to requirements gathering...
```

---

## Phase 2: Research Requirements

### Analyze Product Context

Invoke the **spec-creation** skill to provide templates and quality standards for this phase.

Read these files to understand broader context:

| Document                      | What to Extract                         |
| ----------------------------- | --------------------------------------- |
| @docs/product/mission.md      | Mission, target users, core problems    |
| @docs/product/roadmap.md      | Completed features, where this fits     |
| @docs/product/tech-stack.md   | Technologies, constraints, capabilities |

**Validation:** If any file is missing, note it but continue — not all projects have complete product docs.

### Generate Clarifying Questions

Generate 4-8 targeted, NUMBERED questions that:

- Start with reasonable assumptions ("I assume X, is that correct?")
- Make it easy to confirm or provide alternatives
- End with a question about exclusions/out-of-scope

**Format:**

```markdown
Based on your idea for [spec name], I have some clarifying questions:

1. I assume [assumption]. Is that correct, or [alternative]?
2. I'm thinking [approach]. Should we [alternative]?
3. [Continue with numbered questions...]
[N]. What should be explicitly OUT of scope for this feature?

**Visual Assets:**
Do you have mockups, wireframes, or screenshots?

If yes, place them in: `[spec-path]/planning/visuals/`
```

**STOP and wait for user response.**

### Process Answers and Check for Visuals

After receiving answers:

1. Store answers for documentation

2. **MANDATORY: Check for visual assets** (users often add files without mentioning):

   Check visuals folder: ❯`ls -la [spec-path]/planning/visuals/ 2>/dev/null | grep -E '\.(png|jpg|jpeg|gif|svg|pdf|md)$' || echo "NO_VISUALS"`

3. If visual files found:
   - Use Read tool to analyze each file
   - Note design elements, patterns, user flows
   - Check filenames for low-fidelity indicators (lofi, wireframe, sketch)

### Generate Follow-up Questions (if needed)

Follow-ups needed when:

| Trigger                              | Example Follow-up                                           |
| ------------------------------------ | ----------------------------------------------------------- |
| Visuals found but not mentioned      | "I found [files] in visuals. Let me analyze these."         |
| Low-fidelity indicators in filenames | "These appear to be wireframes. Use as layout guides only?" |
| Vague requirements                   | Specific clarification questions                            |

Limit to 1-3 follow-up questions. **Wait for responses.**

### Save Requirements

Save all gathered information to `[spec-path]/planning/requirements.md`:

```markdown
# Spec Requirements: [Spec Name]

## Initial Description
[User's original description]

## Requirements Discussion

### Questions & Answers

**Q1:** [Question]
**A:** [Answer]

**Q2:** [Question]
**A:** [Answer]

[Continue for all Q&A]

### Follow-up Questions
[If any were asked]

## Visual Assets

### Files Found
[Based on bash check, not user statement]
- `filename.png`: [Description from analysis]

### Visual Insights
- [Design patterns identified]
- [Fidelity level: high-fidelity mockup / low-fidelity wireframe]

[If no files: "No visual assets provided."]

## Requirements Summary

### Functional Requirements
- [Core functionality]
- [User actions enabled]
- [Data to be managed]

### Scope Boundaries

**In Scope:**
- [What will be built]

**Out of Scope:**
- [What won't be built]

### Technical Considerations
- [Integration points]
- [Existing constraints]
```

---

## Completion

```markdown
✅ Spec initialized: `[spec-path]`

- ✅ Requirements gathered
- ✅ Visual check: [Found X files / No files]

📁 Created: `[spec-path]/planning/requirements.md`

👉 Next: Run `/write-spec` to create the specification document.
```

---

## Constraints

- **MANDATORY**: Always run bash to check visuals folder after receiving answers
- Do NOT write technical specifications — just record findings
- Visual check is based on actual files found, not user statements
- Keep follow-ups minimal (1-3 questions max)
- Save user's exact answers, not interpretations
- Output questions and STOP to wait for responses
