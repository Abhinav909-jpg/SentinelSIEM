# ADR-001: Use Python for Log Processing

## Status

Accepted

---

## Date

2026-07-05

---

## Context

SentinelSIEM requires a processing engine responsible for parsing security logs, normalizing events, and executing detection rules.

Several implementation languages were considered.

---

## Decision

Use Python for the log processing component.

---

## Rationale

Python was selected because it provides:

- Excellent support for text processing
- Strong regular expression capabilities
- Mature cybersecurity ecosystem
- Readable and maintainable syntax
- Large collection of libraries for parsing, detection, and automation

This choice also aligns with the project's educational goals and the developer's existing experience.

---

## Alternatives Considered

### Go

Pros

- Excellent performance
- Good concurrency

Cons

- More verbose
- Slower development for this project

---

### Java

Pros

- Enterprise ecosystem

Cons

- More boilerplate
- Slower iteration

---

### Node.js

Pros

- Already used for backend API

Cons

- Less suitable for parsing-heavy workloads
- Splitting responsibilities between Python and Node.js results in cleaner architecture

---

## Consequences

Positive

- Faster development
- Easier parser implementation
- Better ecosystem for security tooling

Negative

- Two programming languages in the project
- Requires Python runtime

---

## Related Issues

Issue #001