import json
from collections import OrderedDict
from pathlib import Path

_PROJECT_PATH = Path.cwd()
_ADDONS_PATH = _PROJECT_PATH / "{{ cookiecutter.plugin_name }}"

_CONGRATS = f"""
Congratulations! Your cookie has now been baked. It is located at {_PROJECT_PATH}.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry shell
* invoke makemigrations

The file `creds.env` will be ignored by git and can be used to override default environment variables.
"""

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        (_PROJECT_PATH / "LICENSE").unlink()

    if "{{ cookiecutter.model_class_name }}" == "None":
        files_to_remove = [
            "api/__init__.py",
            "api/nested_serializers.py",
            "api/serializers.py",
            "api/urls.py",
            "api/views.py",
            "filters.py",
            "forms.py",
            "migrations/__init__.py",
            "models.py",
            "navigation.py",
            "tables.py",
            "templates/{{ cookiecutter.plugin_name }}/{{ cookiecutter.model_class_name.lower() }}.html",
            "tests/fixtures.py",
            "tests/test_api_views.py",
            "tests/test_filter_{{ cookiecutter.model_class_name.lower() }}.py",
            "tests/test_form_{{ cookiecutter.model_class_name.lower() }}.py",
            "tests/test_model_{{ cookiecutter.model_class_name.lower() }}.py",
            "tests/test_views.py",
            "urls.py",
            "views/{{ cookiecutter.model_class_name.lower() }}.py",
        ]
        for file in files_to_remove:
            (_ADDONS_PATH / file).unlink()
        folders_to_remove = [
            "api",
            "migrations",
            "templates/{{ cookiecutter.plugin_name }}",
            "templates",
            "views",
        ]
        for folder in folders_to_remove:
            (_ADDONS_PATH / folder).rmdir()

    # Persist the baked cookie parameters in-repo for future usage as a replay file or for the drift management.
    cookie = {{ cookiecutter }}
    (_PROJECT_PATH / ".cookiecutter.json").write_text(json.dumps({"cookiecutter": cookie}, indent=4) + "\n", encoding="utf-8")

    print(_CONGRATS)
