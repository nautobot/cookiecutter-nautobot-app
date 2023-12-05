"""DiffSyncModel subclasses for Nautobot-to-{{ cookiecutter.system_of_record }} data sync."""
from typing import Optional
from uuid import UUID
from diffsync import DiffSyncModel


class Device(DiffSyncModel):
    """DiffSync model for {{ cookiecutter.system_of_record }} devices."""

    _modelname = "device"
    _identifiers = ("name",)
    _attributes = (
        "status",
        "role",
        "model",
        "location",
        "ip_address",
    )
    _children = {}

    name: str
    status: Optional[str]
    role: Optional[str]
    model: Optional[str]
    location: Optional[str]
    ip_address: Optional[str]

    uuid: Optional[UUID]
