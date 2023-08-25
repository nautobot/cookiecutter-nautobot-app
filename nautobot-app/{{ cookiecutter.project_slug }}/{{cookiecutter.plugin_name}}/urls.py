"""Django urlpatterns declaration for {{cookiecutter.plugin_name}} plugin."""
from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from {{ cookiecutter.plugin_name }} import models
from {{ cookiecutter.plugin_name }}.views import {{ cookiecutter.model_class_name.lower() }}

urlpatterns = [
    # {{ cookiecutter.model_class_name }} URLs
    path("{{ cookiecutter.model_class_name | lower }}/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}ListView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path("{{ cookiecutter.model_class_name | lower }}/add/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}CreateView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_add"),
    path("{{ cookiecutter.model_class_name | lower }}/delete/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}BulkDeleteView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_bulk_delete"),
    path("{{ cookiecutter.model_class_name | lower }}/edit/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}BulkEditView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_bulk_edit"),
    path("{{ cookiecutter.model_class_name | lower }}/<slug:slug>/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}View.as_view(), name="{{ cookiecutter.model_class_name.lower() }}"),
    path("{{ cookiecutter.model_class_name | lower }}/<slug:slug>/delete/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}DeleteView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_delete"),
    path("{{ cookiecutter.model_class_name | lower }}/<slug:slug>/edit/", {{ cookiecutter.model_class_name.lower() }}.{{ cookiecutter.model_class_name }}EditView.as_view(), name="{{ cookiecutter.model_class_name.lower() }}_edit"),
    path(
        "{{ cookiecutter.model_class_name | lower }}/<slug:slug>/changelog/",
        ObjectChangeLogView.as_view(),
        name="{{ cookiecutter.model_class_name.lower() }}_changelog",
        kwargs={"model": models.{{ cookiecutter.model_class_name }}},
    ),
]
