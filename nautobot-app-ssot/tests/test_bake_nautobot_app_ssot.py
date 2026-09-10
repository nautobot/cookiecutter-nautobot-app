# pylint: disable=duplicate-code
"""Cookie tests"""
from os import environ


def test_bake_project(cookies):
    # pylint: disable-next=protected-access
    environ["COOKIECUTTER_CONFIG"] = str(cookies._config_file)
    result = cookies.bake(template="nautobot-app-ssot")

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    found_toplevel_files = [item.name for item in result.project_path.iterdir() if item.is_file()]
    assert "pyproject.toml" in found_toplevel_files
    assert "README.md" in found_toplevel_files
    assert "LICENSE" in found_toplevel_files
    assert "CONTRIBUTING.md" in found_toplevel_files
    assert "AGENTS.md" in found_toplevel_files
    assert "CLAUDE.md" in found_toplevel_files
    assert "GEMINI.md" in found_toplevel_files
    assert ".cursorrules" in found_toplevel_files
    assert (result.project_path / ".github" / "copilot-instructions.md").is_file()


def test_bake_nautobot_execution(cookies_baked_nautobot_app_ssot):
    """
    Tests creation of example nautobot with the cookiecutter default values
    """
    results, examples_projects = cookies_baked_nautobot_app_ssot
    app_slug = "nautobot-app-ssot-ext-sor"
    assert results[app_slug].exit_code == 0
    assert results[app_slug].exception is None
    assert examples_projects[app_slug].is_dir()
