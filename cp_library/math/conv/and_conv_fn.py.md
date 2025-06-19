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
    \nimport operator\nfrom typing import Callable\nfrom typing import TypeVar\n_T\
    \ = TypeVar('T')\n_U = TypeVar('U')\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n                \u2573         \
    \ \u2572 \u2571          \u2572     \u2571          \n    x\u2084 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2081\n             \
    \              \u2573 \u2573          \u2572 \u2572 \u2571 \u2571          \n\
    \    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2573\
    \u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2082\n                \u2573          \u2571 \u2572          \u2572 \u2573\
    \ \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2083\n                                        \u2573\
    \ \u2573 \u2573 \u2573         \n    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2084\n                \u2573          \u2572\
    \ \u2571          \u2571 \u2573 \u2573 \u2572          \n    x\u2085 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2085\n             \
    \              \u2573 \u2573          \u2571 \u2571 \u2572 \u2572          \n\
    \    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2500\
    \u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2086\n                \u2573          \u2571 \u2572          \u2571     \u2572\
    \          \n    x\u2087 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                      Math - Convolution                     \n\
    '''\n\ndef superset_transform(A: list[_T], N: int, /, op = operator.add) -> list[_T]:\n\
    \    Z = len(A)\n    for i in range(N):\n        m = b = 1<<i\n        while m\
    \ < Z: A[m^b], m = op(A[m^b], A[m]), m+1|b\n    return A\n\ndef and_conv(A: list[_T],\
    \ B: list[_T], N: int,\n             mul: Callable[[_T,_T],_T] = operator.mul,\n\
    \             sub: Callable[[_T,_T],_T] = operator.sub,\n             add: Callable[[_T,_T],_T]\
    \ = operator.add) -> list[_T]:\n    assert len(A) == len(B)\n    superset_transform(A,\
    \ N, op=add), superset_transform(B, N, op=add)\n    for i, b in enumerate(B):\
    \ A[i] = mul(A[i], b)\n    return superset_transform(A, N, op=sub)\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport operator\n\
    from typing import Callable\nfrom cp_library.misc.typing import _T\nimport cp_library.math.conv.__header__\n\
    from cp_library.math.conv.superset_transform_fn import superset_transform\n\n\
    def and_conv(A: list[_T], B: list[_T], N: int,\n             mul: Callable[[_T,_T],_T]\
    \ = operator.mul,\n             sub: Callable[[_T,_T],_T] = operator.sub,\n  \
    \           add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:\n    assert\
    \ len(A) == len(B)\n    superset_transform(A, N, op=add), superset_transform(B,\
    \ N, op=add)\n    for i, b in enumerate(B): A[i] = mul(A[i], b)\n    return superset_transform(A,\
    \ N, op=sub)\n"
  dependsOn:
  - cp_library/math/conv/superset_transform_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/and_conv_fn.py
  requiredBy: []
  timestamp: '2025-06-20 03:24:59+09:00'
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
