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
    from typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\nimport operator\n\
    \n\n\ndef presum2d(A: list[list[_T]], op = operator.add, initial: _T = None, step\
    \ = 1) -> list[list[_T]]:\n    if initial is None:\n        N, M, B = len(A),\
    \ len(A[0]), [Ai[:] for Ai in A]\n    else:\n        N, M = len(A)+1, len(A[0])+1\n\
    \        B = [[initial]*M for _ in range(N)]\n        for i in range(N-1):\n \
    \           for j in range(M-1):\n                B[i+1][j+1] = A[i][j]\n    for\
    \ i in range(N-step):\n        for j in range(M):\n            B[i+step][j] =\
    \ op(B[i+step][j], B[i][j])\n    for i in range(N):\n        for j in range(M-step):\n\
    \            B[i][j+step] = op(B[i][j+step], B[i][j])\n    return B\n"
  code: "import cp_library.__header__\nfrom cp_library.misc.typing import _T\nimport\
    \ operator\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef presum2d(A: list[list[_T]], op = operator.add, initial: _T = None, step\
    \ = 1) -> list[list[_T]]:\n    if initial is None:\n        N, M, B = len(A),\
    \ len(A[0]), [Ai[:] for Ai in A]\n    else:\n        N, M = len(A)+1, len(A[0])+1\n\
    \        B = [[initial]*M for _ in range(N)]\n        for i in range(N-1):\n \
    \           for j in range(M-1):\n                B[i+1][j+1] = A[i][j]\n    for\
    \ i in range(N-step):\n        for j in range(M):\n            B[i+step][j] =\
    \ op(B[i+step][j], B[i][j])\n    for i in range(N):\n        for j in range(M-step):\n\
    \            B[i][j+step] = op(B[i][j+step], B[i][j])\n    return B"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum2d_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/presum2d_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum2d_fn.py
- /library/cp_library/alg/iter/presum2d_fn.py.html
title: cp_library/alg/iter/presum2d_fn.py
---
