import os
from pathlib import Path
import shutil

import pytest
import py


def init_examples_project(project_name):
    """
    Initialize the examples project folder (by deleting and reconstructing it if
    already created, or just create).
    Args:
        project_name (str): Cookiecutter example project name
    Returns:
        examples_project (py.path.local): Created example project
    """
    # Set examples folder to cookiecutter level directory
    # e.g. "../../examples/{project_name}"
    # examples_project = Path(__file__).parent.parent / "examples" / project_name
    examples_project = py.path.local(__file__ + f"/../../examples/{project_name}")

    # Clean examples project
    if examples_project.isdir():
        shutil.rmtree(examples_project)
        examples_project.mkdir()
    else:
        examples_project.mkdir()
    return examples_project


@pytest.fixture
def cookies_baked_nautobot_app(cookies):
    """
    Sets up an example cookiecutter project
    Args:
        cookies: wrapper for cookiecutter API when generating project
    Return:
        results (dict): of (cookies.bake) cookies baked project with execution results indexed by prod_env
        examples_project (dict): of (py.path.local) created example project indexed by prod_env
    """
    examples_projects = {}
    results = {}
    cookie_data = {
        "nautobot-app": {
            "open_source_license": "Not open source",
            "app_name": "nautobot_app",
        },
        "my-app": {
            "open_source_license": "Apache-2.0",
            "app_name": "my_app",
        },
    }
    os.environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    for app_slug, extra_context in cookie_data.items():
        results[app_slug] = cookies.bake(extra_context=extra_context)

        assert results[app_slug].exception is None

        examples_projects[app_slug] = init_examples_project(
            results[app_slug].project_path.name
        )
        results[app_slug].project_path.rename(examples_projects[app_slug])
    return results, examples_projects


def test_bake_project(cookies):
    os.environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    for filename in ["pyproject.toml", "README.md", "LICENSE"]:
        assert filename in found_toplevel_files


def test_bake_nautobot_execution(cookies_baked_nautobot_app):
    """
    Tests creation of example nautobot with the cookiecutter default values
    """
    results, examples_projects = cookies_baked_nautobot_app
    app_slug = "nautobot-app"
    assert results[app_slug].exit_code == 0
    assert results[app_slug].exception is None
    assert examples_projects[app_slug].isdir()
