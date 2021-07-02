"""
This type stub file was generated by pyright.
"""

Type = ...
Attribute = ...
ServerVersion = ...
class Range:
    """Immutable representation of PostgreSQL `range` type."""
    __slots__ = ...
    def __init__(self, lower=..., upper=..., *, lower_inc=..., upper_inc=..., empty=...) -> None:
        ...
    
    @property
    def lower(self): # -> None:
        ...
    
    @property
    def lower_inc(self): # -> Literal[False]:
        ...
    
    @property
    def lower_inf(self): # -> bool:
        ...
    
    @property
    def upper(self): # -> None:
        ...
    
    @property
    def upper_inc(self): # -> Literal[False]:
        ...
    
    @property
    def upper_inf(self): # -> bool:
        ...
    
    @property
    def isempty(self):
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    __str__ = ...

