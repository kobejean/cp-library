---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/cnt/range_distinct_counter_cls.py
    title: cp_library/ds/cnt/range_distinct_counter_cls.py
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
    from collections import Counter\n\n\n\nclass DistinctCounter:\n    def __init__(dc,\
    \ Amax: int):\n        dc.cnt = 0\n        dc.freq = [0]*(Amax+1) if Amax < 5_000_000\
    \ else Counter()\n\n    def add(dc, a):\n        dc.cnt += dc.freq[a] == 0\n \
    \       dc.freq[a] += 1\n\n    def remove(dc, a):\n        dc.freq[a] -= 1\n \
    \       dc.cnt -= dc.freq[a] == 0\n    \n    def count(dc): return dc.cnt\n"
  code: "import cp_library.__header__\nfrom collections import Counter\nimport cp_library.ds.__header__\n\
    import cp_library.ds.cnt.__header__\n\nclass DistinctCounter:\n    def __init__(dc,\
    \ Amax: int):\n        dc.cnt = 0\n        dc.freq = [0]*(Amax+1) if Amax < 5_000_000\
    \ else Counter()\n\n    def add(dc, a):\n        dc.cnt += dc.freq[a] == 0\n \
    \       dc.freq[a] += 1\n\n    def remove(dc, a):\n        dc.freq[a] -= 1\n \
    \       dc.cnt -= dc.freq[a] == 0\n    \n    def count(dc): return dc.cnt\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/cnt/distinct_counter_cls.py
  requiredBy:
  - cp_library/ds/cnt/range_distinct_counter_cls.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/cnt/distinct_counter_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/cnt/distinct_counter_cls.py
- /library/cp_library/ds/cnt/distinct_counter_cls.py.html
title: cp_library/ds/cnt/distinct_counter_cls.py
---
