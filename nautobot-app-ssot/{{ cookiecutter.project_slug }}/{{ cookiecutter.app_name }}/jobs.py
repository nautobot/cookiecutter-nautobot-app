"""Jobs for {{ cookiecutter.system_of_record }} SSoT integration."""

from diffsync import DiffSyncFlags
from nautobot.extras.jobs import BooleanVar, Job
from nautobot_ssot.jobs.base import DataSource, DataTarget
from {{ cookiecutter.app_name }}.diffsync.adapters import {{ cookiecutter.system_of_record_slug }}, nautobot


name = "{{ cookiecutter.system_of_record }} SSoT"  # pylint: disable=invalid-name


class {{ cookiecutter.system_of_record_camel }}DataSource(DataSource, Job):
    """{{ cookiecutter.system_of_record }} SSoT Data Source."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

    def __init__(self):
        """Initialize {{ cookiecutter.system_of_record }} Data Source."""
        super().__init__()
        # pylint: disable-next=unsupported-binary-operation
        self.diffsync_flags = self.diffsync_flags | DiffSyncFlags.CONTINUE_ON_FAILURE

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta data for {{ cookiecutter.system_of_record }}."""

        name = "{{ cookiecutter.system_of_record }} to Nautobot"
        data_source = "{{ cookiecutter.system_of_record }}"
        data_target = "Nautobot"
        description = "Sync information from {{ cookiecutter.system_of_record }} to Nautobot"

    @classmethod
    def config_information(cls):
        """Dictionary describing the configuration of this DataSource."""
        return {}

    @classmethod
    def data_mappings(cls):
        """List describing the data mappings involved in this DataSource."""
        return ()

    def load_source_adapter(self):
        """Load data from {{ cookiecutter.system_of_record }} into DiffSync models."""
        self.source_adapter = {{ cookiecutter.system_of_record_slug }}.{{ cookiecutter.system_of_record_camel }}Adapter(job=self, sync=self.sync)
        self.source_adapter.load()

    def load_target_adapter(self):
        """Load data from Nautobot into DiffSync models."""
        self.target_adapter = nautobot.NautobotAdapter(job=self, sync=self.sync)
        self.target_adapter.load()


class {{ cookiecutter.system_of_record_camel }}DataTarget(DataTarget, Job):
    """{{ cookiecutter.system_of_record }} SSoT Data Target."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

    def __init__(self):
        """Initialize {{ cookiecutter.system_of_record }} Data Target."""
        super().__init__()
        self.diffsync_flags = int(self.diffsync_flags) | DiffSyncFlags.CONTINUE_ON_FAILURE

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta data for {{ cookiecutter.system_of_record }}."""

        name = "Nautobot to {{ cookiecutter.system_of_record }}"
        data_source = "Nautobot"
        data_target = "{{ cookiecutter.system_of_record }}"
        description = "Sync information from Nautobot to {{ cookiecutter.system_of_record }}"

    @classmethod
    def config_information(cls):
        """Dictionary describing the configuration of this DataTarget."""
        return {}

    @classmethod
    def data_mappings(cls):
        """List describing the data mappings involved in this DataSource."""
        return ()

    def load_source_adapter(self):
        """Load data from Nautobot into DiffSync models."""
        self.source_adapter = nautobot.NautobotAdapter(job=self, sync=self.sync)
        self.source_adapter.load()

    def load_target_adapter(self):
        """Load data from {{ cookiecutter.system_of_record }} into DiffSync models."""
        self.target_adapter = {{ cookiecutter.system_of_record_slug }}.{{ cookiecutter.system_of_record_camel }}Adapter(job=self, sync=self.sync)
        self.target_adapter.load()


jobs = [{{ cookiecutter.system_of_record_camel }}DataSource, {{ cookiecutter.system_of_record_camel }}DataTarget]
