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
    from typing import Reversible\n\n\n\ndef enumerate_rev(A: Reversible, start: int\
    \ = 0):\n    start -= 1\n    for i in range(len(A)-1,-1,-1):\n        yield (start:=start+1),\
    \ A[i]\n"
  code: "import cp_library.__header__\nfrom typing import Reversible\nimport cp_library.alg.__header__\n\
    import cp_library.alg.iter.__header__\n\ndef enumerate_rev(A: Reversible, start:\
    \ int = 0):\n    start -= 1\n    for i in range(len(A)-1,-1,-1):\n        yield\
    \ (start:=start+1), A[i]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/enumerate_rev_fn.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/enumerate_rev_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/enumerate_rev_fn.py
- /library/cp_library/alg/iter/enumerate_rev_fn.py.html
title: cp_library/alg/iter/enumerate_rev_fn.py
---
