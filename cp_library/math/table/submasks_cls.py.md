---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    \n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n  \
    \  x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f)\
    \ + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n  \
    \  x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n    return x\n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n\n\
    class Submasks(list[list[int]]):\n    def __init__(S,N):\n        Z = 1 << N\n\
    \        super().__init__([elist(popcnt32(m)) for m in range(Z)])\n        for\
    \ s in range(Z):\n            sub = S[t := s]\n            while t:\n        \
    \        sub.append(t)\n                t = (t-1)&s\n            sub.append(0)\n\
    \            sub.reverse()\n        \n"
  code: "import cp_library.math.table.__header__\nfrom cp_library.bit.popcnt32_fn\
    \ import popcnt32\nfrom cp_library.ds.elist_fn import elist\n\nclass Submasks(list[list[int]]):\n\
    \    def __init__(S,N):\n        Z = 1 << N\n        super().__init__([elist(popcnt32(m))\
    \ for m in range(Z)])\n        for s in range(Z):\n            sub = S[t := s]\n\
    \            while t:\n                sub.append(t)\n                t = (t-1)&s\n\
    \            sub.append(0)\n            sub.reverse()\n        "
  dependsOn:
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/math/table/submasks_cls.py
  requiredBy: []
  timestamp: '2025-03-30 20:17:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/submasks_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/submasks_cls.py
- /library/cp_library/math/table/submasks_cls.py.html
title: cp_library/math/table/submasks_cls.py
---
