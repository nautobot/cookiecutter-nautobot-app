# Contributing to {{ cookiecutter.verbose_name }}

Thank you for your interest in this project. The full guide is in the
documentation, at [Contributing to the App]({{ cookiecutter.docs_app_url }}/dev/contributing/).
This page is the short version, plus the policy on AI assistance.

## Before You Open a Pull Request

1. Open an issue, or comment on an existing one, so a maintainer can approve the work.
2. Branch from `develop`. For a fix to a Nautobot LTM release, branch from the latest
   `ltm-<major.minor>` branch instead.
3. Add a changelog fragment at `changes/<issue>.<type>`. Valid types are `added`,
   `changed`, `deprecated`, `fixed`, `removed`, and `security`.
4. Add tests for new behavior. Add a regression test for a bug fix.
5. Run the suite, and confirm that it passes:

   ```shell
   poetry run invoke tests
   ```

6. Open the pull request against `develop`, and complete the checklist in the template.

## AI-Assisted Contributions

This project accepts contributions written with the help of AI coding tools. The
following conditions apply.

- **A human owns the change.** You are the author. You understand every line you
  submit, and you answer review questions yourself.
- **You test the change.** Run `poetry run invoke tests` locally before you open the
  pull request. Do not submit output you have not run.
- **You disclose the assistance.** Tick the disclosure item in the pull request
  template, and name the provider and the model, for example
  `Anthropic Claude Opus 4.5` or `GitHub Copilot (GPT-5)`. Disclosure is not a
  penalty; it helps reviewers calibrate their attention.
- **You keep the change small.** Maintainers close large, unreviewed,
  machine-generated pull requests without a detailed review.
- **You follow the repository standards.** [`AGENTS.md`](AGENTS.md) states the design
  patterns, the do's and don'ts, and the maintainer expectations for this repository.
  Point your agent at that file.

`AGENTS.md` is the canonical instruction file. `CLAUDE.md`, `GEMINI.md`,
`.cursorrules`, and `.github/copilot-instructions.md` all point to it.
