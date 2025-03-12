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
    from typing import SupportsIndex\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    \ndef sum_range(A: list[_T], l: SupportsIndex, r: SupportsIndex, step: SupportsIndex\
    \ = 1, /, initial: _T = 0) -> _T:\n    for i in range(l,r,step): initial += A[i]\n\
    \    return initial\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import SupportsIndex\n\
    from cp_library.misc.typing import _T\n\ndef sum_range(A: list[_T], l: SupportsIndex,\
    \ r: SupportsIndex, step: SupportsIndex = 1, /, initial: _T = 0) -> _T:\n    for\
    \ i in range(l,r,step): initial += A[i]\n    return initial\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sum_range_fn.py
  requiredBy: []
  timestamp: '2025-03-12 22:12:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/sum_range_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sum_range_fn.py
- /library/cp_library/alg/iter/sum_range_fn.py.html
title: cp_library/alg/iter/sum_range_fn.py
---
