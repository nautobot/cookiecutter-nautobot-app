import re

from cookiecutter.utils import simple_filter

@simple_filter
def camel_case_to_kebab(name: str) -> str:
    """Converts a camel case name to kebab case (-).

    Args:
        name: The name to convert.
    """
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+|[A-Z]{2,}|[A-Z]$", name)
    return "-".join(words).lower()