"""Tables for {{ cookiecutter.plugin_name }}."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from {{ cookiecutter.plugin_name }} import models


class {{ cookiecutter.model_class_name }}Table(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.{{ cookiecutter.model_class_name }},
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="slug",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.{{ cookiecutter.model_class_name }}
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )
