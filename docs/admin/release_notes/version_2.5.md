# v2.5 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added coverage reporting in pull requests.
- Added markdown file linter.

## [nautobot-app-v2.5.1 (2025-08-20)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.5.1)

### Added

- [#253](https://github.com/nautobot/cookiecutter-nautobot-app/issues/253) - Added default labels to issue templates.

### Removed

- [#273](https://github.com/nautobot/cookiecutter-nautobot-app/issues/273) - Removed support for Python 3.8.

### Fixed

- [#268](https://github.com/nautobot/cookiecutter-nautobot-app/issues/268) - Fixed a missing import in the SSoT cookie.

## [nautobot-app-v2.5.0 (2025-04-25)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.5.0)

### Security

- [#245](https://github.com/nautobot/cookiecutter-nautobot-app/issues/245) - Pined github actions to their commit refs instead of tags/branches.

### Added

- [#219](https://github.com/nautobot/cookiecutter-nautobot-app/issues/219) - Added a feature to invoke tasks to automatically copy creds.example.env to creds.env.
- [#239](https://github.com/nautobot/cookiecutter-nautobot-app/issues/239) - Added `pymarkdownlnt` and associated configuration for linting markdown files.
- [#236](https://github.com/nautobot/cookiecutter-nautobot-app/issues/236) - Added a check in `invoke build-and-check-docs` to check for missing release notes.
- [#249](https://github.com/nautobot/cookiecutter-nautobot-app/issues/249) - Added coverage reporting in CI.
- [#252](https://github.com/nautobot/cookiecutter-nautobot-app/issues/252) - Added coverage_lcov and coverage_xml to invoke tasks.

### Changed

- [#226](https://github.com/nautobot/cookiecutter-nautobot-app/issues/226) - Disabled coverage reporting on invoke unittest unless --coverage is used.

### Fixed

- [#217](https://github.com/nautobot/cookiecutter-nautobot-app/issues/217) - Fixed documentation link in pull request template.
- [#246](https://github.com/nautobot/cookiecutter-nautobot-app/issues/246) - Fixed `pymarkdownlnt` to work with python 3.8.
- [#250](https://github.com/nautobot/cookiecutter-nautobot-app/issues/250) - Fixed missing CI dependency introduced in #249.
- [#248](https://github.com/nautobot/cookiecutter-nautobot-app/issues/248) - Fixed wheel files being built without the documentation.
- [#244](https://github.com/nautobot/cookiecutter-nautobot-app/issues/244) - Applied various fixes to resolve the cookie drifting from our current standards.

### Dependencies

- [#232](https://github.com/nautobot/cookiecutter-nautobot-app/issues/232) - Changed towncrier dependency range to `>=23.6.0,<=24.8.0`.
- [#251](https://github.com/nautobot/cookiecutter-nautobot-app/issues/251) - Updated docker image versions.

### Documentation

- [#238](https://github.com/nautobot/cookiecutter-nautobot-app/issues/238) - Fixed Slack url in copyright notice.
- [#234](https://github.com/nautobot/cookiecutter-nautobot-app/issues/234) - Removed jquery loading for readthedocs.
