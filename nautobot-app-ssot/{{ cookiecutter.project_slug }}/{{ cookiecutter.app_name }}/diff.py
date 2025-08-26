"""Custom Diff object for {{ cookiecutter.system_of_record }} SSoT integration."""

from diffsync.diff import Diff
from diffsync.enum import DiffSyncActions


class CustomOrderingDiff(Diff):
    """Customised Diff Object, extend it to support custom ordering."""

    def get_children(self):
        """Iterate over all child elements in all groups in self.children.

        Check if a custom order method is defined, and otherwise use the default
        method.
        """
        overall_deferred_children = []

        for group in self.groups():
            group_deferred_chdrn = []

            for child in self.children[group].values():
                # Custom handling to defer deletions until last
                if child.action == DiffSyncActions.DELETE:
                    group_deferred_chdrn.append(child)
                else:
                    yield child

            # Custom handling logic for each group
            if group_deferred_chdrn:
                # Custom handling to order location deletions correctly
                if group == "location":

                    def location_depth(loc):
                        keys = loc.keys
                        depth = 0
                        if keys.get("parent__name"):
                            depth += 1
                        if keys.get("parent__parent__name"):
                            depth += 1
                        # TODO: If locations are nested deeper, extend this functionality
                        return depth

                    # Sort the locations by depth
                    group_deferred_chdrn.sort(key=location_depth)

                overall_deferred_children.extend(group_deferred_chdrn)

        # Reverse ALL deferred deletions from their natural (creation) order
        yield from reversed(overall_deferred_children)
