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
    from typing import MutableSequence\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    _U = TypeVar('U')\n\n\n\ndef ishift(A: MutableSequence[_T], offset=-1):\n    for\
    \ i,a in enumerate(A): A[i] = a+offset\n    return A\n"
  code: "import cp_library.__header__\nfrom typing import MutableSequence\nfrom cp_library.misc.typing\
    \ import _T\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef ishift(A: MutableSequence[_T], offset=-1):\n    for i,a in enumerate(A):\
    \ A[i] = a+offset\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/ishift_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/ishift_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/ishift_fn.py
- /library/cp_library/alg/iter/ishift_fn.py.html
title: cp_library/alg/iter/ishift_fn.py
---
