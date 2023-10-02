"""Cookie tests"""
from os import environ


def test_bake_project(cookies):
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
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
    plugin_slug = f"nautobot-plugin-ssot-ext-sor"
    assert results[plugin_slug].exit_code == 0
    assert results[plugin_slug].exception is None
    assert examples_projects[plugin_slug].isdir()
