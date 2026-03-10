# v3.1 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added support for Python `3.14`.

<!-- towncrier release notes start -->
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
