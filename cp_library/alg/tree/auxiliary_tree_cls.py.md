---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':question:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':question:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\nfrom itertools import pairwise\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nfrom typing import Any, Callable, List\n\nclass SparseTable:\n\
    \    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):\n    \
    \    self.n = len(arr)\n        self.log = self.n.bit_length()\n        self.op\
    \ = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n\
    \        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass BinaryIndexTree:\n\
    \    def __init__(self, v: int|list):\n        if isinstance(v, int):\n      \
    \      self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: int) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        data, size\
    \ = self.data, self.size\n        while i <= size:\n            data[i-1], i =\
    \ data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0\
    \ <= i <= self.size\n        s = 0\n        data = self.data\n        for _ in\
    \ range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n        return\
    \ s\n    \n    def range_sum(self, l: int, r: int):\n        return self.pref_sum(r)\
    \ - self.pref_sum(l)\n\nclass LCATable(SparseTable):\n    def __init__(self, T,\
    \ root = 0):\n        self.start = [-1] * len(T)\n        self.end = [-1] * len(T)\n\
    \        self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:\n       \
    \         self.start[u] = len(self.euler)\n                \n                for\
    \ v in reversed(T[u]):\n                    if v != p:\n                     \
    \   stack.append((u, p, d))\n                        stack.append((v, u, d+1))\n\
    \                        \n            self.euler.append(u)\n            self.depth.append(d)\n\
    \            self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r = min(self.start[u], self.start[v]), max(self.start[u],\
    \ self.start[v])+1\n        d, _ = super().query(l, r)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n        \n\nclass AuxiliaryTree(LCATable):\n\n    def\
    \ build_auxiliary_tree(self, V):\n        V = sorted(V, key=lambda x: self.start[x])\n\
    \        stack = [V[0]]\n        for u, v in pairwise(V):\n            lca, _\
    \ = self.query(u, v)\n            while len(stack) > 1 and self.start[stack[-1]]\
    \ > self.start[lca]:\n                stack.pop()\n            if stack[-1] !=\
    \ lca:\n                stack.append(lca)\n            stack.append(v)\n\n   \
    \     aux_tree = { v: [] for v in stack }\n        for p, c in pairwise(stack):\n\
    \            aux_tree[p].append(c)\n        return aux_tree\n\n    def get_path(self,\
    \ u, v):\n        lca, _ = self.query(u, v)\n        path = []\n        \n   \
    \     # Path from u to LCA\n        current = u\n        while current != lca:\n\
    \            path.append(current)\n            for parent in self.T[current]:\n\
    \                if self.start[parent] < self.start[current]:\n              \
    \      current = parent\n                    break\n        \n        # Add LCA\n\
    \        path.append(lca)\n        \n        # Path from LCA to v (in reverse\
    \ order)\n        current = v\n        reverse_path = []\n        while current\
    \ != lca:\n            reverse_path.append(current)\n            for parent in\
    \ self.T[current]:\n                if self.start[parent] < self.start[current]:\n\
    \                    current = parent\n                    break\n        # Combine\
    \ paths\n        path.extend(reversed(reverse_path))\n        return path\n"
  code: "import cp_library.alg.tree.__header__\nfrom itertools import pairwise\nfrom\
    \ cp_library.alg.tree.lca_table_iterative_cls import LCATable\n\nclass AuxiliaryTree(LCATable):\n\
    \n    def build_auxiliary_tree(self, V):\n        V = sorted(V, key=lambda x:\
    \ self.start[x])\n        stack = [V[0]]\n        for u, v in pairwise(V):\n \
    \           lca, _ = self.query(u, v)\n            while len(stack) > 1 and self.start[stack[-1]]\
    \ > self.start[lca]:\n                stack.pop()\n            if stack[-1] !=\
    \ lca:\n                stack.append(lca)\n            stack.append(v)\n\n   \
    \     aux_tree = { v: [] for v in stack }\n        for p, c in pairwise(stack):\n\
    \            aux_tree[p].append(c)\n        return aux_tree\n\n    def get_path(self,\
    \ u, v):\n        lca, _ = self.query(u, v)\n        path = []\n        \n   \
    \     # Path from u to LCA\n        current = u\n        while current != lca:\n\
    \            path.append(current)\n            for parent in self.T[current]:\n\
    \                if self.start[parent] < self.start[current]:\n              \
    \      current = parent\n                    break\n        \n        # Add LCA\n\
    \        path.append(lca)\n        \n        # Path from LCA to v (in reverse\
    \ order)\n        current = v\n        reverse_path = []\n        while current\
    \ != lca:\n            reverse_path.append(current)\n            for parent in\
    \ self.T[current]:\n                if self.start[parent] < self.start[current]:\n\
    \                    current = parent\n                    break\n        # Combine\
    \ paths\n        path.extend(reversed(reverse_path))\n        return path"
  dependsOn:
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/auxiliary_tree_cls.py
  requiredBy: []
  timestamp: '2024-11-16 11:24:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/auxiliary_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/auxiliary_tree_cls.py
- /library/cp_library/alg/tree/auxiliary_tree_cls.py.html
title: cp_library/alg/tree/auxiliary_tree_cls.py
---
