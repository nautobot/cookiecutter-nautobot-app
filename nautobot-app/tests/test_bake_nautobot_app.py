# pylint: disable=duplicate-code
"""Cookie tests"""
from os import environ


def test_bake_project(cookies):
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    found_toplevel_files = [item.name for item in result.project_path.iterdir() if item.is_file()]
    assert "pyproject.toml" in found_toplevel_files
    assert "README.md" in found_toplevel_files
    assert "LICENSE" in found_toplevel_files


def test_bake_nautobot_execution(cookies_baked_nautobot_app):
    """
    Tests creation of example nautobot with the cookiecutter default values
    """
    results, examples_projects = cookies_baked_nautobot_app
    plugin_slug = "nautobot-plugin"
    assert results[plugin_slug].exit_code == 0
    assert results[plugin_slug].exception is None
    assert examples_projects[plugin_slug].is_dir()
