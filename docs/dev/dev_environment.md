# Building Your Development Environment

## Quickstart Guide

The development environment can be used in two ways:

1. **(Recommended)** All services, including Nautobot, are spun up using Docker containers and a volume mount so you can develop locally.
2. With a local Poetry environment if you wish to develop outside of Docker, with the caveat of using external services provided by Docker for the database (PostgreSQL by default, MySQL optionally) and Redis services.

This is a quick reference guide if you're already familiar with the development environment provided, which you can read more about later in this document.

### Invoke

The [Invoke](http://www.pyinvoke.org/) library is used to provide some helper commands based on the environment. There are a few configuration parameters which can be passed to Invoke to override the default configuration:

- `project_name`: the default docker compose project name (default: `cookiecutter-nautobot-app`)
- `python_ver`: the version of Python to use as a base for any built docker containers (default: 3.11)
- `local`: a boolean flag indicating if invoke tasks should be run on the host or inside the docker containers (default: True, commands will be run the host)
- `compose_dir`: the full path to a directory containing the project compose files
- `compose_files`: a list of compose files applied in order (see [Multiple Compose files](https://docs.docker.com/compose/extends/#multiple-compose-files) for more information)
- `templates`: a list of templates for local development & testing

Using **Invoke** these configuration options can be overridden using [several methods](https://docs.pyinvoke.org/en/stable/concepts/configuration.html). Perhaps the simplest is setting an environment variable `INVOKE_COOKIECUTTER_NAUTOBOT_APP_VARIABLE_NAME` where `VARIABLE_NAME` is the variable you are trying to override. The only exception is `compose_files`, because it is a list it must be overridden in a YAML file. There is an example `invoke.yml` (`invoke.example.yml`) in this directory which can be used as a starting point.

### Local Poetry Development Environment

!!! tip
    This is the recommended option for development.

Run the following commands:

```shell
poetry shell
poetry install
invoke tests
```

### Docker Development Environment

- Create an `invoke.yml` file with the following contents at the root of the repo and edit as necessary

```yaml
---
cookiecutter_nautobot_app:
  local: false
```

This project is managed by [Python Poetry](https://python-poetry.org/) and has a few requirements to setup your development environment:

1. Install Poetry, see the [Poetry documentation](https://python-poetry.org/docs/#installation) for your operating system.
2. Install Docker, see the [Docker documentation](https://docs.docker.com/get-docker/) for your operating system.
3. Install Docker-compose, see the [Docker-compose documentation](https://github.com/docker/compose) for your operation system.

Once you have Poetry and Docker installed you can run the following commands (in the root of the repository) to install all other development dependencies in an isolated Python virtual environment:

```shell
poetry install
poetry shell
invoke build
invoke tests
```

To either stop or destroy the development environment use the following options.

- **invoke stop** - Stop the containers, but keep all underlying systems intact
- **invoke destroy** - Stop and remove all containers, volumes, etc. (This results in data loss due to the volume being deleted)

### Updating the Documentation

Documentation dependencies are pinned to exact versions to ensure consistent results. For the development environment, they are defined in the `pyproject.toml` file.

If you need to update any of the documentation dependencies to a newer version, make sure you copy the exact same versions pinned in `pyproject.toml` to the `docs/requirements.txt` file as well. The latter is used in the automated build pipeline on ReadTheDocs to build the live version of the documentation.

### CLI Helper Commands

The project features a CLI helper based on [Invoke](https://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories:

- `dev environment`
- `utility`
- `testing`

Each command can be executed with `invoke <command>`. All commands support the arguments `--python-ver` if you want to manually define the version of Python to use. Each command also has its own help `invoke <command> --help`

#### Local Development Environment

```
  build            Build development container images.
  debug            Start development container in debug mode.
  destroy          Destroy all containers and volumes.
  restart          Restart development container in detached mode.
  start            Start development container in detached mode.
  stop             Stop development container.
  logs             View logs for the development container.
```

#### Utility

```
  cli              Launch a bash shell inside the running development container.
```

#### Testing

```
  ruff             Run ruff to perform code formatting and/or linting.
  pylint           Run pylint code analysis.
  markdownlint     Run pymarkdown linting.
  tests            Run all tests for this app.
  unittest         Run Django unit tests for the app.
```

## Poetry

Poetry is used in lieu of the "virtualenv" commands and is leveraged in both environments. The virtual environment will provide all of the Python packages required to manage the development environment such as **Invoke**. See the [Local Development Environment](#local-poetry-development-environment) section to see how to install Nautobot if you're going to be developing locally (i.e. not using the Docker container).

The `pyproject.toml` file outlines all of the relevant dependencies for the project:

- `tool.poetry.dependencies` - the main list of dependencies.
- `tool.poetry.group.dev.dependencies` - development dependencies, to facilitate linting, testing, and documentation building.

The `poetry shell` command is used to create and enable a virtual environment managed by Poetry, so all commands ran going forward are executed within the virtual environment. This is similar to running the `source venv/bin/activate` command with virtualenvs. To install project dependencies in the virtual environment, you should run `poetry install` - this will install **both** project and development dependencies.

For more details about Poetry and its commands please check out its [online documentation](https://python-poetry.org/docs/).

## Full Docker Development Environment

This project is set up with a number of **Invoke** tasks consumed as simple CLI commands to get developing fast. You'll use a few `invoke` commands to get your environment up and running.

### Invoke - Building the Docker Image

The first thing you need to do is build the necessary development container image.

```bash
➜ invoke build
... <omitted for brevity>
#15 [cookiecutter] exporting to image
#15 exporting layers 1.1s done
#15 writing image sha256:85627092abfb1f9abca3faf4990dfd413028bb6a55140125a50386776b9749c2 done
#15 naming to docker.io/library/cookiecutter-nautobot-app:3.11 done
#15 DONE 1.1s
```

### Invoke - Using Development Container

The development containers are used for running tests & linters. 

```bash
➜ invoke tests
Running yamllint...
Running poetry check...
All set!
Running pylint...

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Running mkdocs...
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: /home/whitej6/cookiecutter-nautobot-app/site
INFO    -  The following pages exist in the docs directory, but are not included in the "nav" configuration:
  - admin/compatibility_matrix.md
  - admin/install.md
  - admin/upgrade.md
  - dev/contributing.md
  - dev/dev_environment.md
  - dev/extending.md
  - user/faq.md
  - user/quick-start.md
INFO    -  Doc file 'index.md' contains an unrecognized relative link './nautobot-app', it was left as is.
INFO    -  Doc file 'index.md' contains an unrecognized relative link './nautobot-app-ssot', it was left as is.
INFO    -  Doc file 'index.md' contains an unrecognized relative link './nautobot-app-chatops', it was left as is.
INFO    -  Documentation built in 0.35 seconds
Running unit tests...
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/whitej6/cookiecutter-nautobot-app
configfile: pyproject.toml
testpaths: nautobot-app/tests, nautobot-app-chatops/tests, nautobot-app-ssot/tests
plugins: cookies-0.7.0
collected 6 items

nautobot-app/tests/test_bake_nautobot_app.py ..                          [ 33%]
nautobot-app-chatops/tests/test_bake_nautobot_app_chatops.py ..          [ 66%]
nautobot-app-ssot/tests/test_bake_nautobot_app_ssot.py ..                [100%]

============================== 6 passed in 2.11s ===============================
All tests have passed!
```

### Invoke - Cleaning Up Development Environment

The last command to know for now is `invoke stop`.

```bash
➜ invoke stop
Stopping container...
Running docker compose command "down --remove-orphans"
 Container cookiecutter-nautobot-app-docs-1  Stopping
 Container cookiecutter-nautobot-app-docs-1  Stopped
 Container cookiecutter-nautobot-app-docs-1  Removing
 Container cookiecutter-nautobot-app-docs-1  Removed
 Network cookiecutter-nautobot-app_default  Removing
 Network cookiecutter-nautobot-app_default  Removed
```

This will safely shut down all of your running Docker containers for this project. The previously built image will remain just the container used for running tests & documentation container will be removed.

### Real-Time Updates? How Cool!

Your environment should now be fully setup, all necessary Docker containers are created and running, and you're logged into Nautobot in your web browser. Now what?

Now you can start developing your app in the project folder!

The magic here is the root directory is mounted inside your Docker containers when built and ran, so **any** changes made to the files in here are directly updated to the Nautobot app code running in Docker. This means that as you modify the code in your app folder, the changes will be instantly updated in Nautobot.

!!! warning
	There are a few exceptions to this, as outlined in the section [To Rebuild or Not To Rebuild](#to-rebuild-or-not-to-rebuild).

### Docker Logs

When trying to debug an issue, one helpful thing you can look at are the logs within the Docker containers.

```bash
➜ docker logs <name of container> -f
```

!!! note
	The `-f` tag will keep the logs open, and output them in realtime as they are generated.

!!! info
    Want to limit the log output even further? Use the `--tail <#>` command line argument in conjunction with `-f`.

So for example, our compose project is named `cookiecutter-nautobot-app`, the command would most likely be `docker logs cookiecutter-nautobot-app_cookiecutter_1 -f`. You can find the name of all running containers via `docker ps`.

If you want to view the logs specific to the worker container, simply use the name of that container instead.

## To Rebuild or Not to Rebuild

Most of the time, you will not need to rebuild your images. Simply running `invoke tests` and `invoke stop` is enough to keep your environment going.

However there are a couple of instances when you will want to.

### Updating Environment Variables

To add environment variables to your containers, thus allowing Nautobot to use them, you will update/add them in the `development/development.env` file. However, doing so is considered updating the underlying container shell, instead of Django (which auto restarts itself on changes).

To get new environment variables to take effect, you will need stop any running images, rebuild the images, then restart them. This can easily be done with 3 commands:

```bash
➜ invoke stop
➜ invoke build
➜ invoke tests
```

Once completed, the new/updated environment variables should now be live.

### Installing Additional Python Packages

If you want your app to leverage another available Nautobot app or another Python package, you can easily add them into your Docker environment.

```bash
➜ poetry shell
➜ poetry add <package_name>
```

Once the dependencies are resolved, stop the existing containers, rebuild the Docker image, and then start all containers again.

```bash
➜ invoke stop
➜ invoke build
➜ invoke tests
```

### Updating Python Version

To update the Python version, you can update it within `tasks.py`.

```python
namespace = Collection("cookiecutter_nautobot_app")
namespace.configure(
    {
        "cookiecutter_nautobot_app": {
            ...
            "python_ver": "3.11",
	    ...
        }
    }
)
```

Or set the `INVOKE_COOKIECUTTER_NAUTOBOT_APP_PYTHON_VER` variable.

## Other Miscellaneous Commands To Know

### Tests

To run tests against your code, you can run all of the tests that TravisCI runs against any new PR with:

```bash
➜ invoke tests
```

To run an individual test, you can run any or all of the following:

```bash
➜ invoke unittest
➜ invoke ruff
➜ invoke pylint
```
