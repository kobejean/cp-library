---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/bit/bit_reverse_fn.py
    title: cp_library/bit/bit_reverse_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/ctz_fn.py
    title: cp_library/bit/ctz_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt_fn.py
    title: cp_library/bit/popcnt_fn.py
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
    \ndef bit_reverse(x):\n    x = (x >> 16) | (x << 16)\n    x = ((x >> 8) & 0x00FF00FF)\
    \ | ((x << 8) & 0xFF00FF00)\n    x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)\n\
    \    x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)\n    x = ((x >> 1)\
    \ & 0x55555555) | ((x << 1) & 0xAAAAAAAA)\n    return x\n\ndef popcnt(x):\n  \
    \  x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333)\
    \ + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n  \
    \  x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff)\
    \ + (x & 0x0000ffff)\n    return x\n\nif hasattr(int, 'bit_count'):\n    popcnt\
    \ = int.bit_count\n\ndef ctz(x): return popcnt(~x & (x - 1))\n\ndef clz(x): return\
    \ ctz(bit_reverse(x))\n"
  code: 'import cp_library.bit.__header__

    from cp_library.bit.bit_reverse_fn import bit_reverse

    from cp_library.bit.ctz_fn import ctz


    def clz(x): return ctz(bit_reverse(x))

    '
  dependsOn:
  - cp_library/bit/bit_reverse_fn.py
  - cp_library/bit/ctz_fn.py
  - cp_library/bit/popcnt_fn.py
  isVerificationFile: false
  path: cp_library/bit/clz_fn.py
  requiredBy: []
  timestamp: '2024-12-27 10:06:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/bit/clz_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/clz_fn.py
- /library/cp_library/bit/clz_fn.py.html
title: cp_library/bit/clz_fn.py
---
