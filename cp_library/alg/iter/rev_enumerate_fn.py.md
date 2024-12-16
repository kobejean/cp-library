---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/abc249_f_max_k_heap.test.py
    title: test/abc249_f_max_k_heap.test.py
  - icon: ':x:'
    path: test/abc249_f_min_k_heap.test.py
    title: test/abc249_f_min_k_heap.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "\nfrom typing import Reversible\n\ndef rev_enumerate(A: Reversible,\
    \ start: int = 0):\n    A = list(enumerate(A, start))\n    return A[::-1]\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import Reversible\n\n\
    def rev_enumerate(A: Reversible, start: int = 0):\n    A = list(enumerate(A, start))\n\
    \    return A[::-1]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/rev_enumerate_fn.py
  requiredBy: []
  timestamp: '2024-12-17 07:25:33+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/abc249_f_max_k_heap.test.py
  - test/abc249_f_min_k_heap.test.py
documentation_of: cp_library/alg/iter/rev_enumerate_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/rev_enumerate_fn.py
- /library/cp_library/alg/iter/rev_enumerate_fn.py.html
title: cp_library/alg/iter/rev_enumerate_fn.py
---
