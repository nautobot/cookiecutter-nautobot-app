"""Nautobot DiffSync models for {{ cookiecutter.system_of_record }} SSoT."""
from diffsync import DiffSyncModel

from nautobot.dcim.models import Device as NewDevice
from nautobot.dcim.models import Site, DeviceRole
from nautobot.extras.models import Status
from {{ cookiecutter.plugin_name }}.diffsync.models.base import Device


class NautobotDevice(DiffSyncModel):
    """Nautobot implementation of {{ cookiecutter.system_of_record }} Device model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in Nautobot from NautobotDevice object."""
        new_device = NewDevice(
            name=ids["name"],
            status=Status.objects.get_or_create(name=attrs["status"]),
            role=DeviceRole.objects.get_or_create(name=attrs["role"]),
            site=Site.objects.get_or_create(name=attrs["site"]),
        )
        new_device.validated_save()
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in Nautobot from NautobotDevice object."""
        device = Device.objects.get(id=attrs["uuid"])
        if "status" in attrs:
            device.status = Status.objects.get_or_create(name=attrs["status"])
        if "role" in attrs:
            device.role = DeviceRole.objects.get_or_create(name=attrs["role"])
        if "site" in attrs:
            device.site = Site.objects.get_or_create(name=attrs["site"])
        device.validated_save()
        return super().update(attrs)

    def delete(self):
        """Delete Device in Nautobot from NautobotDevice object."""
        dev = Device.objects.get(id=self.uuid)
        super().delete()
        dev.delete()
        return self
