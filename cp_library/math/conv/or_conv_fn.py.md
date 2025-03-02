---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/math/conv/subset_transform_fn.py
    title: cp_library/math/conv/subset_transform_fn.py
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
    from typing import TypeVar\n_T = TypeVar('T')\nimport operator\n\ndef subset_transform(A:\
    \ list[_T], N: int, /, op = operator.add) -> list[_T]:\n    Z = len(A)\n    for\
    \ i in range(N):\n        m = b = 1<<i\n        while m < Z: A[m], m = op(A[m],\
    \ A[m^b]), m+1|b\n    return A\nfrom typing import Callable\n\ndef or_conv(A:\
    \ list[_T], B: list[_T], N: int,\n            mul: Callable[[_T,_T],_T] = operator.mul,\n\
    \            sub: Callable[[_T,_T],_T] = operator.sub,\n            add: Callable[[_T,_T],_T]\
    \ = operator.add) -> list[_T]:\n    assert len(A) == len(B)\n    subset_transform(A,\
    \ N, op=add), subset_transform(B, N, op=add)\n    for i, b in enumerate(B): A[i]\
    \ = mul(A[i], b)\n    return subset_transform(A, N, op=sub)\n"
  code: "import cp_library.math.conv.__header__\nfrom cp_library.math.conv.subset_transform_fn\
    \ import subset_transform\nimport operator\nfrom typing import Callable\nfrom\
    \ cp_library.misc.typing import _T\n\ndef or_conv(A: list[_T], B: list[_T], N:\
    \ int,\n            mul: Callable[[_T,_T],_T] = operator.mul,\n            sub:\
    \ Callable[[_T,_T],_T] = operator.sub,\n            add: Callable[[_T,_T],_T]\
    \ = operator.add) -> list[_T]:\n    assert len(A) == len(B)\n    subset_transform(A,\
    \ N, op=add), subset_transform(B, N, op=add)\n    for i, b in enumerate(B): A[i]\
    \ = mul(A[i], b)\n    return subset_transform(A, N, op=sub)\n"
  dependsOn:
  - cp_library/math/conv/subset_transform_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/or_conv_fn.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/or_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/or_conv_fn.py
- /library/cp_library/math/conv/or_conv_fn.py.html
title: cp_library/math/conv/or_conv_fn.py
---
