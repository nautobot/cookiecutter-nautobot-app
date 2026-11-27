"""Tests for the Playwright helpers in the `tasks.py` of a baked commercial app."""

import importlib.util
from os import environ
from pathlib import Path

import pytest
from invoke import Config, MockContext
from invoke.exceptions import Exit

PLAYWRIGHT_LOCK = '[[package]]\nname = "playwright"\nversion = "1.62.0"\n'


@pytest.fixture(name="baked_tasks")
def fixture_baked_tasks(cookies):
    """Bake the commercial template and return its `tasks.py`, imported as a module."""
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    result = cookies.bake(template="nautobot-app-commercial")
    assert result.exit_code == 0, result.exception
    spec = importlib.util.spec_from_file_location("baked_tasks", result.project_path / "tasks.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_lock(tasks_module, content):
    """Write `content` as the `poetry.lock` next to the baked `tasks.py`."""
    (Path(tasks_module.__file__).parent / "poetry.lock").write_text(content, encoding="utf-8")


def task_context(tasks_module):
    """Return an invoke context that has the baked app's task configuration."""
    config = Config()
    config.load_collection(tasks_module.namespace.configuration())
    return MockContext(config=config)


def test_locked_version_returns_the_pinned_version(baked_tasks):
    write_lock(baked_tasks, PLAYWRIGHT_LOCK)

    assert baked_tasks._locked_version("playwright") == "1.62.0"  # pylint: disable=protected-access


def test_locked_version_is_empty_without_a_lock_file(baked_tasks):
    assert not (Path(baked_tasks.__file__).parent / "poetry.lock").exists(), "A fresh bake has no poetry.lock"

    assert baked_tasks._locked_version("playwright") == ""  # pylint: disable=protected-access


def test_locked_version_is_empty_for_a_package_that_the_lock_does_not_list(baked_tasks):
    write_lock(baked_tasks, PLAYWRIGHT_LOCK)

    assert baked_tasks._locked_version("pytest-playwright") == ""  # pylint: disable=protected-access


def test_playwright_exits_without_a_lock_file(baked_tasks):
    assert not (Path(baked_tasks.__file__).parent / "poetry.lock").exists(), "A fresh bake has no poetry.lock"

    with pytest.raises(Exit, match="poetry.lock does not list playwright") as exit_info:
        baked_tasks.playwright(task_context(baked_tasks))

    assert exit_info.value.code == 1


def test_playwright_look_exits_for_a_full_url(baked_tasks):
    write_lock(baked_tasks, PLAYWRIGHT_LOCK)

    with pytest.raises(Exit, match="--look takes a path") as exit_info:
        baked_tasks.playwright(task_context(baked_tasks), look="http://localhost:8080/dcim/devices/")

    assert exit_info.value.code == 1
