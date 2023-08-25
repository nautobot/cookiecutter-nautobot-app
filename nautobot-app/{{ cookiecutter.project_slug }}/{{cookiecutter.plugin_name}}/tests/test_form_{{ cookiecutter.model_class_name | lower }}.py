"""Test {{ cookiecutter.model_class_name.lower() }} forms."""
from django.test import TestCase

from {{ cookiecutter.plugin_name }} import forms


class {{ cookiecutter.model_class_name }}Test(TestCase):
    """Test {{ cookiecutter.model_class_name }} forms."""

    def test_specifying_all_fields_success(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(
            data={
                "name": "Development",
                "slug": "development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(
            data={
                "name": "Development",
                "slug": "development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_{{ cookiecutter.model_class_name.lower() }}_is_required(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(data={"slug": "development"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])

    def test_validate_slug_is_required(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(data={"name": "Development"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["slug"])
