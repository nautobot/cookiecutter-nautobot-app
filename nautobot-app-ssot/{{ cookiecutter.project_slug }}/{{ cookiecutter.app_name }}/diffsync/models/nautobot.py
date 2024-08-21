"""Nautobot DiffSync models for {{ cookiecutter.system_of_record }} SSoT."""

from django.contrib.contenttypes.models import ContentType

from nautobot.dcim.models import Device as NewDevice, Location, LocationType, DeviceType
from nautobot.extras.models import Status, Role
from {{ cookiecutter.app_name }}.diffsync.models.base import Device


def ensure_location(location_name):
    """Safely returns a Location with a LocationType that support Devices."""
    location_type, _ = LocationType.objects.get_or_create(name="Site")
    content_type = ContentType.objects.get_for_model(NewDevice)
    location_type.content_types.add(content_type)
    status = Status.objects.get(name="Active")
    return Location.objects.get_or_create(name=location_name, location_type=location_type, status=status)[0]


def ensure_role(role_name):
    """Safely returns a Role that support Devices."""
    content_type = ContentType.objects.get_for_model(NewDevice)
    role, _ = Role.objects.get_or_create(name=role_name)
    role.content_types.add(content_type)
    return role


class NautobotDevice(Device):
    """Nautobot implementation of {{ cookiecutter.system_of_record }} Device model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in Nautobot from NautobotDevice object."""
        new_device = NewDevice(
            name=ids["name"],
            device_type=DeviceType.objects.get_or_create(model=attrs["model"])[0],
            status=Status.objects.get_or_create(name=attrs["status"])[0],
            role=ensure_role(attrs["role"]),
            location=ensure_location(attrs["location"]),
        )
        new_device.validated_save()
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in Nautobot from NautobotDevice object."""
        device = NewDevice.objects.get(id=self.uuid)
        if "status" in attrs:
            device.status = Status.objects.get_or_create(name=attrs["status"])[0]
        if "role" in attrs:
            device.role = ensure_role(attrs["role"])
        if "location" in attrs:
            device.location = ensure_location(attrs["location"])
        device.validated_save()
        return super().update(attrs)

    def delete(self):
        """Delete Device in Nautobot from NautobotDevice object."""
        dev = NewDevice.objects.get(id=self.uuid)
        super().delete()
        dev.delete()
        return self
