"""
This type stub file was generated by pyright.
"""

import abc

class ReversibleProxy:
    _proxy_objects = ...


class StartableContext(abc.ABC):
    @abc.abstractmethod
    async def start(self, is_ctxmanager=...): # -> None:
        ...
    
    def __await__(self): # -> Generator[Any, None, None]:
        ...
    
    async def __aenter__(self): # -> None:
        ...
    
    @abc.abstractmethod
    async def __aexit__(self, type_, value, traceback): # -> None:
        ...
    


class ProxyComparable(ReversibleProxy):
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    

