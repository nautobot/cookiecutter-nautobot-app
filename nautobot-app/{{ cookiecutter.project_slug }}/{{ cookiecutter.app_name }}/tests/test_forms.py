"""Test {{ cookiecutter.model_class_name.lower() }} forms."""

from django.test import TestCase

from {{ cookiecutter.app_name }} import forms


class {{ cookiecutter.model_class_name }}Test(TestCase):
    """Test {{ cookiecutter.model_class_name }} forms."""

    def test_specifying_all_fields_success(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_{{ cookiecutter.model_class_name.lower() }}_is_required(self):
        form = forms.{{ cookiecutter.model_class_name }}Form(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
