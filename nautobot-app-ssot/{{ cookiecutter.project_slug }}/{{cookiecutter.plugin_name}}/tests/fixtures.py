"""Create fixtures for tests."""
from {{ cookiecutter.plugin_name }}.models import {{ cookiecutter.model_class_name }}


def create_{{ cookiecutter.model_class_name.lower() }}():
    """Fixture to create necessary number of {{ cookiecutter.model_class_name }} for tests."""
    {{ cookiecutter.model_class_name }}.objects.create(name="Test One", slug="test-one")
    {{ cookiecutter.model_class_name }}.objects.create(name="Test Two", slug="test-two")
    {{ cookiecutter.model_class_name }}.objects.create(name="Test Three", slug="test-three")
