import json
from collections import OrderedDict
from pathlib import Path

_PROJECT_PATH = Path.cwd()
_ADDONS_PATH = _PROJECT_PATH / "{{ cookiecutter.app_name }}"

_CONGRATS = f"""
Congratulations! Your cookie has now been baked. It is located at {_PROJECT_PATH}.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* poetry install
* poetry self add poetry-plugin-shell
* poetry shell
* invoke makemigrations
* inv ruff --fix # this will ensure all python files are formatted correctly, may require `sudo chown -R $USER ./` as migrations may be owned by root

Note: The file `development/creds.env` may be automatically created and ignored by git. It can be used to override default environment variables within the docker containers.
"""

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        (_PROJECT_PATH / "LICENSE").unlink()

    if "No" == "{{ cookiecutter.setup_local_mattermost_dev_env }}":
        files_to_remove = [
            "development/mattermost/docker-compose.yml",
            "development/mattermost/nautobot_bootstrap.py",
            "development/mattermost/Dockerfile",
        ]
        for file in files_to_remove:
            (_ADDONS_PATH / file).unlink()

        (_ADDONS_PATH / "development/mattermost").rmdir()

    if "{{ cookiecutter.model_class_name }}" == "None":
        files_to_remove = [
            "api/__init__.py",
            "api/serializers.py",
            "api/urls.py",
            "api/views.py",
            "filters.py",
            "forms.py",
            "migrations/__init__.py",
            "models.py",
            "navigation.py",
            "tables.py",
            "templates/{{ cookiecutter.app_name }}/{{ cookiecutter.model_class_name.lower() }}_retrieve.html",
            "tests/fixtures.py",
            "tests/test_api.py",
            "tests/test_filters.py",
            "tests/test_forms.py",
            "tests/test_models.py",
            "tests/test_views.py",
            "urls.py",
            "views.py",
        ]
        for file in files_to_remove:
            (_ADDONS_PATH / file).unlink()
        folders_to_remove = [
            "api",
            "migrations",
            "templates/{{ cookiecutter.app_name }}",
            "templates",
        ]
        for folder in folders_to_remove:
            (_ADDONS_PATH / folder).rmdir()

        (_PROJECT_PATH / "docs/models/{{ cookiecutter.model_class_name.lower() }}.md").unlink()
        (_PROJECT_PATH / "docs/models").rmdir()

    # Persist the baked cookie parameters in-repo for future usage as a replay file or for the drift management.
    cookie = {{ cookiecutter }}
    (_PROJECT_PATH / ".cookiecutter.json").write_text(
        json.dumps({"cookiecutter": cookie}, indent=4) + "\n", encoding="utf-8"
    )

    print(_CONGRATS)
