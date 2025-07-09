---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from functools import wraps\nfrom typing import Any, Callable, TypeVar\n\
    \nF = TypeVar('F', bound=Callable[..., Any])\n\ndef list_cache(max_size: int =\
    \ 16):\n    def decorator(func: F) -> F:\n        K, V = [], []\n        @wraps(func)\n\
    \        def wrapper(arg):\n            if len(K) > max_size: return func(arg)\n\
    \            try:\n                return V[K.index(arg)]\n            except:\n\
    \                result = func(arg)\n                K.append(arg); V.append(result)\n\
    \                return result\n        return wrapper\n    return decorator\n"
  code: "from functools import wraps\nfrom typing import Any, Callable, TypeVar\n\n\
    F = TypeVar('F', bound=Callable[..., Any])\n\ndef list_cache(max_size: int = 16):\n\
    \    def decorator(func: F) -> F:\n        K, V = [], []\n        @wraps(func)\n\
    \        def wrapper(arg):\n            if len(K) > max_size: return func(arg)\n\
    \            try:\n                return V[K.index(arg)]\n            except:\n\
    \                result = func(arg)\n                K.append(arg); V.append(result)\n\
    \                return result\n        return wrapper\n    return decorator"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/misc/decorators/list_cache_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/misc/decorators/list_cache_fn.py
layout: document
redirect_from:
- /library/cp_library/misc/decorators/list_cache_fn.py
- /library/cp_library/misc/decorators/list_cache_fn.py.html
title: cp_library/misc/decorators/list_cache_fn.py
---
