nautobot-server nbshell <<EOF
import os
from nautobot_chatops import models

def create_access_grant(grant_type):
    access_grant_name = "MM-" + grant_type.upper()
    existing_access_grant = models.AccessGrant.objects.filter(name=access_grant_name)
    if not existing_access_grant:
        access_grant = models.AccessGrant()
        access_grant.command = "*"
        access_grant.subcommand = "*"
        access_grant.name = access_grant_name
        access_grant.grant_type = grant_type
        access_grant.value = "*"
        access_grant.validated_save()

def create_command_token(command):
    with open(f"/source/development/{command}_cmd_token.txt") as file_in:
        mm_command_token = file_in.read().strip()
    existing_command_token = models.CommandToken.objects.filter(token=mm_command_token)
    if not existing_command_token:
        command_token = models.CommandToken()
        command_token.comment = f"Token for Mattermost '{command}' command."
        command_token.platform = "mattermost"
        command_token.token = mm_command_token
        command_token.validated_save()

def create_command_tokens():
    chatbot_commands = [cmd.strip() for cmd in os.environ.get("CHATBOT_COMMANDS", "nautobot").split(",")]
    for chatbot_command in chatbot_commands:
        create_command_token(chatbot_command)

create_access_grant("organization")
create_access_grant("channel")
create_access_grant("user")
create_command_tokens()

EOF
