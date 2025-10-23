# v2.6 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added Nautobot component UI framework example.
- Changed minimum Nautobot version to `2.4.2`.
- Updated Poetry to v2.

<!-- towncrier release notes start -->
## [nautobot-app-v2.6.0 (2025-09-16)](https://github.com/nautobot/cookiecutter-nautobot-app/releases/tag/nautobot-app-v2.6.0)

### Added

- [#270](https://github.com/nautobot/cookiecutter-nautobot-app/issues/270) - Added UI Component Framework example.
- [#270](https://github.com/nautobot/cookiecutter-nautobot-app/issues/270) - Added Global variable for `min_nautobot_version` and `max_nautobot_version`.
- [#278](https://github.com/nautobot/cookiecutter-nautobot-app/issues/278) - Added searchable models to AppConfig.
- [#259](https://github.com/nautobot/cookiecutter-nautobot-app/issues/259) - Enabled front-matter extension for pymarkdown.
- [#266](https://github.com/nautobot/cookiecutter-nautobot-app/issues/266) - Enabled pymarkdown `selectively_enable_rules` configuration.
- [#271](https://github.com/nautobot/cookiecutter-nautobot-app/issues/271) - Updated Poetry from `1.8.5` to `2.1.3`.
- [#281](https://github.com/nautobot/cookiecutter-nautobot-app/issues/281) - Added djlint for django template linting.
- [#283](https://github.com/nautobot/cookiecutter-nautobot-app/issues/283) - Added `pymdownx.details` markdown extension to mkdocs.yml.
- [#285](https://github.com/nautobot/cookiecutter-nautobot-app/issues/285) - Added DjHTML for Django template formatting.

### Changed

- [#270](https://github.com/nautobot/cookiecutter-nautobot-app/issues/270) - Changed default minimum nautobot version to `2.4.2`.
- [#283](https://github.com/nautobot/cookiecutter-nautobot-app/issues/283) - Updated readthedocs config to use poetry and removed `docs/requirements.txt`.
- [#283](https://github.com/nautobot/cookiecutter-nautobot-app/issues/283) - Changed `SLACK_WEBHOOK_URL` secret to `OSS_PYPI_SLACK_WEBHOOK_URL`.
- [#283](https://github.com/nautobot/cookiecutter-nautobot-app/issues/283) - Updated github actions runners to use ubuntu-latest.
- [#283](https://github.com/nautobot/cookiecutter-nautobot-app/issues/283) - Updated charfields max_length to use nautobot.apps.constants.CHARFIELD_MAX_LENGTH.
- [#284](https://github.com/nautobot/cookiecutter-nautobot-app/issues/284) - Added support for python patch version in `invoke lock --constrain-python-ver`.
- [#284](https://github.com/nautobot/cookiecutter-nautobot-app/issues/287) - Disabled pylint rules `too-many-positional-arguments`, `nb-warn-dunder-filter-field`, `nb-no-search-function`, and `nb-no-char-filter-q`.

### Removed

- [#270](https://github.com/nautobot/cookiecutter-nautobot-app/issues/270) - Removed `min_nautobot_version` and `max_nautobot_version` from inputs.
- [#270](https://github.com/nautobot/cookiecutter-nautobot-app/issues/270) - Removed deprecated `min_nautobot_version` and `max_nautobot_version` from AppConfig.
