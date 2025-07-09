---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
    title: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  - icon: ':warning:'
    path: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
    title: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
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
    path: test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
    title: test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_range_frequency.test.py
    title: test/library-checker/data-structure/static_range_frequency.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/tree_path_composite_sum.test.py
    title: test/library-checker/tree/tree_path_composite_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_set_path_composite.test.py
    title: test/library-checker/tree/vertex_set_path_composite.test.py
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
    \n\ndef pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\n"
  code: 'import cp_library.__header__

    import cp_library.bit.__header__

    import cp_library.bit.pack.__header__

    def pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1'
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/pack/pack_sm_fn.py
  requiredBy:
  - cp_library/ds/tree/bit/sum_cnt_bit_cls.py
  - cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/tree/tree_path_composite_sum.test.py
  - test/library-checker/tree/vertex_set_path_composite.test.py
  - test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_weighted.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_segtree_compressed.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_segtree.test.py
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
  - test/library-checker/data-structure/static_range_frequency.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_group.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_add_point_get_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_weighted_compressed.test.py
documentation_of: cp_library/bit/pack/pack_sm_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/pack/pack_sm_fn.py
- /library/cp_library/bit/pack/pack_sm_fn.py.html
title: cp_library/bit/pack/pack_sm_fn.py
---
