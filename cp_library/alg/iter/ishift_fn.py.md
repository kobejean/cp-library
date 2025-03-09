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
    \ndef ishift(A: MutableSequence[_T], offset=-1):\n    for i,a in enumerate(A):\
    \ A[i] = a+offset\n    return A\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import MutableSequence\n\
    from cp_library.misc.typing import _T\n\ndef ishift(A: MutableSequence[_T], offset=-1):\n\
    \    for i,a in enumerate(A): A[i] = a+offset\n    return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/ishift_fn.py
  requiredBy: []
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/ishift_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/ishift_fn.py
- /library/cp_library/alg/iter/ishift_fn.py.html
title: cp_library/alg/iter/ishift_fn.py
---
