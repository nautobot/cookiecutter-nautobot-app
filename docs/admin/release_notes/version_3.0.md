# v3.0 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Changed minimum Nautobot version to `3.0.0`.
- Changed maximum Nautobot version to `<4.0.0`.
- Added support for Python `3.13`.

<!-- towncrier release notes start -->

## [3.0.1 (2026-03-10)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/3.0.1)

### Added

- [#329](https://github.com/nautobot/cookiecutter-nautobot-app/issues/329) - Added a CI job to check that pull requests into `main` are only allowed from branches starting with `release`.
- [#337](https://github.com/nautobot/cookiecutter-nautobot-app/issues/337) - Added djlint to the CI workflow.
- [#345](https://github.com/nautobot/cookiecutter-nautobot-app/issues/345) - Added a new workflow to Automate the Release Process.
- [#345](https://github.com/nautobot/cookiecutter-nautobot-app/issues/345) - Added a new step in release.yml to Automate merging release back to develop.
- [#347](https://github.com/nautobot/cookiecutter-nautobot-app/issues/347) - Added mkdocs plugin glightbox with default behavior of being enabled on all images
- Added `--livereload` keyword argument to mkdocs serve command to explicitly enable live reload functionality.

### Changed

- [#324](https://github.com/nautobot/cookiecutter-nautobot-app/issues/324) - Updated the shared Poetry install workflow to use `gh-action-setup-poetry-environment` version 7.
- [#326](https://github.com/nautobot/cookiecutter-nautobot-app/issues/326) - Added a pre-release version to the default project version number to prevent CI failures in newly baked projects.
- [#328](https://github.com/nautobot/cookiecutter-nautobot-app/issues/328) - Changed invoke `start`, `restart`, `stop`, `debug`, and `logs` commands to accept multiple services as arguments.
- [#349](https://github.com/nautobot/cookiecutter-nautobot-app/issues/349) - Changed Python version range to 3.14 on cookies.

### Fixed

- [#334](https://github.com/nautobot/cookiecutter-nautobot-app/issues/334) - Fixed a typo in `invoke generate-release-notes --help`.
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

- [#332](https://github.com/nautobot/cookiecutter-nautobot-app/issues/332) - Updated pull request template to ask submitter to test changes in dev example.
- [#335](https://github.com/nautobot/cookiecutter-nautobot-app/issues/335) - Updated `CODEOWNERS` file to include only the Nautobot Apps team.

## [3.0.0 (2025-12-30)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/3.0.0)

### Added

- [#291](https://github.com/nautobot/cookiecutter-nautobot-app/issues/291) - Added support for Python `3.13`.

### Changed

- [#291](https://github.com/nautobot/cookiecutter-nautobot-app/issues/291) - Updated minimum Nautobot version to `3.0.0`.
- [#291](https://github.com/nautobot/cookiecutter-nautobot-app/issues/291) - Updated maximum Nautobot version to `<4.0.0`.
- [#309](https://github.com/nautobot/cookiecutter-nautobot-app/issues/309) - Change the tag-nautobot-app workflow to support multiple nautobot-app versions.
- [#320](https://github.com/nautobot/cookiecutter-nautobot-app/issues/320) - Upstream testing now runs against selected branches.

### Documentation

- [#319](https://github.com/nautobot/cookiecutter-nautobot-app/issues/319) - Fixed nav typo and added missing 2.7.2 release notes.

### Housekeeping

- [#322](https://github.com/nautobot/cookiecutter-nautobot-app/issues/322) - Updated CI workflow to always regenerate poetry lockfile.
