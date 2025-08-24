import cp_library.__header__
from functools import wraps
from typing import Any, Callable, TypeVar
import cp_library.misc.__header__
import cp_library.misc.decorators.__header__

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
                K.append(arg); V.append(result := func(arg))
                return result
        return wrapper
    return decorator