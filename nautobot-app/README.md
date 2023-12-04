# Nautobot App

## Introduction

> NOTE: If you're just getting started with using Cookiecutter, please refer back to the main [README](../README.md) to understand how Cookiecutter works.

This folder provides a Cookiecutter template for a Nautobot App that adheres to Network to Code's Development Standards. The cookie provides a development environment to develop and test your Nautobot App with, which is provided by Docker Compose.

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{ cookiecutter.plugin_slug }}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing the documentation. Catch'em all with `rgrep "Developer Note"`.
- The documentation website will be built and hosted on `readthedocs.io` for open source projects and follows the standard Network to Code branding for all our open source projects.

## Getting Started

To use this template, follow the [instructions in the README](../README.md).

Once the cookie is generated the next step is to start developing the App! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.

## Template Inputs

The following table lists the inputs that you will be prompted for when generating a new cookie from this template.

| Setting | Description |
|-------- | ----------- |
| **codeowner_github_usernames** | The Github codeowners for the new plugin |
| **full_name** | Used in the **author** field within `pyproject.toml` and `PluginConfig` |
| **email** | Used in the **author** field within `pyproject.toml` |
| **github_org** | Used to construct **repo_url** |
| **plugin_name** | The Python name of the plugin |
| **verbose_name** | Used in `PluginConfig` |
| **plugin_slug** | Python packaging name |
| **project_slug** | Used to construct **repo_url** |
| **base_url** | Defines plugin's base url used in Nautobot |
| **min_nautobot_version** | The minimum supported Nautobot version |
| **max_nautobot_version** | The maximum supported Nautobot version |
| **nautobot_version** | Used for development purposes to decide with Nautobot-dev Docker image to use for development |
| **camel_name** | Used to define the plugin's subclassing of `PluginConfig`, e.g. `MyPluginConfig(PluginConfig):` |
| **project_short_description** | Used in the **description** field within `PluginConfig` |
| **model_class_name** | If you want to generate initial files, such as `models.py`, `forms.py`, `filters.py`, `navigation.py`, `tables.py`, `views`, and API models, initialize this name to a valid model name. The default value is `None` |
| **Select open_source_license** | Determine if project is open source or not |
| **docs_base_url**| The main URL where the project documentation will be hosted. For open source projects use the default (`https://docs.nautobot.com`). |
| **docs_app_url**| The full URL for documentation hosting. You might want to shorten the project alias, for example `https://docs.nautobot.com/projects/data-validation/en/latest` instead of `https://docs.nautobot.com/projects/nautobot-plugin-data-validation/en/latest`. Make sure there's no trailing `/`! |
