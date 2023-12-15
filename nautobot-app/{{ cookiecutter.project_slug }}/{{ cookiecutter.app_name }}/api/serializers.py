"""API serializers for {{ cookiecutter.app_name }}."""
from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from {{ cookiecutter.app_name }} import models


class {{ cookiecutter.model_class_name }}Serializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
