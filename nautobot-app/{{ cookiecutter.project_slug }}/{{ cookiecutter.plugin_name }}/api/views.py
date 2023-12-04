"""API views for {{ cookiecutter.plugin_name }}."""

from nautobot.apps.api import NautobotModelViewSet

from {{ cookiecutter.plugin_name }} import filters, models
from {{ cookiecutter.plugin_name }}.api import serializers


class {{ cookiecutter.model_class_name }}ViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} viewset."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    serializer_class = serializers.{{ cookiecutter.model_class_name }}Serializer
    filterset_class = filters.{{ cookiecutter.model_class_name }}FilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
