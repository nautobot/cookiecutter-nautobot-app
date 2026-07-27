# Nautobot Commercial App

## Introduction

> NOTE: If you're just getting started with using Cookiecutter, please refer back to the main [README](../README.md) to understand how Cookiecutter works.

This folder provides a Cookiecutter template for a **commercial (licensed) Nautobot App** that adheres to Network to Code's Development Standards. The cookie provides a development environment to develop and test your Nautobot App with, which is provided by Docker Compose.

Commercial apps generated from this template are distributed through Network to Code's private Artifactory repository. They ship a `COPYRIGHT` notice (no open-source LICENSE), do not publish to PyPI, and have all GitHub-related content stripped from the public documentation site. Release artifacts are still attached to the GitHub release as a backup for Artifactory.

### IMPORTANT Cookie Notes

- The logo of the project is a placeholder (`docs/images/icon-{{ cookiecutter.app_slug }}.png`) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!
- Please resolve and remove **all** of the comments and blocks marked with `Developer Note - Remove Me!` prior to publishing the documentation. Catch'em all with `grep -r "Developer Note"`.
- The documentation website is built and hosted at `docs.nautobot.com` for Network to Code commercial Apps.
- This cookie wires up the private `artifactory-pypi` Poetry source and the credential plumbing to authenticate against it (Docker BuildKit secrets in `development/Dockerfile` and `development/docker-compose.base.yml`, `ARTIFACTORY_USERNAME`/`ARTIFACTORY_PASSWORD` passthrough in `tasks.py`, and `POETRY_HTTP_BASIC_ARTIFACTORY_PYPI_*` in CI). To depend on a package published only to Artifactory, uncomment the example in `pyproject.toml` and add `source = "artifactory-pypi"` to the dependency. Everything degrades gracefully when credentials are absent, so a cookie with no private dependencies builds without any setup.
- The baked repository needs `ARTIFACTORY_USERNAME` and `ARTIFACTORY_PASSWORD` added as GitHub Actions secrets before CI can resolve private dependencies. Note that `upstream_testing.yml` calls Nautobot core's reusable workflow, which cannot receive these credentials — those runs will fail for any app with a private dependency.

## Getting Started

To use this template, follow the [instructions in the README](../README.md).

To bake a cookie use the proper template name:

```
invoke bake --template nautobot-app-commercial
```

Once the cookie is generated the next step is to start developing the App! If you're not familiar with the development environment provided by this cookie, we recommend checking out the Development Environment guide located in the documentation tree at `docs/dev/dev_environment.md`.

## Template Inputs

The following table lists the inputs that you will be prompted for when generating a new cookie from this template.

| Setting | Description |
|-------- | ----------- |
| **codeowner_github_usernames** | The Github codeowners for the new app |
| **full_name** | Used in the **author** field within `pyproject.toml` and `NautobotAppConfig` |
| **email** | Used in the **author** field within `pyproject.toml` |
| **github_org** | Used to construct **repo_url**. Defaults to `networktocode-llc` for commercial apps. |
| **app_name** | The Python module name of the app (snake_case, e.g., `my_commercial_app`). Drives every other derived value. |
| **verbose_name** | Human-readable name used in `NautobotAppConfig` (derived from `app_name`). |
| **app_slug** | Python packaging name (kebab-case, derived from `app_name`). |
| **project_slug** | Used to construct **repo_url** (derived: `nautobot-app-<app_slug>`). |
| **base_url** | Defines the app's base url used in Nautobot (derived: `<app_slug>`). |
| **camel_name** | Used to define the app's subclassing of `NautobotAppConfig`, e.g. `MyAppConfig(NautobotAppConfig):` |
| **project_short_description** | Used in the **description** field within `NautobotAppConfig` |
| **model_class_name** | If you want to generate initial files (`models.py`, `forms.py`, `filters.py`, `navigation.py`, `tables.py`, `views`, and API models), initialize this name to a valid model name. Default `None`. |
| **open_source_license** | Always `Not open source` for commercial apps. |
| **docs_base_url** | The main URL where the project documentation will be hosted. Default: `https://docs.nautobot.com`. |
| **docs_app_url** | The full URL for documentation hosting. Make sure there's no trailing `/`. |

## Globals

The variables `min_nautobot_version` and `upper_bound_nautobot_version` are now global variables and can no longer be provided as an input. These are now controlled by the template.
