---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/nt/chinese_remainder_theorem_fn.py
    title: cp_library/math/nt/chinese_remainder_theorem_fn.py
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
    \ndef mod_inv(x, mod):\n    a,b,s,t = x, mod, 1, 0\n    while b:\n        a,b,s,t\
    \ = b,a%b,t,s-a//b*t\n    if a == 1: return s % mod\n    raise ValueError(f\"\
    {x} is not invertible in mod {mod}\")\n"
  code: "import cp_library.math.nt.__header__\n\ndef mod_inv(x, mod):\n    a,b,s,t\
    \ = x, mod, 1, 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n    if a ==\
    \ 1: return s % mod\n    raise ValueError(f\"{x} is not invertible in mod {mod}\"\
    )\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/nt/mod_inv_fn.py
  requiredBy:
  - cp_library/math/nt/chinese_remainder_theorem_fn.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/nt/mod_inv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/nt/mod_inv_fn.py
- /library/cp_library/math/nt/mod_inv_fn.py.html
title: cp_library/math/nt/mod_inv_fn.py
---
