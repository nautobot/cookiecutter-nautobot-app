<<<<<<< HEAD
# Cookiecutter Templates for Creating Nautobot Apps
=======
# cookiecutter-ntc

- [cookiecutter-ntc](#cookiecutter-ntc)
  - [Introduction](#introduction)
  - [Where To Find Us](#where-to-find-us)
  - [Pre-requisites](#pre-requisites)
  - [Why Cookiecutter?](#why-cookiecutter)
  - [How To Use Cookiecutter Templates](#how-to-use-cookiecutter-templates)
    - [Using Provided Poetry Environment To Consume Cookiecutter Templates](#using-provided-poetry-environment-to-consume-cookiecutter-templates)
    - [Consuming Cookiecutter Using Git Clone](#consuming-cookiecutter-using-git-clone)
    - [Consuming Cookiecutter Templates via Cookiecutter Commands Without Git Clone](#consuming-cookiecutter-templates-via-cookiecutter-commands-without-git-clone)
  - [Why Poetry?](#why-poetry)
  - [How To Use Poetry](#how-to-use-poetry)
    - [Adding Dependencies To pyproject.toml](#adding-dependencies-to-pyprojecttoml)
    - [Poetry Lock](#poetry-lock)
    - [Poetry Shell](#poetry-shell)
  - [Why Invoke?](#why-invoke)
  - [How To Use Invoke](#how-to-use-invoke)

## Introduction

> The previously available [Nautobot Plugin ChatOps](https://github.com/nautobot/nautobot-chatops-cookiecutter) has moved! It is now open source. Please use the Open Source cookie for your ChatOps projects.

The intention of this repository is to provide developer environments by making use of [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) that adheres to NTC's Development Standards. There will be situations for deviation, but adhering to these standards is recommended to allow any NTC member to be able to pick up a project and go with the technologies defined in this repository.

This repository includes the following Cookiecutter templates:

- [ansible-project](ansible-project/README.md) - template for standard Ansible projects
- [ansible-collection](ansible-collection/README.md) - template for standard Ansible collections
- [nautobot](nautobot/README.md) - template for Nautobot deployment projects
- [nautobot-plugin](nautobot-plugin/README.md) - template for Nautobot plugins
- [nautobot-plugin-ssot](nautobot-plugin-ssot/README.md) - template for Nautobot SSoT plugins
- [python](python/README.md) - template for Python projects

> The previously available [Nautobot Plugin ChatOps](https://github.com/nautobot/nautobot-chatops-cookiecutter) has moved! It is now open source. Please use the Open Source cookie for your ChatOps projects.

Most projects will take advantage of the following tools: **Cookiecutter**, **Poetry**, **Invoke**, and **Docker Compose**.

## Where To Find Us

We're available on Slack at the [#dev-standards](https://networktocode-llc.slack.com/archives/CV0FAKQAH) channel as well as [Confluence](https://networktocode.atlassian.net/wiki/spaces/CTO/pages/122618041/Dev+Standards).

## Pre-requisites

If you have not already done so, you must have the following already installed.

- [Docker](https://docs.docker.com/get-docker/)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)

## Why Cookiecutter?

Before we get started, let's provide some context around the terminology used within Cookiecutter.

- **cookie** - The Cookiecutter template that provides the framework for specific projects to allow developers to get started developing faster such as the ones defined [above](#cookiecutter-ntc).
- **bake/baking** - The output of a **cookie**. If a **cookie** is baked, it means the project was created from a Cookiecutter template.

Cookiecutter allows us to codify and package up NTC Development Standards into a consumable manner that benefits NTC employees on quickly getting started with new projects and provides a consistent experience across the company.

Cookiecutter uses the concept of a questionnaire and templating to provide logic when building a new project. Let's take a look at one of the existing Cookiecutter templates to see the components.

```bash
❯ tree -L 2 nautobot-plugin
nautobot-plugin
├── README.md
├── cookiecutter.json
├── examples
│   ├── nautobot-plugin-my-plugin
│   └── nautobot-plugin-nautobot-plugin
├── hooks
│   ├── post_gen_project.py
│   └── pre_gen_project.py
├── tests
│   └── test_bake_nautobot_plugin.py
└── {{\ cookiecutter.project_slug\ }}
    ├── FAQ.md
    ├── LICENSE
    ├── README.md
    ├── development
    ├── docs
    ├── invoke.example.yml
    ├── mkdocs.yml
    ├── pyproject.toml
    ├── tasks.py
    └── {{cookiecutter.plugin_name}}
```

You can see that we're able to template folders and the contents of files using similar syntax to Jinja2.

```toml
[tool.poetry]
name = "{{cookiecutter.plugin_slug}}"
version = "{{cookiecutter.version}}"
description = "{{cookiecutter.project_short_description}}"
authors = ["{{cookiecutter.full_name}} <{{cookiecutter.email}}>"]
{%- if cookiecutter.open_source_license == 'Apache-2.0' %}
license = "{{cookiecutter.open_source_license}}"
{%- endif %}
```

Within the root of the **nautobot-plugin** cookie, we have the **cookiecutter.json** file that provides the questions to a user that is then used in templating.

```json
{
  "codeowner_github_usernames": "@smith-ntc",
  "full_name": "Network to Code, LLC",
  "email": "info@networktocode.com",
  "github_org": "nautobot",
  "plugin_name": "my_plugin",
  "verbose_name": "{{cookiecutter.plugin_name.title().replace('_', ' ')}}",
  "plugin_slug": "{{cookiecutter.plugin_name.lower().replace(' ', '-').replace('_', '-')}}",
  "project_slug": "nautobot-plugin-{{cookiecutter.plugin_slug}}",
  "repo_url": "https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_slug}}",
  "base_url": "{{cookiecutter.plugin_slug}}",
  "min_nautobot_version": "1.0.0",
  "max_nautobot_version": "1.9999",
  "nautobot_version": "1.0.1",
  "camel_name": "{{cookiecutter.plugin_slug.title().replace('-', '')}}",
  "project_short_description": "{{cookiecutter.verbose_name}}",
  "version": "0.1.0",
  "open_source_license": ["Apache-2.0", "Not open source"]
}
```

Here is an example of what it would look like by using just the defaults provided in the **cookiecutter.json** file.

```bash
❯ cookiecutter cookiecutter-ntc/nautobot-plugin
codeowner_github_usernames [@smith-ntc]:
full_name [Network to Code, LLC]:
email [info@networktocode.com]:
github_org [nautobot]:
plugin_name [my_plugin]:
verbose_name [My Plugin]:
plugin_slug [my-plugin]:
project_slug [nautobot-plugin-my-plugin]:
repo_url [https://github.com/nautobot/nautobot-plugin-my-plugin]:
base_url [my-plugin]:
min_nautobot_version [1.0.0]:
max_nautobot_version [1.9999]:
nautobot_version [1.0.1]:
camel_name [MyPlugin]:
project_short_description [My Plugin]:
version [0.1.0]:
Select open_source_license:
1 - Apache-2.0
2 - Not open source
Choose from 1, 2 [1]:

Congratulations!  Your cookie has now been baked. It is located at /Users/myohman/cloned-repos/nautobot-plugin-my-plugin.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env

creds.env will be ignored by git and can be used to override default environment variables.
```

## How To Use Cookiecutter Templates

> NOTE: Cookiecutter is a Python package and can be installed via normal Python means.

Cookiecutter must be installed to be able to consume the Cookiecutter templates that this repository holds per the **Pre-requisites** above. The link above provides how to install Cookiecutter, but we also provide a Poetry virtual environment within this repository.

If you have not used **Poetry** prior to this, it is a Python virtual environment, dependency and packaging manager. Poetry replaces the **requirements.txt** and **setup.py** with a **pyproject.toml** file. Damien (@dgarros) has a great [blog post](https://blog.networktocode.com/post/upgrade-your-python-project-with-poetry/) to get started on using it. Please read **Using Provided Poetry Environment To Consume Cookiecutter Templates** below.

### Using Provided Poetry Environment To Consume Cookiecutter Templates

1. Clone down this repository - `git clone git@github.com:networktocode-llc/cookiecutter-ntc.git`
2. Change directory into repository - `cd cookiecutter-ntc`
3. Activate the Poetry virtual environment - `poetry shell`

### Consuming Cookiecutter Using Git Clone

> NOTE: Cookiecutter will create the file structure needed within the current working directory unless otherwise specified.

If you followed **Using Provided Poetry Environment To Consume Cookiecutter Templates** or have the repository cloned down already and inside a virtual environment that has Cookiecutter installed then follow these directions.

> NOTE: If not freshly cloned down, please navigate into the root of the `cookiecutter-ntc` and perform a `git pull` to make sure you have the latest updates prior to baking a cookie.

1. If you need to, navigate to where you're not inside the root of this repository, but adjacent to it. If you're within the root of this repository locally, you can also use the `-o` option to specify a directory where you want the baked cookie to be outputted to.

```bash
❯ ls -la
total 32
drwxr-xr-x  23 ntc  staff    736 Jun  9 21:16 cookiecutter-ntc
```

2. Run `cookiecutter cookiecutter-ntc/<template_name>` and answer the Cookiecutter prompts to build a specific template. This should output the newly baked cookie into your current working directory.

```bash
❯ ls -la
total 32
drwxr-xr-x  23 ntc  staff    736 Jun  9 21:16 cookiecutter-ntc
drwxr-xr-x  20 ntc  staff    640 Jun  9 22:02 nautobot-plugin-my-plugin
```

### Consuming Cookiecutter Templates via Cookiecutter Commands Without Git Clone

> NOTE: Cookiecutter will create the file structure needed within the current working directory unless otherwise specified.

1. Navigate to the directory where you want the cookie to be outputted to or use the `-o` option to specify the output directory of the baked cookie.

   ```bash
   ❯ ls -la
   total 32
   drwxr-xr-x  23 ntc  staff    736 Jun  9 21:16 cookiecutter-ntc
   ```

2. Run the following commands depending on your preference.

   - SSH auth: `cookiecutter git@github.com:networktocode-llc/cookiecutter-ntc --directory <template_name>`
     - Make sure your SSH key is tied to your Github account.
     - Answer prompts from Cookiecutter.
   - HTTPS auth: `cookiecutter gh:networktocode-llc/cookiecutter-ntc --directory <template_name>`
     - This will prompt for credentials.
     - Answer prompts from Cookiecutter.

3. The cookie should now be baked.

   ```bash
   ❯ ls -la
   total 32
   drwxr-xr-x  23 ntc  staff    736 Jun  9 21:16 cookiecutter-ntc
   drwxr-xr-x  20 ntc  staff    640 Jun  9 22:02 nautobot-plugin-my-plugin
   ```

> NOTE: Refer to the template READMEs for specifics on how to use each template.

## Why Poetry?

Poetry was chosen to replace both **requirements.txt** and **setup.py**. Poetry uses the `pyproject.toml` file to define package details, main package dependencies, development dependencies, and tool related configurations. Poetry resolves dependencies and stores the hashes and metadata within the `poetry.lock` file that is then similar to performing a `pip freeze > requirements.txt`, but is more secure due to tracking package hashes. The `poetry.lock` is what is used to provide consistency for package versions across the project to make sure anyone who is developing on it is using the same Python dependency versions. Poetry also provides virtual environments by simply being in the same directory as the `pyproject.toml` and `poetry.lock` files and executing the `poetry shell`.

## How To Use Poetry

Let's get familiar with the `pyproject.toml` file to understand how to use **Poetry**.

```toml
[tool.poetry]
name = "my-plugin"
version = "0.1.0"
description = "My Plugin"
authors = ["Network to Code, LLC <info@networktocode.com>"]
license = "Apache-2.0"
readme = "README.md"
homepage = "https://github.com/nautobot/nautobot-plugin-my-plugin"
repository = "https://github.com/nautobot/nautobot-plugin-my-plugin"
keywords = ["nautobot", "nautobot-plugin"]
include = [
    "LICENSE",
    "README.md",
]
packages = [
    { include = "my_plugin" },
]
```

The `[tool.poetry]` provides the metadata required for taking advantage of the publishing provided by **Poetry**.

```toml
[tool.poetry.dependencies]
# Used for local development
nautobot = { version = "*", optional = true }
python = "^3.7"
# NOTE: There is a bug in Markdown v3.3.5 that crashes Poetry
Markdown = "3.3.4"
```

The `[tool.poetry.dependencies]` is where we define our projects main dependencies that will be installed along with it.

```toml
[tool.poetry.group.dev.dependencies]
bandit = "*"
black = "*"
coverage = "*"
django-debug-toolbar = "*"
flake8 = "*"
invoke = "*"
mkdocs = "*"
pydocstyle = "*"
pylint = "*"
pylint-django = "*"
yamllint = "*"
```

The `[tool.poetry.group.dev.dependencies]` is where we can find development related dependencies. We use this for our testing tools.

```toml
[tool.pytest.ini_options]
testpaths = [
    "tests"
]
addopts = "-vv --doctest-modules"
```

Then each tool can provide their own configuration sections that replaces their existing configuration file such as `pytest.ini`.

### Adding Dependencies To pyproject.toml

It is rarely a good idea to manage dependencies within `pyproject.toml` by editing the file directly, but instead use the provided `poetry` CLI options.

To add a main dependency, use the `poetry add` command.

> NOTE: To see a few extra examples or available options use `poetry add --help`.

```shell
❯ poetry add sentry-sdk@^1.1.0

Updating dependencies
Resolving dependencies... (1.2s)

Writing lock file

Package operations: 3 installs, 0 updates, 0 removals

  • Installing certifi (2021.5.30)
  • Installing urllib3 (1.26.5)
  • Installing sentry-sdk (1.1.0)
```

If we look at the `pyproject.toml` file, we will see the following.

```toml
[tool.poetry.dependencies]
# Used for local development
nautobot = { version = "*", optional = true }
python = "^3.7"
# NOTE: There is a bug in Markdown v3.3.5 that crashes Poetry
Markdown = "3.3.4"
sentry-sdk = "^1.1.0"
```

> NOTE: To understand how to specify dependency constraints, read the [dependency specification](https://python-poetry.org/docs/dependency-specification/) resources provided by **Poetry**.

To add a development dependency, it would be the same command, but you append the `--dev` option.

```shell
❯ poetry add sentry-sdk@^1.1.0 --dev
```

### Poetry Lock

Most of our Cookiecutter templates only provide the `pyproject.toml` file and the `poetry.lock` file needs to be generated to be able to use a virtual environment. To generate the `poetry.lock` file is simply running the `poetry lock` command and it will resolve the dependencies and generate the file.

```shell
❯ poetry lock
Updating dependencies
Resolving dependencies... (12.2s)
```

### Poetry Shell

Once the `poetry.lock` file is generated, you can launch the virtual environment using `poetry shell`.

```shell
❯ poetry shell
```

This will get you into a virtual environment, but then you must install the dependencies using the `poetry install` command. By default, this will install all dependencies including development dependencies.

```shell
❯ poetry install
```

You can add `--help` to the `poetry install` command to get more information. To not install development dependencies, add `--no-dev`. To not install the local Python package, add `--no-root`.

```shell
❯ poetry install --help
USAGE
  poetry install [--no-dev] [--no-root] [--dry-run] [--remove-untracked] [-E <...>]

OPTIONS
  --no-dev               Do not install the development dependencies.
  --no-root              Do not install the root package (the current project).
  --dry-run              Output the operations but do not execute anything (implicitly enables --verbose).
  --remove-untracked     Removes packages not present in the lock file.
  -E (--extras)          Extra sets of dependencies to install. (multiple values allowed)

GLOBAL OPTIONS
  -h (--help)            Display this help message
  -q (--quiet)           Do not output any message
  -v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more verbose output and "-vvv" for debug
  -V (--version)         Display this application version
  --ansi                 Force ANSI output
  --no-ansi              Disable ANSI output
  -n (--no-interaction)  Do not ask any interactive question

DESCRIPTION
  The install command reads the poetry.lock file from
  the current directory, processes it, and downloads and installs all the
  libraries and dependencies outlined in that file. If the file does not
  exist it will look for pyproject.toml and do the same.

  poetry install

  By default, the above command will also install the current project. To install only the
  dependencies and not including the current project, run the command with the
  --no-root option like below:

   poetry install --no-root
```

## Why Invoke?

Invoke is a Python replacement for Make. Invoke looks for a `tasks.py` file that contains functions decorated by `@task` that provides the equivalent of a **Make target**.

The reason it was chosen over Makefile was due to our collective familiarity with Python and the ability to organize and re-use Invoke tasks across our Cookiecutter templates.

## How To Use Invoke

Invoke is packaged with each Cookiecutter template within the `pyproject.toml` that allows the user to run `poetry shell && poetry install` and have access to the Invoke CLI.

If a `tasks.py` does not exist in the current working directory, the following message will be displayed when attempting to use Invoke.

```shell
❯ invoke
Can't find any collection named 'tasks'!
```

Once in a directory that has a `tasks.py`, you can run `invoke` and see the following output that provides several options for generic Invoke related options.

```shell
❯ invoke
Usage: inv[oke] [--core-opts] task1 [--task1-opts] ... taskN [--taskN-opts]

Core options:

  --complete                         Print tab-completion candidates for given parse remainder.
  --hide=STRING                      Set default value of run()'s 'hide' kwarg.
  --no-dedupe                        Disable task deduplication.
  --print-completion-script=STRING   Print the tab-completion script for your preferred shell (bash|zsh|fish).
  --prompt-for-sudo-password         Prompt user at start of session for the sudo.password config value.
  --write-pyc                        Enable creation of .pyc files.
  -c STRING, --collection=STRING     Specify collection name to load.
  -d, --debug                        Enable debug output.
  -D INT, --list-depth=INT           When listing tasks, only show the first INT levels.
  -e, --echo                         Echo executed commands before running.
  -f STRING, --config=STRING         Runtime configuration file to use.
  -F STRING, --list-format=STRING    Change the display format used when listing tasks. Should be one of: flat (default), nested, json.
  -h [STRING], --help[=STRING]       Show core or per-task help and exit.
  -l [STRING], --list[=STRING]       List available tasks, optionally limited to a namespace.
  -p, --pty                          Use a pty when executing shell commands.
  -r STRING, --search-root=STRING    Change root directory used for finding task modules.
  -R, --dry                          Echo commands instead of running.
  -T INT, --command-timeout=INT      Specify a global command execution timeout, in seconds.
  -V, --version                      Show version and exit.
  -w, --warn-only                    Warn, instead of failing, when shell commands fail.
```

To see what tasks we have available for us to use, we can use the `invoke --list` command.

```shell
❯ invoke --list
Available tasks:

  bandit              Run bandit to validate basic static code security analysis.
  black               Check Python code style with Black.
  build               Build Nautobot docker image.
  check-migrations    Check for missing migrations.
  cli                 Launch a bash shell inside the running Nautobot container.
  createsuperuser     Create a new Nautobot superuser account (default: "admin"), will prompt for password.
  debug               Start Nautobot and its dependencies in debug mode.
  destroy             Destroy all containers and volumes.
  flake8              Check for PEP8 compliance and other style issues.
  generate-packages   Generate all Python packages inside docker and copy the file locally under dist/.
  hadolint            Check Dockerfile for hadolint compliance and other style issues.
  makemigrations      Perform makemigrations operation in Django.
  migrate             Perform migrate operation in Django.
  nbshell             Launch an interactive nbshell session.
  post-upgrade        Performs Nautobot common post-upgrade operations using a single entrypoint.
  pydocstyle          Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  pylint              Run pylint code analysis.
  restart             Gracefully restart all containers.
  start               Start Nautobot and its dependencies in detached mode.
  stop                Stop Nautobot and its dependencies.
  tests               Run all tests for this plugin.
  unittest            Run Nautobot unit tests.
  unittest-coverage   Report on code test coverage as measured by 'invoke unittest'.
  vscode              Launch Visual Studio Code with the appropriate Environment variables to run in a container.
```

Each task provides a simple description that helps you determine what it is doing. If you want to get more information on a specific task, use the following command `invoke <task-name> --help`.

```shell
❯ invoke build --help
Usage: inv[oke] [--core-opts] build [--options] [other tasks here ...]

Docstring:
  Build Nautobot docker image.

Options:
  -c, --[no-]cache   Whether to use Docker's cache when building the image (defaults to enabled)
  -f, --force-rm     Always remove intermediate containers
```
>>>>>>> 6a0c5b3 (Move poetry dev dependencies to tool.poetry.group.dev.dependencies)
