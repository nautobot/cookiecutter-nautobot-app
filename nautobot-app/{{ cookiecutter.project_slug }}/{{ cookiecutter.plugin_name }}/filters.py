"""Filtering for {{ cookiecutter.plugin_name }}."""

from nautobot.apps.filters import NautobotFilterSet, NameSearchFilterSet

from {{ cookiecutter.plugin_name }} import models


class {{ cookiecutter.model_class_name }}FilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for {{ cookiecutter.model_class_name }}."""

    class Meta:
        """Meta attributes for filter."""

        model = models.{{ cookiecutter.model_class_name }}

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description"]
