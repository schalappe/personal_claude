# Specification: User Authentication

## Goal

Enable users to securely create accounts and access the application through email/password authentication, establishing a foundation for personalized user experiences.

## User Stories

- As a new user, I want to sign up with my email and password so that I can create an account and access the app.
- As a returning user, I want to log in with my credentials so that I can access my account.
- As a logged-in user, I want to log out so that I can secure my session on shared devices.

## Specific Requirements

**User Registration Form:**

- Form fields: email, password, confirm password
- Client-side validation using Zod (consistent with existing forms)
- Email format validation with clear error message
- Password requirements: minimum 8 characters, at least one number
- Password confirmation must match
- Disable submit button while processing
- Redirect to dashboard on successful registration

**User Login Form:**

- Form fields: email, password
- Client-side validation using Zod
- Display inline error for invalid credentials
- Disable submit button while processing
- Redirect to intended destination or dashboard on success

**Logout Functionality:**

- Clear JWT token from httpOnly cookie
- Redirect to login page after logout
- Invalidate session on server side

**JWT Session Management:**

- Generate JWT token on successful login/registration
- Store token in httpOnly cookie (not localStorage)
- Include user ID and expiration in token payload
- Token expiration: 7 days
- Middleware to validate token on protected routes

**Login Rate Limiting:**

- Track failed login attempts per email address
- Lock account after 5 consecutive failed attempts
- Lockout duration: 15 minutes
- Display remaining lockout time to user
- Reset counter on successful login

## Visual Design

**`planning/visuals/login-wireframe.png`**

- Centered card layout on page (use existing Card component styling)
- Email input field with label above
- Password input field with label above
- Full-width primary button: "Log in"
- Link below button: "Don't have an account? Sign up"
- Note: Low-fidelity wireframe - use existing application styling

**`planning/visuals/signup-wireframe.png`**

- Same centered card layout as login
- Email input field with label above
- Password input field with label above
- Confirm password input field with label above
- Full-width primary button: "Sign up"
- Link below button: "Already have an account? Log in"
- Note: Low-fidelity wireframe - use existing application styling

## Existing Code to Leverage

**ContactForm Component - `src/components/ContactForm.tsx`**

- What it does: Handles form state, validation, and submission with loading states
- How to reuse: Replicate form structure and validation patterns for auth forms
- Key patterns: Zod schema definition, error display, submit handling

**Contact API Route - `src/api/contact.ts`**

- What it does: Handles POST requests with validation and error responses
- How to reuse: Follow same pattern for auth endpoints (register, login, logout)
- Key patterns: Request validation, error handling, response structure

## Out of Scope

- OAuth login providers (Google, Facebook, GitHub)
- Email verification flow
- Password reset / forgot password
- Two-factor authentication (2FA)
- Remember me / persistent sessions
- User profile management
- Account settings or preferences
- Admin user management
- Login analytics or audit logs
