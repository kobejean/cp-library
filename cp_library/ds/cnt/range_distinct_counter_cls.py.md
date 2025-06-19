---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/ds/cnt/distinct_counter_cls.py
    title: cp_library/ds/cnt/distinct_counter_cls.py
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
    \n\nfrom collections import Counter\n\nclass DistinctCounter:\n    def __init__(dc,\
    \ Amax: int):\n        dc.cnt = 0\n        dc.freq = [0]*(Amax+1) if Amax < 5_000_000\
    \ else Counter()\n\n    def add(dc, a):\n        dc.cnt += dc.freq[a] == 0\n \
    \       dc.freq[a] += 1\n\n    def remove(dc, a):\n        dc.freq[a] -= 1\n \
    \       dc.cnt -= dc.freq[a] == 0\n    \n    def count(dc): return dc.cnt\n\n\
    class RangeDistinctCounter(DistinctCounter):\n    def __init__(rdc, A: list[int],\
    \ Amax: int):\n        super().__init__(Amax)\n        rdc.A = A\n        rdc.l\
    \ = rdc.r = 0\n    def add(rdc, i): super().add(rdc.A[i])\n    def remove(rdc,\
    \ i): super().remove(rdc.A[i])\n    def move_query(rdc, l: int, r: int):\n   \
    \     while rdc.r < r: rdc.add(rdc.r); rdc.r += 1\n        while l < rdc.l: rdc.l\
    \ -= 1; rdc.add(rdc.l)\n        while r < rdc.r: rdc.r -= 1; rdc.remove(rdc.r)\n\
    \        while rdc.l < l: rdc.remove(rdc.l); rdc.l += 1\n        return super().count()\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.cnt.__header__\n\
    from cp_library.ds.cnt.distinct_counter_cls import DistinctCounter\n\nclass RangeDistinctCounter(DistinctCounter):\n\
    \    def __init__(rdc, A: list[int], Amax: int):\n        super().__init__(Amax)\n\
    \        rdc.A = A\n        rdc.l = rdc.r = 0\n    def add(rdc, i): super().add(rdc.A[i])\n\
    \    def remove(rdc, i): super().remove(rdc.A[i])\n    def move_query(rdc, l:\
    \ int, r: int):\n        while rdc.r < r: rdc.add(rdc.r); rdc.r += 1\n       \
    \ while l < rdc.l: rdc.l -= 1; rdc.add(rdc.l)\n        while r < rdc.r: rdc.r\
    \ -= 1; rdc.remove(rdc.r)\n        while rdc.l < l: rdc.remove(rdc.l); rdc.l +=\
    \ 1\n        return super().count()"
  dependsOn:
  - cp_library/ds/cnt/distinct_counter_cls.py
  isVerificationFile: false
  path: cp_library/ds/cnt/range_distinct_counter_cls.py
  requiredBy: []
  timestamp: '2025-06-20 03:24:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/cnt/range_distinct_counter_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/cnt/range_distinct_counter_cls.py
- /library/cp_library/ds/cnt/range_distinct_counter_cls.py.html
title: cp_library/ds/cnt/range_distinct_counter_cls.py
---
