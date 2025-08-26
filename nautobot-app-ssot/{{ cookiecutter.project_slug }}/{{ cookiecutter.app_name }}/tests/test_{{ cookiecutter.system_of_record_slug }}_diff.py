"""Test {{ cookiecutter.system_of_record }} SSoT integration customised Diff Object."""

from unittest.mock import MagicMock

from diffsync.enum import DiffSyncActions
from nautobot.core.testing import TestCase

from {{ cookiecutter.app_name }}.jobs import CustomOrderingDiff


class TestCustomOrderingDiff(TestCase):
    """Test the CustomOrderingDiff."""

    def setUp(self):
        """Setup CustomOrderingDiff instance."""
        self.diff = CustomOrderingDiff()
        self.diff.children = {}
        self.diff.groups = MagicMock()

    def test_yields_non_delete_first_then_deletes(self):
        """Verify deletes are yielded last and reversed."""
        self.diff.groups.return_value = ["group1"]
        child1 = MagicMock()
        child1.action = DiffSyncActions.DELETE
        child2 = MagicMock()
        child2.action = DiffSyncActions.CREATE
        child3 = MagicMock()
        child3.action = DiffSyncActions.DELETE
        child4 = MagicMock()
        child4.action = DiffSyncActions.UPDATE

        self.diff.children = {"group1": {"a": child1, "b": child2, "c": child3, "d": child4}}

        results = list(self.diff.get_children())
        # Non-deletes first
        self.assertIn(child2, results[:2])
        self.assertIn(child4, results[:2])
        # Deletes at the end (in reverse order)
        self.assertEqual(results[-1], child1)
        self.assertEqual(results[-2], child3)

    def test_location_deletes_sorted_by_depth(self):
        """Verify Location deletes are correctly sorted by depth."""
        self.diff.groups.return_value = ["location"]

        def make_loc(keys):
            loc = MagicMock()
            loc.action = DiffSyncActions.DELETE
            loc.keys = keys
            return loc

        loc1 = make_loc({"parent__name": "parentA"})
        loc2 = make_loc({"parent__name": "parentA", "parent__parent__name": "grandparent"})
        loc3 = make_loc({})

        self.diff.children = {"location": {"loc1": loc1, "loc2": loc2, "loc3": loc3}}

        results = list(self.diff.get_children())

        self.assertEqual(results, [loc2, loc1, loc3])

    def test_mixed_groups(self):
        """Verify mixed groups with mixed delete and non-delete children are returned in the correct order"""
        self.diff.groups.return_value = ["group1", "location"]

        # Group1 children
        child1 = MagicMock()
        child1.action = DiffSyncActions.UPDATE
        child2 = MagicMock()
        child2.action = DiffSyncActions.DELETE

        def make_loc(keys):
            loc = MagicMock()
            loc.action = DiffSyncActions.DELETE
            loc.keys = keys
            return loc

        loc1 = make_loc({"parent__name": "p1"})
        loc2 = make_loc({})

        self.diff.children = {"group1": {"c1": child1, "c2": child2}, "location": {"l1": loc1, "l2": loc2}}

        results = list(self.diff.get_children())

        self.assertEqual(results[0], child1)
        self.assertEqual(results[-3:], [loc1, loc2, child2])
