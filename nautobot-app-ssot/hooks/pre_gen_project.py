import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

plugin_name = "{{ cookiecutter.plugin_name }}"

if not re.match(MODULE_REGEX, plugin_name):
    print(
        "ERROR: The plugin Name (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % plugin_name
    )

    # Exit to cancel project
    sys.exit(1)
