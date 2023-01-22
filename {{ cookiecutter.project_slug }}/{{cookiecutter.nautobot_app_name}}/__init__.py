"""Nautobot App declaration for {{ cookiecutter.nautobot_app_name }}."""
# Metadata is inherited from Nautobot. If not including Nautobot in the  environment, this should be added.
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.apps import NautobotAppConfig


class {{ cookiecutter.camel_name }}Config(NautobotAppConfig):
    """Nautobot App configuration for {{ cookiecutter.nautobot_app_name }}."""

    name = "{{ cookiecutter.nautobot_app_name }}"
    verbose_name = "{{ cookiecutter.verbose_name }}"
    version = __version__
    author = "{{ cookiecutter.full_name }}"
    description = "{{ cookiecutter.project_short_description }}."
    base_url = "{{ cookiecutter.base_url }}"
    required_settings = []
    min_version = "{{ cookiecutter.min_nautobot_version }}"
    default_settings = {}
    caching_config = {}


config = {{ cookiecutter.camel_name }}Config  # pylint:disable=invalid-name
