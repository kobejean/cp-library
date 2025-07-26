---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/bit/bit_reverse32_fn.py
    title: cp_library/bit/bit_reverse32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/ctz32_fn.py
    title: cp_library/bit/ctz32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
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
    \ndef bit_reverse32(x):\n    x = (x >> 16) | (x << 16)\n    x = ((x >> 8) & 0x00FF00FF)\
    \ | ((x << 8) & 0xFF00FF00)\n    x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)\n\
    \    x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)\n    x = ((x >> 1)\
    \ & 0x55555555) | ((x << 1) & 0xAAAAAAAA)\n    return x\n\ndef popcnt32(x):\n\
    \    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333)\
    \ + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n  \
    \  x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff)\
    \ + (x & 0x0000ffff)\n    return x\nif hasattr(int, 'bit_count'):\n    popcnt32\
    \ = int.bit_count\n\ndef ctz32(x): return popcnt32(~x&(x-1))\n\ndef clz32(x):\
    \ return ctz32(bit_reverse32(x))\n"
  code: 'import cp_library.bit.__header__

    from cp_library.bit.bit_reverse32_fn import bit_reverse32

    from cp_library.bit.ctz32_fn import ctz32


    def clz32(x): return ctz32(bit_reverse32(x))

    '
  dependsOn:
  - cp_library/bit/bit_reverse32_fn.py
  - cp_library/bit/ctz32_fn.py
  - cp_library/bit/popcnt32_fn.py
  isVerificationFile: false
  path: cp_library/bit/clz32_fn.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/bit/clz32_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/clz32_fn.py
- /library/cp_library/bit/clz32_fn.py.html
title: cp_library/bit/clz32_fn.py
---
