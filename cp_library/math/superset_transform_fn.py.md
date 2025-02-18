---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/and_conv_fn.py
    title: cp_library/math/and_conv_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/bitwise_and_convolution.test.py
    title: test/library-checker/convolution/bitwise_and_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import TypeVar\n_T = TypeVar('T')\nimport operator\n\ndef superset_transform(A:\
    \ list[_T], N: int, Z: int = None, /, op = operator.add) -> list[_T]:\n    Z =\
    \ 1<<N\n    for i in range(N):\n        m = b = 1<<i\n        while m < Z: A[m^b],\
    \ m = op(A[m^b], A[m]), m+1|b\n    return A\n"
  code: "import cp_library.math.__header__\nfrom cp_library.misc.typing import _T\n\
    import operator\n\ndef superset_transform(A: list[_T], N: int, Z: int = None,\
    \ /, op = operator.add) -> list[_T]:\n    Z = 1<<N\n    for i in range(N):\n \
    \       m = b = 1<<i\n        while m < Z: A[m^b], m = op(A[m^b], A[m]), m+1|b\n\
    \    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/superset_transform_fn.py
  requiredBy:
  - cp_library/math/and_conv_fn.py
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_and_convolution.test.py
documentation_of: cp_library/math/superset_transform_fn.py
layout: document
redirect_from:
- /library/cp_library/math/superset_transform_fn.py
- /library/cp_library/math/superset_transform_fn.py.html
title: cp_library/math/superset_transform_fn.py
---
