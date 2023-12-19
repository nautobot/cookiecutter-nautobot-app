# {{ cookiecutter.verbose_name }} SSoT

An app for [Nautobot](https://github.com/nautobot/nautobot).

The term SSoT, or Single Source of Truth, refers to the intention of using Nautobot to consolidate data from disparate Systems of Record to create a single resource for all automation needs. This is done by extending the [Nautobot SSoT framework](https://github.com/nautobot/nautobot-plugin-ssot) which uses the DiffSync library. This plug-in is built with the capability in mind to import and export data from your desired System of Record.

<!--
Developer Note - Remove Me!

The README will have certain links/images broken until the PR is merged into `develop`. Update the GitHub links with whichever branch you're using (main etc.) if different.

The logo of the project is a placeholder (docs/images/icon-{{ cookiecutter.app_slug }}.png) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!

To avoid extra work and temporary links, make sure that publishing docs (or merging a PR) is done at the same time as setting up the docs site on RTD, then test everything.
-->

<p align="center">
  <img src="https://raw.githubusercontent.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/develop/docs/images/icon-{{ cookiecutter.app_slug }}.png" class="logo" height="200px">
  <br>
  <a href="{{ cookiecutter.repo_url }}/actions"><img src="{{ cookiecutter.repo_url }}/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="{{ cookiecutter.docs_app_url }}"><img src="https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/"></a>
  <a href="https://pypi.org/project/{{ cookiecutter.app_slug }}/"><img src="https://img.shields.io/pypi/v/{{ cookiecutter.app_slug }}"></a>
  <a href="https://pypi.org/project/{{ cookiecutter.app_slug }}/"><img src="https://img.shields.io/pypi/dm/{{ cookiecutter.app_slug }}"></a>
  <br>
  An <a href="https://www.networktocode.com/nautobot/apps/">App</a> for <a href="https://nautobot.com/">Nautobot</a>.
</p>

## Overview

> Developer Note: Add a long (2-3 paragraphs) description of what the App does, what problems it solves, what functionality it adds to Nautobot, what external systems it works with etc.

### Screenshots

> Developer Note: Add any representative screenshots of the App in action. These images should also be added to the `docs/user/app_use_cases.md` section.

> Developer Note: Place the files in the `docs/images/` folder and link them using only full URLs from GitHub, for example: `![Overview](https://raw.githubusercontent.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/develop/docs/images/app-overview.png)`. This absolute static linking is required to ensure the README renders properly in GitHub, the docs site, and any other external sites like PyPI.

More screenshots can be found in the [Using the App]({{ cookiecutter.docs_app_url }}/user/app_use_cases/) page in the documentation. Here's a quick overview of some of the app's added functionality:

![](https://raw.githubusercontent.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/develop/docs/images/placeholder.png)

## Try it out!

> Developer Note: Only keep this section if appropriate. Update link to correct sandbox.

This App is installed in the Nautobot Community Sandbox found over at [demo.nautobot.com](https://demo.nautobot.com/)!

> For a full list of all the available always-on sandbox environments, head over to the main page on [networktocode.com](https://www.networktocode.com/nautobot/sandbox-environments/).

## Documentation

Full documentation for this App can be found over on the [Nautobot Docs]({{ cookiecutter.docs_base_url }}) website:

- [User Guide]({{ cookiecutter.docs_app_url }}/user/app_overview/) - Overview, Using the App, Getting Started.
- [Administrator Guide]({{ cookiecutter.docs_app_url }}/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the App.
- [Developer Guide]({{ cookiecutter.docs_app_url }}/dev/contributing/) - Extending the App, Code Reference, Contribution Guide.
- [Release Notes / Changelog]({{ cookiecutter.docs_app_url }}/admin/release_notes/).
- [Frequently Asked Questions]({{ cookiecutter.docs_app_url }}/user/faq/).

### Contributing to the Documentation

You can find all the Markdown source for the App documentation under the [`docs`]({{ cookiecutter.repo_url }}/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient: clone the repository and edit away.

If you need to view the fully-generated documentation site, you can build it with [MkDocs](https://www.mkdocs.org/). A container hosting the documentation can be started using the `invoke` commands (details in the [Development Environment Guide]({{ cookiecutter.docs_app_url }}/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). Using this container, as your changes to the documentation are saved, they will be automatically rebuilt and any pages currently being viewed will be reloaded in your browser.

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ]({{ cookiecutter.docs_app_url }}/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#nautobot`), sign up [here](http://slack.networktocode.com/) if you don't have an account.
