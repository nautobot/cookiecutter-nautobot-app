"""Unit tests for {{ cookiecutter.verbose_name }}."""
from nautobot.utilities.testing import APIViewTestCases

from {{ cookiecutter.nautobot_app_name }} import models
from {{ cookiecutter.nautobot_app_name }}.tests import fixtures


class {{ cookiecutter.model_class_name }}APIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for {{ cookiecutter.model_class_name }}."""

    model = models.{{ cookiecutter.model_class_name }}
    create_data = [
        {
            "name": "Test Model 1",
            "slug": "test-model-1",
        },
        {
            "name": "Test Model 2",
            "slug": "test-model-2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}
    brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

    @classmethod
    def setUpTestData(cls):
        fixtures.create_{{ cookiecutter.model_class_name.lower() }}()
