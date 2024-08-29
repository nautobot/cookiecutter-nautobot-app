"""Nautobot DiffSync models for {{ cookiecutter.system_of_record }} SSoT."""
from diffsync import DiffSyncModel

from nautobot.dcim.models import Device as NewDevice
from nautobot.dcim.models import Site, DeviceRole, DeviceType
from nautobot.extras.models import Status
from {{ cookiecutter.plugin_name }}.diffsync.models.base import Device


class NautobotDevice(Device):
    """Nautobot implementation of {{ cookiecutter.system_of_record }} Device model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in Nautobot from NautobotDevice object."""
        new_device = NewDevice(
            name=ids["name"],
            device_type=DeviceType.objects.get_or_create(model=attrs["model"])[0],
            status=Status.objects.get_or_create(name=attrs["status"])[0],
            device_role=DeviceRole.objects.get_or_create(name=attrs["role"])[0],
            site=Site.objects.get_or_create(name=attrs["site"])[0],
        )
        new_device.validated_save()
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in Nautobot from NautobotDevice object."""
        device = NewDevice.objects.get(id=self.uuid)
        if "status" in attrs:
            device.status = Status.objects.get_or_create(name=attrs["status"])[0]
        if "role" in attrs:
            device.device_role = DeviceRole.objects.get_or_create(name=attrs["role"])[0]
        if "site" in attrs:
            device.site = Site.objects.get_or_create(name=attrs["site"])[0]
        device.validated_save()
        return super().update(attrs)

    def delete(self):
        """Delete Device in Nautobot from NautobotDevice object."""
        dev = NewDevice.objects.get(id=self.uuid)
        super().delete()
        dev.delete()
        return self