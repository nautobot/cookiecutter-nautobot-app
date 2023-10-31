"""Test {{ cookiecutter.system_of_record }} adapter."""

import json
from unittest.mock import MagicMock

from nautobot.extras.models import JobResult
from nautobot.core.testing import TransactionTestCase
from {{ cookiecutter.plugin_name }}.diffsync.adapters.{{ cookiecutter.system_of_record_slug }} import {{ cookiecutter.system_of_record_camel }}Adapter
from {{ cookiecutter.plugin_name }}.jobs import {{ cookiecutter.system_of_record_camel }}DataSource


def load_json(path):
    """Load a json file."""
    with open(path, encoding="utf-8") as file:
        return json.loads(file.read())


DEVICE_FIXTURE = load_json("./{{ cookiecutter.plugin_name }}/tests/fixtures/get_devices.json")


class Test{{ cookiecutter.system_of_record_camel }}AdapterTestCase(TransactionTestCase):
    """Test {{ cookiecutter.camel_name }}Adapter class."""

    job_class = {{ cookiecutter.system_of_record_camel }}DataSource
    databases = ("default", "job_logs")

    def setUp(self):
        """Initialize test case."""
        self.{{ cookiecutter.system_of_record_slug }}_client = MagicMock()
        self.{{ cookiecutter.system_of_record_slug }}_client.get_devices.return_value = DEVICE_FIXTURE

        self.job = self.job_class()
        self.job.job_result = JobResult.objects.create(
            name=self.job.class_path, task_name="fake task", worker="default"
        )
        self.{{ cookiecutter.system_of_record_slug }} = {{ cookiecutter.system_of_record_camel }}Adapter(job=self.job, sync=None, client=self.{{ cookiecutter.system_of_record_slug }}_client)

    def test_data_loading(self):
        """Test {{ cookiecutter.verbose_name }} load() function."""
        # self.{{ cookiecutter.system_of_record_slug }}.load()
        # self.assertEqual(
        #     {dev["name"] for dev in DEVICE_FIXTURE},
        #     {dev.get_unique_id() for dev in self.{{ cookiecutter.system_of_record_slug }}.get_all("device")},
        # )
