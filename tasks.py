import pathlib
import shutil
import sys
from glob import glob

from invoke import task


@task
def test(context):
    """Test that the cookie bakes."""
    test_dir = pathlib.Path.cwd() / "tests"
    if test_dir.exists():
        print("Starting Tests")
        context.run(f"pytest { test_dir } -v")
    else:
        sys.exit("No tests found.")


@task(
    help={
        "build": "Whether to re-bake (build) the example before testing it",
    }
)
def baked_test(context, build=False):
    """Execute tests within a baked cookie example."""
    context.run(f"invoke test")

    for baked_cookie in glob("examples/*"):
        print(f"Running Tests for example {baked_cookie}")
        with context.cd(baked_cookie):
            # Make sure to copy creds.example.env to creds.env for tests.
            context.run("cp development/creds.example.env development/creds.env")

            if build:
                context.run("invoke build --no-cache")

            context.run("invoke tests")
            context.run("invoke stop")


@task
def cleanup(context):
    """Cleanup baked cookie example directories."""
    for example in glob("examples/*"):
        shutil.rmtree(example)
