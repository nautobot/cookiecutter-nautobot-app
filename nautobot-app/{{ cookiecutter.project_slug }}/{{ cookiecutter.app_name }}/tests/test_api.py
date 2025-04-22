"""Unit tests for {{ cookiecutter.app_name }}."""

from nautobot.apps.testing import APIViewTestCases

from {{ cookiecutter.app_name }} import models


class {{ cookiecutter.model_class_name }}APIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for {{ cookiecutter.model_class_name }}."""

    model = models.{{ cookiecutter.model_class_name }}
    # Any choice fields will require the choices_fields to be set
    # to the field names in the model that are choice fields.
    choices_fields = ()

    @classmethod
    def setUpTestData(cls):
        """Create test data for {{ cookiecutter.model_class_name }} API viewset."""
        super().setUpTestData()
        # Create 3 objects for the api test cases.
        cls.create_data = [
            {
                "name": "Test One",
                "description": "Test One Description",
            },
            {
                "name": "Test Two",
                "description": "Test Two Description",
            },
            {
                "name": "Test Three",
                "description": "Test Three Description",
            },
        ]
        cls.update_data = {
            "name": "Test Two",
            "description": "Test Two Description",
        }
        cls.bulk_update_data = {
            "description": "Test Bulk Update Description",
        }
