"""Cookie tests configuration"""
from os import environ

import py
from pytest import fixture


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


@fixture
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
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    for plugin_slug in ["nautobot-plugin", "my-plugin"]:
        results[plugin_slug] = cookies.bake(extra_context=extra_context[plugin_slug])

        assert results[plugin_slug].exception is None

        examples_projects[plugin_slug] = init_examples_project(results[plugin_slug].project.basename)
        results[plugin_slug].project.move(examples_projects[plugin_slug])
    return results, examples_projects
