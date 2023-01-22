"""Test {{ cookiecutter.model_class_name }}."""

from django.test import TestCase

from {{ cookiecutter.nautobot_app_name }} import models


class Test{{ cookiecutter.model_class_name }}(TestCase):
    """Test {{ cookiecutter.model_class_name }}."""

    def test_create_{{ cookiecutter.model_class_name.lower() }}_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        {{ cookiecutter.model_class_name.lower() }} = models.{{ cookiecutter.model_class_name }}.objects.create(name="Development", slug="development")
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.name, "Development")
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.description, "")
        self.assertEqual(str({{ cookiecutter.model_class_name.lower() }}), "Development")
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.slug, "development")

    def test_create_{{ cookiecutter.model_class_name.lower() }}_all_fields_success(self):
        """Create {{ cookiecutter.model_class_name }} with all fields."""
        {{ cookiecutter.model_class_name.lower() }} = models.{{ cookiecutter.model_class_name }}.objects.create(
            name="Development", slug="development", description="Development Test"
        )
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.name, "Development")
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.slug, "development")
        self.assertEqual({{ cookiecutter.model_class_name.lower() }}.description, "Development Test")
