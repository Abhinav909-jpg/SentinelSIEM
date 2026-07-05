# Issue #001 - SSH Log Generator

## Status

🟡 Planned

---

## Description

Develop a modular SSH log generator capable of continuously generating realistic authentication events for SentinelSIEM.

The generated logs will serve as the primary data source for the parser, detection engine, and dashboard during development.

---

## Objectives

- Generate successful SSH login events
- Generate failed SSH login attempts
- Simulate brute-force attacks
- Produce realistic timestamps
- Produce realistic process IDs (PIDs)
- Save generated logs to the appropriate directory

---

## Functional Requirements

### FR-001

Generate successful login events.

### FR-002

Generate failed login events.

### FR-003

Simulate brute-force attacks.

### FR-004

Generate logs continuously.

### FR-005

Write logs to the configured output directory.

---

## Non-Functional Requirements

- Modular design
- Readable code
- PEP 8 compliance
- Type hints
- Easily extensible for additional log sources

---

## Acceptance Criteria

- [ ] SSH logs are generated
- [ ] Brute-force simulation works
- [ ] Logs are saved correctly
- [ ] Code is documented
- [ ] Unit tests pass

---

## Dependencies

None

---

## Priority

High

---

## Estimated Version

v0.1