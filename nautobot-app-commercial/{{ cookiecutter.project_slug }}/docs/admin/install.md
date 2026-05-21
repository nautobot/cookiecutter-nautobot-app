# Installing the App in Nautobot

Here you will find detailed instructions on how to **install** and **configure** the App within your Nautobot environment.

## Prerequisites

- The app is compatible with Nautobot {{ min_nautobot_version }} and higher.
- Databases supported: PostgreSQL, MySQL

!!! note
    Please check the [dedicated page](compatibility_matrix.md) for a full compatibility matrix and the deprecation policy.

### Access Requirements

!!! warning "Developer Note - Remove Me!"
    Document what external systems (if any) the App needs access to in order to work.

## Install Guide

The app is distributed as a Python package (`{{ cookiecutter.app_slug }}`) which can be installed by Python package managers (e.g. pip, poetry, uv etc.) from an authorized private repository.

!!! warning "Important"
    {{ cookiecutter.verbose_name }} is commercial (licensed) software. To obtain access to the Network To Code private package repository, please contact us through the [customer portal](https://support.networktocode.com/). Then review the [instructions](https://networktocode.atlassian.net/servicedesk/customer/portal/9/topic/741089cc-445d-458c-91b6-f8054f63edb7/article/3882057731) on how to set up the repository in your Python package manager of choice.

To ensure {{ cookiecutter.verbose_name }} is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `{{ cookiecutter.app_slug }}` package:

```shell
echo {{ cookiecutter.app_slug }} >> local_requirements.txt
```

Once installed, the app needs to be enabled in your Nautobot configuration. The following block of code below shows the additional configuration required to be added to your `nautobot_config.py` file:

- Append `"{{ cookiecutter.app_name }}"` to the `PLUGINS` list.
- Append the `"{{ cookiecutter.app_name }}"` dictionary to the `PLUGINS_CONFIG` dictionary and override any defaults.

```python
# In your nautobot_config.py
PLUGINS = ["{{ cookiecutter.app_name }}"]

PLUGINS_CONFIG = {
    "{{ cookiecutter.app_name }}": {
        # ADD YOUR SETTINGS HERE
    },
}
```

Once the Nautobot configuration is updated, run the Post Upgrade command (`nautobot-server post_upgrade`) to run migrations and clear any cache:

```shell
nautobot-server post_upgrade
```

Then restart (if necessary) the Nautobot services which may include:

- Nautobot
- Nautobot Workers
- Nautobot Scheduler

```shell
sudo systemctl restart nautobot nautobot-worker nautobot-scheduler
```

## App Configuration

!!! warning "Developer Note - Remove Me!"
    Any configuration required to get the App set up. Edit the table below as per the examples provided.

The app behavior can be controlled with the following list of settings:

| Key     | Example | Default | Description                          |
| ------- | ------ | -------- | ------------------------------------- |
| n/a | n/a | n/a | n/a |
