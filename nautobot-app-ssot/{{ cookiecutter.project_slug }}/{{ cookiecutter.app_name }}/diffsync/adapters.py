"""Diffsync adapters for {{ cookiecutter.app_name }}."""

from diffsync import Adapter

from {{ cookiecutter.app_name }}.diffsync.models import DiffsyncDevice


class {{ cookiecutter.system_of_record_camel }}RemoteAdapter(Adapter):
    """DiffSync adapter for {{ cookiecutter.system_of_record }}."""

    device = DiffsyncDevice

    top_level = ["device"]

    def __init__(self, *args, job=None, sync=None, client=None, **kwargs):
        """Initialize {{ cookiecutter.system_of_record }}.

        Args:
            job (object, optional): {{ cookiecutter.system_of_record }} job. Defaults to None.
            sync (object, optional): {{ cookiecutter.system_of_record }} DiffSync. Defaults to None.
            client (object): {{ cookiecutter.system_of_record }} API client connection object.
        """
        super().__init__(*args, **kwargs)
        self.job = job
        self.sync = sync
        self.conn = client

    def load(self):
        """Load data from {{ cookiecutter.system_of_record }} into DiffSync models."""
        raise NotImplementedError()


class {{ cookiecutter.system_of_record_camel }}NautobotAdapter(NautobotAdapter):
    """DiffSync adapter for Nautobot."""

    device = NautobotDevice

    top_level = ["device"]

    {% if cookiecutter.direction_of_sync == "From Nautobot" %}
    def load(self):
        """Load data from Nautobot into DiffSync models."""
        raise NotImplementedError()
    {% endif %}
