"""Nautobot Adapter for {{ cookiecutter.system_of_record }} SSoT app."""

from diffsync import DiffSync
from {{ cookiecutter.app_name }}.diffsync.models.nautobot import NautobotDevice


class NautobotAdapter(DiffSync):
    """DiffSync adapter for Nautobot."""

    device = NautobotDevice

    top_level = ["device"]

    def __init__(self, *args, job=None, sync=None, **kwargs):
        """Initialize Nautobot.

        Args:
            job (object, optional): Nautobot job. Defaults to None.
            sync (object, optional): Nautobot DiffSync. Defaults to None.
        """
        super().__init__(*args, **kwargs)
        self.job = job
        self.sync = sync

    def load(self):
        """Load data from Nautobot into DiffSync models."""
        raise NotImplementedError
