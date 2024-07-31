"""Bootstrap script for Nautobot to allow Mattermost integration."""

import contextlib
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from nautobot_chatops.models import (
    AccessGrantTypeChoices,
    PlatformChoices,
    AccessGrant,
    CommandToken,
    ChatOpsAccountLink,
)


User = get_user_model()

for grant_type in AccessGrantTypeChoices.values():
    AccessGrant.objects.update_or_create(
        command="*",
        subcommand="*",
        grant_type=grant_type,
        name="*",
        value="*",
    )

# The following tokens are for the development only and safe to store in the repo.
_COMMAND_TOKENS = {
    "clear": "u7p1an973bd1jqg75i3y7pxj7y",  # nosec
    "nautobot": "ncygprhkt3rrxr4rkytcaa7c9c",  # nosec
    "{{ cookiecutter.chatops_interactive_command }}": "fh1kbk45xtgm8r48jzr39ru1ww",  # nosec
}

for command, token in _COMMAND_TOKENS.items():
    CommandToken.objects.update_or_create(
        platform=PlatformChoices.MATTERMOST,
        comment=command,
        token=token,
    )

with contextlib.suppress(ObjectDoesNotExist):
    admin = User.objects.get(name="admin")
    ChatOpsAccountLink.objects.update_or_create(
        user_id="jactwicuqb8bu8pau8mgjydzeo",
        platform=PlatformChoices.MATTERMOST,
        defaults={"nautobot_user": admin},
    )
