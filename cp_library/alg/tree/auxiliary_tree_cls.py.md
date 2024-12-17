---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
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
    from itertools import pairwise\n\n\nfrom typing import Any, Callable, List\n\n\
    class SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.N = N = len(arr)\n        self.log = N.bit_length()\n\
    \        self.op = op\n        \n        self.offsets = offsets = [0]\n      \
    \  for i in range(1, self.log):\n            offsets.append(offsets[-1] + N -\
    \ (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1] +\
    \ N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for i\
    \ in range(self.log - 1):\n            d = 1 << i\n            start = offsets[i]\n\
    \            next_start = offsets[i + 1]\n            for j in range(N - (1 <<\
    \ (i+1)) + 1):\n                st[next_start + j] = op(st[k := start+j], st[k\
    \ + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return self.op(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows = []\n        for i in range(self.log):\n            start = self.offsets[i]\n\
    \            end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n   \
    \         rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)\n\
    \nimport operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter: Iterable[T], func: Callable[[T,T],T]\
    \ = None, initial: T = None, step = 1) -> list[T]:\n    match step:\n        case\
    \ 1:\n            return list(accumulate(iter, func, initial=initial))\n     \
    \   case step:\n            assert step >= 2\n            if func is None:\n \
    \               func = operator.add\n            A = list(iter)\n            if\
    \ initial is not None:\n                A = [initial] + A\n            for i in\
    \ range(step,len(A)):\n                A[i] = func(A[i], A[i-step])\n        \
    \    return A\n\nclass LCATable(SparseTable):\n    def __init__(self, T, root\
    \ = 0):\n        N = len(T)\n        T.euler_tour(root)\n        self.depth =\
    \ depth = presum(T.delta)\n        self.start, self.stop = T.tin, T.tout\n\n \
    \       self.mask = (1 << (shift := N.bit_length()))-1\n        self.shift = shift\n\
    \        order = T.order\n        M = len(order)\n        packets = [0]*M\n  \
    \      for i in range(M):\n            packets[i] = depth[i] << shift | order[i]\
    \ \n\n        super().__init__(min, packets)\n\n    def _query(self, u, v):\n\
    \        l,r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n\
    \        da = super().query(l, r)\n        return l, r, da & self.mask, da >>\
    \ self.shift\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r, a,\
    \ d = self._query(u, v)\n        return a, d\n    \n    def distance(self, u,\
    \ v) -> int:\n        l, r, a, d = self._query(u, v)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n\nclass AuxiliaryTree(LCATable):\n\n    def build_auxiliary_tree(self,\
    \ V):\n        V = sorted(V, key=lambda x: self.start[x])\n        stack = [V[0]]\n\
    \        for u, v in pairwise(V):\n            lca, _ = self.query(u, v)\n   \
    \         while len(stack) > 1 and self.start[stack[-1]] > self.start[lca]:\n\
    \                stack.pop()\n            if stack[-1] != lca:\n             \
    \   stack.append(lca)\n            stack.append(v)\n\n        aux_tree = { v:\
    \ [] for v in stack }\n        for p, c in pairwise(stack):\n            aux_tree[p].append(c)\n\
    \        return aux_tree\n\n    def get_path(self, u, v):\n        lca, _ = self.query(u,\
    \ v)\n        path = []\n        \n        # Path from u to LCA\n        current\
    \ = u\n        while current != lca:\n            path.append(current)\n     \
    \       for parent in self.T[current]:\n                if self.start[parent]\
    \ < self.start[current]:\n                    current = parent\n             \
    \       break\n        \n        # Add LCA\n        path.append(lca)\n       \
    \ \n        # Path from LCA to v (in reverse order)\n        current = v\n   \
    \     reverse_path = []\n        while current != lca:\n            reverse_path.append(current)\n\
    \            for parent in self.T[current]:\n                if self.start[parent]\
    \ < self.start[current]:\n                    current = parent\n             \
    \       break\n        # Combine paths\n        path.extend(reversed(reverse_path))\n\
    \        return path\n"
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
  - cp_library/alg/iter/presum_fn.py
  isVerificationFile: false
  path: cp_library/alg/tree/auxiliary_tree_cls.py
  requiredBy: []
  timestamp: '2024-12-17 20:59:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/auxiliary_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/auxiliary_tree_cls.py
- /library/cp_library/alg/tree/auxiliary_tree_cls.py.html
title: cp_library/alg/tree/auxiliary_tree_cls.py
---
