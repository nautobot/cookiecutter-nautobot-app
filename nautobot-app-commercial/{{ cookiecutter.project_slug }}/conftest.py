"""Registers Nautobot's Playwright fixtures. pytest reads `pytest_plugins` only from the rootdir conftest."""

pytest_plugins = ["nautobot.playwright.fixtures"]
