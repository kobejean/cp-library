---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "import sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\nfrom typing import Any, Callable, List, TypeVar, Generic\n\
    \nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n        self.size\
    \ = len(data)\n        self.prefix = [e] + data.copy()\n        self.suffix =\
    \ data.copy() + [e]\n        self.e = e\n        self.op = op\n        for i in\
    \ range(self.size):\n            self.prefix[i+1] = op(self.prefix[i], self.prefix[i+1])\n\
    \        for i in range(self.size,0,-1):\n            self.suffix[i-1] = op(self.suffix[i-1],\
    \ self.suffix[i])\n    def left(self, l): return self.prefix[l]\n    def right(self,\
    \ r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n    def\
    \ out(self, l, r=None):\n        r = l+1 if r is None else r\n        return self.op(self.prefix[l],\
    \ self.suffix[r])\n\nT = TypeVar('T')\n\nclass ReRootingDP(Generic[T]):\n    def\
    \ __init__(self, T: List[List[int]], e: T, merge: Callable[[T, T], T], add_node:\
    \ Callable[[int, T], T]) -> None:\n        self.T = T\n        self.e = e\n  \
    \      self.merge = merge\n        self.add_node = add_node\n\n    def solve(self)\
    \ -> List[T]:\n        dp = [[self.e]*len(adj) for adj in self.T]\n        ans\
    \ = [None for _ in range(len(self.T))]\n        \n        def dfs_up(u, p=None):\n\
    \            res = self.e\n            for i,v in enumerate(self.T[u]):\n    \
    \            if v != p:\n                    dp[u][i] = dfs_up(v,u)\n        \
    \            res = self.merge(res, dp[u][i])\n            return self.add_node(u,\
    \ res)\n        \n        def dfs_down(u, p=None):\n            ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n            for i,v in enumerate(self.T[u]):\n         \
    \       if v != p:\n                    dp[v][self.T[v].index(u)] = self.add_node(u,\
    \ ba.out(i))\n                    dfs_down(v,u)\n            ans[u] = ba.all()\n\
    \        \n        dfs_up(0)\n        dfs_down(0)\n        return ans\n"
  code: "import cp_library.misc.setrecursionlimit\nfrom typing import Any, Callable,\
    \ List, TypeVar, Generic\nfrom cp_library.ds.bidirectional_array_cls import BidirectionalArray\n\
    \nT = TypeVar('T')\n\nclass ReRootingDP(Generic[T]):\n    def __init__(self, T:\
    \ List[List[int]], e: T, merge: Callable[[T, T], T], add_node: Callable[[int,\
    \ T], T]) -> None:\n        self.T = T\n        self.e = e\n        self.merge\
    \ = merge\n        self.add_node = add_node\n\n    def solve(self) -> List[T]:\n\
    \        dp = [[self.e]*len(adj) for adj in self.T]\n        ans = [None for _\
    \ in range(len(self.T))]\n        \n        def dfs_up(u, p=None):\n         \
    \   res = self.e\n            for i,v in enumerate(self.T[u]):\n             \
    \   if v != p:\n                    dp[u][i] = dfs_up(v,u)\n                 \
    \   res = self.merge(res, dp[u][i])\n            return self.add_node(u, res)\n\
    \        \n        def dfs_down(u, p=None):\n            ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n            for i,v in enumerate(self.T[u]):\n         \
    \       if v != p:\n                    dp[v][self.T[v].index(u)] = self.add_node(u,\
    \ ba.out(i))\n                    dfs_down(v,u)\n            ans[u] = ba.all()\n\
    \        \n        dfs_up(0)\n        dfs_down(0)\n        return ans\n"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/bidirectional_array_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/rerooting_recursive_cls.py
  requiredBy: []
  timestamp: '2024-08-29 20:41:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/alg/dp/rerooting_recursive_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/rerooting_recursive_cls.py
- /library/cp_library/alg/dp/rerooting_recursive_cls.py.html
title: cp_library/alg/dp/rerooting_recursive_cls.py
---
