# Installing the App in Nautobot

Here you will find detailed instructions on how to **install** and **configure** the App within your Nautobot environment.

!!! warning "Developer Note - Remove Me!"
    Detailed instructions on installing the App. You will need to update this section based on any additional dependencies or prerequisites.

## Prerequisites

- This Nautobot App is compatible with Nautobot 1.5.7 and higher.
- Databases supported: PostgreSQL, MySQL

!!! note
    Please check the [dedicated page](compatibility_matrix.md) for a full compatibility matrix and the deprecation policy.

### Access Requirements

!!! warning "Developer Note - Remove Me!"
    What external systems (if any) it needs access to in order to work.

## Install Guide

!!! note
    Nautobot Apps can be installed manually or using Python's `pip`. See the [nautobot documentation](https://nautobot.readthedocs.io/en/latest/plugins/#install-the-package) for more details. The pip package name for this Nautobot App 
    is [`my-nautobot-app`](https://pypi.org/project/my-nautobot-app/).

This Nautobot App is available as a Python package via PyPI and can be installed with `pip`:

```shell
pip install my-nautobot-app
```

To ensure My Nautobot App is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `my-nautobot-app` package:

```shell
echo my-nautobot-app >> local_requirements.txt
```

Once installed, this Nautobot App needs to be enabled in your Nautobot configuration. The following block of code below shows the additional configuration required to be added to your `nautobot_config.py` file:

- Append `"my_nautobot_app"` to the `NAUTOBOT_APPS` list.
- Append the `"my_nautobot_app"` dictionary to the `NAUTOBOT_APPS_CONFIG` dictionary and override any defaults.

```python
# In your nautobot_config.py
NAUTOBOT_APPS = ["my_nautobot_app"]

# NAUTOBOT_APPS_CONFIG = {
#   "my_nautobot_app": {
#     ADD YOUR SETTINGS HERE
#   }
# }
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

This Nautobot App behavior can be controlled with the following list of settings:

| Key     | Example | Default | Description                          |
| ------- | ------ | -------- | ------------------------------------- |
| `enable_backup` | `True` | `True` | A boolean to represent whether or not to run backup configurations within the Nautobot App. |
| `platform_slug_map` | `{"cisco_wlc": "cisco_aireos"}` | `None` | A dictionary in which the key is the platform slug and the value is what netutils uses in any "network_os" parameter. |
| `per_feature_bar_width` | `0.15` | `0.15` | The width of the table bar within the overview report |
