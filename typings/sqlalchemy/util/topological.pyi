"""
This type stub file was generated by pyright.
"""

"""Topological sorting algorithms."""
def sort_as_subsets(tuples, allitems): # -> Generator[list[Unknown], None, None]:
    ...

def sort(tuples, allitems, deterministic_order=...): # -> Generator[Unknown, None, None]:
    """sort the given list of items by dependency.

    'tuples' is a list of tuples representing a partial ordering.

    deterministic_order is no longer used, the order is now always
    deterministic given the order of "allitems".    the flag is there
    for backwards compatibility with Alembic.

    """
    ...

def find_cycles(tuples, allitems): # -> set[Unknown]:
    ...
