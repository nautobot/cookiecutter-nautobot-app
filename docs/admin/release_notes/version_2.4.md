# v2.4 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Various CI fixes for pull requests and upstream testing.
- Various documentation updates and fixes.

## [nautobot-app-v2.4.0 (2024-10-10)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.4.0)

### Added

- [#117](https://github.com/nautobot/cookiecutter-nautobot-app/issues/117) - Added environment variable `NAUTOBOT_LOG_DEPRECATION_WARNINGS=True` to development environment to enable deprecation warnings.
- [#180](https://github.com/nautobot/cookiecutter-nautobot-app/issues/180) - Added "backporting" section to contributing docs.
- [#183](https://github.com/nautobot/cookiecutter-nautobot-app/issues/183) - Added pylint django migrations checker to the `invoke pylint` command.

### Changed

- [#115](https://github.com/nautobot/cookiecutter-nautobot-app/issues/115) - Changed `invoke generate-release-notes` to always run locally.
- [#144](https://github.com/nautobot/cookiecutter-nautobot-app/issues/144) - Updated release checklist documentation.
- [#144](https://github.com/nautobot/cookiecutter-nautobot-app/issues/144) - Updated ci workflow to skip `changelog` step on release branches.
- [#157](https://github.com/nautobot/cookiecutter-nautobot-app/issues/157) - Further cleanup of bandit remnants.
- [#157](https://github.com/nautobot/cookiecutter-nautobot-app/issues/157) - Disabled pylint ruff rules as pylint is still being used.
- [#165](https://github.com/nautobot/cookiecutter-nautobot-app/issues/165) - Updated drift manager post actions to remove `black` and add `ruff`, `poetry lock` and add a changelog fragment to the drift manager pull request.

### Fixed

- [#109](https://github.com/nautobot/cookiecutter-nautobot-app/issues/109) - Fixed links to templates in docs index.
- [#118](https://github.com/nautobot/cookiecutter-nautobot-app/issues/118) - Updated docs build to activate the link on the Installed Apps page.
- [#128](https://github.com/nautobot/cookiecutter-nautobot-app/issues/128) - Fixed urls in readmes and docs.
- [#134](https://github.com/nautobot/cookiecutter-nautobot-app/issues/134) - Fixed typo in upstream testing workflow.
- [#166](https://github.com/nautobot/cookiecutter-nautobot-app/issues/166) - Fixed `invoke ruff` not properly exiting with non-zero status when a ruff check fails.
- [#167](https://github.com/nautobot/cookiecutter-nautobot-app/issues/167) - Fixed missing variable in upstream testing workflow.
- [#170](https://github.com/nautobot/cookiecutter-nautobot-app/issues/170) - Fixed Dockerfile to allow installing Nautobot from a branch as well as a tag.
