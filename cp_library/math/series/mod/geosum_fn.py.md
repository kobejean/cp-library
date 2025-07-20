---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
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
    \n\ndef mod_inv(x, mod):\n    a,b,s,t = x, mod, 1, 0\n    while b:\n        a,b,s,t\
    \ = b,a%b,t,s-a//b*t\n    if a == 1: return s % mod\n    raise ValueError(f\"\
    {x} is not invertible in mod {mod}\")\n\ndef geosum(a, r, n, mod):\n    if r ==\
    \ 1: return a*n\n    return a*(pow(r,n,mod)-1)%mod*mod_inv(r-1, mod)%mod\n"
  code: "import cp_library.math.series.mod.__header__\nfrom cp_library.math.nt.mod_inv_fn\
    \ import mod_inv\n\ndef geosum(a, r, n, mod):\n    if r == 1: return a*n\n   \
    \ return a*(pow(r,n,mod)-1)%mod*mod_inv(r-1, mod)%mod\n"
  dependsOn:
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: cp_library/math/series/mod/geosum_fn.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/series/mod/geosum_fn.py
layout: document
redirect_from:
- /library/cp_library/math/series/mod/geosum_fn.py
- /library/cp_library/math/series/mod/geosum_fn.py.html
title: cp_library/math/series/mod/geosum_fn.py
---
