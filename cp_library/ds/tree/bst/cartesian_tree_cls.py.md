---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_cls.py
    title: cp_library/ds/tree/bst/bst_cls.py
  _extendedRequiredBy:
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
    \ hint.bit_length() << 1)\n\nclass CartesianTree(BST):\n    K, P, sub, st = [-1],\
    \ [42], [-1, -1], []\n\n    def _new_node(T, key, prior = -1): T.P.append(prior);\
    \ return super()._new_node(key)\n\n    def get(T, key):\n        if ~(id:=T._find(key)):\
    \ return T.P[id]\n        raise KeyError\n\n    def split(T, key):\n        S\
    \ = T._new_tree(); T.st.append(T.root); T.st.append(S.root); \n        T._split(T.sub[T.root<<1],\
    \ key, S.root<<1, T.root<<1); T._repair()\n        return S, T\n\n    def insert(T,\
    \ key, prior):\n        T.st.append(T.root); T._insert(T.root<<1, nid := T._new_node(key,\
    \ prior)); T._repair()\n        return nid\n\n    def pop(T, key): return T.P[super().pop(key)]\n\
    \n    def __getitem__(T, key): return T.get(key)\n\n    def _insert(T, sid, nid):\n\
    \        while ~T.sub[sid] and T.P[id:=T.sub[sid]]<T.P[nid]: T.st.append(id);\
    \ sid=id<<1|(T.K[id]<T.K[nid])\n        id, T.sub[sid] = T.sub[sid], nid\n   \
    \     if ~id: T.st.append(nid); T._split(id, T.K[nid], nid<<1, nid<<1|1)\n\n \
    \   def _split(T, id, key, l, r):\n        while ~id:\n            T.st.append(id)\n\
    \            if T.K[id] < key: T.sub[l] = id; id = T.sub[l := id<<1|1]\n     \
    \       else: T.sub[r] = id; id = T.sub[r := id<<1]\n        T.sub[l] = T.sub[r]\
    \ = -1\n\n    def _merge(T, sid, l, r):\n        T.st.append(sid>>1)\n       \
    \ while ~l and ~r:\n            if T.P[l]<T.P[r]: T.st.append(l); T.sub[sid] =\
    \ l; l = T.sub[sid:=l<<1|1]\n            else: T.st.append(r); T.sub[sid] = r;\
    \ r = T.sub[sid:=r<<1]\n        T.sub[sid] = l if ~l else r\n\n    def _del(T,\
    \ id):\n        pid = T.st[-1]\n        T._merge(pid<<1|(pid!=T.root and T.K[pid]<T.K[id]),\
    \ T.sub[id<<1], T.sub[id<<1|1])\n\n    @classmethod\n    def reserve(cls, hint:\
    \ int): super(CartesianTree, cls).reserve(hint); reserve(cls.P, hint+1)\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nimport cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bst.__header__\n\
    from cp_library.ds.tree.bst.bst_cls import BST\n\nclass CartesianTree(BST):\n\
    \    K, P, sub, st = [-1], [42], [-1, -1], []\n\n    def _new_node(T, key, prior\
    \ = -1): T.P.append(prior); return super()._new_node(key)\n\n    def get(T, key):\n\
    \        if ~(id:=T._find(key)): return T.P[id]\n        raise KeyError\n\n  \
    \  def split(T, key):\n        S = T._new_tree(); T.st.append(T.root); T.st.append(S.root);\
    \ \n        T._split(T.sub[T.root<<1], key, S.root<<1, T.root<<1); T._repair()\n\
    \        return S, T\n\n    def insert(T, key, prior):\n        T.st.append(T.root);\
    \ T._insert(T.root<<1, nid := T._new_node(key, prior)); T._repair()\n        return\
    \ nid\n\n    def pop(T, key): return T.P[super().pop(key)]\n\n    def __getitem__(T,\
    \ key): return T.get(key)\n\n    def _insert(T, sid, nid):\n        while ~T.sub[sid]\
    \ and T.P[id:=T.sub[sid]]<T.P[nid]: T.st.append(id); sid=id<<1|(T.K[id]<T.K[nid])\n\
    \        id, T.sub[sid] = T.sub[sid], nid\n        if ~id: T.st.append(nid); T._split(id,\
    \ T.K[nid], nid<<1, nid<<1|1)\n\n    def _split(T, id, key, l, r):\n        while\
    \ ~id:\n            T.st.append(id)\n            if T.K[id] < key: T.sub[l] =\
    \ id; id = T.sub[l := id<<1|1]\n            else: T.sub[r] = id; id = T.sub[r\
    \ := id<<1]\n        T.sub[l] = T.sub[r] = -1\n\n    def _merge(T, sid, l, r):\n\
    \        T.st.append(sid>>1)\n        while ~l and ~r:\n            if T.P[l]<T.P[r]:\
    \ T.st.append(l); T.sub[sid] = l; l = T.sub[sid:=l<<1|1]\n            else: T.st.append(r);\
    \ T.sub[sid] = r; r = T.sub[sid:=r<<1]\n        T.sub[sid] = l if ~l else r\n\n\
    \    def _del(T, id):\n        pid = T.st[-1]\n        T._merge(pid<<1|(pid!=T.root\
    \ and T.K[pid]<T.K[id]), T.sub[id<<1], T.sub[id<<1|1])\n\n    @classmethod\n \
    \   def reserve(cls, hint: int): super(CartesianTree, cls).reserve(hint); reserve(cls.P,\
    \ hint+1)"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/tree/bst/bst_cls.py
  isVerificationFile: false
  path: cp_library/ds/tree/bst/cartesian_tree_cls.py
  requiredBy:
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  - cp_library/ds/tree/bst/treap_cls.py
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
  - test/unittests/ds/tree/bst/treap_monoid_cls_test.py
documentation_of: cp_library/ds/tree/bst/cartesian_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bst/cartesian_tree_cls.py
- /library/cp_library/ds/tree/bst/cartesian_tree_cls.py.html
title: cp_library/ds/tree/bst/cartesian_tree_cls.py
---
