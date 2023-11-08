"""Plugin declaration for {{cookiecutter.plugin_name}}."""
from importlib import metadata

from nautobot.extras.plugins import NautobotAppConfig

__version__ = metadata.version(__name__)


class {{cookiecutter.camel_name}}Config(NautobotAppConfig):
    """Plugin configuration for the {{cookiecutter.plugin_name}} plugin."""

    name = "{{cookiecutter.plugin_name}}"
    verbose_name = "{{cookiecutter.verbose_name}}"
    version = __version__
    author = "{{cookiecutter.full_name}}"
    description = "{{cookiecutter.project_short_description}}."
    base_url = "{{cookiecutter.base_url}}"
    required_settings = []
    min_version = "{{cookiecutter.min_nautobot_version}}"
    max_version = "{{cookiecutter.max_nautobot_version}}"
    default_settings = {}
    caching_config = {}


config = {{cookiecutter.camel_name}}Config  # pylint:disable=invalid-name
