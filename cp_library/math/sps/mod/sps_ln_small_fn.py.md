---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_ln_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_ln_adaptive_fn.py
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
    \n\n\ndef sps_ln_small(P, mod):\n    assert P[0] == 1\n    ln = [0]*(Z:=1<<(N:=len(P).bit_length()-1))\n\
    \    for i in range(1, Z):\n        fg, b, j = 0, 1<<(i.bit_length()-1), i-1&i\n\
    \        while b <= j: fg += ln[j]*P[i^j]%mod; j = j-1&i\n        ln[i] = (P[i]-fg)%mod\n\
    \    return ln\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.sps.__header__\n\
    \ndef sps_ln_small(P, mod):\n    assert P[0] == 1\n    ln = [0]*(Z:=1<<(N:=len(P).bit_length()-1))\n\
    \    for i in range(1, Z):\n        fg, b, j = 0, 1<<(i.bit_length()-1), i-1&i\n\
    \        while b <= j: fg += ln[j]*P[i^j]%mod; j = j-1&i\n        ln[i] = (P[i]-fg)%mod\n\
    \    return ln"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_ln_small_fn.py
  requiredBy:
  - cp_library/math/sps/mod/sps_ln_adaptive_fn.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/sps/mod/sps_ln_small_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_ln_small_fn.py
- /library/cp_library/math/sps/mod/sps_ln_small_fn.py.html
title: cp_library/math/sps/mod/sps_ln_small_fn.py
---
