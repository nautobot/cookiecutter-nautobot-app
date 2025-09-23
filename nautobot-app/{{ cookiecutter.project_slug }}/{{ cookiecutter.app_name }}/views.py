"""Views for {{ cookiecutter.app_name }}."""

from nautobot.apps.views import NautobotUIViewSet
from nautobot.apps.ui import ObjectDetailContent, ObjectFieldsPanel, ObjectsTablePanel, SectionChoices
from nautobot.core.templatetags import helpers

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

    # Here is an example of using the UI  Component Framework for the detail view.
    # More information can be found in the Nautobot documentation:
    # https://docs.nautobot.com/projects/core/en/stable/development/core/ui-component-framework/
    object_detail_content = ObjectDetailContent(
        panels=[
            ObjectFieldsPanel(
                weight=100,
                section=SectionChoices.LEFT_HALF,
                fields="__all__",
                # Alternatively, you can specify a list of field names:
                # fields=[
                #     "name",
                #     "description",
                # ],
                # Some fields may require additional configuration, we can use value_transforms
                # value_transforms={
                #     "name": [helpers.bettertitle]
                # },
            ),
            # If there is a ForeignKey or M2M with this model we can use ObjectsTablePanel
            # to display them in a table format.
            # ObjectsTablePanel(
                # weight=200,
                # section=SectionChoices.RIGHT_HALF,
                # table_class=tables.{{ cookiecutter.model_class_name }}Table,
                # You will want to filter the table using the related_name
                # filter="{{ cookiecutter.model_class_name|lower }}s",
            # ),
        ],
    )
