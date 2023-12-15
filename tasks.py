"""Tasks for use with Invoke.

(c) 2023 Network To Code
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from pathlib import Path
from time import sleep

from invoke.collection import Collection
from invoke.tasks import task as invoke_task


def is_truthy(arg):
    """Convert "truthy" strings into Booleans.

    Examples:
        >>> is_truthy('yes')
        True
    Args:
        arg (str): Truthy string (True values are y, yes, t, true, on and 1; false values are n, no,
        f, false, off and 0. Raises ValueError if val is anything else.
    """
    if isinstance(arg, bool):
        return arg

    val = str(arg).lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError(f"Invalid truthy value: `{arg}`")


# Use pyinvoke configuration for default values, see http://docs.pyinvoke.org/en/stable/concepts/configuration.html
# Variables may be overwritten in invoke.yml or by the environment variables INVOKE_COOKIECUTTER_NAUTOBOT_APP_xxx
namespace = Collection("cookiecutter_nautobot_app")
namespace.configure(
    {
        "cookiecutter_nautobot_app": {
            "project_name": "cookiecutter-nautobot-app",
            "python_ver": "3.11",
            "local": "True",
            "compose_dir": os.path.join(os.path.dirname(__file__), "development"),
            "compose_files": [
                "docker-compose.yml",
            ],
            "templates": [
                "nautobot-app",
                # "nautobot-app-chatops",
                "nautobot-app-ssot",
            ],
            "compose_http_timeout": "86400",
        }
    }
)


def collect_files(context, patterns=["*.py"]):
    "Helper method for collecting applicable python files."
    for template in context.cookiecutter_nautobot_app.templates:
        patterns.append(f"{template}/tests")
    return " ".join(patterns)


def task(function=None, *args, **kwargs):
    """Task decorator to override the default Invoke task decorator and add each task to the invoke namespace."""

    def task_wrapper(function=None):
        """Wrapper around invoke.task to add the task to the namespace as well."""
        if args or kwargs:
            task_func = invoke_task(*args, **kwargs)(function)
        else:
            task_func = invoke_task(function)
        namespace.add_task(task_func)
        return task_func

    if function:
        # The decorator was called with no arguments
        return task_wrapper(function)
    # The decorator was called with arguments
    return task_wrapper


def docker_compose(context, command, **kwargs):
    """Helper function for running a specific docker compose command with all appropriate parameters and environment.

    Args:
        context (obj): Used to run specific commands
        command (str): Command string to append to the "docker compose ..." command, such as "build", "up", etc.
        **kwargs: Passed through to the context.run() call.
    """
    build_env = {
        # Note: 'docker compose logs' will stop following after 60 seconds by default,
        # so we are overriding that by setting this environment variable.
        "COMPOSE_HTTP_TIMEOUT": context.cookiecutter_nautobot_app.compose_http_timeout,
        "PYTHON_VER": context.cookiecutter_nautobot_app.python_ver,
        **kwargs.pop("env", {}),
    }
    compose_command_tokens = [
        "docker compose",
        f"--project-name {context.cookiecutter_nautobot_app.project_name}",
        f'--project-directory "{context.cookiecutter_nautobot_app.compose_dir}"',
    ]

    for compose_file in context.cookiecutter_nautobot_app.compose_files:
        compose_file_path = os.path.join(context.cookiecutter_nautobot_app.compose_dir, compose_file)
        compose_command_tokens.append(f' -f "{compose_file_path}"')

    compose_command_tokens.append(command)

    # If `service` was passed as a kwarg, add it to the end.
    service = kwargs.pop("service", None)
    if service is not None:
        compose_command_tokens.append(service)

    print(f'Running docker compose command "{command}"')
    compose_command = " ".join(compose_command_tokens)

    return context.run(compose_command, env=build_env, **kwargs)


def run_command(context, command, **kwargs):
    """Wrapper to run a command locally or inside the nautobot container."""
    if is_truthy(context.cookiecutter_nautobot_app.local):
        context.run(command, **kwargs)
    else:
        docker_compose_status = "ps --services --filter status=running"
        results = docker_compose(context, docker_compose_status, hide="out")
        if "cookiecutter" in results.stdout:
            compose_command = f"exec cookiecutter {command}"
        else:
            compose_command = f"run --rm --entrypoint '{command}' cookiecutter"

        pty = kwargs.pop("pty", True)

        docker_compose(context, compose_command, pty=pty, **kwargs)


# ------------------------------------------------------------------------------
# BUILD
# ------------------------------------------------------------------------------
@task(
    help={
        "force_rm": "Always remove intermediate containers",
        "cache": "Whether to use Docker's cache when building the image (defaults to enabled)",
    }
)
def build(context, force_rm=False, cache=True):
    """Build QA docker image."""
    command = "build"

    if not cache:
        command += " --no-cache"
    if force_rm:
        command += " --force-rm"

    print(f"Building QA with Python {context.cookiecutter_nautobot_app.python_ver}...")
    docker_compose(context, command)


@task
def generate_packages(context):
    """Generate all Python packages inside docker and copy the file locally under dist/."""
    command = "poetry build"
    run_command(context, command)


@task(
    help={
        "check": (
            "If enabled, check for outdated dependencies in the poetry.lock file, "
            "instead of generating a new one. (default: disabled)"
        )
    }
)
def lock(context, check=False):
    """Generate poetry.lock inside the container."""
    run_command(context, f"poetry {'check' if check else 'lock --no-update'}")


# ------------------------------------------------------------------------------
# START / STOP / DEBUG
# ------------------------------------------------------------------------------
@task(help={"service": "If specified, only affect this service."})
def debug(context, service=""):
    """Start specified or all services and its dependencies in debug mode."""
    print(f"Starting {service} in debug mode...")
    docker_compose(context, "up", service=service)


@task(help={"service": "If specified, only affect this service."})
def start(context, service=""):
    """Start specified or all services and its dependencies in detached mode."""
    print("Starting container in detached mode...")
    docker_compose(context, "up --detach", service=service)


@task(help={"service": "If specified, only affect this service."})
def restart(context, service=""):
    """Gracefully restart specified or all services."""
    print("Restarting container...")
    docker_compose(context, "restart", service=service)


@task(help={"service": "If specified, only affect this service."})
def stop(context, service=""):
    """Stop specified or all services, if service is not specified, remove all containers."""
    print("Stopping container...")
    docker_compose(context, "stop" if service else "down --remove-orphans", service=service)


@task(
    aliases=("down",),
    help={"volumes": "Remove Docker compose volumes (default: True)"},
)
def destroy(context, volumes=True, import_db_file=""):
    """Destroy all containers and volumes."""
    print("Destroying container...")
    docker_compose(context, f"down --remove-orphans {'--volumes' if volumes else ''}")


@task
def export(context):
    """Export docker compose configuration to `compose.yaml` file.

    Useful to:

    - Debug docker compose configuration.
    - Allow using `docker compose` command directly without invoke.
    """
    docker_compose(context, "convert > compose.yaml")


@task(name="ps", help={"all": "Show all, including stopped containers"})
def ps_task(context, all=False):
    """List containers."""
    docker_compose(context, f"ps {'--all' if all else ''}")


@task
def vscode(context):
    """Launch Visual Studio Code with the appropriate Environment variables to run in a container."""
    command = "code nautobot.code-workspace"

    context.run(command)


@task(
    help={
        "service": "If specified, only display logs for this service (default: all)",
        "follow": "Flag to follow logs (default: False)",
        "tail": "Tail N number of lines (default: all)",
    }
)
def logs(context, service="", follow=False, tail=0):
    """View the logs of a docker compose service."""
    command = "logs "

    if follow:
        command += "--follow "
    if tail:
        command += f"--tail={tail} "

    docker_compose(context, command, service=service)


# ------------------------------------------------------------------------------
# ACTIONS
# ------------------------------------------------------------------------------


@task
def cli(context):
    """Launch a bash shell inside the container."""
    compose_command = f"run --rm --entrypoint bash cookiecutter"

    docker_compose(context, compose_command, pty=True)


# ------------------------------------------------------------------------------
# DOCS
# ------------------------------------------------------------------------------
@task
def docs(context):
    """Build and serve docs locally for development."""
    command = "mkdocs serve -v"

    if is_truthy(context.cookiecutter_nautobot_app.local):
        print(">>> Serving Documentation at http://localhost:8001")
        run_command(context, command)
    else:
        start(context, service="docs")


@task
def build_and_check_docs(context):
    """Build documentation to be available within the container."""
    command = "mkdocs build --no-directory-urls --strict"
    run_command(context, command)


@task(name="help")
def help_task(context):
    """Print the help of available tasks."""
    import tasks  # pylint: disable=all

    root = Collection.from_module(tasks)
    for task_name in sorted(root.task_names):
        print(50 * "-")
        print(f"invoke {task_name} --help")
        context.run(f"invoke {task_name} --help")


# ------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------------
@task(
    help={
        "autoformat": "Apply formatting recommendations automatically, rather than failing if formatting is incorrect."
    }
)
def black(context, autoformat=False, template=""):
    """Check Python code style with Black."""
    if autoformat:
        black_command = "black"
    else:
        black_command = "black --check --diff"

    command = f"{black_command} {collect_files(context, patterns=[])}"
    run_command(context, command)


@task
def pylint(context):
    """Run pylint code analysis."""
    command = f"pylint --rcfile pyproject.toml {collect_files(context)}"
    run_command(context, command)


@task
def hadolint(context):
    """Check Dockerfile for hadolint compliance and other style issues."""
    command = "hadolint development/Dockerfile"
    run_command(context, command)


@task
def yamllint(context):
    """Run yamllint to validate formatting adheres to NTC defined YAML standards.

    Args:
        context (obj): Used to run specific commands
    """
    command = "yamllint . --format standard"
    run_command(context, command)


@task(
    help={
        "label": "specify a directory with tests directory instead of running all tests for all templates (e.g. -l='nautobot-app/tests')",
        "failfast": "fail as soon as a single test fails don't run the entire test suite",
        "pattern": "Run specific test methods, classes, or modules instead of all tests",
        "verbose": "Enable verbose test output.",
    }
)
def unittest(context, label="", failfast=False, pattern="", verbose=False):
    """Run Cookie bake unit tests."""
    command = f"pytest"

    if failfast:
        command += " --failfast"
    if pattern:
        command += f" -k='{pattern}'"
    if verbose:
        command += " --verbosity 2"
    if label:
        command += f" {label}"

    run_command(context, command)


@task(
    help={
        "failfast": "fail as soon as a single test fails don't run the entire test suite. (default: False)",
        "keepdb": "Save and re-use test database between test runs for faster re-testing. (default: False)",
        "lint-only": "Only run linters; unit tests will be excluded. (default: False)",
    }
)
def tests(context, failfast=False, keepdb=False, lint_only=False):
    """Run all tests for this plugin."""
    # If we are not running locally, start the docker containers so we don't have to for each test
    if not is_truthy(context.cookiecutter_nautobot_app.local):
        print("Starting Docker Containers...")
        start(context)
    # Sorted loosely from fastest to slowest
    print("Running black...")
    black(context)
    print("Running yamllint...")
    yamllint(context)
    print("Running poetry check...")
    lock(context, check=True)
    print("Running pylint...")
    pylint(context)
    print("Running mkdocs...")
    build_and_check_docs(context)
    if not lint_only:
        print("Running unit tests...")
        unittest(context, failfast=failfast)
    print("All tests have passed!")


@task(
    help={
        "debug": "Whether to run in debug mode (defaults to False)",
        "input": "Whether to require user input, ignored with `--json-file` (defaults to True)",
        "json-file": "Path to a JSON file containing answers to prompts (defaults to empty)",
        "output-dir": "Path to the output directory (defaults to ./outputs)",
        "template": "Path to the cookiecutter template to bake (defaults to ./nautobot-app)",
    },
)
def bake(context, _debug=False, _input=True, json_file="", output_dir="./outputs", template="./nautobot-app"):
    """Bake a new cookie from the template."""

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    command = [
        "cookiecutter",
        f"--output-dir={output_dir}",
        f"--replay-file={json_file}" if json_file else "",
    ]

    if not _input:
        command.append("--no-input")

    if _debug:
        command.append("--verbose")
        command.append(f"--debug-file={output_dir}/debug.log")
        command.append("--keep-project-on-failure")

    command.append(template)

    run_command(context, " ".join(command))
