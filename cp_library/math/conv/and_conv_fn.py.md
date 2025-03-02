---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/superset_transform_fn.py
    title: cp_library/math/conv/superset_transform_fn.py
  _extendedRequiredBy: []
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
    import operator\nfrom typing import Callable\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n\ndef superset_transform(A: list[_T], N: int, /, op = operator.add)\
    \ -> list[_T]:\n    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n\
    \        while m < Z: A[m^b], m = op(A[m^b], A[m]), m+1|b\n    return A\n\ndef\
    \ and_conv(A: list[_T], B: list[_T], N: int,\n             mul: Callable[[_T,_T],_T]\
    \ = operator.mul,\n             sub: Callable[[_T,_T],_T] = operator.sub,\n  \
    \           add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:\n    assert\
    \ len(A) == len(B)\n    superset_transform(A, N, op=add), superset_transform(B,\
    \ N, op=add)\n    for i, b in enumerate(B): A[i] = mul(A[i], b)\n    return superset_transform(A,\
    \ N, op=sub)\n"
  code: "import cp_library.math.conv.__header__\nimport operator\nfrom typing import\
    \ Callable\nfrom cp_library.misc.typing import _T\nfrom cp_library.math.conv.superset_transform_fn\
    \ import superset_transform\n\ndef and_conv(A: list[_T], B: list[_T], N: int,\n\
    \             mul: Callable[[_T,_T],_T] = operator.mul,\n             sub: Callable[[_T,_T],_T]\
    \ = operator.sub,\n             add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:\n\
    \    assert len(A) == len(B)\n    superset_transform(A, N, op=add), superset_transform(B,\
    \ N, op=add)\n    for i, b in enumerate(B): A[i] = mul(A[i], b)\n    return superset_transform(A,\
    \ N, op=sub)\n"
  dependsOn:
  - cp_library/math/conv/superset_transform_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/and_conv_fn.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/bitwise_and_convolution.test.py
documentation_of: cp_library/math/conv/and_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/and_conv_fn.py
- /library/cp_library/math/conv/and_conv_fn.py.html
title: cp_library/math/conv/and_conv_fn.py
---
