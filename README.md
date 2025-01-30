# Cookiecutter Templates for Creating Nautobot Apps

This repository houses Cookiecutter templates, designed to kick-start your Nautobot App development journey. Leveraging these templates allows for a standardized and rapid creation of Nautobot Apps, adhering to best practices and common structural paradigms.

## About Nautobot Apps

A Nautobot App is a Django application designed to extend the functionality of [Nautobot](https://github.com/nautobot/nautobot), an open-source Network Source of Truth and Automation Platform. By creating a Nautobot App, developers can introduce custom data models, views, templates, and REST API endpoints, enabling bespoke network management solutions and integrations. This modular approach fosters a flexible and scalable environment, allowing for a tailored experience in managing network resources and workflows.

## About Cookiecutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line utility that simplifies the creation of new projects by generating them from predefined templates. These templates utilize the [Jinja](https://jinja.palletsprojects.com/) templating engine, allowing for dynamic content generation and customization. By providing a structured and consistent framework, Cookiecutter helps developers to avoid boilerplate code and to adhere to best practices right from the project's inception. The flexibility and power of Jinja under the hood enable Cookiecutter templates to encapsulate complex setups, making it a valuable tool for accelerating project initialization in various ecosystems.

## Templates

The following templates are available:

- [`nautobot-app`](https://github.com/nautobot/cookiecutter-nautobot-app/tree/develop/nautobot-app) - A template for creating a new Nautobot App.
- [`nautobot-app-ssot`](https://github.com/nautobot/cookiecutter-nautobot-app/tree/develop/nautobot-app-ssot) - A template for creating a new Nautobot App that extends the capabilities of the Nautobot Single Source of Truth (SSoT) App. The [Nautobot SSoT App](https://github.com/nautobot/nautobot-app-ssot) facilitates integration and data synchronization between various "source of truth" (SoT) systems, with Nautobot acting as a central clearinghouse for data.
- [`nautobot-app-chatops`](https://github.com/nautobot/cookiecutter-nautobot-app/tree/develop/nautobot-app-chatops) - A template for creating a new Nautobot App that extends the capabilities of the Nautobot ChatOps App. The [Nautobot ChatOps App](https://github.com/nautobot/nautobot-app-chatops) provides a multi-chat-vendor framework for developing chat bots for Slack, Microsoft Teams, Cisco WebEx, & Mattermost.

To find out which template version corresponds to which Nautobot version, please check out the [Compatibility Matrix](https://docs.nautobot.com/projects/cookiecutter-nautobot-app/en/latest/admin/compatibility_matrix/) in the online documentation.

## Usage with Cookiecutter

It's possible to use Cookiecutter directly without installing templates locally. To do so, set up your environment first.

Pre-requisites:

- Python with pip.

```shell
pip install cookiecutter
mkdir outputs
```

It is recommended that you check out the latest tag with `git checkout nautobot-app-vX.Y.Z` before proceeding so you start your app on the latest, stable state.

Then run the following command:

```shell
cookiecutter \
  --output-dir=./outputs \
  --directory=nautobot-app \
  https://github.com/nautobot/cookiecutter-nautobot-app
```
