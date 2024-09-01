---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_heap_fn.py
    title: cp_library/alg/graph/kruskal_heap_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/inf_cnst.py
    title: cp_library/misc/inf_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    inf = float('inf')\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\ndef read_edges(M, i0=1):\n    E = []\n    for _\
    \ in range(M):\n        u,v,w = rint(-i0)\n        w += i0\n        E.append((w,u,v))\n\
    \    return E\nfrom heapq import heapify, heappop\n\nclass DSU:\n    def __init__(self,\
    \ n) -> None:\n        self.n = n\n        self.par = [-1] * n\n\n    def merge(self,\
    \ u, v) -> int:\n        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\
    \n        x, y = self.leader(u), self.leader(v)\n        if x == y: return x\n\
    \n        if -self.par[x] < -self.par[y]:\n            x, y = y, x\n\n       \
    \ self.par[x] += self.par[y]\n        self.par[y] = x\n\n        return x\n\n\
    \    def same(self, u: int, v: int) -> bool:\n        assert 0 <= u < self.n\n\
    \        assert 0 <= v < self.n\n        return self.leader(u) == self.leader(v)\n\
    \n    def leader(self, i) -> int:\n        assert 0 <= i < self.n\n\n        p\
    \ = self.par[i]\n        while p >= 0:\n            if self.par[p] < 0:\n    \
    \            return p\n            self.par[i], i, p = self.par[p], self.par[p],\
    \ self.par[self.par[p]]\n\n        return i\n\n    def size(self, i) -> int:\n\
    \        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\ndef kruskal(N, M, E):\n \
    \   heapify(E)\n    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and\
    \ need > 0:\n        edge = heappop(E)\n        _,u,v = edge\n        if not dsu.same(u,v):\n\
    \            dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n\nN, M = rint()\nE = read_edges(M, 0)\nMST = kruskal(N, M,\
    \ E)\nans = sum(w for w,u,v in MST)\nprint(ans)\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

    from cp_library.misc.inf_cnst import inf

    from cp_library.io.rint_fn import rint

    from cp_library.io.read_edges_weighted_fn import read_edges

    from cp_library.alg.graph.kruskal_heap_fn import kruskal


    N, M = rint()

    E = read_edges(M, 0)

    MST = kruskal(N, M, E)

    ans = sum(w for w,u,v in MST)

    print(ans)'
  dependsOn:
  - cp_library/misc/inf_cnst.py
  - cp_library/io/rint_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/kruskal_heap_fn.py
  - cp_library/ds/dsu_cls.py
  isVerificationFile: true
  path: test/grl_2_a_kruskal_heap.test.py
  requiredBy: []
  timestamp: '2024-09-02 01:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_a_kruskal_heap.test.py
layout: document
redirect_from:
- /verify/test/grl_2_a_kruskal_heap.test.py
- /verify/test/grl_2_a_kruskal_heap.test.py.html
title: test/grl_2_a_kruskal_heap.test.py
---
