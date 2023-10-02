"""API serializers for {{ cookiecutter.plugin_name }}."""
from rest_framework import serializers

from nautobot.core.api.serializers import ValidatedModelSerializer

from {{ cookiecutter.plugin_name }} import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class {{ cookiecutter.model_class_name }}Serializer(ValidatedModelSerializer):
    """{{ cookiecutter.model_class_name }} Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:{{ cookiecutter.plugin_name }}-api:{{ cookiecutter.model_class_name | lower }}-detail")

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
