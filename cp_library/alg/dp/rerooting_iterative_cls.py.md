---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
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
    import typing\n\n\nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n\
    \        self.size = len(data)\n        self.prefix = [e] + data.copy()\n    \
    \    self.suffix = data.copy() + [e]\n        self.e = e\n        self.op = op\n\
    \        for i in range(self.size):\n            self.prefix[i+1] = op(self.prefix[i],\
    \ self.prefix[i+1])\n        for i in range(self.size,0,-1):\n            self.suffix[i-1]\
    \ = op(self.suffix[i-1], self.suffix[i])\n    def left(self, l): return self.prefix[l]\n\
    \    def right(self, r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n\
    \    def out(self, l, r=None):\n        r = l+1 if r is None else r\n        return\
    \ self.op(self.prefix[l], self.suffix[r])\n\nclass ReRootingDP():\n    \"\"\"\
    \ A class implementation of the Re-rooting Dynamic Programming technique. \"\"\
    \"\n    \n    S = typing.TypeVar('S')\n    MergeOp = typing.Callable[[S, S], S]\n\
    \    AddNodeOp = typing.Callable[[int, S], S]\n    AddEdgeOp = typing.Callable[[int,\
    \ int, S], S]\n\n    def __init__(self, T: list[list[int]], e: S,\n          \
    \       merge: MergeOp, \n                 add_node: AddNodeOp = lambda u,s:s,\
    \ \n                 add_edge: AddEdgeOp = lambda u,v,s:s):\n        \"\"\"\n\
    \        T: list[list[int]] - Adjacency list representation of the tree.\n   \
    \     e: S - Identity element for the merge operation.\n        merge: (S,S) ->\
    \ S - Function to merge two states.\n        add_node: (int,S) -> S - Function\
    \ to incorporate a node into the state.\n        add_edge: (int,int,S) -> S -\
    \ Function to incorporate an edge into the state.\n        \"\"\"\n        self.T\
    \ = T\n        self.e = e\n        self.merge = merge\n        self.add_node =\
    \ add_node\n        self.add_edge = add_edge\n\n    def solve(self) -> list[S]:\n\
    \        dp = [[self.e]*len(adj) for adj in self.T]\n        ans = [self.e for\
    \ _ in range(len(self.T))]\n        parent_idx = [None for _ in range(len(self.T))]\n\
    \        child_idx = [None for _ in range(len(self.T))]\n        stack = [(2,0,None),(0,0,None)]\n\
    \        while stack:\n            phase, u, p = stack.pop()\n            match\
    \ phase:\n                case 0:  # Visit children\n                    if p\
    \ is not None:\n                        stack.append((1,u,p))\n              \
    \      for i,v in enumerate(self.T[u]):\n                        if v != p:\n\
    \                            stack.append((0,v,u))\n                         \
    \   child_idx[v] = i\n                        else:\n                        \
    \    parent_idx[u] = i\n                case 1:  # Upward updates\n          \
    \          val = dp[p][child_idx[u]] = self.add_edge(p, u, self.add_node(u, ans[u]))\n\
    \                    ans[p] = self.merge(ans[p], val)\n                case 2:\
    \  # Downward updates\n                    ba = BidirectionalArray(self.e, self.merge,\
    \ dp[u])\n                    for i,v in enumerate(self.T[u]):\n             \
    \           if v != p:\n                            dp[v][parent_idx[v]] = self.add_edge(v,\
    \ u, self.add_node(u, ba.out(i)))\n                            stack.append((2,v,u))\n\
    \                    ans[u] = ba.all()\n        return ans\n"
  code: "import cp_library.alg.dp.__header__\nimport typing\nfrom cp_library.ds.bidirectional_array_cls\
    \ import BidirectionalArray\n\nclass ReRootingDP():\n    \"\"\" A class implementation\
    \ of the Re-rooting Dynamic Programming technique. \"\"\"\n    \n    S = typing.TypeVar('S')\n\
    \    MergeOp = typing.Callable[[S, S], S]\n    AddNodeOp = typing.Callable[[int,\
    \ S], S]\n    AddEdgeOp = typing.Callable[[int, int, S], S]\n\n    def __init__(self,\
    \ T: list[list[int]], e: S,\n                 merge: MergeOp, \n             \
    \    add_node: AddNodeOp = lambda u,s:s, \n                 add_edge: AddEdgeOp\
    \ = lambda u,v,s:s):\n        \"\"\"\n        T: list[list[int]] - Adjacency list\
    \ representation of the tree.\n        e: S - Identity element for the merge operation.\n\
    \        merge: (S,S) -> S - Function to merge two states.\n        add_node:\
    \ (int,S) -> S - Function to incorporate a node into the state.\n        add_edge:\
    \ (int,int,S) -> S - Function to incorporate an edge into the state.\n       \
    \ \"\"\"\n        self.T = T\n        self.e = e\n        self.merge = merge\n\
    \        self.add_node = add_node\n        self.add_edge = add_edge\n\n    def\
    \ solve(self) -> list[S]:\n        dp = [[self.e]*len(adj) for adj in self.T]\n\
    \        ans = [self.e for _ in range(len(self.T))]\n        parent_idx = [None\
    \ for _ in range(len(self.T))]\n        child_idx = [None for _ in range(len(self.T))]\n\
    \        stack = [(2,0,None),(0,0,None)]\n        while stack:\n            phase,\
    \ u, p = stack.pop()\n            match phase:\n                case 0:  # Visit\
    \ children\n                    if p is not None:\n                        stack.append((1,u,p))\n\
    \                    for i,v in enumerate(self.T[u]):\n                      \
    \  if v != p:\n                            stack.append((0,v,u))\n           \
    \                 child_idx[v] = i\n                        else:\n          \
    \                  parent_idx[u] = i\n                case 1:  # Upward updates\n\
    \                    val = dp[p][child_idx[u]] = self.add_edge(p, u, self.add_node(u,\
    \ ans[u]))\n                    ans[p] = self.merge(ans[p], val)\n           \
    \     case 2:  # Downward updates\n                    ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n                    for i,v in enumerate(self.T[u]):\n \
    \                       if v != p:\n                            dp[v][parent_idx[v]]\
    \ = self.add_edge(v, u, self.add_node(u, ba.out(i)))\n                       \
    \     stack.append((2,v,u))\n                    ans[u] = ba.all()\n        return\
    \ ans"
  dependsOn:
  - cp_library/ds/bidirectional_array_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/rerooting_iterative_cls.py
  requiredBy: []
  timestamp: '2024-12-29 16:20:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/alg/dp/rerooting_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/rerooting_iterative_cls.py
- /library/cp_library/alg/dp/rerooting_iterative_cls.py.html
title: cp_library/alg/dp/rerooting_iterative_cls.py
---
