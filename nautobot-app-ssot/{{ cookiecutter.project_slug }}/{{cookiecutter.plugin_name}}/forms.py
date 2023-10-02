"""Forms for {{ cookiecutter.plugin_name }}."""
from django import forms
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
)

from {{ cookiecutter.plugin_name }} import models


class {{ cookiecutter.model_class_name }}Form(BootstrapMixin, forms.ModelForm):
    """{{ cookiecutter.model_class_name }} creation/edit form."""

    slug = SlugField()

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = [
            "name",
            "slug",
            "description",
        ]


class {{ cookiecutter.model_class_name }}BulkEditForm(BootstrapMixin, BulkEditForm):
    """{{ cookiecutter.model_class_name }} bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.{{ cookiecutter.model_class_name }}.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class {{ cookiecutter.model_class_name }}FilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
    slug = forms.CharField(required=False, label="Slug")

    class Meta:
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
            "name",
            "slug",
            "description",
        ]
