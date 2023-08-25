"""API nested serializers for {{ cookiecutter.plugin_name }}."""
from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from {{ cookiecutter.plugin_name }} import models


class {{ cookiecutter.model_class_name }}NestedSerializer(WritableNestedSerializer):
    """{{ cookiecutter.model_class_name }} Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:{{ cookiecutter.plugin_name }}-api:{{ cookiecutter.model_class_name | lower }}-detail")

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = "__all__"
