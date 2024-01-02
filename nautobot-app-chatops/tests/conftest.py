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
def cookies_baked_nautobot_app_chatops(cookies):
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
        "nautobot-app-chatops-platform1": {
            "open_source_license": "Not open source",
            "chatops_interactive_command": "platform1",
        },
        "nautobot-app-chatops-platform2": {
            "open_source_license": "Apache-2.0",
            "chatops_interactive_command": "platform2",
        },
    }
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    for app_slug, extra_context in extra_contexts.items():
        results[app_slug] = cookies.bake(extra_context=extra_context, template="nautobot-app-chatops")

        assert results[app_slug].exception is None

        examples_projects[app_slug] = init_examples_project(app_slug)
        shutil.move(results[app_slug].project_path, examples_projects[app_slug])

    return results, examples_projects
