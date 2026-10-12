"""App-specific values the Playwright tests, fixtures and page objects share, grouped by model."""

# As reported by /api/apps/installed-apps/.
PACKAGE_NAME = "{{ cookiecutter.app_name }}"
# As shown on the Installed Apps page.
VERBOSE_NAME = "{{ cookiecutter.verbose_name }}"
{%- if cookiecutter.model_class_name != "None" %}
{%- set model_const = cookiecutter.model_class_name | camel_case_to_kebab | replace("-", "_") | upper %}

# {{ cookiecutter.model_class_name | camel_case_to_words }}
{{ model_const }}_LIST_PATH = "/plugins/{{ cookiecutter.base_url }}/{{ cookiecutter.model_class_name | camel_case_to_kebab }}s/"
{{ model_const }}_LIST_HEADING = "{{ cookiecutter.model_class_name | camel_case_to_words }}s"
{%- endif %}
