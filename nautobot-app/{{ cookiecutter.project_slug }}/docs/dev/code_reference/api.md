# {{ cookiecutter.verbose_name }} API Package

{%- if cookiecutter.model_class_name != "None" %}
::: {{ cookiecutter.app_name }}.api
    options:
        show_submodules: True
{%- else %}
!!! warning "Developer Note - Remove Me!"
    This app does not expose a REST API (no model was defined).
{%- endif %}
