"""Test {{ cookiecutter.system_of_record }} adapter."""

import json
import uuid
from unittest.mock import MagicMock

from django.contrib.contenttypes.models import ContentType
from nautobot.extras.models import Job, JobResult
from nautobot.utilities.testing import TransactionTestCase
from {{ cookiecutter.plugin_name }}.diffsync.adapters.{{ cookiecutter.system_of_record_slug }} import {{ cookiecutter.system_of_record_camel }}Adapter
from {{ cookiecutter.plugin_name }}.jobs import {{ cookiecutter.system_of_record_camel }}DataSource


def load_json(path):
    """Load a json file."""
    with open(path, encoding="utf-8") as file:
        return json.loads(file.read())


DEVICE_FIXTURE = load_json("./{{ cookiecutter.plugin_name }}/tests/fixtures/fixtures/get_devices.json")


class Test{{ cookiecutter.system_of_record_camel }}AdapterTestCase(TransactionTestCase):
    """Test {{ cookiecutter.camel_name }}Adapter class."""

    databases = ("default", "job_logs")

    def setUp(self):
        """Initialize test case."""
        self.{{ cookiecutter.system_of_record_slug }}_client = MagicMock()
        self.{{ cookiecutter.system_of_record_slug }}_client.get_devices.return_value = DEVICE_FIXTURE

        self.job = {{ cookiecutter.system_of_record_camel }}DataSource()
        self.job.job_result = JobResult.objects.create(
            name=self.job.class_path, obj_type=ContentType.objects.get_for_model(Job), user=None, job_id=uuid.uuid4()
        )
        self.{{ cookiecutter.system_of_record_slug }} = {{ cookiecutter.system_of_record_camel }}Adapter(job=self.job, sync=None, client=self.{{ cookiecutter.system_of_record_slug }}_client)

    def test_data_loading(self):
        """Test {{ cookiecutter.verbose_name }} load() function."""
        # self.{{ cookiecutter.system_of_record_slug }}.load()
        # self.assertEqual(
        #     {dev["name"] for dev in DEVICE_FIXTURE},
        #     {dev.get_unique_id() for dev in self.{{ cookiecutter.system_of_record_slug }}.get_all("device")},
        # )
