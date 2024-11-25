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
  bundledCode: "\nfrom itertools import accumulate\nfrom typing import Callable, Reversible,\
    \ TypeVar\n\nT = TypeVar('T')\ndef sufsum(iter: Reversible[T], func: Callable[[T,T],T]\
    \ = None, initial: T = None) -> list[T]:\n    return list(accumulate(reversed(iter),\
    \ func, initial=initial))[::-1]\n"
  code: "import cp_library.alg.iter.__header__\nfrom itertools import accumulate\n\
    from typing import Callable, Reversible, TypeVar\n\nT = TypeVar('T')\ndef sufsum(iter:\
    \ Reversible[T], func: Callable[[T,T],T] = None, initial: T = None) -> list[T]:\n\
    \    return list(accumulate(reversed(iter), func, initial=initial))[::-1]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sufsum_fn.py
  requiredBy: []
  timestamp: '2024-11-25 19:30:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sufsum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sufsum_fn.py
- /library/cp_library/alg/iter/sufsum_fn.py.html
title: cp_library/alg/iter/sufsum_fn.py
---
