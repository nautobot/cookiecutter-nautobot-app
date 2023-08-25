"""Models for {{ cookiecutter.verbose_name }}."""

# Django imports
from django.db import models
from django.urls import reverse

# Nautobot imports
from nautobot.core.models import BaseModel
from nautobot.extras.models.change_logging import ChangeLoggedModel


# from nautobot.extras.utils import extras_features
# If you want to use the extras_features decorator please reference the following documentation
# https://nautobot.readthedocs.io/en/latest/plugins/development/#using-the-extras_features-decorator-for-graphql
# Then based on your reading you may decide to put the following decorator before the declaration of your class
# @extras_features("custom_fields", "custom_validators", "relationships", "graphql")

# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://nautobot.readthedocs.io/en/stable/plugins/development/#database-models
class {{ cookiecutter.model_class_name }}(BaseModel, ChangeLoggedModel):
    """Base model for {{ cookiecutter.verbose_name }} plugin."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # additional model fields

    class Meta:
        """Meta class."""

        ordering = ["name"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "{{ cookiecutter.verbose_name }}"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "{{ cookiecutter.verbose_name }}s"

    def get_absolute_url(self):
        """Return detail view for {{ cookiecutter.model_class_name }}."""
        return reverse("plugins:{{ cookiecutter.plugin_name }}:{{ cookiecutter.model_class_name.lower() }}", args=[self.slug])

    def __str__(self):
        """Stringify instance."""
        return self.name
