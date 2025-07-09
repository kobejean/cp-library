---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_bit_cls.py
    title: cp_library/alg/tree/csr/hld_bit_cls.py
  - icon: ':warning:'
    path: cp_library/ds/tree/bit/bir_cls.py
    title: cp_library/ds/tree/bit/bir_cls.py
  - icon: ':warning:'
    path: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
    title: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_bit_cls.py
    title: cp_library/ds/wavelet/wm_bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_bit_compressed_cls.py
    title: cp_library/ds/wavelet/wm_bit_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_bit_points_cls.py
    title: cp_library/ds/wavelet/wm_bit_points_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/invcnt_fn.py
    title: cp_library/math/invcnt_fn.py
  - icon: ':warning:'
    path: test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
    title: test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_hld.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_hld.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_hld_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_hld_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
    title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_range_sum.test.py
    title: test/library-checker/data-structure/point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/predecessor_problem_bit.test.py
    title: test/library-checker/data-structure/predecessor_problem_bit.test.py
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
    path: test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_path_sum_hld.test.py
    title: test/library-checker/tree/vertex_add_path_sum_hld.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_path_sum_hld_bit.test.py
    title: test/library-checker/tree/vertex_add_path_sum_hld_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_subtree_sum.test.py
    title: test/library-checker/tree/vertex_add_subtree_sum.test.py
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
    \n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513            \n            \u2503                           \
    \         7 \u2503            \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B            \n            \u250F\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2513                 \u2502              \n  \
    \          \u2503                3 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524           \
    \   \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B                 \u2502\
    \              \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\
    \       \u2502              \n            \u2503      1 \u2503\u25C4\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\
    \u252F\u2501\u251B       \u2502              \n            \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502              \n       \
    \     \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503\
    \ 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524              \n\
    \            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502              \n              \u2502    \u2502    \u2502    \u2502  \
    \  \u2502    \u2502    \u2502    \u2502              \n              \u25BC  \
    \  \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC        \
    \      \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\
    \u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503 1 \u2503\
    \u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503\
    \ 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data Structure -\
    \ Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def __init__(bit,\
    \ v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n        else:\
    \ bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def build(bit,\
    \ data):\n        bit._d, bit._n = data, len(data)\n        for i in range(bit._n):\n\
    \            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\n    def add(bit,\
    \ i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1], n&n-1\n\
    \        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n   \
    \ \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    import cp_library.ds.tree.bit.__header__\n\nclass BIT:\n    def __init__(bit,\
    \ v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n        else:\
    \ bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def build(bit,\
    \ data):\n        bit._d, bit._n = data, len(data)\n        for i in range(bit._n):\n\
    \            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\n    def add(bit,\
    \ i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1], n&n-1\n\
    \        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n   \
    \ \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit/bit_cls.py
  requiredBy:
  - test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
  - cp_library/ds/tree/bit/bir_cls.py
  - cp_library/ds/tree/bit/sum_cnt_bit_cls.py
  - cp_library/ds/wavelet/wm_bit_cls.py
  - cp_library/ds/wavelet/wm_bit_points_cls.py
  - cp_library/ds/wavelet/wm_bit_compressed_cls.py
  - cp_library/alg/tree/csr/hld_bit_cls.py
  - cp_library/math/invcnt_fn.py
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/tree/vertex_add_subtree_sum.test.py
  - test/library-checker/tree/vertex_add_path_sum_hld_bit.test.py
  - test/library-checker/tree/vertex_add_path_sum_hld.test.py
  - test/library-checker/data-structure/point_add_range_sum.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
  - test/library-checker/data-structure/predecessor_problem_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit_compressed.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_bit.test.py
  - test/library-checker/data-structure/rectangle_add_point_get_wm_bit.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
  - test/atcoder/abc/abc294_g_fast_tree_hld.test.py
  - test/atcoder/abc/abc294_g_fast_tree_hld_bit.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
documentation_of: cp_library/ds/tree/bit/bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit/bit_cls.py
- /library/cp_library/ds/tree/bit/bit_cls.py.html
title: cp_library/ds/tree/bit/bit_cls.py
---
