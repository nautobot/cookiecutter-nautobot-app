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
    status: Optional[str] = None
    role: Optional[str] = None
    model: Optional[str] = None
    location: Optional[str] = None
    ip_address: Optional[str] = None

    uuid: Optional[UUID] = None
