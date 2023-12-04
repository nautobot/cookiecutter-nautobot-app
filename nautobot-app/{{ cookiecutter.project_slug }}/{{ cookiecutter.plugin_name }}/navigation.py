"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab


items = (
    NavMenuItem(
        link="plugins:{{ cookiecutter.plugin_name }}:{{ cookiecutter.model_class_name.lower() }}_list",
        name="{{ cookiecutter.verbose_name }}",
        permissions=["{{ cookiecutter.plugin_name }}.view_{{ cookiecutter.model_class_name.lower() }}"],
        buttons=(
            NavMenuAddButton(
                link="plugins:{{ cookiecutter.plugin_name }}:{{ cookiecutter.model_class_name.lower() }}_add",
                permissions=["{{ cookiecutter.plugin_name }}.add_{{ cookiecutter.model_class_name.lower() }}"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Plugins",
        groups=(NavMenuGroup(name="{{ cookiecutter.verbose_name }}", items=tuple(items)),),
    ),
)
