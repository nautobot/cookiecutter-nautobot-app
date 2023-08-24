"""API views for {{ cookiecutter.nautobot_app_name }}."""

from nautobot.core.api.views import ModelViewSet

from {{ cookiecutter.nautobot_app_name }} import filters, models

from {{ cookiecutter.nautobot_app_name }}.api import serializers


class {{ cookiecutter.model_class_name }}ViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} viewset."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    serializer_class = serializers.{{ cookiecutter.model_class_name }}Serializer
    filterset_class = filters.{{ cookiecutter.model_class_name }}FilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
