"""Test {{ cookiecutter.model_class_name }} Filter."""

from nautobot.apps.testing import FilterTestCases

from {{ cookiecutter.app_name }} import filters, models
from {{ cookiecutter.app_name }}.tests import fixtures


class {{ cookiecutter.model_class_name }}FilterTestCase(FilterTestCases.FilterTestCase):
    """{{ cookiecutter.model_class_name }} Filter Test Case."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    filterset = filters.{{ cookiecutter.model_class_name }}FilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for {{ cookiecutter.model_class_name }} Model."""
        fixtures.create_{{ cookiecutter.model_class_name.lower() }}()

    def test_q_search_name(self):
        """Test using Q search with name of {{ cookiecutter.model_class_name }}."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for {{ cookiecutter.model_class_name }}."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
