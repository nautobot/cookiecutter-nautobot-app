import os
import shutil

from cookiecutter.config import get_user_config

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ADDONS_DIR = f"{PROJECT_DIRECTORY}/{{ cookiecutter.nautobot_app_name }}/"
USER_CONFIG = get_user_config()


def remove_file(directory, filepath):
    """
    Remove a file from the project directory.

    >>> remove_file('./api/', 'text.txt')
    # It will delete './api/text.txt' from project dir

    Args:
        directory (str): base directory path
        filepath (str): file path within the base directory
    """
    os.remove(os.path.join(directory, filepath))


CONGRATS = f"""
Congratulations! Your cookie has now been baked. It is located at {PROJECT_DIRECTORY}.

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry shell
* invoke makemigrations

The file "creds.env will be ignored by git and can be used to override default environment variables.
"""


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file(PROJECT_DIRECTORY, "LICENSE")

    if "{{ cookiecutter.model_class_name }}" == "None":
        files_to_remove = [
            "api/nested_serializers.py",
            "api/serializers.py",
            "api/urls.py",
            "api/views.py",
            "filters.py",
            "forms.py",
            "models.py",
            "navigation.py",
            "tables.py",
            "templates/{{ cookiecutter.nautobot_app_name }}/{{ cookiecutter.model_class_name.lower() }}.html",
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
            remove_file(ADDONS_DIR, file)

    # Persist the baked cookie parameters in-repo for future usage as a replay file.
    shutil.copy(
        os.path.join(USER_CONFIG["replay_dir"], "nautobot-app.json"),
        f"{PROJECT_DIRECTORY}/.cookiecutter.json",
    )

    print(CONGRATS)
