import pathlib
import sys
from invoke import task
from glob import glob


@task
def test(context):
    """Test a specific cookiecutter template."""
    test_dir = pathlib.Path.cwd() / "tests"
    if test_dir.exists():
        print("Starting Tests")
        context.run(f"pytest { test_dir } -v")
    else:
        sys.exit("No tests found.")


@task(
    help={
        "build": "Whether to re-bake (build) the example before testing it",
        "example": "Glob-style pattern specifying which baked example(s) to test (default '*')",
    }
)
def baked_test(context, build=False, example="*"):
    """Execute tests within a baked cookiecutter example."""
    if not glob(f"examples/{example}"):
        sys.exit("No example matching '{example}' found.")
    for baked_cookie in glob(f"examples/{example}"):
        print(f"Running Tests for example {baked_cookie}")
        with context.cd(baked_cookie):
            # This will go ahead and build the lock file as part of the poetry update command for
            # builds to pass.
            context.run("cp development/creds.example.env development/creds.env")

            if build:
                context.run("invoke build --no-cache")

            context.run("invoke tests")
