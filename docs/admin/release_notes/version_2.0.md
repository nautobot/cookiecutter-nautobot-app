# v2.0 Release Notes

This document describes all new features and changes in the release `2.0`. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v2.0.0] - 2024-01-04

### Added

- Nautobot `2.0` support
- Nautobot App ChatOps cookie
- Changelog fragments using [Towncrier](https://towncrier.readthedocs.io/en/stable/tutorial.html)

### Changed

- Changed documentation for baking cookies and development to no longer use Docker by default
- Updated Nautobot components to import from `nautobot.apps.*` and use `NautobotUIViewSet` instead of individual views & paths

### Fixed

- CI no building docs prior to publishing to PyPI & GitHub on release
