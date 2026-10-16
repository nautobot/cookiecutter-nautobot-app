"""Drift-guard tests for the Dependabot auto-merge workflow."""

import re
import subprocess
from pathlib import Path
from unittest import TestCase

import yaml

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib

# These files are not part of the built image; the test needs the repository bind-mounted (e.g. `../:/source`).
REPO_ROOT = Path(__file__).resolve().parents[2]
PYPROJECT = REPO_ROOT / "pyproject.toml"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "dependabot_automerge.yml"


def _optional_groups():
    """Return the names of the optional Poetry dependency groups in pyproject.toml."""
    with PYPROJECT.open("rb") as handle:
        groups = tomllib.load(handle)["tool"]["poetry"].get("group", {})
    return {name for name, config in groups.items() if config.get("optional") is True}


def _normalize(name):
    """Normalize a group name the way Poetry does (`packaging.utils.canonicalize_name`)."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _declared_groups():
    """Return the normalized names of all dependency groups in pyproject.toml.

    Includes PEP 735 `[dependency-groups]` and Poetry's `[tool.poetry.group.<name>]` tables.
    """
    with PYPROJECT.open("rb") as handle:
        pyproject = tomllib.load(handle)
    names = set(pyproject.get("dependency-groups", {}))
    names.update(pyproject.get("tool", {}).get("poetry", {}).get("group", {}))
    return {_normalize(name) for name in names}


def _workflow_with_groups():
    """Return the groups passed via `--with` to `poetry show --top-level` in the workflow."""
    with WORKFLOW.open(encoding="utf-8") as handle:
        workflow = yaml.safe_load(handle)
    found = set()
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            run = step.get("run", "")
            if "poetry show --top-level" in run:
                for match in re.finditer(r"--with[ =](\S+)", run):
                    found.update(match.group(1).split(","))
    return found


def _workflow_title_pattern():
    """Return the bash regex the workflow assigns to `title_pattern`."""
    with WORKFLOW.open(encoding="utf-8") as handle:
        workflow = yaml.safe_load(handle)
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            match = re.search(r"^\s*title_pattern='([^']*)'$", step.get("run", ""), re.MULTILINE)
            if match:
                return match.group(1)
    raise AssertionError(f"No `title_pattern='...'` assignment found in {WORKFLOW.name}")


def _bash_match(title, pattern):
    """Match `title` against `pattern` with bash `=~`, as the workflow does; return the groups or None."""
    result = subprocess.run(
        ["bash", "-c", '[[ "$1" =~ $2 ]] && printf "%s\\n" "${BASH_REMATCH[@]:1}"', "_", title, pattern],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    return tuple(result.stdout.splitlines())


class DependabotAutomergeTest(TestCase):
    """Verify the auto-merge workflow stays in sync with the repository."""

    def test_optional_groups_are_checked_by_workflow(self):
        """Every optional Poetry group must be included when the workflow lists top-level dependencies."""
        optional = _optional_groups()
        with_groups = _workflow_with_groups()
        self.assertLessEqual(
            optional,
            with_groups,
            f"Optional groups missing from `--with` in {WORKFLOW.name}: {sorted(optional - with_groups)}",
        )

    def test_workflow_groups_exist(self):
        """Every group passed via `--with` must be declared in pyproject.toml, or `poetry show` fails."""
        unknown = {_normalize(name) for name in _workflow_with_groups()} - _declared_groups()
        self.assertFalse(unknown, f"`--with` groups in {WORKFLOW.name} not found in pyproject.toml: {sorted(unknown)}")

    def test_title_pattern(self):
        """The workflow's title pattern matches single-dependency bumps and rejects grouped updates."""
        pattern = _workflow_title_pattern()
        self.assertEqual(_bash_match("Bump oauthlib from 3.3.1 to 4.0.0", pattern), ("oauthlib", "3.3.1", "4.0.0"))
        self.assertIsNone(_bash_match("Bump the pip group with 3 updates", pattern))
