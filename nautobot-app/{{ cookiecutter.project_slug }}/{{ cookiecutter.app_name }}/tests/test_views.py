"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from {{ cookiecutter.app_name }} import models
from {{ cookiecutter.app_name }}.tests import fixtures


class {{ cookiecutter.model_class_name }}ViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the {{ cookiecutter.model_class_name }} views."""

    model = models.{{ cookiecutter.model_class_name }}
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_{{ cookiecutter.model_class_name.lower() }}()
