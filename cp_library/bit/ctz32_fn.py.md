---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bit_graph_cls.py
    title: cp_library/alg/graph/bit_graph_cls.py
  - icon: ':warning:'
    path: cp_library/bit/clz32_fn.py
    title: cp_library/bit/clz32_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/chromatic_number.test.py
    title: test/library-checker/graph/chromatic_number.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n    x\
    \ = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f)\
    \ + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n  \
    \  x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n    return x\n\ndef ctz32(x):\
    \ return popcnt32(~x & (x - 1))\n"
  code: 'import cp_library.bit.__header__

    from cp_library.bit.popcnt32_fn import popcnt32


    def ctz32(x): return popcnt32(~x & (x - 1))

    '
  dependsOn:
  - cp_library/bit/popcnt32_fn.py
  isVerificationFile: false
  path: cp_library/bit/ctz32_fn.py
  requiredBy:
  - cp_library/alg/graph/bit_graph_cls.py
  - cp_library/bit/clz32_fn.py
  timestamp: '2025-03-28 21:58:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/chromatic_number.test.py
documentation_of: cp_library/bit/ctz32_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/ctz32_fn.py
- /library/cp_library/bit/ctz32_fn.py.html
title: cp_library/bit/ctz32_fn.py
---
