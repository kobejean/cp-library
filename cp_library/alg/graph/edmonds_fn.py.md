---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: cp_library/alg/graph/floyds_cycle_fn.py
    title: cp_library/alg/graph/floyds_cycle_fn.py
  - icon: ':question:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "from functools import reduce\nfrom heapq import heapify\nfrom math\
    \ import inf\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\nclass DSU:\n    def __init__(self, n) -> None:\n\
    \        self.n = n\n        self.par = [-1] * n\n\n    def merge(self, u, v)\
    \ -> int:\n        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\n\
    \        x, y = self.leader(u), self.leader(v)\n        if x == y: return x\n\n\
    \        if -self.par[x] < -self.par[y]:\n            x, y = y, x\n\n        self.par[x]\
    \ += self.par[y]\n        self.par[y] = x\n\n        return x\n\n    def same(self,\
    \ u: int, v: int) -> bool:\n        assert 0 <= u < self.n\n        assert 0 <=\
    \ v < self.n\n        return self.leader(u) == self.leader(v)\n\n    def leader(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n\n        p = self.par[i]\n    \
    \    while p >= 0:\n            if self.par[p] < 0:\n                return p\n\
    \            self.par[i], i, p = self.par[p], self.par[p], self.par[self.par[p]]\n\
    \n        return i\n\n    def size(self, i) -> int:\n        assert 0 <= i < self.n\n\
    \        \n        return -self.par[self.leader(i)]\n\n    def groups(self) ->\
    \ list[list[int]]:\n        leader_buf = [self.leader(i) for i in range(self.n)]\n\
    \n        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n\ndef floyds_cycle(F, root):\n    slow = fast = root\n    while\
    \ F[fast] != -1 and F[F[fast]] != -1:\n        slow, fast = F[slow], F[F[fast]]\n\
    \        if slow == fast:\n            cyc = [slow]\n            while F[slow]\
    \ != cyc[0]:\n                slow = F[slow]\n                cyc.append(slow)\n\
    \            return cyc\n    return None\n\ndef edmonds_branching(E, N, root)\
    \ -> list[tuple[any,int,int]]:\n    # obtain incoming edges\n    Gin = [[] for\
    \ _ in range(N)]\n    for id,(w,u,v) in enumerate(E):\n        if v != root:\n\
    \            Gin[v].append([w,u,id])\n    \n\n    # heapify for fast access to\
    \ optimal edges\n    for v in range(N):\n        heapify(Gin[v])\n\n    groups\
    \ = DSU(N)\n    active = set(range(N))\n    active.discard(root)\n\n    def find_cycle(min_in):\n\
    \        for v in active:\n            cyc = floyds_cycle(min_in, v)\n       \
    \     if cyc: return cyc\n        return None\n    \n    def contract(cyc):\n\
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
  code: "from functools import reduce\nfrom heapq import heapify\nfrom math import\
    \ inf\nimport cp_library.misc.setrecursionlimit\nfrom cp_library.ds.dsu_cls import\
    \ DSU\nfrom cp_library.alg.graph.floyds_cycle_fn import floyds_cycle\n\ndef edmonds_branching(E,\
    \ N, root) -> list[tuple[any,int,int]]:\n    # obtain incoming edges\n    Gin\
    \ = [[] for _ in range(N)]\n    for id,(w,u,v) in enumerate(E):\n        if v\
    \ != root:\n            Gin[v].append([w,u,id])\n    \n\n    # heapify for fast\
    \ access to optimal edges\n    for v in range(N):\n        heapify(Gin[v])\n\n\
    \    groups = DSU(N)\n    active = set(range(N))\n    active.discard(root)\n\n\
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
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_2_b_edmonds_branching.test.py
documentation_of: cp_library/alg/graph/edmonds_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edmonds_fn.py
- /library/cp_library/alg/graph/edmonds_fn.py.html
title: cp_library/alg/graph/edmonds_fn.py
---
