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
    def pack_sm(N: int): s=N.bit_length(); return s, (1<<s)-1\ndef pack_enc(a: int,\
    \ b: int, s: int): return a<<s|b\ndef pack_dec(ab: int, s: int, m: int): return\
    \ ab>>s,ab&m\ndef pack_indices(A, s): return [a<<s|i for i,a in enumerate(A)]\n"
  code: 'import cp_library.bit.__header__

    def pack_sm(N: int): s=N.bit_length(); return s, (1<<s)-1

    def pack_enc(a: int, b: int, s: int): return a<<s|b

    def pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m

    def pack_indices(A, s): return [a<<s|i for i,a in enumerate(A)]'
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/pack_sm_fn.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/bit/pack_sm_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/pack_sm_fn.py
- /library/cp_library/bit/pack_sm_fn.py.html
title: cp_library/bit/pack_sm_fn.py
---
