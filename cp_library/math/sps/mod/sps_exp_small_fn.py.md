---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
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
    \n\n\n\ndef sps_exp_small(P, mod):\n    assert P[0] == 0\n    exp = [0]*(Z :=\
    \ 1<<(len(P).bit_length()-1)); exp[0] = 1\n    for i in range(1, Z):\n       \
    \ fg, b, j = 0, 1 << (i.bit_length() - 1), i-1&i\n        while b <= j: fg +=\
    \ P[j]*exp[i^j]%mod; j = j-1&i\n        exp[i] = (P[i]+fg)%mod\n    return exp\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.sps.__header__\n\
    import cp_library.math.sps.mod.__header__\n\ndef sps_exp_small(P, mod):\n    assert\
    \ P[0] == 0\n    exp = [0]*(Z := 1<<(len(P).bit_length()-1)); exp[0] = 1\n   \
    \ for i in range(1, Z):\n        fg, b, j = 0, 1 << (i.bit_length() - 1), i-1&i\n\
    \        while b <= j: fg += P[j]*exp[i^j]%mod; j = j-1&i\n        exp[i] = (P[i]+fg)%mod\n\
    \    return exp\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_exp_small_fn.py
  requiredBy:
  - cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/sps/mod/sps_exp_small_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_exp_small_fn.py
- /library/cp_library/math/sps/mod/sps_exp_small_fn.py.html
title: cp_library/math/sps/mod/sps_exp_small_fn.py
---
