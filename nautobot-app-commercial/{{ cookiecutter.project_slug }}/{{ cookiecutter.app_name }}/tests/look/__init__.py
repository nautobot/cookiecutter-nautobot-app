"""The page report behind `invoke playwright --look`. Not a test suite; pytest reaches it only by explicit path."""

import unittest


def load_tests(loader, tests, pattern):  # pylint: disable=unused-argument
    """Keep `nautobot-server test` from importing this pytest-only package."""
    return unittest.TestSuite()
