# Upgrading the App

This page describes how to upgrade this app in an existing Nautobot installation.

## Upgrade Guide

1. Read the [Release Notes](release_notes/index.md) for every version between your version and the new one. Check for breaking changes and new requirements.
2. Check the [Compatibility Matrix](compatibility_matrix.md). Make sure that the new version supports your Nautobot version.
3. Back up the Nautobot database.
4. Upgrade the package:

    ```shell
    pip install --upgrade {{ cookiecutter.app_slug }}
    ```

5. Apply the database migrations and clear the cache:

    ```shell
    nautobot-server post_upgrade
    ```

6. Restart the Nautobot services:

    ```shell
    sudo systemctl restart nautobot nautobot-worker nautobot-scheduler
    ```
