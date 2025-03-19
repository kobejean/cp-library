---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/bit/clz32_fn.py
    title: cp_library/bit/clz32_fn.py
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
    \ & 0x55555555) | ((x << 1) & 0xAAAAAAAA)\n    return x\n"
  code: "import cp_library.bit.__header__\n\ndef bit_reverse32(x):\n    x = (x >>\
    \ 16) | (x << 16)\n    x = ((x >> 8) & 0x00FF00FF) | ((x << 8) & 0xFF00FF00)\n\
    \    x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)\n    x = ((x >> 2)\
    \ & 0x33333333) | ((x << 2) & 0xCCCCCCCC)\n    x = ((x >> 1) & 0x55555555) | ((x\
    \ << 1) & 0xAAAAAAAA)\n    return x\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/bit_reverse32_fn.py
  requiredBy:
  - cp_library/bit/clz32_fn.py
  timestamp: '2025-03-19 07:50:34+07:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/bit/bit_reverse32_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/bit_reverse32_fn.py
- /library/cp_library/bit/bit_reverse32_fn.py.html
title: cp_library/bit/bit_reverse32_fn.py
---
