---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/lis_fn.py
    title: cp_library/alg/dp/lis_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/mo_cls.py
    title: cp_library/alg/dp/mo_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
    title: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':warning:'
    path: cp_library/alg/iter/rank/rank_multi_fn.py
    title: cp_library/alg/iter/rank/rank_multi_fn.py
  - icon: ':warning:'
    path: cp_library/perf/examples/rank_benchmark.py
    title: cp_library/perf/examples/rank_benchmark.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
    title: test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc261_g_mo.test.py
    title: test/atcoder/abc/abc261_g_mo.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_add_point_get_wm_bit.test.py
    title: test/library-checker/data-structure/rectangle_add_point_get_wm_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_bit.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_bit_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_bit_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_group.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_group.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_weighted.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_weighted.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_weighted_compressed.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_weighted_compressed.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/other/longest_increasing_sequence.test.py
    title: test/library-checker/other/longest_increasing_sequence.test.py
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
    \ndef max2(a, b):\n    return a if a > b else b\n"
  code: "import cp_library.alg.dp.__header__\n\ndef max2(a, b):\n    return a if a\
    \ > b else b"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/max2_fn.py
  requiredBy:
  - cp_library/alg/dp/lis_fn.py
  - cp_library/alg/dp/mo_cls.py
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/alg/iter/rank/rank_multi_fn.py
  - cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  - cp_library/perf/examples/rank_benchmark.py
  - perf/rank.py
  timestamp: '2025-07-10 02:39:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_3_b_cut_edges_snippet.test.py
  - test/library-checker/other/longest_increasing_sequence.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_weighted.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
  - test/library-checker/data-structure/point_set_range_composite_large_array.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_add_point_get_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_weighted_compressed.test.py
  - test/atcoder/abc/abc261_g_mo.test.py
documentation_of: cp_library/alg/dp/max2_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/max2_fn.py
- /library/cp_library/alg/dp/max2_fn.py.html
title: cp_library/alg/dp/max2_fn.py
---
