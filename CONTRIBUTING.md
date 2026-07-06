# Contributing to SentinelSIEM

First off, thank you for considering contributing to SentinelSIEM! 🎉 This project is built by and for the security community, and contributions of all sizes — code, documentation, bug reports, or ideas — are genuinely appreciated.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Branching & Commit Conventions](#branching--commit-conventions)
- [Pull Request Process](#pull-request-process)
- [Coding Style](#coding-style)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Security Vulnerabilities](#security-vulnerabilities)

## Code of Conduct

Be respectful, be constructive, and assume good intent. We want SentinelSIEM to be a welcoming project for security practitioners of all experience levels. Harassment, discrimination, or hostile behavior of any kind will not be tolerated.

## How Can I Contribute?

There are lots of ways to help, even without writing code:

- 🐛 **Report bugs** you run into
- 💡 **Suggest features** or improvements
- 📝 **Improve documentation** (README, docs/, code comments)
- 🧪 **Write tests** for existing functionality
- 🔧 **Fix issues** tagged [`good first issue`](https://github.com/Ovotron-net/SentinelSIEM/issues) or [`help wanted`](https://github.com/Ovotron-net/SentinelSIEM/issues)
- 🎨 **Improve the dashboard UI/UX**
- 🔍 **Add detection logic or parsers** to the processor module

## Development Setup

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/SentinelSIEM.git
   cd SentinelSIEM
   ```

2. **Add the upstream remote** so you can keep your fork in sync:

   ```bash
   git remote add upstream https://github.com/Ovotron-net/SentinelSIEM.git
   ```

3. **Set up your environment:**

   ```bash
   cp .env.sample .env
   ```

   Update `.env` with values suited to your local setup (e.g. your local `MONGO_URI`, a `JWT_SECRET` you generate yourself, etc.). Never commit your `.env` file.

4. **Install dependencies** for the module(s) you're working on:

   ```bash
   cd backend && npm install
   cd ../frontend && npm install
   cd ../processor && npm install
   ```

5. **Run the stack** locally, either via Docker Compose:

   ```bash
   docker compose up --build
   ```

   or by running each module individually with `npm start` in its own terminal.

6. Confirm everything runs cleanly before you start making changes.

## Project Structure

| Directory     | Purpose                                                        |
| ------------- | ---------------------------------------------------------------- |
| `backend/`    | REST API — authentication, data access, alert logic               |
| `processor/`  | Log ingestion and event-processing pipeline                       |
| `frontend/`   | Web dashboard UI                                                   |
| `docs/`       | Project documentation                                              |

If your change touches more than one module (e.g. an API change that also needs a frontend update), please mention this clearly in your PR description.

## Branching & Commit Conventions

- Create a new branch off `main` for each change:

  ```bash
  git checkout -b feature/short-description
  # or
  git checkout -b fix/short-description
  ```

- Use clear, descriptive branch prefixes: `feature/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/`.

- Write commit messages in the imperative mood and keep the first line under ~72 characters:

  ```
  Add JWT refresh token support to backend auth
  ```

  Add more detail in the commit body if needed.

- Keep commits focused — one logical change per commit is easier to review and revert if necessary.

## Pull Request Process

1. **Sync with upstream** before opening a PR:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Make sure your branch builds and runs locally, and that any existing tests pass.

3. **Update documentation** (README, docs/, inline comments) if your change affects setup, configuration, or usage.

4. Push your branch and open a pull request against `main`. In the PR description, include:
   - What the change does and why
   - Any related issue number (e.g. `Closes #12`)
   - Steps to test/verify the change
   - Screenshots or sample output, if the change is visual or affects API responses

5. Be responsive to review feedback — small iterative fixes are normal and expected.

6. A maintainer will merge once the PR is approved. Please don't merge your own PR unless explicitly asked to.

## Coding Style

- Match the existing style/formatting already used in the file you're editing.
- Prefer clear, descriptive variable and function names over clever abbreviations.
- Keep functions small and focused; add comments where logic isn't self-explanatory.
- Avoid introducing new dependencies unless there's a clear need — mention the reasoning in your PR if you do.
- Do not commit secrets, API keys, or `.env` files.

## Reporting Bugs

Before opening a new issue, please search [existing issues](https://github.com/Ovotron-net/SentinelSIEM/issues) to avoid duplicates. When filing a bug report, include:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Environment details (OS, Node version, Docker or not, etc.)
- Relevant logs or error output (redact any sensitive data first)

## Suggesting Enhancements

Feature requests are welcome! Please open an issue describing:

- The problem you're trying to solve
- Your proposed solution or approach
- Any alternatives you've considered

This helps maintainers and other contributors weigh in before implementation work starts.

## Security Vulnerabilities

**Please do not open a public issue for security vulnerabilities.** Since SentinelSIEM handles security event data, responsible disclosure matters. Instead, contact the maintainers directly through the repository owner's GitHub profile ([Ovotron-net](https://github.com/Ovotron-net)) to report the issue privately, and allow time for a fix before any public disclosure.

---

Thanks again for contributing — every bit of help moves SentinelSIEM forward. 🛡️
