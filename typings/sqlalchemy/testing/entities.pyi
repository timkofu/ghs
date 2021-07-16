"""
This type stub file was generated by pyright.
"""

_repr_stack = ...
class BasicEntity:
    def __init__(self, **kw) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


_recursion_stack = ...
class ComparableMixin:
    def __ne__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        """'Deep, sparse compare.

        Deeply compare two entities, following the non-None attributes of the
        non-persisted object, if possible.

        """
        ...
    


class ComparableEntity(ComparableMixin, BasicEntity):
    def __hash__(self) -> int:
        ...
    

