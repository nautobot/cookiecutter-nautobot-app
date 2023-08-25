# Nautobot App (Plugin)

## Introduction

> NOTE: If you're just getting started with using Cookiecutter, please refer back to the main [README](../README.md) to understand how Cookiecutter works.

This Cookiecutter template provides a framework, also known as a **cookie**, for a Nautobot plugin that adheres to Network to Code's Development Standards. The cookie provides a development environment to develop and test your Nautobot plugin with that is provided by Docker Compose.

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{cookiecutter.plugin_slug}}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing the documentation. Catch'em all with `rgrep "Developer Note"`.
- The documentation website will be built and hosted on `readthedocs.io` for open source projects and follows the standard Network to Code branding for all our open source projects.

## Getting Started

Below are the steps outlined in detail for getting started along with various tips and tricks that may be beneficial.

## Generating a New Nautobot Plugin

Let's walk you through baking a **nautobot-plugin**.

> NOTE: It is recommended to leave these first 4 options as default:

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
| **version** | Version of the new Nautobot plugin |
| **model_class_name** | If you want to generate initial files, such as `models.py`, `forms.py`, `filters.py`, `navigation.py`, `tables.py`, `views`, and API models, initialize this name to a valid model name. The default value is `None` |
| **Select open_source_license** | Determine if project is open source or not |
| **docs_base_url**| The main URL where the project documentation will be hosted. For open source projects use the default (`https://docs.nautobot.com`). |
| **docs_app_url**| The full URL for documentation hosting. You might want to shorten the project alias, for example `https://docs.nautobot.com/projects/data-validation/en/latest` instead of `https://docs.nautobot.com/projects/nautobot-plugin-data-validation/en/latest`. Make sure there's no trailing `/`! |

> NOTE: Cookiecutter by default bakes the new cookie within the current working directory. If that is not desirable then use the `-o` option to specify a different output folder.

```bash
> cookiecutter cookiecutter-ntc/nautobot-plugin
codeowner_github_usernames [@smith-ntc]:
full_name [Network to Code, LLC]:
email [info@networktocode.com]:
github_org [nautobot]:
plugin_name [my_plugin]: nautobot_data_validation_engine
verbose_name [Nautobot Data Validation Engine]: Data Validation Engine
plugin_slug [nautobot-data-validation-engine]:
project_slug [nautobot-plugin-nautobot-data-validation-engine]: nautobot-plugin-data-validation-engine
repo_url [https://github.com/nautobot/nautobot-plugin-data-validation-engine]:
base_url [nautobot-data-validation-engine]:
min_nautobot_version [1.5.2]:
max_nautobot_version [1.9999]:
nautobot_version [latest]:
camel_name [NautobotDataValidationEngine]:
project_short_description [Data Validation Engine]:
version [0.1.0]:
model_class_name [None]:
Select open_source_license:
1 - Apache-2.0
2 - Not open source
Choose from 1, 2 [1]:
docs_base_url [https://docs.nautobot.com]:
docs_app_url [https://docs.nautobot.com/projects/nautobot-data-validation-engine/en/latest]: https://docs.nautobot.com/projects/data-validation/en/latest

Congratulations!  Your cookie has now been baked. It is located at /vagrant/nautobot-plugin-data-validation-engine.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* invoke makemigrations

creds.env will be ignored by git and can be used to override default environment variables.
```

Follow the directions provided at the end of baking the cookie.

```bash
➜ cd nautobot-plugin-data-validation-engine
➜ poetry lock
➜ cp development/creds.example.env development/creds.env
➜ invoke makemigrations
```

Here is an example of what your directory structure may look like (subject to change as the project is developed over time).

```bash
➜ ll nautobot-plugin-data-validation-engine
total 96K
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 ./
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 ../
-rw-rw-r-- 1 vagrant vagrant  118 Oct 24 15:30 .bandit.yml
-rw-rw-r-- 1 vagrant vagrant  295 Oct 24 15:30 .dockerignore
-rw-rw-r-- 1 vagrant vagrant  192 Oct 24 15:30 .flake8
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 .github/
-rw-rw-r-- 1 vagrant vagrant 4.9K Oct 24 15:30 .gitignore
-rw-rw-r-- 1 vagrant vagrant  451 Oct 24 15:30 .readthedocs.yaml
-rw-rw-r-- 1 vagrant vagrant  214 Oct 24 15:30 .yamllint.yml
-rw-rw-r-- 1 vagrant vagrant  591 Oct 24 15:30 LICENSE
-rw-rw-r-- 1 vagrant vagrant 5.0K Oct 24 15:30 README.md
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 development/
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 docs/
-rw-rw-r-- 1 vagrant vagrant  325 Oct 24 15:30 invoke.example.yml
-rw-rw-r-- 1 vagrant vagrant  322 Oct 24 15:30 invoke.mysql.yml
-rw-rw-r-- 1 vagrant vagrant 3.8K Oct 24 15:30 mkdocs.yml
drwxrwxr-x 1 vagrant vagrant 4.0K Oct 24 15:30 nautobot_data_validation_engine/
-rw-rw-r-- 1 vagrant vagrant 3.3K Oct 24 15:30 pyproject.toml
-rw-rw-r-- 1 vagrant vagrant  14K Oct 24 15:30 tasks.py
```

Once the cookie is generated the next step is to start developing the plugin! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.
