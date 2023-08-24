import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

nautobot_app_name = "{{ cookiecutter.nautobot_app_name }}"

if not re.match(MODULE_REGEX, nautobot_app_name):
    print(
        "ERROR: The Nautobot App name (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % nautobot_app_name
    )

    # Exit to cancel project
    sys.exit(1)
