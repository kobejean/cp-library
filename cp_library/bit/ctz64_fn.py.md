---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/bit/popcnt64_fn.py
    title: cp_library/bit/popcnt64_fn.py
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
    \ndef popcnt64(x):\n    x = ((x >> 1)  & 0x5555555555555555) + (x & 0x5555555555555555)\n\
    \    x = ((x >> 2)  & 0x3333333333333333) + (x & 0x3333333333333333)\n    x =\
    \ ((x >> 4)  & 0x0f0f0f0f0f0f0f0f) + (x & 0x0f0f0f0f0f0f0f0f)\n    x = ((x >>\
    \ 8)  & 0x00ff00ff00ff00ff) + (x & 0x00ff00ff00ff00ff)\n    x = ((x >> 16) & 0x0000ffff0000ffff)\
    \ + (x & 0x0000ffff0000ffff)\n    x = ((x >> 32) & 0x00000000ffffffff) + (x &\
    \ 0x00000000ffffffff)\n    return x\n\ndef ctz64(x): return popcnt64(~x & (x -\
    \ 1))\n"
  code: 'import cp_library.bit.__header__

    from cp_library.bit.popcnt64_fn import popcnt64


    def ctz64(x): return popcnt64(~x & (x - 1))

    '
  dependsOn:
  - cp_library/bit/popcnt64_fn.py
  isVerificationFile: false
  path: cp_library/bit/ctz64_fn.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/bit/ctz64_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/ctz64_fn.py
- /library/cp_library/bit/ctz64_fn.py.html
title: cp_library/bit/ctz64_fn.py
---