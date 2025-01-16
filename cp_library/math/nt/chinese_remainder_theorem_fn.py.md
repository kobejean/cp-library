---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
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
    from math import prod\n\ndef mod_inv(x, mod):\n    a,b,s,t = x, mod, 1, 0\n  \
    \  while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n    if a == 1: return s % mod\n\
    \    raise ValueError(f\"{x} is not invertible in mod {mod}\")\n\ndef chinese_remainder_theorem(rems,\
    \ mods):\n    mod, a = prod(mods), 0\n    for r,m in zip(rems, mods):\n      \
    \  N = mod_inv(M:=mod//m,m)\n        a += r*M*N % mod\n    return a % mod\n"
  code: "import cp_library.math.nt.__header__\nfrom math import prod\nfrom cp_library.math.nt.mod_inv_fn\
    \ import mod_inv\n\ndef chinese_remainder_theorem(rems, mods):\n    mod, a = prod(mods),\
    \ 0\n    for r,m in zip(rems, mods):\n        N = mod_inv(M:=mod//m,m)\n     \
    \   a += r*M*N % mod\n    return a % mod"
  dependsOn:
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: cp_library/math/nt/chinese_remainder_theorem_fn.py
  requiredBy: []
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/nt/chinese_remainder_theorem_fn.py
layout: document
redirect_from:
- /library/cp_library/math/nt/chinese_remainder_theorem_fn.py
- /library/cp_library/math/nt/chinese_remainder_theorem_fn.py.html
title: cp_library/math/nt/chinese_remainder_theorem_fn.py
---
