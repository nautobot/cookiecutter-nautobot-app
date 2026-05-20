# Nautobot Private App

## Introduction

> NOTE: If you're just getting started with using Cookiecutter, please refer back to the main [README](../README.md) to understand how Cookiecutter works.

This folder provides a Cookiecutter template for a **private (licensed) Nautobot App** that adheres to Network to Code's Development Standards. The cookie provides a development environment to develop and test your Nautobot App with, which is provided by Docker Compose.

Private apps generated from this template are intended to be distributed exclusively through Network to Code's private Artifactory repository. They ship a `COPYRIGHT` notice (no open-source LICENSE), publish only to Artifactory (no PyPI, no public GitHub release artifacts), and have all GitHub-related content stripped from the public documentation site.

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{ cookiecutter.app_slug }}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing the documentation. Catch'em all with `grep -r "Developer Note"`.
- The documentation website is built and hosted at `docs.nautobot.com` for Network to Code private Apps.

## Getting Started

To use this template, follow the [instructions in the README](../README.md).

To bake a cookie use the proper template name:

```
invoke bake --template nautobot-app-private
```

Once the cookie is generated the next step is to start developing the App! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.

## Template Inputs

The following table lists the inputs that you will be prompted for when generating a new cookie from this template.

| Setting | Description |
|-------- | ----------- |
| **codeowner_github_usernames** | The Github codeowners for the new app |
| **full_name** | Used in the **author** field within `pyproject.toml` and `NautobotAppConfig` |
| **email** | Used in the **author** field within `pyproject.toml` |
| **github_org** | Used to construct **repo_url**. Defaults to `networktocode-llc` for private apps. |
| **app_short_name** | The human-friendly short name of the app (e.g., `OS Upgrades`, `Tools`, `Ansible Automation`). Drives the derived `app_name`, `verbose_name`, `app_slug`, `project_slug`, and `base_url`. |
| **app_name** | The Python module name of the app (derived: `nautobot_<short_name_snake>`) |
| **verbose_name** | Human-readable name used in `NautobotAppConfig` (derived: `Nautobot <Short Name>`) |
| **app_slug** | Python packaging name (derived: `nautobot-<short_name_kebab>`) |
| **project_slug** | Used to construct **repo_url** (derived: `nautobot-app-<short_name_kebab>`) |
| **base_url** | Defines the app's base url used in Nautobot (derived: `<short_name_kebab>`) |
| **camel_name** | Used to define the app's subclassing of `NautobotAppConfig`, e.g. `MyAppConfig(NautobotAppConfig):` |
| **project_short_description** | Used in the **description** field within `NautobotAppConfig` |
| **model_class_name** | If you want to generate initial files (`models.py`, `forms.py`, `filters.py`, `navigation.py`, `tables.py`, `views`, and API models), initialize this name to a valid model name. Default `None`. |
| **open_source_license** | Always `Not open source` for private apps. |
| **docs_base_url** | The main URL where the project documentation will be hosted. Default: `https://docs.nautobot.com`. |
| **docs_app_url** | The full URL for documentation hosting. Make sure there's no trailing `/`. |

## Globals

The variables `min_nautobot_version` and `upper_bound_nautobot_version` are now global variables and can no longer be provided as an input. These are now controlled by the template.
