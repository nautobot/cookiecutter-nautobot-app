"""App declaration for {{ cookiecutter.app_name }}."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class {{ cookiecutter.camel_name }}Config(NautobotAppConfig):
    """App configuration for the {{ cookiecutter.app_name }} app."""

    name = "{{ cookiecutter.app_name }}"
    verbose_name = "{{ cookiecutter.verbose_name }}"
    version = __version__
    author = "{{ cookiecutter.full_name }}"
    description = "{{ cookiecutter.project_short_description }}."
    base_url = "{{ cookiecutter.base_url }}"
    required_settings = []
    default_settings = {}
    docs_view_name = "plugins:{{ cookiecutter.app_name }}:docs"
    searchable_models = [{% if cookiecutter.model_class_name and cookiecutter.model_class_name|trim|lower != 'none' %}"{{ cookiecutter.model_class_name|trim|lower }}"{% endif %}]


config = {{ cookiecutter.camel_name }}Config  # pylint:disable=invalid-name
