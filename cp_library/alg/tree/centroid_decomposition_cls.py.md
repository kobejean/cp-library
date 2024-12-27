---
data:
  _extendedDependsOn: []
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
    \nclass CentroidDecomposition():\n    def __init__(self, tree):\n        n = len(tree)\n\
    \        self.n = n\n        self.tree = tree\n        self.par = [-1] * n\n \
    \       self.dep = [-1] * n\n        self.size = [1] * n\n        self.used =\
    \ [0] * n\n        self.root = None\n\n    def set_root(self, r):\n        self.root\
    \ = r\n        self.par[r] = -1\n        self.dep[r] = 0\n        self.size[r]\
    \ = 1\n        self.ord = [r]\n        stack = [r]\n        while stack:\n   \
    \         v = stack.pop()\n            for a in self.tree[v]:\n              \
    \  if self.par[v] == a or self.used[a]: continue\n                self.size[a]\
    \ = 1\n                self.par[a] = v\n                self.dep[a] = self.dep[v]\
    \ + 1\n                self.ord.append(a)\n                stack.append(a)\n \
    \       for v in reversed(self.ord):\n            for a in self.tree[v]:\n   \
    \             if self.par[v] == a or self.used[a]: continue\n                self.size[v]\
    \ += self.size[a]\n\n    def centroid(self, r):\n        v = r\n        while\
    \ True:\n            for a in self.tree[v]:\n                if self.par[v] ==\
    \ a or self.used[a]: continue\n                if self.size[a] > self.size[r]\
    \ // 2:\n                    v = a\n                    break\n            else:\n\
    \                return v\n\n    def centroid_decomposition(self, vis_centroid,\
    \ vis_subtree):\n        self.set_root(0)\n        stack = [self.centroid(0)]\n\
    \        while stack:\n            v = stack.pop()\n            self.used[v] =\
    \ True\n            self.set_root(v)\n            vis_centroid(self, v)\n    \
    \        for a in self.tree[v]:\n                if self.used[a]: continue\n \
    \               self.set_root(a)\n                vis_subtree(self, a)\n     \
    \           stack.append(self.centroid(a))\n"
  code: "import cp_library.alg.tree.__header__\n\nclass CentroidDecomposition():\n\
    \    def __init__(self, tree):\n        n = len(tree)\n        self.n = n\n  \
    \      self.tree = tree\n        self.par = [-1] * n\n        self.dep = [-1]\
    \ * n\n        self.size = [1] * n\n        self.used = [0] * n\n        self.root\
    \ = None\n\n    def set_root(self, r):\n        self.root = r\n        self.par[r]\
    \ = -1\n        self.dep[r] = 0\n        self.size[r] = 1\n        self.ord =\
    \ [r]\n        stack = [r]\n        while stack:\n            v = stack.pop()\n\
    \            for a in self.tree[v]:\n                if self.par[v] == a or self.used[a]:\
    \ continue\n                self.size[a] = 1\n                self.par[a] = v\n\
    \                self.dep[a] = self.dep[v] + 1\n                self.ord.append(a)\n\
    \                stack.append(a)\n        for v in reversed(self.ord):\n     \
    \       for a in self.tree[v]:\n                if self.par[v] == a or self.used[a]:\
    \ continue\n                self.size[v] += self.size[a]\n\n    def centroid(self,\
    \ r):\n        v = r\n        while True:\n            for a in self.tree[v]:\n\
    \                if self.par[v] == a or self.used[a]: continue\n             \
    \   if self.size[a] > self.size[r] // 2:\n                    v = a\n        \
    \            break\n            else:\n                return v\n\n    def centroid_decomposition(self,\
    \ vis_centroid, vis_subtree):\n        self.set_root(0)\n        stack = [self.centroid(0)]\n\
    \        while stack:\n            v = stack.pop()\n            self.used[v] =\
    \ True\n            self.set_root(v)\n            vis_centroid(self, v)\n    \
    \        for a in self.tree[v]:\n                if self.used[a]: continue\n \
    \               self.set_root(a)\n                vis_subtree(self, a)\n     \
    \           stack.append(self.centroid(a))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/tree/centroid_decomposition_cls.py
  requiredBy: []
  timestamp: '2024-12-27 22:35:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/centroid_decomposition_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/centroid_decomposition_cls.py
- /library/cp_library/alg/tree/centroid_decomposition_cls.py.html
title: cp_library/alg/tree/centroid_decomposition_cls.py
---
