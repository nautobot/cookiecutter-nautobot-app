# v3.1 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added support for Python `3.14`.

<!-- towncrier release notes start -->

## [nautobot-app-v3.1.4 (2026-08-06)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v3.1.4)

### Added

- [#376](https://github.com/nautobot/cookiecutter-nautobot-app/issues/376) - Added support for `--no-input` option to `invoke unittest` and `invoke tests` tasks.
- [#378](https://github.com/nautobot/cookiecutter-nautobot-app/issues/378) - Added `invoke generate-test-data` task and a boilerplate `generate_<app_name>_test_data` management command to the `nautobot-app` cookie.
- [#380](https://github.com/nautobot/cookiecutter-nautobot-app/issues/380) - Added previous_version to the Prepare Release workflow to allow overriding the previous_version.
- [#386](https://github.com/nautobot/cookiecutter-nautobot-app/issues/386) - Added opt-in ephemeral Docker host ports for generated app development environments.
- [#388](https://github.com/nautobot/cookiecutter-nautobot-app/issues/388) - Added `nautobot-app-commercial` template for creating commercial (licensed) Nautobot Apps distributed through NTC's private Artifactory repository.
- [#393](https://github.com/nautobot/cookiecutter-nautobot-app/issues/393) - Added a `--missing` option to the `unittest-coverage` invoke target to show missing coverage lines.

### Changed

- [#318](https://github.com/nautobot/cookiecutter-nautobot-app/issues/318) - Added a `--diff` option to the `invoke ruff` tasks.
- [#370](https://github.com/nautobot/cookiecutter-nautobot-app/issues/370) - Changed the minimum version of Nautobot to 3.1.0.
- [#371](https://github.com/nautobot/cookiecutter-nautobot-app/issues/371) - Added various AI agent files to the gitignore.
- [#372](https://github.com/nautobot/cookiecutter-nautobot-app/issues/372) - Updated ruff target python version to 3.10.
- [#373](https://github.com/nautobot/cookiecutter-nautobot-app/issues/373) - Added `target` and `recursive` options to `invoke pylint` tasks.
- [#386](https://github.com/nautobot/cookiecutter-nautobot-app/issues/386) - Aligned the generated app `docs` container to serve and publish on port 8001, matching `mkdocs.yml` and Nautobot core.
- [#407](https://github.com/nautobot/cookiecutter-nautobot-app/issues/407) - Changed the minimum supported Nautobot version to 3.2.0 for apps baked from the `nautobot-app-commercial` cookie, updating both the baked `pyproject.toml` constraint and the CI test matrix.

### Fixed

- [#381](https://github.com/nautobot/cookiecutter-nautobot-app/issues/381) - Updated the CI pipeline so that we auto increment post-release versions when creating a release from main, develop, next, and ltm-*.
- [#383](https://github.com/nautobot/cookiecutter-nautobot-app/issues/383) - Fixed the prepare release workflow bumping the version on prereleases resulting in a version number that is 2 ahead of the last release.
- [#387](https://github.com/nautobot/cookiecutter-nautobot-app/issues/387) - Fixed github actions not running on pull requests when using automated releases.
- [#405](https://github.com/nautobot/cookiecutter-nautobot-app/issues/405) - Changed `.gitignore` to allow committing shared Claude Code configuration, ignoring only per-user local files.

### Housekeeping

- [#385](https://github.com/nautobot/cookiecutter-nautobot-app/issues/385) - Added a release workflow job to sync release notes from `ltm` branches back to `develop` via an automated pull request.
- [#389](https://github.com/nautobot/cookiecutter-nautobot-app/issues/389) - Replaced the unmaintained `toml` dev dependency with stdlib `tomllib` (Python 3.11+) and `tomli` (Python 3.10 fallback).
- [#390](https://github.com/nautobot/cookiecutter-nautobot-app/issues/390) - Bumped CI workflow matrix to test against Python 3.14.
- [#402](https://github.com/nautobot/cookiecutter-nautobot-app/issues/402) - Fixed djlint CI failure for apps with no Django templates
- [#403](https://github.com/nautobot/cookiecutter-nautobot-app/issues/403) - Changed the release workflow to define the Python and Poetry versions as workflow-level environment variables.
- [#404](https://github.com/nautobot/cookiecutter-nautobot-app/issues/404) - Added a release workflow job that opens a pull request from `main` into `next` after a release is published from `main`.
- [#406](https://github.com/nautobot/cookiecutter-nautobot-app/issues/406) - Excluded the templated `development/docker-compose.base.yml` and `.github/workflows/ci.yml` files from `yamllint`.

## [nautobot-app-v3.1.3 (2026-04-09)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v3.1.3)

### Housekeeping

- [#364](https://github.com/nautobot/cookiecutter-nautobot-app/issues/364) - Fixed the logo in the footer of the documentation.

## [nautobot-app-v3.1.2 (2026-03-10)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v3.1.2)

### Fixed

- [#359](https://github.com/nautobot/cookiecutter-nautobot-app/issues/359) - Fixed glightbox dependency.
- [#361](https://github.com/nautobot/cookiecutter-nautobot-app/issues/361) - Fixed ruff formatting.
- [#361](https://github.com/nautobot/cookiecutter-nautobot-app/issues/361) - Fixed bugs in invoke commands.

## [nautobot-app-v3.1.1 (2026-03-10)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v3.1.1)

### Added

- [#350](https://github.com/nautobot/cookiecutter-nautobot-app/issues/350) - Added glightbox as a dependency to custom group docs in pyproject.toml files.

## [nautobot-app-v3.1.0 (2026-03-10)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v3.1.0)

### Added

- [#337](https://github.com/nautobot/cookiecutter-nautobot-app/issues/337) - Added djlint to the CI workflow.
- [#345](https://github.com/nautobot/cookiecutter-nautobot-app/issues/345) - Added a new workflow to automate the release process.
- [#345](https://github.com/nautobot/cookiecutter-nautobot-app/issues/345) - Added a new step in release.yml to automate merging release back to develop.
- [#347](https://github.com/nautobot/cookiecutter-nautobot-app/issues/347) - Added mkdocs plugin glightbox with default behavior of being enabled on all images.
- [#317](https://github.com/nautobot/cookiecutter-nautobot-app/pull/317) - Added `--livereload` keyword argument to mkdocs serve command to explicitly enable live reload functionality.

### Changed

- [#324](https://github.com/nautobot/cookiecutter-nautobot-app/issues/324) - Updated the shared Poetry install workflow to use `gh-action-setup-poetry-environment` version 7.
- [#326](https://github.com/nautobot/cookiecutter-nautobot-app/issues/326) - Added a pre-release version to the default project version number to prevent CI failures in newly baked projects.
- [#328](https://github.com/nautobot/cookiecutter-nautobot-app/issues/328) - Changed invoke `start`, `restart`, `stop`, `debug`, and `logs` commands to accept multiple services as arguments.
- [#349](https://github.com/nautobot/cookiecutter-nautobot-app/issues/349) - Changed Python version range to allow Python 3.14.

### Fixed

- [#336](https://github.com/nautobot/cookiecutter-nautobot-app/issues/336) - Fixed extra linebreaks being added to release notes files.
- [#339](https://github.com/nautobot/cookiecutter-nautobot-app/issues/339) - Changed the nautobot-ssot dependency to the proper version for Nautobot v3 in the nautobot-app-ssot template.
- [#340](https://github.com/nautobot/cookiecutter-nautobot-app/issues/340) - Added the missing djlint dev dependency to the nautobot-app-ssot and nautobot-app-chatops templates.

### Dependencies

- [#341](https://github.com/nautobot/cookiecutter-nautobot-app/issues/341) - Added djhtml and tomli to the nautobot-app-chatops and nautobot-app-ssot project templates.

### Documentation

- [#327](https://github.com/nautobot/cookiecutter-nautobot-app/issues/327) - Fixed a typo in the release checklist documentation.
- [#331](https://github.com/nautobot/cookiecutter-nautobot-app/issues/331) - Added documentation outlining testing standards for Nautobot apps.
- [#346](https://github.com/nautobot/cookiecutter-nautobot-app/issues/346) - Updated the LTM release checklist to include steps for pulling in the release notes from the LTM branch to the develop branch.

### Housekeeping

- [#334](https://github.com/nautobot/cookiecutter-nautobot-app/issues/334) - Fixed a typo in `invoke generate-release-notes --help`.
