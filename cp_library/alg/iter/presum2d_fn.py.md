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
    import operator\nfrom typing import Callable\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n\ndef presum2d(A: list[list[_T]], op: Callable[[_T,_T],_T] = operator.add,\
    \ initial: _T = None, step = 1) -> list[_T]:\n    if initial is None:\n      \
    \  N, M, B = len(A), len(A[0]), [Ai[:] for Ai in A]\n    else:\n        N, M,\
    \ B = len(A)+1, len(A[0])+1, [[initial]*M for _ in range(N)]\n        for i in\
    \ range(1,N):\n            for j in range(1,M):\n                B[i][j] = A[i-1][j-1]\n\
    \    for i in range(N-step):\n        for j in range(M):\n            B[i+step][j]\
    \ = op(B[i+step][j], B[i][j])\n    for i in range(N):\n        for j in range(M-step):\n\
    \            B[i][j+step] = op(B[i][j+step], B[i][j])\n    return B\n"
  code: "import cp_library.alg.iter.__header__\nimport operator\nfrom typing import\
    \ Callable\nfrom cp_library.misc.typing import _T\n\ndef presum2d(A: list[list[_T]],\
    \ op: Callable[[_T,_T],_T] = operator.add, initial: _T = None, step = 1) -> list[_T]:\n\
    \    if initial is None:\n        N, M, B = len(A), len(A[0]), [Ai[:] for Ai in\
    \ A]\n    else:\n        N, M, B = len(A)+1, len(A[0])+1, [[initial]*M for _ in\
    \ range(N)]\n        for i in range(1,N):\n            for j in range(1,M):\n\
    \                B[i][j] = A[i-1][j-1]\n    for i in range(N-step):\n        for\
    \ j in range(M):\n            B[i+step][j] = op(B[i+step][j], B[i][j])\n    for\
    \ i in range(N):\n        for j in range(M-step):\n            B[i][j+step] =\
    \ op(B[i][j+step], B[i][j])\n    return B"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum2d_fn.py
  requiredBy: []
  timestamp: '2025-03-19 01:19:38+07:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/presum2d_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum2d_fn.py
- /library/cp_library/alg/iter/presum2d_fn.py.html
title: cp_library/alg/iter/presum2d_fn.py
---
