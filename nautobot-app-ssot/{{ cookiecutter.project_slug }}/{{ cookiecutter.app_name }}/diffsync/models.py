"""Diffsync models for {{ cookiecutter.app_name }}."""
from typing import Optional, Annotated

{% if cookiecutter.direction_of_sync == "From Nautobot" %}
from diffsync import DiffSyncModel
{% endif %}
from nautobot.dcim.models import Device
{% if cookiecutter.direction_of_sync == "To Nautobot" %}
from nautobot_ssot.contrib import CustomFieldAnnotation, NautobotModel
{% endif %}

class DiffsyncDevice({{ "NautobotModel" if cookiecutter.direction_of_sync == "To Nautobot" else "DiffSyncModel" }}):
    """DiffSync model for {{ cookiecutter.system_of_record }} devices."""

    {% if cookiecutter.direction_of_sync == "To Nautobot" %}_model = Device{% endif %}
    _modelname = "device"
    _identifiers = ("name",)
    _attributes = (
        "status__name",
        "role__name",
        "device_type__name",
        "location__name",
        "example_custom_field"
    )

    name: str
    status__name: Optional[str] = None
    role__name: Optional[str] = None
    device_type__name: Optional[str] = None
    location__name: Optional[str] = None
    ip_address: Optional[str] = None
    example_custom_field: Annotated[str, CustomFieldAnnotation(key="my_example_custom_field")]
    {% if cookiecutter.direction_of_sync == "From Nautobot" %}
    @classmethod
    def create(cls, adapter, ids, attrs):
        """Create device in {{ cookiecutter.system_of_record }}."""
        raise NotImplementedError("Device creation is not implemented.")

    def update(self, attrs):
        """Update device in {{ cookiecutter.system_of_record }}."""
        raise NotImplementedError("Device updates are not implemented.")

    def delete(self):
        """Delete device in {{ cookiecutter.system_of_record }}."""
        raise NotImplementedError("Device deletion is not implemented.")
    {% endif %}