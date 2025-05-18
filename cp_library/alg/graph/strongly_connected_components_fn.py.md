---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/slice_iterator_reverse_cls.py
    title: cp_library/alg/iter/slice_iterator_reverse_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/i32f_fn.py
    title: cp_library/ds/array/i32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    from typing import Iterator\n\nfrom typing import Iterator, SupportsIndex\nfrom\
    \ typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass SliceIteratorReverse(Iterator[_T]):\n\
    \    def __init__(self, A: list[_T], L: list[SupportsIndex]):\n        self.A,\
    \ self.L, self.r = A, L, len(A)\n    def __len__(self): return len(self.L)\n \
    \   def __next__(self):\n        L = self.L\n        if not L: raise StopIteration\n\
    \        self.r, r = (l := L.pop()), self.r\n        return self.A[l:r]\n\n\n\
    def chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n\n\
    from array import array\ndef i32f(N: int, elm: int = 0):     return array('i',\
    \ (elm,))*N  # signed int\ndef u8f(N: int, elm: int = 0):      return array('B',\
    \ (elm,))*N  # unsigned char\ndef u32f(N: int, elm: int = 0):     return array('I',\
    \ (elm,))*N  # unsigned int\n\ndef strongly_connected_components(G) -> Iterator[list[int]]:\n\
    \    '''\n    Finds strongly connected sccs in directed graph using Tarjan's algorithm.\n\
    \    Returns sccs in topological order.\n    '''\n    tin, low, on_stack, time\
    \ = i32f(N := G.N, -1), u32f(N), u8f(N), 0\n    order, sccs, L = elist(N), elist(N),\
    \ elist(N)\n    \n    def enter(u):\n        nonlocal time\n        tin[u] = low[u]\
    \ = (time := time+1)\n        order.append(u)\n        on_stack[u] = 1\n\n   \
    \ def back_or_cross(u,v):\n        if on_stack[v]: chmin(low, u, tin[v])\n\n \
    \   def leave(u):\n        if low[u] == tin[u]:\n            L.append(len(sccs))\n\
    \            while True:\n                on_stack[v := order.pop()] = 0\n   \
    \             sccs.append(v)\n                if v == u: break\n\n    def up(u,v):\n\
    \        chmin(low, v, low[u])\n\n    G.dfs(enter_fn=enter, back_fn=back_or_cross,\
    \ cross_fn=back_or_cross, leave_fn=leave, up_fn=up)\n    return SliceIteratorReverse(sccs,\
    \ L)\n"
  code: "import cp_library.alg.graph.__header__\nfrom typing import Iterator\nfrom\
    \ cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse\n\
    from cp_library.alg.dp.chmin_fn import chmin\nfrom cp_library.ds.elist_fn import\
    \ elist\nfrom cp_library.ds.array.i32f_fn import i32f\nfrom cp_library.ds.array.u8f_fn\
    \ import u8f\nfrom cp_library.ds.array.u32f_fn import u32f\n\ndef strongly_connected_components(G)\
    \ -> Iterator[list[int]]:\n    '''\n    Finds strongly connected sccs in directed\
    \ graph using Tarjan's algorithm.\n    Returns sccs in topological order.\n  \
    \  '''\n    tin, low, on_stack, time = i32f(N := G.N, -1), u32f(N), u8f(N), 0\n\
    \    order, sccs, L = elist(N), elist(N), elist(N)\n    \n    def enter(u):\n\
    \        nonlocal time\n        tin[u] = low[u] = (time := time+1)\n        order.append(u)\n\
    \        on_stack[u] = 1\n\n    def back_or_cross(u,v):\n        if on_stack[v]:\
    \ chmin(low, u, tin[v])\n\n    def leave(u):\n        if low[u] == tin[u]:\n \
    \           L.append(len(sccs))\n            while True:\n                on_stack[v\
    \ := order.pop()] = 0\n                sccs.append(v)\n                if v ==\
    \ u: break\n\n    def up(u,v):\n        chmin(low, v, low[u])\n\n    G.dfs(enter_fn=enter,\
    \ back_fn=back_or_cross, cross_fn=back_or_cross, leave_fn=leave, up_fn=up)\n \
    \   return SliceIteratorReverse(sccs, L)"
  dependsOn:
  - cp_library/alg/iter/slice_iterator_reverse_cls.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/array/i32f_fn.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/strongly_connected_components_fn.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/strongly_connected_components_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/strongly_connected_components_fn.py
- /library/cp_library/alg/graph/strongly_connected_components_fn.py.html
title: cp_library/alg/graph/strongly_connected_components_fn.py
---
