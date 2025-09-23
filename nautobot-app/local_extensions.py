"""Local extensions for Nautobot Cookies."""
import re

from jinja2 import Environment
from jinja2.ext import Extension
from cookiecutter.utils import simple_filter

@simple_filter
def camel_case_to_kebab(name: str) -> str:
    """Converts a camel case name to kebab case (-).

    Args:
        name: The name to convert.
    """
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+|[A-Z]{2,}|[A-Z]$", name)
    return "-".join(words).lower()

@simple_filter
def camel_case_to_words(name: str) -> str:
    """Converts a camel case name to words.

    Args:
        name: The name to convert.
    """
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+|[A-Z]{2,}|[A-Z]$", name)
    return " ".join(words)

class NautobotVersions(Extension):  # pylint: disable=abstract-method
    """Jinja2 extension to set a minimum/maximum Nautobot version."""

    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.globals.update(min_nautobot_version="3.0.0")
        environment.globals.update(upper_bound_nautobot_version="4.0.0")
