"""Forms for {{ cookiecutter.app_name }}."""

from django import forms
from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from {{ cookiecutter.app_name }} import models


class {{ cookiecutter.model_class_name }}Form(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = "__all__"


class {{ cookiecutter.model_class_name }}BulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """{{ cookiecutter.model_class_name }} bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.{{ cookiecutter.model_class_name }}.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False, max_length=CHARFIELD_MAX_LENGTH)

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
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
