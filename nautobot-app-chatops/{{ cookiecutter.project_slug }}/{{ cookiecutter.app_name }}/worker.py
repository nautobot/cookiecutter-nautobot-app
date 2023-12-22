"""Worker functions implementing Nautobot "{{ cookiecutter.chatops_interactive_command }}" command and subcommands."""

from django.conf import settings

from nautobot_chatops.workers.base import subcommand_of, handle_subcommands
from .{{ cookiecutter.chatops_interactive_command }} import {{ cookiecutter.camel_name }}


# Import config vars from nautobot_config.py
EXAMPLE_VAR = settings.PLUGINS_CONFIG["{{ cookiecutter.app_name }}"].get("example_var")


def {{ cookiecutter.chatops_interactive_command }}(subcommand, **kwargs):
    """Interact with {{ cookiecutter.chatops_interactive_command }} app."""
    return handle_subcommands("{{ cookiecutter.chatops_interactive_command }}", subcommand, **kwargs)


@subcommand_of("{{ cookiecutter.chatops_interactive_command }}")
def hello_world(dispatcher, arg1):
    """Run logic and return to user via client command '/{{ cookiecutter.chatops_interactive_command }} hello-world arg1'."""
    dispatcher.send_markdown(f"Command /{{ cookiecutter.chatops_interactive_command }} hello-world received with arg1={arg1}")

    # Creating an instance of {{cookiecutter.camel_name}} for pylint
    {{cookiecutter.camel_name}}()

    # Logic/external API calls go here

    # Send Markdown formatted text
    # dispatcher.send_markdown(f"Markdown formatted text goes here.")

    # Send block of text
    # dispatcher.send_blocks(
    #     [
    #         *dispatcher.command_response_header(
    #             "{{ cookiecutter.chatops_interactive_command }}", "hello-world",
    #         ),
    #         dispatcher.markdown_block(f"example-return-string"),
    #     ]
    # )

    # Send large table
    # dispatcher.send_large_table(
    #     ["Name", "Description"],
    #     ["name1", "description1"],
    # )
    return True
