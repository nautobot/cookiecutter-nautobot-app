# pylint: disable=duplicate-code
"""Cookie tests configuration"""
import shutil
from os import environ
from pathlib import Path

from pytest import fixture


def init_examples_project(project_name):
    """Initialize the examples project folder (by deleting and reconstructing it if
    already created, or just create).
    Args:
        project_name (str): Cookiecutter example project name
    Returns:
        examples_project (Path): Created example project
    """
    # Set examples folder to cookiecutter level directory
    examples_project = (Path(__file__) / "../../examples" / project_name).resolve()

    # Clean examples project
    if examples_project.is_dir():
        shutil.rmtree(examples_project)
    else:
        examples_project.parent.mkdir(parents=True, exist_ok=True)
    return examples_project


@fixture
def cookies_baked_nautobot_app(cookies):
    """Sets up an example cookiecutter project
    Args:
        cookies: wrapper for cookiecutter API when generating project
    Return:
        results (dict): of (cookies.bake) cookies baked project with execution results indexed by prod_env
        examples_project (dict[Path]): created example project indexed by prod_env
    """
    examples_projects = {}
    results = {}
    extra_contexts = {
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
    for plugin_slug, extra_context in extra_contexts.items():
        results[plugin_slug] = cookies.bake(extra_context=extra_context)

        assert results[plugin_slug].exception is None

        examples_projects[plugin_slug] = init_examples_project(plugin_slug)
        shutil.move(results[plugin_slug].project_path, examples_projects[plugin_slug])

    return results, examples_projects
