---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_cls.py
    title: cp_library/ds/heap/skew_heap_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/directedmst
    links:
    - https://judge.yosupo.jp/problem/directedmst
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    import os,sys,io\ninput=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\n\
    \nclass UnionFind:\n    def __init__(self, n):\n        self.parent = [-1] * n\n\
    \        self.n = n\n\n    def root(self, x):\n        if self.parent[x] < 0:\n\
    \            return x\n        else:\n            self.parent[x] = self.root(self.parent[x])\n\
    \            return self.parent[x]\n\n    def merge(self, x, y):\n        x =\
    \ self.root(x)\n        y = self.root(y)\n        if x == y:\n            return\
    \ False\n        self.parent[x] += self.parent[y]\n        self.parent[y] = x\n\
    \        return True\n\n    def same(self, x, y):\n        return self.root(x)\
    \ == self.root(y)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\nimport operator\nfrom typing import Generic, TypeVar\n_T = TypeVar('T')\n\
    _U = TypeVar('U')\n\n\n_TSkewHeap = TypeVar(\"SkewHeap\", bound=\"SkewHeap\")\n\
    class SkewHeap(Generic[_T]):\n    __slots__ = 'root', 'op', 'e'\n    V, A, L,\
    \ R, st = [-1], [-1], [-1], [-1], []\n    def __init__(H, op = operator.add, e:\
    \ _T = 0):\n        H.root, H.op, H.e = -1, op, e\n    \n    def merge(H: _TSkewHeap,\
    \ O: _TSkewHeap):\n        H.root = H.merge_nodes(H.root, O.root)\n        O.root\
    \ = -1\n\n    def min(H):\n        assert ~H.root\n        H.propagate(H.root)\n\
    \        return H.V[H.root]\n\n    def push(H, x: _T):\n        id = len(H.V)\n\
    \        H.V.append(x); H.A.append(H.e); H.L.append(-1); H.R.append(-1)\n    \
    \    H.root = H.merge_nodes(H.root, id)\n\n    def pop(H) -> _T:\n        assert\
    \ ~H.root\n        H.propagate(H.root)\n        val, H.root = H.V[H.root], H.merge_nodes(H.L[H.root],\
    \ H.R[H.root])\n        return val\n    \n    def add(H, val: _T): H.A[H.root]\
    \ = H.op(H.A[H.root], val)\n    def empty(H): return H.root == -1\n    def __bool__(H):\
    \ return H.root != -1\n    \n    def propagate(H, u: int):\n        if (a := H.A[u])\
    \ != H.e:\n            if ~(l := H.L[u]): H.A[l] = H.op(H.A[l], a)\n         \
    \   if ~(r := H.R[u]): H.A[r] = H.op(H.A[r], a)\n            H.V[u] = H.op(H.V[u],\
    \ a); H.A[u] = H.e\n\n    def merge_nodes(H, u: int, v:int):\n        while ~u\
    \ and ~v:\n            H.propagate(u); H.propagate(v)\n            if H.V[v] <\
    \ H.V[u]: u, v = v, u\n            H.st.append(u); H.R[u], u = H.L[u], H.R[u]\n\
    \        u = u if ~u else v\n        while H.st: H.L[u := H.st.pop()] = u\n  \
    \      return u\n\ndef directed_mst(n, edges, root):\n    OFFSET = 1 << 31\n \
    \   from_cost = [0] * n\n    from_heap = [SkewHeap() for _ in range(n)]\n    from_\
    \ = [0] * n\n\n    uf = UnionFind(n)\n    par_e = [-1] * m\n    stem = [-1] *\
    \ n\n    used = [0] * n\n    used[root] = 2\n    idxs = []\n\n    for idx, (fr,\
    \ to, cost) in enumerate(edges):\n        from_heap[to].push(cost << 31 | idx)\n\
    \n    res = 0\n    for v in range(n):\n        if used[v] != 0:\n            continue\n\
    \        processing = []\n        chi_e = []\n        cycle = 0\n        while\
    \ used[v] != 2:\n            used[v] = 1\n            processing.append(v)\n \
    \           if from_heap[v].empty(): return -1, par\n            from_cost[v],\
    \ idx = divmod(from_heap[v].pop(), OFFSET)\n            from_[v] = uf.root(edges[idx][0])\n\
    \            if stem[v] == -1:\n                stem[v] = idx\n            if\
    \ from_[v] == v: continue\n            res += from_cost[v]\n            idxs.append(idx)\n\
    \            while cycle:\n                par_e[chi_e.pop()] = idx\n        \
    \        cycle -= 1\n            chi_e.append(idx)\n            if used[from_[v]]\
    \ == 1:\n                p = v\n                while True:\n                \
    \    if from_heap[p]: from_heap[p].add(-from_cost[p] << 31)\n                \
    \    if p != v:\n                        uf.merge(v, p)\n                    \
    \    from_heap[v].merge(from_heap[p])\n                    p = uf.root(from_[p])\n\
    \                    cycle += 1\n                    if p == v:\n            \
    \            break\n            else:\n                v = from_[v]\n        for\
    \ v in processing: used[v] = 2\n\n    used_e = [0] * m\n    tree = [-1] * n\n\
    \    for idx in reversed(idxs):\n        if used_e[idx]: continue\n        fr,\
    \ to, cost = edges[idx]\n        tree[to] = fr\n        x = stem[to]\n       \
    \ while x != idx:\n            used_e[x] = 1\n            x = par_e[x]\n    return\
    \ res, tree\n\n\nn, m, root = map(int, input().split())\nedges = [[int(s) for\
    \ s in input().split()] for i in range(m)]\n\n\nres, par = directed_mst(n, edges,\
    \ root)\nif res == -1:\n    print(res)\nelse:\n    print(res)\n    print(*[p if\
    \ p != -1 else i for i, p in enumerate(par)])\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    import os,sys,io\ninput=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\n\
    \nclass UnionFind:\n    def __init__(self, n):\n        self.parent = [-1] * n\n\
    \        self.n = n\n\n    def root(self, x):\n        if self.parent[x] < 0:\n\
    \            return x\n        else:\n            self.parent[x] = self.root(self.parent[x])\n\
    \            return self.parent[x]\n\n    def merge(self, x, y):\n        x =\
    \ self.root(x)\n        y = self.root(y)\n        if x == y:\n            return\
    \ False\n        self.parent[x] += self.parent[y]\n        self.parent[y] = x\n\
    \        return True\n\n    def same(self, x, y):\n        return self.root(x)\
    \ == self.root(y)\n\nfrom cp_library.ds.heap.skew_heap_cls import SkewHeap\n\n\
    def directed_mst(n, edges, root):\n    OFFSET = 1 << 31\n    from_cost = [0] *\
    \ n\n    from_heap = [SkewHeap() for _ in range(n)]\n    from_ = [0] * n\n\n \
    \   uf = UnionFind(n)\n    par_e = [-1] * m\n    stem = [-1] * n\n    used = [0]\
    \ * n\n    used[root] = 2\n    idxs = []\n\n    for idx, (fr, to, cost) in enumerate(edges):\n\
    \        from_heap[to].push(cost << 31 | idx)\n\n    res = 0\n    for v in range(n):\n\
    \        if used[v] != 0:\n            continue\n        processing = []\n   \
    \     chi_e = []\n        cycle = 0\n        while used[v] != 2:\n           \
    \ used[v] = 1\n            processing.append(v)\n            if from_heap[v].empty():\
    \ return -1, par\n            from_cost[v], idx = divmod(from_heap[v].pop(), OFFSET)\n\
    \            from_[v] = uf.root(edges[idx][0])\n            if stem[v] == -1:\n\
    \                stem[v] = idx\n            if from_[v] == v: continue\n     \
    \       res += from_cost[v]\n            idxs.append(idx)\n            while cycle:\n\
    \                par_e[chi_e.pop()] = idx\n                cycle -= 1\n      \
    \      chi_e.append(idx)\n            if used[from_[v]] == 1:\n              \
    \  p = v\n                while True:\n                    if from_heap[p]: from_heap[p].add(-from_cost[p]\
    \ << 31)\n                    if p != v:\n                        uf.merge(v,\
    \ p)\n                        from_heap[v].merge(from_heap[p])\n             \
    \       p = uf.root(from_[p])\n                    cycle += 1\n              \
    \      if p == v:\n                        break\n            else:\n        \
    \        v = from_[v]\n        for v in processing: used[v] = 2\n\n    used_e\
    \ = [0] * m\n    tree = [-1] * n\n    for idx in reversed(idxs):\n        if used_e[idx]:\
    \ continue\n        fr, to, cost = edges[idx]\n        tree[to] = fr\n       \
    \ x = stem[to]\n        while x != idx:\n            used_e[x] = 1\n         \
    \   x = par_e[x]\n    return res, tree\n\n\nn, m, root = map(int, input().split())\n\
    edges = [[int(s) for s in input().split()] for i in range(m)]\n\n\nres, par =\
    \ directed_mst(n, edges, root)\nif res == -1:\n    print(res)\nelse:\n    print(res)\n\
    \    print(*[p if p != -1 else i for i, p in enumerate(par)])"
  dependsOn:
  - cp_library/ds/heap/skew_heap_cls.py
  isVerificationFile: true
  path: test/library-checker/graph/directedmst.test.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/directedmst.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/directedmst.test.py
- /verify/test/library-checker/graph/directedmst.test.py.html
title: test/library-checker/graph/directedmst.test.py
---
