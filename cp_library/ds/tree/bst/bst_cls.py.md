---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_cls.py
    title: cp_library/ds/tree/bst/treap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
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
    \n\ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import\
    \ resizelist_hint\nexcept:\n    def resizelist_hint(A: list, est_len: int):\n\
    \        pass\nreserve = resizelist_hint\n\n\n\nclass BST:\n    __slots__ = 'root'\n\
    \    K, sub, st = [-1], [-1, -1], []\n\n    def __init__(T): T.root = T._new_node(-1)\n\
    \n    def _new_tree(T): return T.__class__()\n\n    def _new_node(T, key):\n \
    \       id = len(T.K); T.K.append(key); T.sub.append(-1); T.sub.append(-1)\n \
    \       return id\n\n    def insert(T, key):\n        T.st.append(T.root); T._insert(T.root<<1,\
    \ nid := T._new_node(key)); T._repair()\n        return nid\n\n    def pop(T,\
    \ key):\n        if ~(id:=T._trace(key)): T._del(id); T._repair(); return id\n\
    \        else: T.st.clear(); raise KeyError\n\n    def __delitem__(T, key):\n\
    \        if ~(id:=T._trace(key)): T._del(id); T._repair()\n        else: T.st.clear();\
    \ raise KeyError\n\n    def __contains__(T, key): return 0 <= T._find(key)\n\n\
    \    def _find(T, key):\n        id = T.sub[T.root<<1]\n        while ~id and\
    \ T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n        return id\n\n    def\
    \ _trace(T, key):\n        id = T.sub[T.root<<1]; T.st.append(T.root)\n      \
    \  while ~id and T.K[id] != key: T.st.append(id); id = T.sub[id<<1|(T.K[id]<key)]\n\
    \        return id\n\n    def _insert(T, sid, nid):\n        while ~T.sub[sid]:\
    \ T.st.append(id:=T.sub[sid]); sid=id<<1|(T.K[id]<T.K[nid])\n        id, T.sub[sid]\
    \ = T.sub[sid], nid\n\n    def _del(T, id): raise NotImplemented\n\n    def _repair(T):\
    \ T.st.clear()\n\n    @classmethod\n    def reserve(cls, hint: int):\n       \
    \ hint += 1\n        reserve(cls.K, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nimport cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bst.__header__\n\
    \nclass BST:\n    __slots__ = 'root'\n    K, sub, st = [-1], [-1, -1], []\n\n\
    \    def __init__(T): T.root = T._new_node(-1)\n\n    def _new_tree(T): return\
    \ T.__class__()\n\n    def _new_node(T, key):\n        id = len(T.K); T.K.append(key);\
    \ T.sub.append(-1); T.sub.append(-1)\n        return id\n\n    def insert(T, key):\n\
    \        T.st.append(T.root); T._insert(T.root<<1, nid := T._new_node(key)); T._repair()\n\
    \        return nid\n\n    def pop(T, key):\n        if ~(id:=T._trace(key)):\
    \ T._del(id); T._repair(); return id\n        else: T.st.clear(); raise KeyError\n\
    \n    def __delitem__(T, key):\n        if ~(id:=T._trace(key)): T._del(id); T._repair()\n\
    \        else: T.st.clear(); raise KeyError\n\n    def __contains__(T, key): return\
    \ 0 <= T._find(key)\n\n    def _find(T, key):\n        id = T.sub[T.root<<1]\n\
    \        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n     \
    \   return id\n\n    def _trace(T, key):\n        id = T.sub[T.root<<1]; T.st.append(T.root)\n\
    \        while ~id and T.K[id] != key: T.st.append(id); id = T.sub[id<<1|(T.K[id]<key)]\n\
    \        return id\n\n    def _insert(T, sid, nid):\n        while ~T.sub[sid]:\
    \ T.st.append(id:=T.sub[sid]); sid=id<<1|(T.K[id]<T.K[nid])\n        id, T.sub[sid]\
    \ = T.sub[sid], nid\n\n    def _del(T, id): raise NotImplemented\n\n    def _repair(T):\
    \ T.st.clear()\n\n    @classmethod\n    def reserve(cls, hint: int):\n       \
    \ hint += 1\n        reserve(cls.K, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/bst/bst_cls.py
  requiredBy:
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_cls.py
  - cp_library/ds/tree/bst/treap_cls.py
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
  - test/unittests/ds/tree/bst/treap_monoid_cls_test.py
documentation_of: cp_library/ds/tree/bst/bst_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bst/bst_cls.py
- /library/cp_library/ds/tree/bst/bst_cls.py.html
title: cp_library/ds/tree/bst/bst_cls.py
---
