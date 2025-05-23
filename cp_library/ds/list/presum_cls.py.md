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
    \n\nclass Presum:\n    def __init__(P, op, e, diff, A: list):\n        P.N = len(A);\
    \ P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)\n        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n\
    \    def __getitem__(P,i):return P.pre[i]\n    def prod(P,l:int,r:int):return\
    \ P.diff(P.pre[r],P.pre[l])\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.list.__header__\n\
    class Presum:\n    def __init__(P, op, e, diff, A: list):\n        P.N = len(A);\
    \ P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)\n        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n\
    \    def __getitem__(P,i):return P.pre[i]\n    def prod(P,l:int,r:int):return\
    \ P.diff(P.pre[r],P.pre[l])"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/list/presum_cls.py
  requiredBy:
  - cp_library/ds/wavelet/wm_group_compressed_cls.py
  - cp_library/ds/wavelet/wm_group_cls.py
  - cp_library/ds/wavelet/wm_group_points_cls.py
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group.test.py
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
documentation_of: cp_library/ds/list/presum_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/list/presum_cls.py
- /library/cp_library/ds/list/presum_cls.py.html
title: cp_library/ds/list/presum_cls.py
---
