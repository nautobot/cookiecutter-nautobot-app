"""Playwright tests for {{ cookiecutter.app_name }}. Run with `invoke playwright`."""

import unittest


def load_tests(loader, tests, pattern):  # pylint: disable=unused-argument
    """Keep `nautobot-server test` from importing this pytest-only package.

    Defined here rather than imported from `nautobot.playwright` because that module does
    not exist before Nautobot 3.3, and the unittest suite runs on older versions.
    """
    return unittest.TestSuite()
