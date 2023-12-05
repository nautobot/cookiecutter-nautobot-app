"""Forms for {{ cookiecutter.plugin_name }}."""
from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from {{ cookiecutter.plugin_name }} import models


class {{ cookiecutter.model_class_name }}Form(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = [
            "name",
            "description",
        ]


class {{ cookiecutter.model_class_name }}BulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.{{ cookiecutter.model_class_name }}.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class {{ cookiecutter.model_class_name }}FilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.{{ cookiecutter.model_class_name }}
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
