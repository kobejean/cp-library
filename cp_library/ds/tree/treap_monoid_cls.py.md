---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
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
    \        pass\nreserve = resizelist_hint\n\n\nclass TreapMonoid:\n    __slots__\
    \ = 'op', 'e', 'root', 'cnt'\n    # class attributes\n    K, V, A, P = [-1], [-1],\
    \ [-1], [42]\n    par, sub, st = [-1], [-1, -1], []\n\n    def __init__(T, op,\
    \ e = -1):\n        T.op, T.e, T.cnt = op, e, -1\n        T.root = T.new_node(-1,\
    \ e)\n\n    def prod(T, l: int, r: int):\n        # find_node common ancestor\n\
    \        a = T.sub[T.root<<1]\n        while ~a and not l <= T.K[a] < r: a = T.sub[a<<1|(T.K[a]<l)]\n\
    \        if a < 0: return T.e\n        # left subtreap\n        acc, i = T.V[a],\
    \ T.sub[a<<1]\n        while ~i:\n            if not (T.K[i]<l):\n           \
    \     if ~T.sub[i<<1|1]: acc = T.op(T.A[T.sub[i<<1|1]], acc)\n               \
    \ acc = T.op(T.V[i], acc)\n            i = T.sub[i<<1|(T.K[i]<l)]\n        # right\
    \ subtreap\n        i = T.sub[a<<1|1]\n        while ~i:\n            if T.K[i]<r:\n\
    \                if ~T.sub[i<<1]: acc = T.op(acc, T.A[T.sub[i<<1]])\n        \
    \        acc = T.op(acc, T.V[i])\n            i = T.sub[i<<1|(T.K[i]<r)]\n   \
    \     return acc\n\n    def all_prod(T): return T.A[T.root]\n    \n    def insert(T,\
    \ key, val):\n        T.insert_node(T.root<<1, nid := T.new_node(key, val))\n\
    \        return nid\n    \n    def split(T, key):\n        T.K[0] = key\n    \
    \    T.split_node(T.sub[T.root<<1], 0)\n        S = T.__class__(T.op, T.e)\n \
    \       if ~S.sub[0]: S.attach_node(S.root<<1, T.sub[0])\n        if ~T.sub[1]:\
    \ T.attach_node(T.root<<1, T.sub[1])\n        T._repair()\n        return S, T\n\
    \    \n    def get(T, key): return T.V[id] if ~(id:=T.find_node(key)) else T.e\n\
    \n    def pop(T, key):\n        if ~(id:=T.find_node(key)): T.del_node(id); return\
    \ T.V[id]\n        return T.e\n\n    def __delitem__(T, key):\n        if ~(id:=T.find_node(key)):\
    \ T.del_node(id)\n    \n    def __setitem__(T, key, val):\n        if ~(id:=T.find_node(key)):\
    \ T.set_node(id, val)\n        else: T.insert(key, val)\n    \n    def __getitem__(T,\
    \ key):\n        if isinstance(key, int): return T.get(key)\n        elif isinstance(key,\
    \ slice): return T.prod(key.start, key.stop)\n    \n    def __contains__(T, key):\
    \ return 0 <= T.find_node(key)\n\n    def __len__(T): return T.cnt\n\n    def\
    \ new_node(T, key, val):\n        id = len(T.K)\n        T.K.append(key); T.V.append(val);\
    \ T.A.append(val)\n        T.P.append((T.P[-1] * 1103515245 + 12345) & 0x7fffffff)\n\
    \        T.par.append(-1); T.sub.append(-1); T.sub.append(-1)\n        T.cnt +=\
    \ 1\n        return id\n\n    def find_node(T, key: int):\n        id = T.sub[T.root<<1]\n\
    \        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n     \
    \   return id\n    \n    def insert_node(T, sid, nid):\n        while ~T.sub[sid]\
    \ and T.P[id:=T.sub[sid]]<T.P[nid]:sid=id<<1|(T.K[id]<T.K[nid])\n        id =\
    \ T.sub[sid]; T.attach_node(sid, nid)\n        if ~id: T.split_node(id, nid)\n\
    \        T._repair()\n    \n    def split_node(T, id, nid):\n        l, r = nid<<1,\
    \ nid<<1|1\n        while ~id:\n            if T.K[id] < T.K[nid]: T.attach_node(l,\
    \ id); id = T.sub[l := id<<1|1]\n            else: T.attach_node(r, id); id =\
    \ T.sub[r := id<<1]\n        T.st.append(l>>1); T.st.append(r>>1)\n        T.sub[l]\
    \ = T.sub[r] = -1\n        T._repair()\n\n    def set_node(T, id: int, val): T.V[id]\
    \ = val; T._propagate(id)\n\n    def merge_nodes(T, sid: int, l: int, r: int):\n\
    \        while ~l and ~r:\n            if T.P[l]<T.P[r]: T.attach_node(sid, l);\
    \ l = T.sub[sid := l<<1|1]\n            else: T.attach_node(sid, r); r = T.sub[sid\
    \ := r<<1]\n        if ~l: T.attach_node(sid, l)\n        elif ~r: T.attach_node(sid,\
    \ r)\n        T._repair()\n\n    def del_node(T, id: int):\n        sid, l, r\
    \ = T.par[id], T.sub[id<<1], T.sub[id<<1|1]\n        T.detach_node(id)\n     \
    \   T.merge_nodes(sid, l, r)\n        T.cnt -= 1\n    \n    def detach_node(T,\
    \ id: int):\n        assert ~T.par[id]\n        T.st.append(T.par[id]>>1)\n  \
    \      T.sub[T.par[id]] = T.par[id] = -1\n    \n    def attach_node(T, sid: int,\
    \ id: int):\n        T.st.append(sid>>1)\n        T.sub[sid], T.par[id] = id,\
    \ sid\n\n    @classmethod\n    def reserve(cls, hint: int):\n        hint += 1\n\
    \        reserve(cls.K, hint); reserve(cls.V, hint); reserve(cls.A, hint); reserve(cls.P,\
    \ hint)\n        reserve(cls.par, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)\n    \n    def _update(T, id):\n        T.A[id] = T.V[id]\n\
    \        if ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])\n        if\
    \ ~(r := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])\n        \n    def _propagate(T,\
    \ id):\n        while ~T.par[id]: T._update(id); id = T.par[id]>>1\n        T._update(id)\n\
    \n    def _repair(T):\n        if T.st:\n            while T.st: T._update(id\
    \ := T.st.pop())\n            if id != T.root: T._propagate(T.par[id]>>1)\n  \
    \  \n    def _validate(T, id = None):\n        if id is None:\n            assert\
    \ T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)\n\
    \            return acc\n        assert ~T.par[id]\n        assert T.sub[T.par[id]]\
    \ == id\n        acc = T.V[id]\n        if ~(l:=T.sub[id<<1]):\n            assert\
    \ T.P[id] <= T.P[l]\n            assert T.K[l] <= T.K[id]\n            acc = T.op(T._validate(l),\
    \ acc)\n        if ~(r:=T.sub[id<<1|1]):\n            assert T.P[id] <= T.P[r]\n\
    \            assert T.K[id] <= T.K[r]\n            acc = T.op(acc, T._validate(r))\n\
    \        assert T.A[id] == acc\n        return acc\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nimport cp_library.ds.tree.__header__\n\nclass TreapMonoid:\n\
    \    __slots__ = 'op', 'e', 'root', 'cnt'\n    # class attributes\n    K, V, A,\
    \ P = [-1], [-1], [-1], [42]\n    par, sub, st = [-1], [-1, -1], []\n\n    def\
    \ __init__(T, op, e = -1):\n        T.op, T.e, T.cnt = op, e, -1\n        T.root\
    \ = T.new_node(-1, e)\n\n    def prod(T, l: int, r: int):\n        # find_node\
    \ common ancestor\n        a = T.sub[T.root<<1]\n        while ~a and not l <=\
    \ T.K[a] < r: a = T.sub[a<<1|(T.K[a]<l)]\n        if a < 0: return T.e\n     \
    \   # left subtreap\n        acc, i = T.V[a], T.sub[a<<1]\n        while ~i:\n\
    \            if not (T.K[i]<l):\n                if ~T.sub[i<<1|1]: acc = T.op(T.A[T.sub[i<<1|1]],\
    \ acc)\n                acc = T.op(T.V[i], acc)\n            i = T.sub[i<<1|(T.K[i]<l)]\n\
    \        # right subtreap\n        i = T.sub[a<<1|1]\n        while ~i:\n    \
    \        if T.K[i]<r:\n                if ~T.sub[i<<1]: acc = T.op(acc, T.A[T.sub[i<<1]])\n\
    \                acc = T.op(acc, T.V[i])\n            i = T.sub[i<<1|(T.K[i]<r)]\n\
    \        return acc\n\n    def all_prod(T): return T.A[T.root]\n    \n    def\
    \ insert(T, key, val):\n        T.insert_node(T.root<<1, nid := T.new_node(key,\
    \ val))\n        return nid\n    \n    def split(T, key):\n        T.K[0] = key\n\
    \        T.split_node(T.sub[T.root<<1], 0)\n        S = T.__class__(T.op, T.e)\n\
    \        if ~S.sub[0]: S.attach_node(S.root<<1, T.sub[0])\n        if ~T.sub[1]:\
    \ T.attach_node(T.root<<1, T.sub[1])\n        T._repair()\n        return S, T\n\
    \    \n    def get(T, key): return T.V[id] if ~(id:=T.find_node(key)) else T.e\n\
    \n    def pop(T, key):\n        if ~(id:=T.find_node(key)): T.del_node(id); return\
    \ T.V[id]\n        return T.e\n\n    def __delitem__(T, key):\n        if ~(id:=T.find_node(key)):\
    \ T.del_node(id)\n    \n    def __setitem__(T, key, val):\n        if ~(id:=T.find_node(key)):\
    \ T.set_node(id, val)\n        else: T.insert(key, val)\n    \n    def __getitem__(T,\
    \ key):\n        if isinstance(key, int): return T.get(key)\n        elif isinstance(key,\
    \ slice): return T.prod(key.start, key.stop)\n    \n    def __contains__(T, key):\
    \ return 0 <= T.find_node(key)\n\n    def __len__(T): return T.cnt\n\n    def\
    \ new_node(T, key, val):\n        id = len(T.K)\n        T.K.append(key); T.V.append(val);\
    \ T.A.append(val)\n        T.P.append((T.P[-1] * 1103515245 + 12345) & 0x7fffffff)\n\
    \        T.par.append(-1); T.sub.append(-1); T.sub.append(-1)\n        T.cnt +=\
    \ 1\n        return id\n\n    def find_node(T, key: int):\n        id = T.sub[T.root<<1]\n\
    \        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n     \
    \   return id\n    \n    def insert_node(T, sid, nid):\n        while ~T.sub[sid]\
    \ and T.P[id:=T.sub[sid]]<T.P[nid]:sid=id<<1|(T.K[id]<T.K[nid])\n        id =\
    \ T.sub[sid]; T.attach_node(sid, nid)\n        if ~id: T.split_node(id, nid)\n\
    \        T._repair()\n    \n    def split_node(T, id, nid):\n        l, r = nid<<1,\
    \ nid<<1|1\n        while ~id:\n            if T.K[id] < T.K[nid]: T.attach_node(l,\
    \ id); id = T.sub[l := id<<1|1]\n            else: T.attach_node(r, id); id =\
    \ T.sub[r := id<<1]\n        T.st.append(l>>1); T.st.append(r>>1)\n        T.sub[l]\
    \ = T.sub[r] = -1\n        T._repair()\n\n    def set_node(T, id: int, val): T.V[id]\
    \ = val; T._propagate(id)\n\n    def merge_nodes(T, sid: int, l: int, r: int):\n\
    \        while ~l and ~r:\n            if T.P[l]<T.P[r]: T.attach_node(sid, l);\
    \ l = T.sub[sid := l<<1|1]\n            else: T.attach_node(sid, r); r = T.sub[sid\
    \ := r<<1]\n        if ~l: T.attach_node(sid, l)\n        elif ~r: T.attach_node(sid,\
    \ r)\n        T._repair()\n\n    def del_node(T, id: int):\n        sid, l, r\
    \ = T.par[id], T.sub[id<<1], T.sub[id<<1|1]\n        T.detach_node(id)\n     \
    \   T.merge_nodes(sid, l, r)\n        T.cnt -= 1\n    \n    def detach_node(T,\
    \ id: int):\n        assert ~T.par[id]\n        T.st.append(T.par[id]>>1)\n  \
    \      T.sub[T.par[id]] = T.par[id] = -1\n    \n    def attach_node(T, sid: int,\
    \ id: int):\n        T.st.append(sid>>1)\n        T.sub[sid], T.par[id] = id,\
    \ sid\n\n    @classmethod\n    def reserve(cls, hint: int):\n        hint += 1\n\
    \        reserve(cls.K, hint); reserve(cls.V, hint); reserve(cls.A, hint); reserve(cls.P,\
    \ hint)\n        reserve(cls.par, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)\n    \n    def _update(T, id):\n        T.A[id] = T.V[id]\n\
    \        if ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])\n        if\
    \ ~(r := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])\n        \n    def _propagate(T,\
    \ id):\n        while ~T.par[id]: T._update(id); id = T.par[id]>>1\n        T._update(id)\n\
    \n    def _repair(T):\n        if T.st:\n            while T.st: T._update(id\
    \ := T.st.pop())\n            if id != T.root: T._propagate(T.par[id]>>1)\n  \
    \  \n    def _validate(T, id = None):\n        if id is None:\n            assert\
    \ T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)\n\
    \            return acc\n        assert ~T.par[id]\n        assert T.sub[T.par[id]]\
    \ == id\n        acc = T.V[id]\n        if ~(l:=T.sub[id<<1]):\n            assert\
    \ T.P[id] <= T.P[l]\n            assert T.K[l] <= T.K[id]\n            acc = T.op(T._validate(l),\
    \ acc)\n        if ~(r:=T.sub[id<<1|1]):\n            assert T.P[id] <= T.P[r]\n\
    \            assert T.K[id] <= T.K[r]\n            acc = T.op(acc, T._validate(r))\n\
    \        assert T.A[id] == acc\n        return acc\n"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/treap_monoid_cls.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
documentation_of: cp_library/ds/tree/treap_monoid_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/treap_monoid_cls.py
- /library/cp_library/ds/tree/treap_monoid_cls.py.html
title: cp_library/ds/tree/treap_monoid_cls.py
---
