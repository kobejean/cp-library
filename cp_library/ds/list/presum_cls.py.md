---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_cls.py
    title: cp_library/ds/wavelet/wm_group_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_compressed_cls.py
    title: cp_library/ds/wavelet/wm_group_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_points_cls.py
    title: cp_library/ds/wavelet/wm_group_points_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_group.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_group.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
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
    import operator\n\n\nclass Presum:\n    def __init__(P, A: list, op=operator.add,\
    \ e = 0, diff=operator.sub):\n        P.N = len(A); P.op, P.e, P.diff, P.pre =\
    \ op, e, diff, [e]*(P.N+1)\n        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n\
    \    def __getitem__(srs, key): return srs.range_sum(key.start, key.stop) if isinstance(key,\
    \ slice) else srs.sum(key)\n    def sum(srs, r: int): return srs.pre[r]\n    def\
    \ range_sum(srs, l: int, r: int): return srs.diff(srs.pre[r], srs.pre[l])\n"
  code: "import cp_library.__header__\nimport operator\nimport cp_library.ds.__header__\n\
    import cp_library.ds.list.__header__\nclass Presum:\n    def __init__(P, A: list,\
    \ op=operator.add, e = 0, diff=operator.sub):\n        P.N = len(A); P.op, P.e,\
    \ P.diff, P.pre = op, e, diff, [e]*(P.N+1)\n        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n\
    \    def __getitem__(srs, key): return srs.range_sum(key.start, key.stop) if isinstance(key,\
    \ slice) else srs.sum(key)\n    def sum(srs, r: int): return srs.pre[r]\n    def\
    \ range_sum(srs, l: int, r: int): return srs.diff(srs.pre[r], srs.pre[l])"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/list/presum_cls.py
  requiredBy:
  - cp_library/ds/wavelet/wm_group_cls.py
  - cp_library/ds/wavelet/wm_group_points_cls.py
  - cp_library/ds/wavelet/wm_group_compressed_cls.py
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group.test.py
documentation_of: cp_library/ds/list/presum_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/list/presum_cls.py
- /library/cp_library/ds/list/presum_cls.py.html
title: cp_library/ds/list/presum_cls.py
---
