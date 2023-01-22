"""Nautobot App declaration for my_nautobot_app."""
# Metadata is inherited from Nautobot. If not including Nautobot in the  environment, this should be added.
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.apps import NautobotAppConfig


class MyNautobotAppConfig(NautobotAppConfig):
    """Nautobot App configuration for my_nautobot_app."""

    name = "my_nautobot_app"
    verbose_name = "My Nautobot App"
    version = __version__
    author = "Network to Code, LLC"
    description = "My Nautobot App."
    base_url = "my-nautobot-app"
    required_settings = []
    min_version = "1.5.7"
    default_settings = {}
    caching_config = {}


config = MyNautobotAppConfig  # pylint:disable=invalid-name
