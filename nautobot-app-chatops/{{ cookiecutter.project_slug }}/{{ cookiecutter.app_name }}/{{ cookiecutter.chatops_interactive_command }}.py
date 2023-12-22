"""All interactions with API behind {{ cookiecutter.chatops_interactive_command }}.

This class is usually a wrapper of an existing SDK, or a raw implementation of it to have reusable code in the worker.py.
"""

import logging


logger = logging.getLogger("nautobot")


class {{ cookiecutter.camel_name }}:  # pylint: disable=too-few-public-methods
    """Representation and methods for interacting with the API behind {{ cookiecutter.chatops_interactive_command }}."""

    def __init__(self):
        """Initialization of {{ cookiecutter.chatops_interactive_command }} class."""
