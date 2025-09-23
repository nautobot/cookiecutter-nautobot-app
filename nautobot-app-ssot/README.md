# Nautobot SSoT App

## Introduction

> NOTE: If you're just getting started with using Cookiecutter, please refer back to the main [README](../README.md) to understand how Cookiecutter works.

This folder provides a Cookiecutter template for a Nautobot Single Source of Truth App that adheres to Network to Code's Development Standards. The cookie provides a development environment to develop and test your Nautobot App with, which is provided by Docker Compose.

The term SSoT, or Single Source of Truth, refers to the intention of using Nautobot to consolidate data from disparate Systems of Record to create a single resource for all automation needs. This is done by extending the [Nautobot SSoT framework](https://github.com/nautobot/nautobot-app-ssot) which uses the DiffSync library. This plug-in is built with the capability in mind to import and export data from your desired System of Record.

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{ cookiecutter.app_slug }}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing the documentation. Catch'em all with `grep -r "Developer Note"`.
- The documentation website will be built and hosted on `readthedocs.io` for open source projects and follows the standard Network to Code branding for all our open source projects.

## Getting Started

To use this template, follow the [instructions in the README](../README.md).

To bake a cookie use the proper template name:

```
invoke bake --template nautobot-app-ssot
```

Once the cookie is generated the next step is to start developing the App! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.

## Template Inputs

The following table lists the inputs that you will be prompted for when generating a new cookie from this template.

| Setting | Description |
|-------- | ----------- |
| **codeowner_github_usernames** | The Github codeowners for the new app |
| **full_name** | Used in the **author** field within `pyproject.toml` and `NautobotAppConfig` |
| **email** | Used in the **author** field within `pyproject.toml` |
| **github_org** | Used to construct **repo_url** |
| **system_of_record** | The System of Record that the plug-in is intended to work with. |
| **system_of_record_slug** | Used to construct model and adapter names. |
| **system_of_record_camel** | Used to construct class names. |
| **app_name** | The Python name of the app |
| **verbose_name** | Used in `NautobotAppConfig` |
| **app_slug** | Python packaging name |
| **project_slug** | Used to construct **repo_url** |
| **base_url** | Defines app's base url used in Nautobot |
| **camel_name** | Used to define the app's subclassing of `NautobotAppConfig`, e.g. `MyNautobotAppConfig(NautobotAppConfig):` |
| **project_short_description** | Used in the **description** field within `NautobotAppConfig` |
| **model_class_name** | If you want to generate initial files, such as `models.py`, `forms.py`, `filters.py`, `navigation.py`, `tables.py`, `views`, and API models, initialize this name to a valid model name. The default value is `None` |
| **Select open_source_license** | Determine if project is open source or not |
| **docs_base_url**| The main URL where the project documentation will be hosted. For open source projects use the default (`https://docs.nautobot.com`). |
| **docs_app_url**| The full URL for documentation hosting. You might want to shorten the project alias, for example `https://docs.nautobot.com/projects/ssot-system-of-record/en/latest` instead of `https://docs.nautobot.com/projects/nautobot-app-ssot-system-of-record/en/latest`. Make sure there's no trailing `/`! |

## Globals

The variables `min_nautobot_version` and `upper_bound_nautobot_version` are now global variables and can no longer be provided as an input. These are now controlled by the template.
