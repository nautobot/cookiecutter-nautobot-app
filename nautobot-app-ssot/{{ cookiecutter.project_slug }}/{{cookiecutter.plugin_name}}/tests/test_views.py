"""Unit tests for views."""
from nautobot.utilities.testing import ViewTestCases

from {{ cookiecutter.plugin_name }} import models
from {{ cookiecutter.plugin_name }}.tests import fixtures


class {{ cookiecutter.model_class_name }}ViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the {{ cookiecutter.model_class_name }} views."""

    model = models.{{ cookiecutter.model_class_name }}
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "slug": "test-1",
        "description": "Initial model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_{{ cookiecutter.model_class_name.lower() }}()

    def test_bulk_import_objects_with_constrained_permission(self):
        """Auto-generated model does not implement `bulk_import`."""

    def test_bulk_import_objects_with_permission(self):
        """Auto-generated model does not implement `bulk_import`."""

    def test_bulk_import_objects_without_permission(self):
        """Auto-generated model does not implement `bulk_import`."""

    def test_bulk_import_objects_with_permission_csv_file(self):
        """Auto-generated model does not implement `bulk_import`."""

    def test_has_advanced_tab(self):
        """Auto-generated model does not implement an advanced tab."""
