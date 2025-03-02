---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc151_f_fbisect_left.test.py
    title: test/atcoder/abc/abc151_f_fbisect_left.test.py
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
    \ndef fbisect_left(key, hi, x = True, lo = 0.0, tol=1e-9):\n    while hi - lo\
    \ > tol:            \n        mid = (lo + hi) / 2\n        if key(mid) >= x:\n\
    \            hi = mid\n        else:\n            lo = mid\n            \n   \
    \ return lo\n\ndef fbisect_right(key, hi, x=False, lo=0.0, tol=1e-9):\n    while\
    \ hi - lo > tol:\n        mid = (lo + hi) / 2\n        if key(mid) > x:\n    \
    \        hi = mid\n        else:\n            lo = mid\n    return hi\n"
  code: "import cp_library.alg.divcon.__header__\n\ndef fbisect_left(key, hi, x =\
    \ True, lo = 0.0, tol=1e-9):\n    while hi - lo > tol:            \n        mid\
    \ = (lo + hi) / 2\n        if key(mid) >= x:\n            hi = mid\n        else:\n\
    \            lo = mid\n            \n    return lo\n\ndef fbisect_right(key, hi,\
    \ x=False, lo=0.0, tol=1e-9):\n    while hi - lo > tol:\n        mid = (lo + hi)\
    \ / 2\n        if key(mid) > x:\n            hi = mid\n        else:\n       \
    \     lo = mid\n    return hi"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/fbisect_fn.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc151_f_fbisect_left.test.py
documentation_of: cp_library/alg/divcon/fbisect_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/fbisect_fn.py
- /library/cp_library/alg/divcon/fbisect_fn.py.html
title: cp_library/alg/divcon/fbisect_fn.py
---
