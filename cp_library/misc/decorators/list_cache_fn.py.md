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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from functools import wraps\nfrom typing import Any, Callable, TypeVar\n\n\n\n\
    F = TypeVar('F', bound=Callable[..., Any])\n\ndef list_cache(max_size: int = 16):\n\
    \    def decorator(func: F) -> F:\n        K, V = [], []\n        @wraps(func)\n\
    \        def wrapper(arg):\n            if len(K) > max_size: return func(arg)\n\
    \            try:\n                return V[K.index(arg)]\n            except:\n\
    \                K.append(arg); V.append(result := func(arg))\n              \
    \  return result\n        return wrapper\n    return decorator\n"
  code: "import cp_library.__header__\nfrom functools import wraps\nfrom typing import\
    \ Any, Callable, TypeVar\nimport cp_library.misc.__header__\nimport cp_library.misc.decorators.__header__\n\
    \nF = TypeVar('F', bound=Callable[..., Any])\n\ndef list_cache(max_size: int =\
    \ 16):\n    def decorator(func: F) -> F:\n        K, V = [], []\n        @wraps(func)\n\
    \        def wrapper(arg):\n            if len(K) > max_size: return func(arg)\n\
    \            try:\n                return V[K.index(arg)]\n            except:\n\
    \                K.append(arg); V.append(result := func(arg))\n              \
    \  return result\n        return wrapper\n    return decorator"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/misc/decorators/list_cache_fn.py
  requiredBy: []
  timestamp: '2025-08-24 20:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/misc/decorators/list_cache_fn.py
layout: document
redirect_from:
- /library/cp_library/misc/decorators/list_cache_fn.py
- /library/cp_library/misc/decorators/list_cache_fn.py.html
title: cp_library/misc/decorators/list_cache_fn.py
---
