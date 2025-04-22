"""Filtering for {{ cookiecutter.app_name }}."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from {{ cookiecutter.app_name }} import models


class {{ cookiecutter.model_class_name }}FilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for {{ cookiecutter.model_class_name }}."""

    class Meta:
        """Meta attributes for filter."""

        model = models.{{ cookiecutter.model_class_name }}

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
