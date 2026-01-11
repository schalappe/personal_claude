# Spec Shaping Guide

Detailed guidance for the requirements gathering phase of specification creation.

## Overview

Spec shaping transforms a vague feature idea into documented, validated requirements through structured questioning and analysis.

## Step-by-Step Process

### 1. Feature Description Acquisition

**If description provided**: Proceed immediately to start the spec.

**If no description**:

1. Read `docs/product/roadmap.md`
2. Find the next planned feature
3. Present to user: "The roadmap shows [X] is next. Proceed with that or provide your own?"
4. **STOP and wait for user response**

### 2. Folder Initialization

Create dated spec folder structure:

```bash
TODAY=$(date +%Y-%m-%d)
SPEC_NAME="kebab-case-feature-name"
DATED_SPEC_NAME="${TODAY}-${SPEC_NAME}"
SPEC_PATH="docs/specs/$DATED_SPEC_NAME"

mkdir -p $SPEC_PATH/planning
mkdir -p $SPEC_PATH/planning/visuals
mkdir -p $SPEC_PATH/implementation
```

**Naming conventions**:

- YYYY-MM-DD date prefix
- Feature name in kebab-case
- Example: `2025-11-16-user-authentication`

### 3. Product Context Analysis

Before asking questions, read these files to understand context:

**`docs/product/mission.md`**:

- Product's overall mission and purpose
- Target users and primary use cases
- Core problems being solved
- How users benefit

**`docs/product/roadmap.md`**:

- Already completed features
- Current product state
- Where this feature fits
- Related features for context

**`docs/product/tech-stack.md`**:

- Technologies and frameworks in use
- Technical constraints
- Available libraries and tools

**Why this matters**: Questions become more relevant, existing features to reuse are identified, and feature alignment with product goals is ensured.

### 4. Question Generation Strategy

Generate 4-8 numbered questions that:

- Propose sensible assumptions based on best practices
- Make it easy for the user to confirm or provide alternatives
- Include specific suggestions to respond to
- Cover functional requirements, constraints, and exclusions

**Question framing patterns**:

- "I assume [specific assumption]. Is that correct, or [alternative]?"
- "I'm thinking [specific approach]. Should we [alternative]?"
- "For [aspect], I suggest [option]. Does that work, or would you prefer [other option]?"

**Question categories to cover**:

1. Core functionality (what the feature does)
2. User interactions (how users engage with it)
3. Data and state (what's stored, how it persists)
4. Integration points (how it connects to existing features)
5. Constraints and limitations (performance, security, etc.)
6. Edge cases and error handling
7. What's explicitly NOT included (scope boundaries)

**Always include at end**:

**Reusability question**:

```text
Are there existing features in the codebase with similar patterns to reference?
For example:
- Similar interface elements or UI components to re-use
- Comparable page layouts or navigation patterns
- Related backend logic or service objects
- Existing models or controllers with similar functionality

Provide file/folder paths or names of these features if they exist.
```

**Visual assets request**:

```text
Do any design mockups, wireframes, or screenshots exist that could guide development?

If yes, place them in: `[spec-path]/planning/visuals/`

Use descriptive file names like:
- homepage-mockup.png
- dashboard-wireframe.jpg
- lofi-form-layout.png
- mobile-view.png
- existing-ui-screenshot.png
```

**Then STOP and wait for user answers.**

### 5. Answer Processing

When user responds:

**Store answers**: Keep exact wording without interpretation or rephrasing.

**MANDATORY visual check** (even if user said "no visuals"):

```bash
# Users often add files without mentioning them!
ls -la [spec-path]/planning/visuals/ 2>/dev/null | grep -E '\.(png|jpg|jpeg|gif|svg|pdf)$' || echo "No visual files found"
```

**If visual files found**:

1. Read EACH file with Read tool
2. Document design elements: layouts, components, colors, typography, spacing
3. Note user flows and interaction patterns
4. Check filename for fidelity indicators:
   - "lofi", "lo-fi", "wireframe", "sketch", "rough" → low-fidelity
   - High-fidelity if detailed colors, final copy, polished design

**If user mentioned similar features**:

- Note the paths/names provided
- DO NOT explore them during shaping (saves time)
- Document for spec-writer to reference later

### 6. Follow-up Questions (If Needed)

Determine if follow-ups are needed based on:

**Visual-triggered**:

- Visuals found but user didn't mention them → acknowledge and analyze
- Low-fidelity filenames → clarify if wireframes or exact designs
- Visual shows features not discussed → ask about them
- Discrepancy between answers and visuals → resolve it

**Reusability-triggered**:

- User didn't provide similar features but spec seems common → ask
- Provided paths seem incomplete → ask for related logic/services

**Answer-triggered**:

- Vague requirements → ask for specifics
- Missing technical details → ask for clarification
- Unclear scope boundaries → define them

**Keep follow-ups minimal**: 1-3 questions maximum.

**Format**:

```text
Based on your answers [and the visual files found], a few follow-up questions:

1. [Specific question]
2. [Another if needed]

Please provide these additional details.
```

**Then STOP and wait.**

### 7. Requirements Documentation

After all questions answered, save to `[spec-path]/planning/requirements.md`:

**Use this exact structure**:

```markdown
# Spec Requirements: [Spec Name]

## Initial Description
[User's original description verbatim]

## Requirements Discussion

### First Round Questions

**Q1:** [Question asked]
**Answer:** [User's exact answer]

**Q2:** [Second question]
**Answer:** [User's exact answer]

[Continue for all questions]

### Existing Code to Reference

**Similar Features Identified:**
- Feature: [Name] - Path: `[path from user]`
- Components to reuse: [what user said]
- Backend logic to reference: [what user said]

[OR if none]
No similar existing features identified for reference.

### Follow-up Questions
[If any asked]

**Follow-up 1:** [Question]
**Answer:** [User's answer]

## Visual Assets

### Files Provided:
[Based on bash check, NOT user statement]
- `filename.png`: [What was observed analyzing it]
- `filename2.jpg`: [Key elements seen]

### Visual Insights:
- [Design patterns identified]
- [User flow implications]
- [UI components shown]
- [Fidelity level: high-fidelity mockup / low-fidelity wireframe]

[OR if bash found none]
No visual assets provided.

## Requirements Summary

### Functional Requirements
- [Core functionality from answers]
- [User actions enabled]
- [Data to be managed]

### Reusability Opportunities
- [Components that might exist based on user input]
- [Backend patterns to investigate]
- [Similar features to model after]

### Scope Boundaries

**In Scope:**
- [What will be built]

**Out of Scope:**
- [What won't be built]
- [Future enhancements mentioned]

### Technical Considerations
- [Integration points mentioned]
- [Existing system constraints]
- [Technology preferences stated]
- [Similar code patterns to follow]
```

**Critical rules**:

- Use user's exact words for answers
- Base "Visual Assets" on bash check, not user claims
- Document fidelity level of visuals
- Note paths to similar features but don't explore them
- Keep it factual, not interpretive

### 8. Completion Output

Display:

```markdown
Spec initialized successfully!

Spec folder created: `[spec-path]`
- Requirements gathered
- Visual assets: [Found X files / No files provided]

Requirements research complete!
- Processed [X] clarifying questions
- Visual check performed: [Found and analyzed Y files / No files found]
- Reusability opportunities: [Identified Z similar features / None identified]
- Requirements documented comprehensively

Requirements saved to: `[spec-path]/planning/requirements.md`

Run `/write-spec` to create the spec.md document.
```

## Best Practices

### DO

- Always check visuals folder via bash after receiving answers
- Ask about existing similar features for reusability
- Propose assumptions to make it easy for user to confirm
- Document user's exact answers, not interpretations
- Analyze every visual file with Read tool
- Check filenames for fidelity indicators
- Keep follow-ups minimal (1-3 max)
- Stop and wait for user responses at each interaction point

### DON'T

- Skip the mandatory visual check
- Rephrase or interpret user answers
- Explore existing code during shaping (save for writing phase)
- Ask too many follow-up questions (overwhelming)
- Proceed without user response when a question was asked
- Write technical specifications yet (that's the writing phase)
- Trust user's claim about visuals (they often forget files they added)

## Common Scenarios

### Scenario 1: User says "no visuals" but files exist

```bash
# Asked about visuals, user said "no"
# But MUST check anyway:
ls -la docs/specs/2025-11-16-feature/planning/visuals/

# Finds: mockup.png, wireframe.jpg

# Response:
"Found mockup.png and wireframe.jpg in the visuals folder.
Let me analyze these to better understand the design requirements."

# Then read each file with Read tool
```

### Scenario 2: Low-fidelity wireframe filenames

```bash
# Files found: lofi-dashboard.png, rough-sketch-form.jpg

# Follow-up:
"I notice lofi-dashboard.png and rough-sketch-form.jpg appear to be
wireframes or low-fidelity mockups. Should these be treated as layout
and structure guides rather than exact design specifications, using
the application's existing styling instead?"
```

### Scenario 3: User mentions similar feature

```bash
# User answer: "Yeah, we have a similar form at app/views/posts/new.html.erb"

# Document it in requirements.md:
**Similar Features Identified:**
- Feature: Post creation form - Path: `app/views/posts/new.html.erb`
- Components to reuse: form layout and validation patterns

# DO NOT read the file during shaping
# The spec-writer will explore it during writing phase
```

## Quality Checklist

Before moving to writing phase:

- [ ] Spec folder created with proper YYYY-MM-DD-name format
- [ ] Product context files read (mission, roadmap, tech-stack)
- [ ] 4-8 clarifying questions asked with sensible defaults
- [ ] Reusability question included
- [ ] Visual assets request included
- [ ] User answers received
- [ ] Mandatory bash visual check performed
- [ ] All visual files analyzed with Read tool
- [ ] Follow-ups asked if needed (max 1-3)
- [ ] All answers documented to requirements.md exactly as stated
- [ ] Visual insights documented based on actual analysis
- [ ] Similar feature paths noted for later reference
- [ ] Completion message output
- [ ] User directed to run `/write-spec` next
