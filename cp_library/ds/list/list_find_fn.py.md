---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/deque_cls.py
    title: cp_library/ds/list/deque_cls.py
  - icon: ':warning:'
    path: cp_library/ds/slidingmax_cls.py
    title: cp_library/ds/slidingmax_cls.py
  - icon: ':warning:'
    path: cp_library/ds/slidingmin_cls.py
    title: cp_library/ds/slidingmin_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/slidingminmax_cls.py
    title: cp_library/ds/slidingminmax_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
    title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
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
    import sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\n"
  code: "import cp_library.ds.list.__header__\nimport sys\n\ndef list_find(lst: list,\
    \ value, start = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value,\
    \ start, stop)\n    except:\n        return -1"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/list/list_find_fn.py
  requiredBy:
  - cp_library/ds/list/deque_cls.py
  - cp_library/ds/slidingmin_cls.py
  - cp_library/ds/slidingmax_cls.py
  - cp_library/ds/slidingminmax_cls.py
  timestamp: '2025-06-08 03:08:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/agc/agc038_b_sliding_min_max.test.py
documentation_of: cp_library/ds/list/list_find_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/list/list_find_fn.py
- /library/cp_library/ds/list/list_find_fn.py.html
title: cp_library/ds/list/list_find_fn.py
---
