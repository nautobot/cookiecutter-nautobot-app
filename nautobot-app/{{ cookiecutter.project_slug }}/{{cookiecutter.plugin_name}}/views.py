"""Views for {{ cookiecutter.plugin_name }}."""
from nautobot.apps.viewsets import NautobotUIViewSet

from {{ cookiecutter.plugin_name }} import filters, forms, models, tables
from {{ cookiecutter.plugin_name }}.api import serializers


class {{ cookiecutter.model_class_name}}UIViewSet(NautobotUIViewSet):
    """ViewSet for {{ cookiecutter.model_class_name}} views."""

    bulk_update_form_class = forms.{{ cookiecutter.model_class_name}}BulkEditForm
    filterset_class = filters.{{ cookiecutter.model_class_name}}FilterSet
    filterset_form_class = forms.{{ cookiecutter.model_class_name}}FilterForm
    form_class = forms.{{ cookiecutter.model_class_name}}Form
    lookup_field = "pk"
    queryset = models.{{ cookiecutter.model_class_name}}.objects.all()
    serializer_class = serializers.{{ cookiecutter.model_class_name}}Serializer
    table_class = tables.{{ cookiecutter.model_class_name}}Table
