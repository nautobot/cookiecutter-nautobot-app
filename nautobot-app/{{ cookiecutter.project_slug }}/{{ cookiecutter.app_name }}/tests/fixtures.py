"""Create fixtures for tests."""
from {{ cookiecutter.app_name }}.models import {{ cookiecutter.model_class_name }}


def create_{{ cookiecutter.model_class_name.lower() }}():
    """Fixture to create necessary number of {{ cookiecutter.model_class_name }} for tests."""
    {{ cookiecutter.model_class_name }}.objects.create(name="Test One")
    {{ cookiecutter.model_class_name }}.objects.create(name="Test Two")
    {{ cookiecutter.model_class_name }}.objects.create(name="Test Three")
