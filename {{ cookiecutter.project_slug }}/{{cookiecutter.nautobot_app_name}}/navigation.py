"""Menu items."""

from nautobot.apps.ui import ButtonColorChoices, NavMenuButton, NavMenuItem


menu_items = (
    NavMenuItem(
        link="plugins:{{ cookiecutter.nautobot_app_name }}:{{ cookiecutter.model_class_name.lower() }}_list",
        link_text="{{ cookiecutter.verbose_name }}",
        buttons=(
            Na vMenuButton(
                link="plugins:{{ cookiecutter.nautobot_app_name }}:{{ cookiecutter.model_class_name.lower() }}_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["{{ cookiecutter.nautobot_app_name }}.add_{{ cookiecutter.model_class_name.lower() }}"],
            ),
        ),
    ),
)
