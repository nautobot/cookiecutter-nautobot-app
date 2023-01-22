"""Views for {{ cookiecutter.model_class_name }}."""

from nautobot.core.views import generic

from {{ cookiecutter.nautobot_app_name }} import filters, forms, models, tables


class {{ cookiecutter.model_class_name }}ListView(generic.ObjectListView):
    """List view."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.{{ cookiecutter.model_class_name }}FilterSet
    filterset_form = forms.{{ cookiecutter.model_class_name }}FilterForm
    table = tables.{{ cookiecutter.model_class_name }}Table

    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class {{ cookiecutter.model_class_name }}View(generic.ObjectView):
    """Detail view."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()


class {{ cookiecutter.model_class_name }}CreateView(generic.ObjectEditView):
    """Create view."""

    model = models.{{ cookiecutter.model_class_name }}
    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    model_form = forms.{{ cookiecutter.model_class_name }}Form


class {{ cookiecutter.model_class_name }}DeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.{{ cookiecutter.model_class_name }}
    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()


class {{ cookiecutter.model_class_name }}EditView(generic.ObjectEditView):
    """Edit view."""

    model = models.{{ cookiecutter.model_class_name }}
    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    model_form = forms.{{ cookiecutter.model_class_name }}Form


class {{ cookiecutter.model_class_name }}BulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more {{ cookiecutter.model_class_name }} records."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    table = tables.{{ cookiecutter.model_class_name }}Table


class {{ cookiecutter.model_class_name }}BulkEditView(generic.BulkEditView):
    """View for editing one or more {{ cookiecutter.model_class_name }} records."""

    queryset = models.{{ cookiecutter.model_class_name }}.objects.all()
    table = tables.{{ cookiecutter.model_class_name }}Table
    form = forms.{{ cookiecutter.model_class_name }}BulkEditForm
