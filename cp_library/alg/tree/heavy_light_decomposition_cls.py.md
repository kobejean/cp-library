---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n\nclass HeavyLightDecomposition:\n    def __init__(self, T, r=0):\n\
    \        N = len(T)\n        # build\n        size = [1]*N\n        pos = [0]*N\n\
    \        par = [-1]*N\n        heavy = [-1]*N\n        head = [-1]*N\n       \
    \ depth = [0]*N\n        weights = [0]*N\n        order = [0]*N\n        time\
    \ = 0\n\n        stack = [(2,r,r), (0,r,-1)]\n        while stack:\n         \
    \   match stack.pop():\n                case 0, v, p: # dfs down\n           \
    \         par[v] = p\n                    stack.append((1, v, p))\n          \
    \          for c, w in T[v]:\n                        if c != p:\n           \
    \                 depth[c] = depth[v] + 1 \n                            weights[c]\
    \ = w\n                            stack.append((0, c, v))\n\n               \
    \ case 1, v, p: # dfs up\n                    l = -1\n                    for\
    \ c, w in T[v]:\n                        if c != p:\n                        \
    \    size[v] += size[c]\n                            if l == -1 or size[c] > size[l]:\n\
    \                                l = c\n                    heavy[v] = l\n\n \
    \               case 2, v, h: # decompose\n                    head[v] = h\n \
    \                   pos[v] = time\n                    order[time] = v\n     \
    \               p = par[v]\n                    time += 1\n                  \
    \  l = heavy[v]\n                    for c, _ in T[v]:\n                     \
    \   if c != p and c != l:\n                            stack.append((2, c, c))\n\
    \n                    if l != -1:\n                        stack.append((2, l,\
    \ h))\n        self.N = N\n        self.T = T\n        self.size = size\n    \
    \    self.pos = pos\n        self.par = par\n        self.heavy = heavy\n    \
    \    self.head = head\n        self.depth = depth\n        self.weights = weights\n\
    \        self.order = order\n\n    def path(self, u, v, exclude_lca=False):\n\
    \        head, depth, par, pos = self.head, self.depth, self.par, self.pos\n \
    \       while head[u] != head[v]:\n            if depth[head[u]] < depth[head[v]]:\n\
    \                u,v = v,u\n            yield pos[head[u]], pos[u]+1\n       \
    \     u = par[head[u]]\n\n        if depth[u] < depth[v]:\n            u,v = v,u\n\
    \        l,r = pos[v], pos[u]+1\n        if exclude_lca:\n            l += 1\n\
    \        yield l, r\n\n"
  code: "import cp_library.alg.tree.__header__\n\nclass HeavyLightDecomposition:\n\
    \    def __init__(self, T, r=0):\n        N = len(T)\n        # build\n      \
    \  size = [1]*N\n        pos = [0]*N\n        par = [-1]*N\n        heavy = [-1]*N\n\
    \        head = [-1]*N\n        depth = [0]*N\n        weights = [0]*N\n     \
    \   order = [0]*N\n        time = 0\n\n        stack = [(2,r,r), (0,r,-1)]\n \
    \       while stack:\n            match stack.pop():\n                case 0,\
    \ v, p: # dfs down\n                    par[v] = p\n                    stack.append((1,\
    \ v, p))\n                    for c, w in T[v]:\n                        if c\
    \ != p:\n                            depth[c] = depth[v] + 1 \n              \
    \              weights[c] = w\n                            stack.append((0, c,\
    \ v))\n\n                case 1, v, p: # dfs up\n                    l = -1\n\
    \                    for c, w in T[v]:\n                        if c != p:\n \
    \                           size[v] += size[c]\n                            if\
    \ l == -1 or size[c] > size[l]:\n                                l = c\n     \
    \               heavy[v] = l\n\n                case 2, v, h: # decompose\n  \
    \                  head[v] = h\n                    pos[v] = time\n          \
    \          order[time] = v\n                    p = par[v]\n                 \
    \   time += 1\n                    l = heavy[v]\n                    for c, _\
    \ in T[v]:\n                        if c != p and c != l:\n                  \
    \          stack.append((2, c, c))\n\n                    if l != -1:\n      \
    \                  stack.append((2, l, h))\n        self.N = N\n        self.T\
    \ = T\n        self.size = size\n        self.pos = pos\n        self.par = par\n\
    \        self.heavy = heavy\n        self.head = head\n        self.depth = depth\n\
    \        self.weights = weights\n        self.order = order\n\n    def path(self,\
    \ u, v, exclude_lca=False):\n        head, depth, par, pos = self.head, self.depth,\
    \ self.par, self.pos\n        while head[u] != head[v]:\n            if depth[head[u]]\
    \ < depth[head[v]]:\n                u,v = v,u\n            yield pos[head[u]],\
    \ pos[u]+1\n            u = par[head[u]]\n\n        if depth[u] < depth[v]:\n\
    \            u,v = v,u\n        l,r = pos[v], pos[u]+1\n        if exclude_lca:\n\
    \            l += 1\n        yield l, r\n\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/tree/heavy_light_decomposition_cls.py
  requiredBy: []
  timestamp: '2024-09-28 03:27:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/tree/heavy_light_decomposition_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py.html
title: cp_library/alg/tree/heavy_light_decomposition_cls.py
---
