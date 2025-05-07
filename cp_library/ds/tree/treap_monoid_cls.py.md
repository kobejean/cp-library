---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
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
    \ = 'key', 'val', 'acc', 'prior', 'sub', 'e', 'op', 'rand', 'st1', 'st2'\n   \
    \ def __init__(T, e, op):\n        T.key = [-1]\n        T.val = [e]\n       \
    \ T.acc = [e]\n        T.prior = [42]\n        T.sub = [-1, -1]\n        T.e =\
    \ e\n        T.op = op\n        T.st1, T.st2 = [], []\n\n    def reserve(T, hint:\
    \ int):\n        hint += 1\n        reserve(T.key, hint)\n        reserve(T.val,\
    \ hint)\n        reserve(T.acc, hint)\n        reserve(T.prior, hint)\n      \
    \  reserve(T.sub, hint << 1)\n\n    def new_node(T, key, value, left = -1, right\
    \ = -1):\n        id = len(T.key)\n        T.key.append(key)\n        T.val.append(value)\n\
    \        T.acc.append(value)\n        T.prior.append((T.prior[-1] * 1103515245\
    \ + 12345) & 0x7fffffff)\n        T.sub.append(left); T.sub.append(right)\n  \
    \      return id\n    \n    def update(T, id):\n        T.acc[id] = T.val[id]\n\
    \        if (l := T.sub[id << 1]) >= 0:\n            T.acc[id] = T.op(T.acc[l],\
    \ T.acc[id])\n        if (r := T.sub[id<<1|1]) >= 0:\n            T.acc[id] =\
    \ T.op(T.acc[id], T.acc[r])\n\n    def split(T, id, key, l, r):\n        while\
    \ True:\n            if id < 0: T.sub[l] = T.sub[r] = -1; break\n            if\
    \ T.key[id] < key:\n                m = id << 1 | 1\n                T.st1.append((id,\
    \ l))\n                id, l, r = T.sub[m], m, r\n            else:\n        \
    \        m = id << 1\n                T.st1.append((id, r))\n                id,\
    \ l, r = T.sub[m], l, m\n        while T.st1:\n            id, sid = T.st1.pop()\n\
    \            T.sub[sid] = id\n            T.update(id)\n        # if id < 0: T.sub[l]\
    \ = T.sub[r] = -1; return\n        # elif T.key[id] < key:\n        #     m =\
    \ id << 1 | 1\n        #     T.split(T.sub[m], key, m, r); T.sub[l] = id\n   \
    \     # else:\n        #     m = id << 1\n        #     T.split(T.sub[m], key,\
    \ l, m); T.sub[r] = id\n        # T.update(id)\n\n    def insert(T, sid, nid):\n\
    \        while True:\n            if T.sub[sid] < 0:\n                T.sub[sid]\
    \ = nid; break\n            elif T.prior[nid] < T.prior[id := T.sub[sid]]:\n \
    \               T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid);\
    \ break\n            else:\n                T.st2.append(id)\n               \
    \ sid, nid = id << 1 | (T.key[id] < T.key[nid]), nid\n        while T.st2:\n \
    \           T.update(T.st2.pop())\n\n        # if T.sub[sid] < 0: T.sub[sid] =\
    \ nid\n        # elif T.prior[nid] < T.prior[id := T.sub[sid]]:\n        #   \
    \  T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid)\n\
    \        # else:\n        #     T.insert(id << 1 | (T.key[id] < T.key[nid]), nid);\
    \ T.update(id)\n\n    def add(T, key, value):\n        T.insert(0, T.new_node(key,\
    \ value))\n\n    def all_prod(T):\n        return T.acc[T.sub[0]] if T.sub[0]\
    \ >= 0 else T.e\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nimport cp_library.ds.tree.__header__\n\nclass TreapMonoid:\n\
    \    __slots__ = 'key', 'val', 'acc', 'prior', 'sub', 'e', 'op', 'rand', 'st1',\
    \ 'st2'\n    def __init__(T, e, op):\n        T.key = [-1]\n        T.val = [e]\n\
    \        T.acc = [e]\n        T.prior = [42]\n        T.sub = [-1, -1]\n     \
    \   T.e = e\n        T.op = op\n        T.st1, T.st2 = [], []\n\n    def reserve(T,\
    \ hint: int):\n        hint += 1\n        reserve(T.key, hint)\n        reserve(T.val,\
    \ hint)\n        reserve(T.acc, hint)\n        reserve(T.prior, hint)\n      \
    \  reserve(T.sub, hint << 1)\n\n    def new_node(T, key, value, left = -1, right\
    \ = -1):\n        id = len(T.key)\n        T.key.append(key)\n        T.val.append(value)\n\
    \        T.acc.append(value)\n        T.prior.append((T.prior[-1] * 1103515245\
    \ + 12345) & 0x7fffffff)\n        T.sub.append(left); T.sub.append(right)\n  \
    \      return id\n    \n    def update(T, id):\n        T.acc[id] = T.val[id]\n\
    \        if (l := T.sub[id << 1]) >= 0:\n            T.acc[id] = T.op(T.acc[l],\
    \ T.acc[id])\n        if (r := T.sub[id<<1|1]) >= 0:\n            T.acc[id] =\
    \ T.op(T.acc[id], T.acc[r])\n\n    def split(T, id, key, l, r):\n        while\
    \ True:\n            if id < 0: T.sub[l] = T.sub[r] = -1; break\n            if\
    \ T.key[id] < key:\n                m = id << 1 | 1\n                T.st1.append((id,\
    \ l))\n                id, l, r = T.sub[m], m, r\n            else:\n        \
    \        m = id << 1\n                T.st1.append((id, r))\n                id,\
    \ l, r = T.sub[m], l, m\n        while T.st1:\n            id, sid = T.st1.pop()\n\
    \            T.sub[sid] = id\n            T.update(id)\n        # if id < 0: T.sub[l]\
    \ = T.sub[r] = -1; return\n        # elif T.key[id] < key:\n        #     m =\
    \ id << 1 | 1\n        #     T.split(T.sub[m], key, m, r); T.sub[l] = id\n   \
    \     # else:\n        #     m = id << 1\n        #     T.split(T.sub[m], key,\
    \ l, m); T.sub[r] = id\n        # T.update(id)\n\n    def insert(T, sid, nid):\n\
    \        while True:\n            if T.sub[sid] < 0:\n                T.sub[sid]\
    \ = nid; break\n            elif T.prior[nid] < T.prior[id := T.sub[sid]]:\n \
    \               T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid);\
    \ break\n            else:\n                T.st2.append(id)\n               \
    \ sid, nid = id << 1 | (T.key[id] < T.key[nid]), nid\n        while T.st2:\n \
    \           T.update(T.st2.pop())\n\n        # if T.sub[sid] < 0: T.sub[sid] =\
    \ nid\n        # elif T.prior[nid] < T.prior[id := T.sub[sid]]:\n        #   \
    \  T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid)\n\
    \        # else:\n        #     T.insert(id << 1 | (T.key[id] < T.key[nid]), nid);\
    \ T.update(id)\n\n    def add(T, key, value):\n        T.insert(0, T.new_node(key,\
    \ value))\n\n    def all_prod(T):\n        return T.acc[T.sub[0]] if T.sub[0]\
    \ >= 0 else T.e\n"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/treap_monoid_cls.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/treap_monoid_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/treap_monoid_cls.py
- /library/cp_library/ds/tree/treap_monoid_cls.py.html
title: cp_library/ds/tree/treap_monoid_cls.py
---
