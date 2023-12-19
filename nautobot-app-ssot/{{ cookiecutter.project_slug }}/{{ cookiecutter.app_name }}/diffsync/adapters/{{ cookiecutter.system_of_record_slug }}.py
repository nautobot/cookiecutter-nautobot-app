"""{{ cookiecutter.verbose_name }} Adapter for {{ cookiecutter.system_of_record }} SSoT app."""

from diffsync import DiffSync
from {{ cookiecutter.app_name }}.diffsync.models.{{ cookiecutter.system_of_record_slug }} import {{ cookiecutter.system_of_record_camel }}Device


class {{ cookiecutter.system_of_record_camel }}Adapter(DiffSync):
    """DiffSync adapter for {{ cookiecutter.system_of_record }}."""

    device = {{ cookiecutter.system_of_record_camel }}Device

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
        raise NotImplementedError
