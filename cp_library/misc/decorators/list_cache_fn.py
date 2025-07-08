from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def list_cache(max_size: int = 16):
    def decorator(func: F) -> F:
        K, V = [], []
        @wraps(func)
        def wrapper(arg):
            if len(K) > max_size: return func(arg)
            try:
                return V[K.index(arg)]
            except:
                result = func(arg)
                K.append(arg); V.append(result)
                return result
        return wrapper
    return decorator