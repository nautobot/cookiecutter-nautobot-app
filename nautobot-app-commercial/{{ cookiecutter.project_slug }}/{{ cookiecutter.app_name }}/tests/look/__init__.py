"""The page report for `invoke playwright --look`. Not a test suite; pytest collects it only from an explicit path."""

import unittest


def load_tests(loader, tests, pattern):  # pylint: disable=unused-argument
    """Keep `nautobot-server test` from importing this pytest-only package."""
    return unittest.TestSuite()
