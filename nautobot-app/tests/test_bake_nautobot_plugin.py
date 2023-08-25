import os

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
    examples_project = py.path.local(__file__ + f"/../../examples/{project_name}")

    # Clean examples project
    if examples_project.isdir():
        examples_project.remove()
        examples_project.mkdir()
    else:
        examples_project.mkdir()
    return examples_project


@pytest.fixture
def cookies_baked_nautobot_plugin(cookies):
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
    extra_context = {
        "nautobot-plugin": {
                "open_source_license": "Not open source",
                "plugin_name": "nautobot_plugin",
            },
        "my-plugin": {
                "open_source_license": "Apache-2.0",
                "plugin_name": "my_plugin",
            },
    }
    os.environ['COOKIECUTTER_CONFIG'] = str(cookies._config_file)
    for plugin_slug in ["nautobot-plugin", "my-plugin"]:
        results[plugin_slug] = cookies.bake(
            extra_context=extra_context[plugin_slug]
        )

        assert results[plugin_slug].exception is None

        examples_projects[plugin_slug] = init_examples_project(
            results[plugin_slug].project.basename
        )
        results[plugin_slug].project.move(examples_projects[plugin_slug])
    return results, examples_projects


def test_bake_project(cookies):
    os.environ['COOKIECUTTER_CONFIG'] = str(cookies._config_file)
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()

    found_toplevel_files = [f.basename for f in result.project.listdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "README.md" in found_toplevel_files
    assert "LICENSE" in found_toplevel_files


def test_bake_nautobot_execution(cookies_baked_nautobot_plugin):
    """
    Tests creation of example nautobot with the cookiecutter default values
    """
    results, examples_projects = cookies_baked_nautobot_plugin
    plugin_slug = f"nautobot-plugin"
    assert results[plugin_slug].exit_code == 0
    assert results[plugin_slug].exception is None
    assert examples_projects[plugin_slug].isdir()
