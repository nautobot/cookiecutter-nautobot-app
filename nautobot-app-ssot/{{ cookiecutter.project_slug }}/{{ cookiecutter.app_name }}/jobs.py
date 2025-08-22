"""Jobs for {{ cookiecutter.system_of_record }} SSoT integration."""

from nautobot.apps.jobs import BooleanVar, register_jobs
from nautobot_ssot.jobs.base import DataSource, DataTarget

from {{ cookiecutter.app_name }}.diff import CustomOrderingDiff
from {{ cookiecutter.app_name }}.diffsync.adapters import {{ cookiecutter.system_of_record_camel }}RemoteAdapter, {{ cookiecutter.system_of_record_camel }}NautobotAdapter

name = "{{ cookiecutter.system_of_record }} SSoT"  # pylint: disable=invalid-name


class {{ cookiecutter.system_of_record_camel }}DataSource(DataSource):
    """{{ cookiecutter.system_of_record }} SSoT Data Source."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

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

    def run(self, dryrun, memory_profiling, debug, *args, **kwargs):  # pylint: disable=arguments-differ
        """Perform data synchronization."""
        self.debug = debug
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun=self.dryrun, memory_profiling=self.memory_profiling, *args, **kwargs)


class {{ cookiecutter.system_of_record_camel }}DataTarget(DataTarget):
    """{{ cookiecutter.system_of_record }} SSoT Data Target."""

    debug = BooleanVar(description="Enable for more verbose debug logging", default=False)

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

    def run(self, dryrun, memory_profiling, debug, *args, **kwargs):  # pylint: disable=arguments-differ
        """Perform data synchronization."""
        self.debug = debug
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun=self.dryrun, memory_profiling=self.memory_profiling, *args, **kwargs)

    def execute_sync(self):
        """Method to synchronize the difference from `self.diff`, from SOURCE to TARGET adapter.

        Overridden to use a CustomOrderingDiff diff_class.
        """
        if self.source_adapter is not None and self.target_adapter is not None:
            self.source_adapter.sync_to(self.target_adapter, flags=self.diffsync_flags, diff_class=CustomOrderingDiff)
        else:
            self.logger.warning("One of the adapters was not properly initialized prior to synchronization.")


jobs = [{{ cookiecutter.system_of_record_camel }}DataSource, {{ cookiecutter.system_of_record_camel }}DataTarget]
register_jobs(*jobs)
