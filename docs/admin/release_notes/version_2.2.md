# v2.2 Release Notes

## [v2.2.0] - 2024-03-06

**Full Changelog**: https://github.com/nautobot/cookiecutter-nautobot-app/compare/nautobot-app-v2.1.0...nautobot-app-v2.2.0

### Added

- Added `nautobot-app-dev-example` to the drift management. #88
- Added link to compatibility matrix to `README.md`. #68
- Added mermaid support to docs. #83
- Added app config schema generation and validation. #75

### Changed

- Bumped CI actions versions. #92
- Changed logging to be single-line. #90
- Changed `invoke autoformat` not to use `ruff format`. #91
- Changed `README.md` references, to point to docs.nautobot.com. #79

### Fixed

- Fixed docs based on [NetBox importer PR](https://github.com/nautobot/nautobot-app-netbox-importer/pull/126). #86
- Fixed template on [ChatOps](https://github.com/nautobot/nautobot-app-chatops). #81

### Removed

- Removed `nautobot-app-nornir` from managed apps. #84
