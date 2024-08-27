# v2.3 Release Notes

This document describes all new features and changes in the release `2.3`. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v2.3.2] - 2024-08-27

### Fixed

- [#155](https://github.com/nautobot/cookiecutter-nautobot-app/pull/155) - Fixed typo in ci.yml.

## [v2.3.1] - 2024-08-26

### Added

- [#129](https://github.com/nautobot/cookiecutter-nautobot-app/issues/129) - Added support for Python 3.12.

### Fixed

- [#148](https://github.com/nautobot/cookiecutter-nautobot-app/issues/148) - Fixed dependency resolution in development environment docker container builds.

### Dependencies

- [#147](https://github.com/nautobot/cookiecutter-nautobot-app/issues/147) - Pinned `griffe` to `1.1.1` to resolve failures in readthedocs builds.
- [#147](https://github.com/nautobot/cookiecutter-nautobot-app/issues/147) - Updated `mkdocs` to `1.6.0`.
- [#147](https://github.com/nautobot/cookiecutter-nautobot-app/issues/147) - Updated `mkdocs-material` to `9.5.32`.
- [#147](https://github.com/nautobot/cookiecutter-nautobot-app/issues/147) - Updated `mkdocstrings` to `0.25.2`.
- [#147](https://github.com/nautobot/cookiecutter-nautobot-app/issues/147) - Updated `mkdocstrings-python` to `1.10.8`.

## [v2.3.0] - 2024-08-06

### Changed

- [#112](https://github.com/nautobot/cookiecutter-nautobot-app/pull/112) - Replaced `mkdocs-version-annotations` mkdocs plugin with new `markdown-version-annotations` markdown extension. No change in functionality, it's the same package.
- [#106](https://github.com/nautobot/cookiecutter-nautobot-app/pull/106) - Replaced `black` and `flake8` with `ruff` for formatting and linting.

### Fixed

- [#101](https://github.com/nautobot/cookiecutter-nautobot-app/pull/101) - Fixed link in README.md.
- [#107](https://github.com/nautobot/cookiecutter-nautobot-app/pull/107) - Fixed SSoT jobs to work with Nautobot v2.0 conventions.
- [#110](https://github.com/nautobot/cookiecutter-nautobot-app/pull/110) - Fixed typo in import statement for SSoT jobs.py.
- [#111](https://github.com/nautobot/cookiecutter-nautobot-app/pull/111) - Fixed command argument causing newer MySQL 8 containers to fail.
- [#132](https://github.com/nautobot/cookiecutter-nautobot-app/pull/132) - Fixed various test failures on newly baked cookies.

### Removed

- [#108](https://github.com/nautobot/cookiecutter-nautobot-app/pull/108) - Removed deprecated `version` in docker compose files.
- [#130](https://github.com/nautobot/cookiecutter-nautobot-app/pull/130) - Removed duplicate `tasks.py` from `.dockerignore`.

### Documentation

- [#116](https://github.com/nautobot/cookiecutter-nautobot-app/pull/116) - Updated contributing.md to remove reference to Golden Config and general cleanup.
