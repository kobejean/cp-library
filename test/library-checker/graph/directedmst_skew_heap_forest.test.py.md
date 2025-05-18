---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_forest_cls.py
    title: cp_library/ds/heap/skew_heap_forest_cls.py
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
    \        \n'''\nimport operator\nfrom typing import Generic\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\n\ndef elist(est_len: int) ->\
    \ list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\n\nclass SkewHeapForest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n        shf.V, shf.A,\
    \ shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N\n        shf.id,\
    \ shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n    def propagate(shf, u:\
    \ int):\n        if (a := shf.A[u]) != shf.e:\n            if ~(l := shf.L[u]):\
    \ shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r := shf.R[u]): shf.A[r] =\
    \ shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] =\
    \ shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u and ~v:\n   \
    \         shf.propagate(u); shf.propagate(v)\n            if shf.V[v] < shf.V[u]:\
    \ u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]\n\
    \        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()] =\
    \ u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.id = (id := shf.id)+1\n      \
    \  shf.V[id] = x\n        shf.roots[i] = shf.merge(shf.roots[i], id)\n\n    def\
    \ pop(shf, i: int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    \n\ndef directed_mst(n, edges, root):\n    OFFSET = 1 << 31\n   \
    \ from_cost = [0] * n\n    from_heap = SkewHeapForest(n, len(edges))\n    from_\
    \ = [0] * n\n\n    uf = UnionFind(n)\n    par_e = [-1] * m\n    stem = [-1] *\
    \ n\n    used = [0] * n\n    used[root] = 2\n    idxs = []\n\n    for idx, (fr,\
    \ to, cost) in enumerate(edges):\n        from_heap.push(to, cost << 31 | idx)\n\
    \n    res = 0\n    for v in range(n):\n        if used[v] != 0:\n            continue\n\
    \        processing = []\n        chi_e = []\n        cycle = 0\n        while\
    \ used[v] != 2:\n            used[v] = 1\n            processing.append(v)\n \
    \           if from_heap.empty(v):\n               return -1, par\n          \
    \  from_cost[v], idx = divmod(from_heap.pop(v), OFFSET)\n            from_[v]\
    \ = uf.root(edges[idx][0])\n            if stem[v] == -1:\n                stem[v]\
    \ = idx\n            if from_[v] == v:\n                continue\n           \
    \ res += from_cost[v]\n            idxs.append(idx)\n            while cycle:\n\
    \                par_e[chi_e.pop()] = idx\n                cycle -= 1\n      \
    \      chi_e.append(idx)\n            if used[from_[v]] == 1:\n              \
    \  p = v\n                while True:\n                    if not from_heap.empty(p):\n\
    \                        from_heap.add(p, -from_cost[p] << 31)\n             \
    \       if p != v:\n                        uf.merge(v, p)\n                 \
    \       from_heap.roots[v] = from_heap.merge(from_heap.roots[v], from_heap.roots[p])\n\
    \                    p = uf.root(from_[p])\n                    cycle += 1\n \
    \                   if p == v:\n                        break\n            else:\n\
    \                v = from_[v]\n        for v in processing:\n            used[v]\
    \ = 2\n\n    used_e = [0] * m\n    tree = [-1] * n\n    for idx in reversed(idxs):\n\
    \        if used_e[idx]:\n            continue\n        fr, to, cost = edges[idx]\n\
    \        tree[to] = fr\n        x = stem[to]\n        while x != idx:\n      \
    \      used_e[x] = 1\n            x = par_e[x]\n    return res, tree\n\n\nn, m,\
    \ root = map(int, input().split())\nedges = [[int(s) for s in input().split()]\
    \ for i in range(m)]\n\n\nres, par = directed_mst(n, edges, root)\nif res == -1:\n\
    \    print(res)\nelse:\n    print(res)\n    print(*[p if p != -1 else i for i,\
    \ p in enumerate(par)])\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    import os,sys,io\ninput=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\n\
    \nclass UnionFind:\n    def __init__(self, n):\n        self.parent = [-1] * n\n\
    \        self.n = n\n\n    def root(self, x):\n        if self.parent[x] < 0:\n\
    \            return x\n        else:\n            self.parent[x] = self.root(self.parent[x])\n\
    \            return self.parent[x]\n\n    def merge(self, x, y):\n        x =\
    \ self.root(x)\n        y = self.root(y)\n        if x == y:\n            return\
    \ False\n        self.parent[x] += self.parent[y]\n        self.parent[y] = x\n\
    \        return True\n\n    def same(self, x, y):\n        return self.root(x)\
    \ == self.root(y)\n\nfrom cp_library.ds.heap.skew_heap_forest_cls import SkewHeapForest\n\
    \ndef directed_mst(n, edges, root):\n    OFFSET = 1 << 31\n    from_cost = [0]\
    \ * n\n    from_heap = SkewHeapForest(n, len(edges))\n    from_ = [0] * n\n\n\
    \    uf = UnionFind(n)\n    par_e = [-1] * m\n    stem = [-1] * n\n    used =\
    \ [0] * n\n    used[root] = 2\n    idxs = []\n\n    for idx, (fr, to, cost) in\
    \ enumerate(edges):\n        from_heap.push(to, cost << 31 | idx)\n\n    res =\
    \ 0\n    for v in range(n):\n        if used[v] != 0:\n            continue\n\
    \        processing = []\n        chi_e = []\n        cycle = 0\n        while\
    \ used[v] != 2:\n            used[v] = 1\n            processing.append(v)\n \
    \           if from_heap.empty(v):\n               return -1, par\n          \
    \  from_cost[v], idx = divmod(from_heap.pop(v), OFFSET)\n            from_[v]\
    \ = uf.root(edges[idx][0])\n            if stem[v] == -1:\n                stem[v]\
    \ = idx\n            if from_[v] == v:\n                continue\n           \
    \ res += from_cost[v]\n            idxs.append(idx)\n            while cycle:\n\
    \                par_e[chi_e.pop()] = idx\n                cycle -= 1\n      \
    \      chi_e.append(idx)\n            if used[from_[v]] == 1:\n              \
    \  p = v\n                while True:\n                    if not from_heap.empty(p):\n\
    \                        from_heap.add(p, -from_cost[p] << 31)\n             \
    \       if p != v:\n                        uf.merge(v, p)\n                 \
    \       from_heap.roots[v] = from_heap.merge(from_heap.roots[v], from_heap.roots[p])\n\
    \                    p = uf.root(from_[p])\n                    cycle += 1\n \
    \                   if p == v:\n                        break\n            else:\n\
    \                v = from_[v]\n        for v in processing:\n            used[v]\
    \ = 2\n\n    used_e = [0] * m\n    tree = [-1] * n\n    for idx in reversed(idxs):\n\
    \        if used_e[idx]:\n            continue\n        fr, to, cost = edges[idx]\n\
    \        tree[to] = fr\n        x = stem[to]\n        while x != idx:\n      \
    \      used_e[x] = 1\n            x = par_e[x]\n    return res, tree\n\n\nn, m,\
    \ root = map(int, input().split())\nedges = [[int(s) for s in input().split()]\
    \ for i in range(m)]\n\n\nres, par = directed_mst(n, edges, root)\nif res == -1:\n\
    \    print(res)\nelse:\n    print(res)\n    print(*[p if p != -1 else i for i,\
    \ p in enumerate(par)])"
  dependsOn:
  - cp_library/ds/heap/skew_heap_forest_cls.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: true
  path: test/library-checker/graph/directedmst_skew_heap_forest.test.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/directedmst_skew_heap_forest.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/directedmst_skew_heap_forest.test.py
- /verify/test/library-checker/graph/directedmst_skew_heap_forest.test.py.html
title: test/library-checker/graph/directedmst_skew_heap_forest.test.py
---
