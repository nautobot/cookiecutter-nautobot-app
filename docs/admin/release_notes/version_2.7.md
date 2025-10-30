# v2.7 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Dropped support for Python 3.9.
- Changed minimum Nautobot version to `2.4.20`.
- Updated `invoke generate-release-notes` with more automation.
- Added support for PyPI Trusted Publisher in release workflow.

<!-- towncrier release notes start -->
## [nautobot-app-v2.7.1 (2025-10-30)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.7.1)

### Fixed

- [#303](https://github.com/nautobot/cookiecutter-nautobot-app/issues/303) - Fixed release workflow missing the docs build step.

## [nautobot-app-v2.7.0 (2025-10-23)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.7.0)

### Changed

- [#295](https://github.com/nautobot/cookiecutter-nautobot-app/issues/295) - Changed default minimum Nautobot version to 2.4.20.
- [#295](https://github.com/nautobot/cookiecutter-nautobot-app/issues/295) - Changed default minimum Python version to 3.10 on cookies.
- [#295](https://github.com/nautobot/cookiecutter-nautobot-app/issues/295) - Changed default minimum Python version to 3.10 on cookiecutter-nautobot-app.
- [#295](https://github.com/nautobot/cookiecutter-nautobot-app/issues/295) - Changed default Python version to 3.12 on cookies.
- [#295](https://github.com/nautobot/cookiecutter-nautobot-app/issues/295) - Changed default Python version to 3.12 on cookiecutter-nautobot-app.
- [#296](https://github.com/nautobot/cookiecutter-nautobot-app/issues/296) - Updated release process into separate workflow that uses the PyPI Trusted Publisher.

### Dependencies

- [#299](https://github.com/nautobot/cookiecutter-nautobot-app/issues/299) - Set minimum version of pylint-django to `>=2.5.4`.
- [#299](https://github.com/nautobot/cookiecutter-nautobot-app/issues/299) - Set minimum version of pylint-nautobot to `>=0.3.1`.

### Documentation

- [#294](https://github.com/nautobot/cookiecutter-nautobot-app/issues/294) - Removed references to docs/requirements.txt in dev environment documentation.

### Housekeeping

- [#298](https://github.com/nautobot/cookiecutter-nautobot-app/issues/298) - Added breaking category to towncrier.
- [#300](https://github.com/nautobot/cookiecutter-nautobot-app/issues/300) - Added automation to the generate-release-notes command.
