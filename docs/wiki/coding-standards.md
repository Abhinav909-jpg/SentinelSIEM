# Coding Standards

> These standards apply to every component of SentinelSIEM.

---

# General Principles

- Write readable code before clever code.
- Prefer composition over duplication.
- Keep functions small and focused.
- Every module should have a single responsibility.
- Document the "why" when it isn't obvious from the code.

---

# Python Standards

- Follow PEP 8.
- Use type hints.
- Write docstrings for public functions and classes.
- Avoid global variables where possible.
- Use descriptive variable names.
- Handle exceptions explicitly.
- Keep business logic separate from input/output.

---

# JavaScript Standards

- Use ES6+ features.
- Prefer `const` over `let`.
- Use async/await instead of callback chains.
- Avoid deeply nested logic.
- Keep functions focused on one responsibility.

---

# React Standards

- Use functional components.
- Use hooks appropriately.
- Keep components reusable.
- Avoid unnecessary state.

---

# Git Standards

- Use Conventional Commits.
- One feature per branch.
- Keep commits focused and meaningful.
- Do not commit generated files or secrets.

---

# Documentation Standards

Every feature should include:
- Updated documentation (if applicable)
- Meaningful commit messages
- Clear comments where necessary

---

# Testing Standards

- New features should include tests where practical.
- Fixes should include regression tests when appropriate.

---

# Security Standards

- Never hardcode secrets.
- Validate all external input.
- Prefer configuration over hardcoding.
- Log errors without exposing sensitive information.