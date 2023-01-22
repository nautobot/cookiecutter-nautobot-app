"""Filtering for {{ cookiecutter.nautobot_app_name }}."""

from nautobot.utilities.filters import BaseFilterSet, NameSlugSearchFilterSet

from {{ cookiecutter.nautobot_app_name }} import models


class {{ cookiecutter.model_class_name }}FilterSet(BaseFilterSet, NameSlugSearchFilterSet):
    """Filter for {{ cookiecutter.model_class_name }}."""

    class Meta:
        """Meta attributes for filter."""

        model = models.{{ cookiecutter.model_class_name }}

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "slug", "description"]
