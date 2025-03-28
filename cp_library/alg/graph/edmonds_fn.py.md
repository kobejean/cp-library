---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyds_cycle_fn.py
    title: cp_library/alg/graph/floyds_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_b_edmonds_branching.test.py
    title: test/aoj/grl/grl_2_b_edmonds_branching.test.py
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
    from functools import reduce\nfrom heapq import heapify\n\n\nimport sys\nsys.setrecursionlimit(10**6)\n\
    import pypyjit\npypyjit.set_param(\"max_unroll_recursion=-1\")\n\n\nclass DSU:\n\
    \    def __init__(self, N):\n        self.N = N\n        self.par = [-1] * N\n\
    \n    def merge(self, u, v, src = False):\n        assert 0 <= u < self.N\n  \
    \      assert 0 <= v < self.N\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return (x,y) if src else x\n\n        if self.par[x] > self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n\
    \        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n        return\
    \ self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n      \
    \  assert 0 <= i < self.N\n        par = self.par\n        p = par[i]\n      \
    \  while p >= 0:\n            if par[p] < 0:\n                return p\n     \
    \       par[i], i, p = par[p], par[p], par[par[p]]\n\n        return i\n\n   \
    \ def size(self, i) -> int:\n        assert 0 <= i < self.N\n        \n      \
    \  return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        leader_buf = [self.leader(i) for i in range(self.N)]\n\n        result\
    \ = [[] for _ in range(self.N)]\n        for i in range(self.N):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return [r for r in result if r]\n\
    \ndef floyds_cycle(F, root):\n    slow = fast = root\n    while F[fast] != -1\
    \ and F[F[fast]] != -1:\n        slow, fast = F[slow], F[F[fast]]\n        if\
    \ slow == fast:\n            cyc = [slow]\n            while F[slow] != cyc[0]:\n\
    \                slow = F[slow]\n                cyc.append(slow)\n          \
    \  return cyc\n    return None\n\ndef edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:\n\
    \    # obtain incoming edges\n    Gin = [[] for _ in range(N)]\n    for id,(u,v,w)\
    \ in enumerate(E):\n        if v != root:\n            Gin[v].append([w,u,id])\n\
    \    \n\n    # heapify for fast access to optimal edges\n    for v in range(N):\n\
    \        heapify(Gin[v])\n\n    groups = DSU(N)\n    active = set(range(N))\n\
    \    active.discard(root)\n\n    def find_cycle(min_in):\n        for v in active:\n\
    \            cyc = floyds_cycle(min_in, v)\n            if cyc: return cyc\n \
    \       return None\n    \n    def contract(cyc):\n        kickout = [-1]*len(E)\n\
    \        active.difference_update(cyc)\n        nv = reduce(groups.merge, cyc)\n\
    \        active.add(nv)\n        new_edges = []\n        \n        # Update Gin\
    \ to reflect the contracted cycle\n        for v in cyc:\n            cw, _, cid\
    \ = Gin[v][0]\n            for edge in Gin[v]:\n                _, u, id = edge\n\
    \                if groups.leader(u) != nv:\n                    edge[0] -= cw\
    \ # update weight\n                    kickout[id] = cid\n                   \
    \ new_edges.append(edge)\n                    if new_edges[-1][0] < new_edges[0][0]:\n\
    \                        new_edges[0], new_edges[-1] = new_edges[-1], new_edges[0]\n\
    \            Gin[v].clear()\n        Gin[nv] = new_edges\n        return kickout\n\
    \n\n    def rec(Gin):\n        min_in = [groups.leader(Gin[v][0][1]) if Gin[v]\
    \ else -1 for v in range(N)]\n        cyc = find_cycle(min_in)\n        if cyc:\n\
    \            C = { Gin[v][0][2] for v in cyc }\n            kickout = contract(cyc)\n\
    \            MCA = rec(Gin)\n            for id in MCA:\n                C.discard(kickout[id])\n\
    \            MCA.extend(C)\n            return MCA\n        else:\n          \
    \  return [edges[0][2] for edges in Gin if edges]\n\n    return [E[id] for id\
    \ in rec(Gin)]\n"
  code: "import cp_library.alg.graph.__header__\nfrom functools import reduce\nfrom\
    \ heapq import heapify\nimport cp_library.misc.setrecursionlimit\nfrom cp_library.ds.dsu_cls\
    \ import DSU\nfrom cp_library.alg.graph.floyds_cycle_fn import floyds_cycle\n\n\
    def edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:\n    # obtain incoming\
    \ edges\n    Gin = [[] for _ in range(N)]\n    for id,(u,v,w) in enumerate(E):\n\
    \        if v != root:\n            Gin[v].append([w,u,id])\n    \n\n    # heapify\
    \ for fast access to optimal edges\n    for v in range(N):\n        heapify(Gin[v])\n\
    \n    groups = DSU(N)\n    active = set(range(N))\n    active.discard(root)\n\n\
    \    def find_cycle(min_in):\n        for v in active:\n            cyc = floyds_cycle(min_in,\
    \ v)\n            if cyc: return cyc\n        return None\n    \n    def contract(cyc):\n\
    \        kickout = [-1]*len(E)\n        active.difference_update(cyc)\n      \
    \  nv = reduce(groups.merge, cyc)\n        active.add(nv)\n        new_edges =\
    \ []\n        \n        # Update Gin to reflect the contracted cycle\n       \
    \ for v in cyc:\n            cw, _, cid = Gin[v][0]\n            for edge in Gin[v]:\n\
    \                _, u, id = edge\n                if groups.leader(u) != nv:\n\
    \                    edge[0] -= cw # update weight\n                    kickout[id]\
    \ = cid\n                    new_edges.append(edge)\n                    if new_edges[-1][0]\
    \ < new_edges[0][0]:\n                        new_edges[0], new_edges[-1] = new_edges[-1],\
    \ new_edges[0]\n            Gin[v].clear()\n        Gin[nv] = new_edges\n    \
    \    return kickout\n\n\n    def rec(Gin):\n        min_in = [groups.leader(Gin[v][0][1])\
    \ if Gin[v] else -1 for v in range(N)]\n        cyc = find_cycle(min_in)\n   \
    \     if cyc:\n            C = { Gin[v][0][2] for v in cyc }\n            kickout\
    \ = contract(cyc)\n            MCA = rec(Gin)\n            for id in MCA:\n  \
    \              C.discard(kickout[id])\n            MCA.extend(C)\n           \
    \ return MCA\n        else:\n            return [edges[0][2] for edges in Gin\
    \ if edges]\n\n    return [E[id] for id in rec(Gin)]\n"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/floyds_cycle_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/edmonds_fn.py
  requiredBy: []
  timestamp: '2025-03-28 15:11:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_2_b_edmonds_branching.test.py
documentation_of: cp_library/alg/graph/edmonds_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edmonds_fn.py
- /library/cp_library/alg/graph/edmonds_fn.py.html
title: cp_library/alg/graph/edmonds_fn.py
---
