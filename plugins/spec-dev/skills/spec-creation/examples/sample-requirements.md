# Spec Requirements: User Authentication

## Initial Description

I want to add user authentication to the app. Users should be able to sign up, log in, and log out. Keep it simple - just email and password for now.

## Requirements Discussion

### First Round Questions

**Q1:** I assume email/password authentication without OAuth providers (Google, Facebook, etc.). Is that correct, or should we plan for OAuth integration?
**Answer:** Correct, just email/password for now. We might add OAuth later but not in this version.

**Q2:** For password requirements, I'm thinking minimum 8 characters with at least one number. Should we enforce stricter rules like special characters?
**Answer:** 8 characters with one number is fine. Don't make it too annoying for users.

**Q3:** Should users verify their email address before accessing the app, or can they use it immediately after signup?
**Answer:** They can use it immediately. Email verification would be nice to have later but not required now.

**Q4:** For session management, I suggest using JWT tokens stored in httpOnly cookies. Does that work, or would you prefer a different approach?
**Answer:** JWT in cookies sounds good.

**Q5:** What should happen when a user forgets their password? Should we include a password reset flow?
**Answer:** Not for this version. Users can contact support if they forget. Add it later.

**Q6:** Should there be any rate limiting on login attempts to prevent brute force attacks?
**Answer:** Yes, that's a good idea. Maybe lock after 5 failed attempts for 15 minutes.

### Existing Code to Reference

**Similar Features Identified:**

- Feature: Contact form - Path: `src/components/ContactForm.tsx`
- Components to reuse: Form layout, input validation patterns, submit handling
- Backend logic to reference: `src/api/contact.ts` for API route patterns

### Follow-up Questions

**Follow-up 1:** The contact form uses Zod for validation. Should we use the same approach for auth forms?
**Answer:** Yes, keep it consistent.

## Visual Assets

### Files Provided

- `login-wireframe.png`: Simple wireframe showing centered login card with email field, password field, and login button. "Sign up" link below.
- `signup-wireframe.png`: Similar layout with email, password, confirm password fields. "Already have an account?" link below.

### Visual Insights

- Clean, minimal design with centered card layout
- Form fields stacked vertically
- Primary action button full-width at bottom
- Secondary link for switching between login/signup
- Fidelity level: low-fidelity wireframe (use existing app styling)

## Requirements Summary

### Functional Requirements

- User registration with email and password
- User login with email and password
- User logout functionality
- JWT-based session management with httpOnly cookies
- Password validation: minimum 8 characters, at least one number
- Rate limiting: 5 failed attempts triggers 15-minute lockout

### Reusability Opportunities

- ContactForm component for form layout patterns
- Zod validation approach from existing forms
- API route patterns from contact.ts

### Scope Boundaries

**In Scope:**

- Email/password registration
- Email/password login
- Logout functionality
- JWT session management
- Basic password validation
- Login rate limiting

**Out of Scope:**

- OAuth providers (Google, Facebook, etc.)
- Email verification
- Password reset flow
- Two-factor authentication
- Remember me / persistent sessions
- User profile management

### Technical Considerations

- Use Zod for form validation (consistent with existing patterns)
- JWT tokens in httpOnly cookies
- Rate limiting implementation for login endpoint
- Follow existing API route patterns from contact.ts
