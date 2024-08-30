---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from typing import Any, Callable, List, TypeVar, Generic\n\nclass\
    \ BidirectionalArray:\n    def __init__(self, e, op, data):\n        self.size\
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
    \ -> List[Any]:\n        dp = [[self.e]*len(adj) for adj in self.T]\n        ans\
    \ = [self.e for _ in range(len(self.T))]\n        parent_idx = [None for _ in\
    \ range(len(self.T))]\n        child_idx = [None for _ in range(len(self.T))]\n\
    \        stack = [(2,0,None),(0,0,None)]\n        \n        while stack:\n   \
    \         phase, u, p = stack.pop()\n            match phase:\n              \
    \  case 0: # phase 0: Visit children\n                    if p != None:\n    \
    \                    stack.append((1,u,p))\n                    for i,v in enumerate(self.T[u]):\n\
    \                        if v != p:\n                            stack.append((0,v,u))\n\
    \                            child_idx[v] = i\n                        else:\n\
    \                            parent_idx[u] = i\n                case 1: # phase\
    \ 1: Upward updates\n                    val = dp[p][child_idx[u]] = self.add_node(u,\
    \ ans[u])\n                    ans[p] = self.merge(ans[p], val)\n            \
    \    case 2: # phase 2: Downward updates\n                    ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n                    for i,v in enumerate(self.T[u]):\n \
    \                       if v != p:\n                            dp[v][parent_idx[v]]\
    \ = self.add_node(u, ba.out(i))\n                            stack.append((2,v,u))\n\
    \                    ans[u] = ba.all()\n        return ans\n"
  code: "from typing import Any, Callable, List, TypeVar, Generic\nfrom cp_library.ds.bidirectional_array_cls\
    \ import BidirectionalArray\n\nT = TypeVar('T')\n\nclass ReRootingDP(Generic[T]):\n\
    \    def __init__(self, T: List[List[int]], e: T, merge: Callable[[T, T], T],\
    \ add_node: Callable[[int, T], T]) -> None:\n        self.T = T\n        self.e\
    \ = e\n        self.merge = merge\n        self.add_node = add_node\n\n    def\
    \ solve(self) -> List[Any]:\n        dp = [[self.e]*len(adj) for adj in self.T]\n\
    \        ans = [self.e for _ in range(len(self.T))]\n        parent_idx = [None\
    \ for _ in range(len(self.T))]\n        child_idx = [None for _ in range(len(self.T))]\n\
    \        stack = [(2,0,None),(0,0,None)]\n        \n        while stack:\n   \
    \         phase, u, p = stack.pop()\n            match phase:\n              \
    \  case 0: # phase 0: Visit children\n                    if p != None:\n    \
    \                    stack.append((1,u,p))\n                    for i,v in enumerate(self.T[u]):\n\
    \                        if v != p:\n                            stack.append((0,v,u))\n\
    \                            child_idx[v] = i\n                        else:\n\
    \                            parent_idx[u] = i\n                case 1: # phase\
    \ 1: Upward updates\n                    val = dp[p][child_idx[u]] = self.add_node(u,\
    \ ans[u])\n                    ans[p] = self.merge(ans[p], val)\n            \
    \    case 2: # phase 2: Downward updates\n                    ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n                    for i,v in enumerate(self.T[u]):\n \
    \                       if v != p:\n                            dp[v][parent_idx[v]]\
    \ = self.add_node(u, ba.out(i))\n                            stack.append((2,v,u))\n\
    \                    ans[u] = ba.all()\n        return ans\n"
  dependsOn:
  - cp_library/ds/bidirectional_array_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/rerooting_iterative_cls.py
  requiredBy: []
  timestamp: '2024-08-30 21:29:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/alg/dp/rerooting_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/rerooting_iterative_cls.py
- /library/cp_library/alg/dp/rerooting_iterative_cls.py.html
title: cp_library/alg/dp/rerooting_iterative_cls.py
---
