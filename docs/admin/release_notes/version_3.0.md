# v3.0 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Changed minimum Nautobot version to `3.0.0`.
- Changed maximum Nautobot version to `<4.0.0`.
- Added support for Python `3.13`.

<!-- towncrier release notes start -->

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
