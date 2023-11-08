"""Unit tests for {{cookiecutter.plugin_name}}."""
from nautobot.apps.testing import APIViewTestCases

from {{ cookiecutter.plugin_name }} import models
from {{ cookiecutter.plugin_name }}.tests import fixtures


class {{ cookiecutter.model_class_name }}APIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for {{ cookiecutter.model_class_name }}."""

    model = models.{{ cookiecutter.model_class_name }}
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_{{ cookiecutter.model_class_name.lower() }}()
