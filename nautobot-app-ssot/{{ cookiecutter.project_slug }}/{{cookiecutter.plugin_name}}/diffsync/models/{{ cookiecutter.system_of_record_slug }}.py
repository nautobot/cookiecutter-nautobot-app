"""{{ cookiecutter.verbose_name }} DiffSync models for {{ cookiecutter.verbose_name }} SSoT."""

from {{ cookiecutter.plugin_name }}.diffsync.models.base import Device


class {{ cookiecutter.system_of_record_camel }}Device(Device):
    """{{ cookiecutter.system_of_record }} implementation of Device DiffSync model."""

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create Device in {{ cookiecutter.system_of_record }} from {{ cookiecutter.system_of_record_camel }}Device object."""
        return super().create(diffsync=diffsync, ids=ids, attrs=attrs)

    def update(self, attrs):
        """Update Device in {{ cookiecutter.system_of_record }} from {{ cookiecutter.system_of_record_camel }}Device object."""
        return super().update(attrs)

    def delete(self):
        """Delete Device in {{ cookiecutter.system_of_record }} from {{ cookiecutter.system_of_record_camel }}Device object."""
        return self
