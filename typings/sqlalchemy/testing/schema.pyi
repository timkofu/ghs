"""
This type stub file was generated by pyright.
"""

table_options = ...
def Table(*args, **kw): # -> Table:
    """A schema.Table wrapper/hook for dialect-specific tweaks."""
    ...

def Column(*args, **kw): # -> Column:
    """A schema.Column wrapper/hook for dialect-specific tweaks."""
    ...

class eq_type_affinity:
    """Helper to compare types inside of datastructures based on affinity.

    E.g.::

        eq_(
            inspect(connection).get_columns("foo"),
            [
                {
                    "name": "id",
                    "type": testing.eq_type_affinity(sqltypes.INTEGER),
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                },
                {
                    "name": "data",
                    "type": testing.eq_type_affinity(sqltypes.NullType),
                    "nullable": True,
                    "default": None,
                    "autoincrement": False,
                },
            ],
        )

    """
    def __init__(self, target) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class eq_clause_element:
    """Helper to compare SQL structures based on compare()"""
    def __init__(self, target) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


def pep435_enum(name): # -> Any:
    ...
