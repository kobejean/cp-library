---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_cls.py
    title: cp_library/ds/tree/bst/bst_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_implicit_cls.py
    title: cp_library/ds/tree/bst/bst_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_reversible_cls.py
    title: cp_library/ds/tree/bst/bst_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_sized_cls.py
    title: cp_library/ds/tree/bst/bst_sized_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_updates_cls.py
    title: cp_library/ds/tree/bst/bst_updates_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_cls.py
    title: cp_library/ds/tree/bst/treap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_implicit_cls.py
    title: cp_library/ds/tree/bst/treap_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_sized_cls.py
    title: cp_library/ds/tree/bst/treap_sized_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/range_reverse_range_sum.test.py
    title: test/library-checker/data-structure/range_reverse_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
    title: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
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
    \n\ni64_max = (1<<63)-1\n"
  code: 'import cp_library.__header__

    import cp_library.bit.__header__

    import cp_library.bit.masks.__header__

    i64_max = (1<<63)-1'
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/masks/i64_max_cnst.py
  requiredBy:
  - cp_library/ds/tree/bst/bst_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - cp_library/ds/tree/bst/bst_updates_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - cp_library/ds/tree/bst/bst_implicit_cls.py
  - cp_library/ds/tree/bst/bst_reversible_cls.py
  - cp_library/ds/tree/bst/treap_cls.py
  - cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - cp_library/ds/tree/bst/treap_sized_cls.py
  - cp_library/ds/tree/bst/bst_sized_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_cls.py
  - cp_library/ds/tree/bst/treap_reversible_cls.py
  - cp_library/ds/tree/bst/treap_implicit_cls.py
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  - test/library-checker/data-structure/range_reverse_range_sum.test.py
  - test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
documentation_of: cp_library/bit/masks/i64_max_cnst.py
layout: document
redirect_from:
- /library/cp_library/bit/masks/i64_max_cnst.py
- /library/cp_library/bit/masks/i64_max_cnst.py.html
title: cp_library/bit/masks/i64_max_cnst.py
---
