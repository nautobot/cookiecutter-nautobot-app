"""Menu items."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:{{ cookiecutter.plugin_name }}:{{ cookiecutter.model_class_name.lower() }}_list",
        link_text="{{ cookiecutter.verbose_name }}",
        permissions=["{{ cookiecutter.plugin_name }}.view_{{ cookiecutter.model_class_name.lower() }}"],
        buttons=(
            PluginMenuButton(
                link="plugins:{{ cookiecutter.plugin_name }}:{{ cookiecutter.model_class_name.lower() }}_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["{{ cookiecutter.plugin_name }}.add_{{ cookiecutter.model_class_name.lower() }}"],
            ),
        ),
    ),
)
