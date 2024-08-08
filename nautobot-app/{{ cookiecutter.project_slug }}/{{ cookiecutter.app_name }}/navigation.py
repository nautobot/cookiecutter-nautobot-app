"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:{{ cookiecutter.app_name }}:{{ cookiecutter.model_class_name.lower() }}_list",
        name="{{ cookiecutter.verbose_name }}",
        permissions=["{{ cookiecutter.app_name }}.view_{{ cookiecutter.model_class_name.lower() }}"],
        buttons=(
            NavMenuAddButton(
                link="plugins:{{ cookiecutter.app_name }}:{{ cookiecutter.model_class_name.lower() }}_add",
                permissions=["{{ cookiecutter.app_name }}.add_{{ cookiecutter.model_class_name.lower() }}"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="{{ cookiecutter.verbose_name }}", items=tuple(items)),),
    ),
)
