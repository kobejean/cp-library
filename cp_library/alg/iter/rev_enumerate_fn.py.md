---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc249_f_max_k_heap.test.py
    title: test/abc249_f_max_k_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc249_f_min_k_heap.test.py
    title: test/abc249_f_min_k_heap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
  timestamp: '2024-12-08 02:40:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc249_f_min_k_heap.test.py
  - test/abc249_f_max_k_heap.test.py
documentation_of: cp_library/alg/iter/rev_enumerate_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/rev_enumerate_fn.py
- /library/cp_library/alg/iter/rev_enumerate_fn.py.html
title: cp_library/alg/iter/rev_enumerate_fn.py
---