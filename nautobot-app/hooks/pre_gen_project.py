import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

app_name = "{{ cookiecutter.app_name }}"

if not re.match(MODULE_REGEX, app_name):
    print(
        "ERROR: The app Name (%s) is not a valid Python module name. Please do not use a - and use _ instead" % app_name
    )

    # Exit to cancel project
    sys.exit(1)
