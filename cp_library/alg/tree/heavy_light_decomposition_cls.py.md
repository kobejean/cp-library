---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n\nclass HLD:\n    def __init__(self, T, r=0):\n        N = len(T)\n\
    \        # build\n        size = [1]*N\n        start = [0]*N\n        end = [0]*N\n\
    \        par = [-1]*N\n        heavy = [-1]*N\n        head = [-1]*N\n       \
    \ depth = [0]*N\n        order = [0]*N\n        time = 0\n\n        stack = [(2,r,r),\
    \ (0,r,-1)]\n        while stack:\n            match stack.pop():\n          \
    \      case 0, v, p: # dfs down\n                    par[v] = p\n            \
    \        stack.append((1, v, p))\n                    for c in T[v]:\n       \
    \                 if c != p:\n                            depth[c] = depth[v]\
    \ + 1 \n                            stack.append((0, c, v))\n\n              \
    \  case 1, v, p: # dfs up\n                    l = -1\n                    for\
    \ c in T[v]:\n                        if c != p:\n                           \
    \ size[v] += size[c]\n                            if l == -1 or size[c] > size[l]:\n\
    \                                l = c\n                    heavy[v] = l\n\n \
    \               case 2, v, h: # decompose down\n                    head[v] =\
    \ h\n                    start[v] = time\n                    order[time] = v\n\
    \                    p = par[v]\n                    time += 1\n             \
    \       l = heavy[v]\n                    stack.append((3, v, h))\n          \
    \          \n                    for c in T[v]:\n                        if c\
    \ != p and c != l:\n                            stack.append((2, c, c))\n\n  \
    \                  if l != -1:\n                        stack.append((2, l, h))\n\
    \                case 3, v, h: # decompose up\n                    end[v] = time\n\
    \        self.N = N\n        self.T = T\n        self.size = size\n        self.start\
    \ = start\n        self.end = end\n        self.par = par\n        self.heavy\
    \ = heavy\n        self.head = head\n        self.depth = depth\n        self.order\
    \ = order\n\n    def __getitem__(self, key):\n        return self.start[key]\n\
    \n    def path(self, u, v, edge=False):\n        head, depth, par, start = self.head,\
    \ self.depth, self.par, self.start\n        while head[u] != head[v]:\n      \
    \      if depth[head[u]] < depth[head[v]]:\n                u,v = v,u\n      \
    \      yield start[head[u]], start[u]+1\n            u = par[head[u]]\n\n    \
    \    if depth[u] < depth[v]:\n            u,v = v,u\n\n        yield start[v]+edge,\
    \ start[u]+1\n"
  code: "import cp_library.alg.tree.__header__\n\nclass HLD:\n    def __init__(self,\
    \ T, r=0):\n        N = len(T)\n        # build\n        size = [1]*N\n      \
    \  start = [0]*N\n        end = [0]*N\n        par = [-1]*N\n        heavy = [-1]*N\n\
    \        head = [-1]*N\n        depth = [0]*N\n        order = [0]*N\n       \
    \ time = 0\n\n        stack = [(2,r,r), (0,r,-1)]\n        while stack:\n    \
    \        match stack.pop():\n                case 0, v, p: # dfs down\n      \
    \              par[v] = p\n                    stack.append((1, v, p))\n     \
    \               for c in T[v]:\n                        if c != p:\n         \
    \                   depth[c] = depth[v] + 1 \n                            stack.append((0,\
    \ c, v))\n\n                case 1, v, p: # dfs up\n                    l = -1\n\
    \                    for c in T[v]:\n                        if c != p:\n    \
    \                        size[v] += size[c]\n                            if l\
    \ == -1 or size[c] > size[l]:\n                                l = c\n       \
    \             heavy[v] = l\n\n                case 2, v, h: # decompose down\n\
    \                    head[v] = h\n                    start[v] = time\n      \
    \              order[time] = v\n                    p = par[v]\n             \
    \       time += 1\n                    l = heavy[v]\n                    stack.append((3,\
    \ v, h))\n                    \n                    for c in T[v]:\n         \
    \               if c != p and c != l:\n                            stack.append((2,\
    \ c, c))\n\n                    if l != -1:\n                        stack.append((2,\
    \ l, h))\n                case 3, v, h: # decompose up\n                    end[v]\
    \ = time\n        self.N = N\n        self.T = T\n        self.size = size\n \
    \       self.start = start\n        self.end = end\n        self.par = par\n \
    \       self.heavy = heavy\n        self.head = head\n        self.depth = depth\n\
    \        self.order = order\n\n    def __getitem__(self, key):\n        return\
    \ self.start[key]\n\n    def path(self, u, v, edge=False):\n        head, depth,\
    \ par, start = self.head, self.depth, self.par, self.start\n        while head[u]\
    \ != head[v]:\n            if depth[head[u]] < depth[head[v]]:\n             \
    \   u,v = v,u\n            yield start[head[u]], start[u]+1\n            u = par[head[u]]\n\
    \n        if depth[u] < depth[v]:\n            u,v = v,u\n\n        yield start[v]+edge,\
    \ start[u]+1\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/tree/heavy_light_decomposition_cls.py
  requiredBy: []
  timestamp: '2024-11-16 03:24:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/tree/heavy_light_decomposition_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py
- /library/cp_library/alg/tree/heavy_light_decomposition_cls.py.html
title: cp_library/alg/tree/heavy_light_decomposition_cls.py
---
