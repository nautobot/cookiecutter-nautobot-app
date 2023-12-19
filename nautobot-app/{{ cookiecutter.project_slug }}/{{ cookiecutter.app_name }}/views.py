"""Views for {{ cookiecutter.app_name }}."""
from nautobot.apps.views import NautobotUIViewSet

from {{ cookiecutter.app_name }} import filters, forms, models, tables
from {{ cookiecutter.app_name }}.api import serializers


class {{ cookiecutter.model_class_name }}UIViewSet(NautobotUIViewSet):
    """ViewSet for {{ cookiecutter.model_class_name }} views."""

    bulk_update_form_class = forms.{{ cookiecutter.model_class_name }}BulkEditForm
    filterset_class = filters.{{ cookiecutter.model_class_name }}FilterSet
    filterset_form_class = forms.{{ cookiecutter.model_class_name }}FilterForm
    form_class = forms.{{ cookiecutter.model_class_name }}Form
    lookup_field = "pk"
    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    serializer_class = serializers.{{ cookiecutter.model_class_name }}Serializer
    table_class = tables.{{ cookiecutter.model_class_name }}Table
