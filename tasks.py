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

import json
import sys
from os import environ
from os import getenv
from os import getuid
from pathlib import Path
from pwd import getpwuid
from typing import Generator

import toml
from dotenv import load_dotenv
from invoke.collection import Collection
from invoke.tasks import task

_PATH = Path(__file__).parent.absolute()


def _jsontobool(value: str) -> bool:
    return bool(json.loads(value.lower()))


def _setup_env():
    load_dotenv(_PATH / ".creds.env", verbose=True)
    load_dotenv(_PATH / ".env", verbose=True)
    load_dotenv(_PATH / "development/default.env", verbose=True)

    def setenv(key, value):
        if key not in environ:
            environ[key] = str(value)

    setenv("REPOSITORY_DIR", _PATH.absolute())
    setenv("TARGET_WORKDIR", _PATH)

    uid = getuid()
    setenv("USER_UID", uid)
    setenv("USER_NAME", getpwuid(uid).pw_name)

    pyproject = toml.load(_PATH / "pyproject.toml")
    setenv("PACKAGE_SLUG", pyproject["tool"]["poetry"]["name"])
    setenv("PACKAGE_NAME", pyproject["tool"]["poetry"]["name"].replace("-", "_"))
    setenv("PACKAGE_VERSION", pyproject["tool"]["poetry"]["version"])

    setenv("COMPOSE_PROJECT_NAME", environ["PACKAGE_SLUG"])
    setenv("IMAGE_PREFIX", f"localhost/{environ['COMPOSE_PROJECT_NAME']}")


_setup_env()

_DEFAULT_EXEC = _jsontobool(getenv("INVOKE_DEFAULT_EXEC", "False"))
_DEFAULT_SERVICE = getenv("INVOKE_DEFAULT_SERVICE", "dev")
_LOCAL = _jsontobool(getenv("INVOKE_LOCAL", "False"))

_TEMPLATES = [
    "nautobot-app"
    # "nautobot-app-chatops",
    # "nautobot-app-ssot",
]

_PYTHON_NAMES_TO_CHECK = [
    "*.py",
    *[f"{template}/tests" for template in _TEMPLATES],
]


def _prefix_command(
    context,
    _exec=_DEFAULT_EXEC,
    root=False,
    service=_DEFAULT_SERVICE,
    entrypoint=None,
    build=None,
) -> Generator[str, None, None]:
    if _LOCAL:
        return

    # Autobuild qa, if not prohibited
    if build or (service == "qa" and build is None):
        build_task(context, service=service)

    yield "docker compose"

    if _exec:
        yield "exec"
    else:
        yield "run"
        yield "--rm"
        if entrypoint is not None:
            yield f"--entrypoint='{entrypoint}'"

    if root:
        yield "--user=root"

    yield "--"
    yield service


@task(
    name="build",
    help={
        "service": "Service to build container for (defaults to all)",
        "cache": "Whether to use Docker's cache when building the image (defaults to enabled)",
        "force_rm": "Always remove intermediate containers (defaults to disabled)",
        "pull": "Always attempt to pull a newer version of the image (defaults to disabled)",
    },
)
def build_task(context, service="", cache=True, force_rm=False, pull=False):
    """Build Docker image."""
    command = [
        "docker compose",
        "build",
        "--pull" if pull else "",
        "--progress=plain",
        "" if cache else "--no-cache",
        "--force-rm" if force_rm else "",
        "--",
        service,
    ]
    context.run(" ".join(command), pty=True)


@task(
    help={
        "template": "Name of the cookiecutter template to test",
    }
)
def test_template(context, template):
    """Test a specific cookiecutter template."""
    test_dir = _PATH / template / "tests"
    if not test_dir.exists():
        sys.exit(f"No Test found for {template}")

    print(f"Starting Test for {template}")
    command = [
        *_prefix_command(context),
        "pytest",
        str(test_dir),
        "-v",
        f"--template={template}",
    ]
    context.run(" ".join(command))


@task(
    help={
        "check": "Whether to run poetry check or lock (defaults to False)",
    }
)
def lock_poetry(context, service=_DEFAULT_SERVICE, check=False):
    """Generate poetry.lock, or run poetry check."""
    command = [
        *_prefix_command(context, service=service, build=check),
        "poetry",
        "check" if check else "lock --no-update",
    ]
    context.run(" ".join(command))


@task(help={"service": "If specified, only affect this service."})
def debug(context, service=""):
    """Start specified or all services and its dependencies in debug mode."""
    context.run(f"docker compose up -- {service}", pty=True)


@task(help={"service": "If specified, only affect this service."})
def start(context, service=""):
    """Start specified or all services and its dependencies in detached mode."""
    context.run(f"docker compose up --detach -- {service}", pty=True)


@task(help={"service": "If specified, only affect this service."})
def restart(context, service=""):
    """Gracefully restart specified or all services."""
    context.run(f"docker compose restart -- {service}", pty=True)


@task(help={"service": "If specified, only affect this service."})
def stop(context, service=""):
    """Stop specified or all services, if service is not specified, remove all containers."""
    command = [
        "docker compose",
        "stop" if service else "down --remove-orphans",
        "--",
        service,
    ]
    context.run(" ".join(command), pty=True)


@task
def destroy(context):
    """Destroy all containers and volumes."""
    context.run("docker compose down --remove-orphans --volumes")


@task
def export(context):
    """Export docker compose configuration to `compose.yaml` file.

    Useful to:

    - Debug docker compose configuration.
    - Allow using `docker compose` command directly without invoke.
    """
    context.run("docker compose convert > compose.yaml")
    print("Exported docker compose configuration to `compose.yaml` file.")
    print("\nBEWARE:\n")
    print("`compose.yaml` can contain credentials. Do not expose it to the editors whispering tools.")


@task(name="ps", help={"all": "Show all, including stopped containers"})
def ps_task(context, _all=False):
    """List containers."""
    context.run(f"docker compose ps {'--all' if _all else ''}")


@task(
    help={
        "service": "If specified, only display logs for this service (default: all)",
        "follow": "Flag to follow logs (default: False)",
        "tail": "Tail N number of lines (default: all)",
    }
)
def logs(context, service="", follow=False, tail=0):
    """View the logs of a docker compose service."""
    command = [
        "docker compose",
        "logs",
        "--follow" if follow else "",
        f"--tail={tail}" if tail else "",
        "--",
        service,
    ]
    context.run(" ".join(command), pty=True)


@task(
    help={
        "command": "Command to be run inside container",
        "exec": "Use existing container using `docker exec` or run in the new one with `docker run`",
        "root": "Run as root or default user",
        "service": "Name of the service to run command in",
        "input": "Input file to run command with (default: empty)",
        "output": "Ouput file, overwrite if exists (default: empty)",
    }
)
# pylint: disable-next=too-many-arguments
def cli(
    context,
    command="bash -l",
    _exec=False,
    root=False,
    service=_DEFAULT_SERVICE,
    _input="",
    output="",
):
    """Launch a bash shell (or other) inside service container."""
    cmd = [
        *_prefix_command(context, _exec, root, service),
        command,
        f"< '{_input}'" if _input else "",
        f"> '{output}'" if output else "",
    ]
    context.run(" ".join(cmd), pty=True)


@task(
    name="exec",
    help={
        "command": "Command to be run inside container",
        "root": "Run as root or default user",
        "service": "Name of the service to run command in",
        "input": "Input file to run command with (default: empty)",
        "output": "Ouput file, overwrite if exists (default: empty)",
    },
)
# pylint: disable-next=too-many-arguments
def exec_task(
    context,
    command="bash",
    root=False,
    service=_DEFAULT_SERVICE,
    _input="",
    output="",
):
    """Execute command inside running service container."""
    cmd = [
        *_prefix_command(context, True, root, service),
        command,
        f"< '{_input}'" if _input else "",
        f"> '{output}'" if output else "",
    ]
    context.run(" ".join(cmd), pty=True)


@task(
    help={
        "command": "Command to be run inside container",
        "root": "Run as root or default user",
        "service": "Name of the service to run command in",
        "input": "Input file to run command with (default: empty)",
        "output": "Ouput file, overwrite if exists (default: empty)",
    }
)
# pylint: disable-next=too-many-arguments
def run(
    context,
    command="bash",
    root=False,
    service=_DEFAULT_SERVICE,
    entrypoint=None,
    _input="",
    output="",
):
    """Run new service container with command."""
    cmd = [
        *_prefix_command(context, False, root, service, entrypoint=entrypoint),
        command,
        f"< '{_input}'" if _input else "",
        f"> '{output}'" if output else "",
    ]
    context.run(" ".join(cmd), pty=True)


@task(
    help={
        "service": "Name of the service to run command in",
    }
)
def bandit(context, service=_DEFAULT_SERVICE):
    """Run bandit to validate basic static code security analysis."""
    command = [
        *_prefix_command(context, service=service),
        "bandit",
        "--configfile=.bandit.yml",
        "--recursive",
        "*.py",
    ]
    context.run(" ".join(command))


@task(
    help={
        "autoformat": "Apply formatting recommendations automatically, rather than failing if formatting is incorrect.",
        "service": "Name of the service to run command in",
    }
)
def isort(context, autoformat=False, service=_DEFAULT_SERVICE):
    """Check Python code style with isort."""
    command = [
        *_prefix_command(context, service=service),
        "isort",
        "--force-single-line-imports",
        "" if autoformat else "--check --diff",
        *_PYTHON_NAMES_TO_CHECK,
    ]
    context.run(" ".join(command))


@task(
    help={
        "autoformat": "Apply formatting recommendations automatically, rather than failing if formatting is incorrect.",
        "service": "Name of the service to run command in",
    }
)
def black(context, autoformat=False, service=_DEFAULT_SERVICE):
    """Check Python code style with black."""
    command = [
        *_prefix_command(context, service=service),
        "black",
        "" if autoformat else "--check --diff",
        *_PYTHON_NAMES_TO_CHECK,
    ]
    context.run(" ".join(command))


@task(name="autoformat", aliases=("a",))
def autoformat_task(context):
    """Autoformat Python code with isort, black and ruff."""
    if not _LOCAL:
        command = [
            *_prefix_command(
                context,
            ),
            "invoke",
            "autoformat",
        ]
        context.run(" ".join(command), pty=True)
        return

    isort(context, autoformat=True)
    black(context, autoformat=True)
    ruff(context, autoformat=True)


@task(
    help={
        "service": "Name of the service to run command in",
    }
)
def pylint(context, service=_DEFAULT_SERVICE):
    """Run pylint code analysis."""
    command = [
        *_prefix_command(context, service=service),
        "pylint",
        "--rcfile=pyproject.toml",
        *_PYTHON_NAMES_TO_CHECK,
    ]
    context.run(" ".join(command))


@task(
    help={
        "autoformat": "Apply formatting recommendations automatically, rather than failing if formatting is incorrect.",
        "service": "Name of the service to run command in",
    }
)
def ruff(context, service=_DEFAULT_SERVICE, autoformat=False):
    """Run ruff code analysis."""
    command = [
        *_prefix_command(context, service=service),
        "ruff",
        "check",
        "--fix" if autoformat else "",
        *_PYTHON_NAMES_TO_CHECK,
    ]
    context.run(" ".join(command))


@task(
    help={
        "service": "Name of the service to run command in",
    }
)
def yamllint(context, service=_DEFAULT_SERVICE):
    """Run yamllint to validate formating adheres to NTC defined YAML standards."""
    command = [
        *_prefix_command(context, service=service),
        "yamllint",
        "./",
        "--format=standard",
    ]
    context.run(" ".join(command))


@task(
    aliases=("qa",),
    help={
        "lint_only": "Only run linting, not tests, (default: False)",
        "service": "Name of the service to run command in",
    },
)
def tests(context, lint_only=False, service="qa"):
    """Run all tests."""
    if not _LOCAL:
        command = [
            *_prefix_command(context, service=service),
            "invoke tests",
        ]
        context.run(" ".join(command), pty=True)
        return

    ruff(context, service=service)
    isort(context, service=service)
    black(context, service=service)
    bandit(context, service=service)
    yamllint(context, service=service)
    pylint(context, service=service)
    lock_poetry(context, service=service, check=True)

    if not lint_only:
        for template in _TEMPLATES:
            test_template(context, template=template)

    print("All tests have passed!")


@task(name="help")
def help_task(context):
    """Print the help of available tasks."""
    for task_name in sorted(ns.task_names):
        print(50 * "-")
        context.run(f"invoke {task_name} --help", echo=True)


def _read_invoke_kwargs():
    result = {}

    # True if not specified
    echo = getenv("INVOKE_ECHO", None)
    result["echo"] = (echo is None) or _jsontobool(echo)

    dry = getenv("INVOKE_DRY")
    if dry:
        result["dry"] = _jsontobool(dry)

    return result


# Must be on the end of the module
ns = Collection.from_module(sys.modules[__name__])
ns.configure({"run": _read_invoke_kwargs()})
