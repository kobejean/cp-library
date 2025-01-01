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
    import operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Reversible, TypeVar\n\nT = TypeVar('T')\ndef sufsum(iter: Reversible[T], func:\
    \ Callable[[T,T],T] = None, initial: T = None, step = 1) -> list[T]:\n    if step\
    \ == 1:\n        A = list(accumulate(reversed(iter), func, initial=initial))\n\
    \        A.reverse()\n        return A   \n    else:\n        assert step >= 2\n\
    \        if func is None:\n            func = operator.add\n        A = list(reversed(iter))\n\
    \        if initial is not None:\n            A = [initial] + A\n        for i\
    \ in range(step,len(A)):\n            A[i] = func(A[i], A[i-step])\n        A.reverse()\n\
    \        return A\n"
  code: "import cp_library.alg.iter.__header__\nimport operator\nfrom itertools import\
    \ accumulate\nfrom typing import Callable, Reversible, TypeVar\n\nT = TypeVar('T')\n\
    def sufsum(iter: Reversible[T], func: Callable[[T,T],T] = None, initial: T = None,\
    \ step = 1) -> list[T]:\n    if step == 1:\n        A = list(accumulate(reversed(iter),\
    \ func, initial=initial))\n        A.reverse()\n        return A   \n    else:\n\
    \        assert step >= 2\n        if func is None:\n            func = operator.add\n\
    \        A = list(reversed(iter))\n        if initial is not None:\n         \
    \   A = [initial] + A\n        for i in range(step,len(A)):\n            A[i]\
    \ = func(A[i], A[i-step])\n        A.reverse()\n        return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sufsum_fn.py
  requiredBy: []
  timestamp: '2025-01-01 22:39:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sufsum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sufsum_fn.py
- /library/cp_library/alg/iter/sufsum_fn.py.html
title: cp_library/alg/iter/sufsum_fn.py
---
