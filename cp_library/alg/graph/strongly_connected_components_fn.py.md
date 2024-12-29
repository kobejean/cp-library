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
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/fill_fn.py
    title: cp_library/ds/fill_fn.py
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
    from typing import Iterator\n\nfrom typing import Iterator, SupportsIndex, TypeVar\n\
    \nT = TypeVar('T')\nclass SliceIteratorReverse(Iterator[T]):\n    def __init__(self,\
    \ A: list[T], L: list[SupportsIndex]):\n        self.A, self.L, self.r = A, L,\
    \ len(A)\n    def __len__(self): return len(self.L)\n    def __next__(self):\n\
    \        L = self.L\n        if not L: raise StopIteration\n        self.r, r\
    \ = (l := L.pop()), self.r\n        return self.A[l:r]\n\n\ndef chmin(dp, i, v):\n\
    \    if ch:=dp[i]>v:dp[i]=v\n    return ch\n\n\ndef elist(est_len: int) -> list:\
    \ ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \nfrom array import array\n\ndef\
    \ i8a(N: int, elm: int = 0): return array('b', (elm,))*N       # signed char\n\
    def u8a(N: int, elm: int = 0): return array('B', (elm,))*N       # unsigned char\n\
    def i16a(N: int, elm: int = 0): return array('h', (elm,))*N      # signed short\n\
    def u16a(N: int, elm: int = 0): return array('H', (elm,))*N      # unsigned short\n\
    def i32a(N: int, elm: int = 0): return array('i', (elm,))*N      # signed int\n\
    def u32a(N: int, elm: int = 0): return array('I', (elm,))*N      # unsigned int\n\
    def i64a(N: int, elm: int = 0): return array('q', (elm,))*N      # signed long\
    \ long\ndef u64a(N: int, elm: int = 0): return array('Q', (elm,))*N      # unsigned\
    \ long long\ndef f32a(N: int, elm: float = 0.0): return array('f', (elm,))*N \
    \ # float\ndef f64a(N: int, elm: float = 0.0): return array('d', (elm,))*N  #\
    \ double\n\ndef strongly_connected_components(G) -> Iterator[list[int]]:\n   \
    \ \"\"\"\n    Finds strongly connected sccs in directed graph using Tarjan's algorithm.\n\
    \    Returns sccs in topological order.\n    \"\"\"\n    tin, low, on_stack, time\
    \ = i32a(N := G.N, -1), u32a(N), u8a(N), 0\n    order, sccs, L = elist(N), elist(N),\
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
    \ elist\nfrom cp_library.ds.fill_fn import i32a, u32a, u8a\n\ndef strongly_connected_components(G)\
    \ -> Iterator[list[int]]:\n    \"\"\"\n    Finds strongly connected sccs in directed\
    \ graph using Tarjan's algorithm.\n    Returns sccs in topological order.\n  \
    \  \"\"\"\n    tin, low, on_stack, time = i32a(N := G.N, -1), u32a(N), u8a(N),\
    \ 0\n    order, sccs, L = elist(N), elist(N), elist(N)\n    \n    def enter(u):\n\
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
  - cp_library/ds/fill_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/strongly_connected_components_fn.py
  requiredBy: []
  timestamp: '2024-12-29 16:20:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/strongly_connected_components_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/strongly_connected_components_fn.py
- /library/cp_library/alg/graph/strongly_connected_components_fn.py.html
title: cp_library/alg/graph/strongly_connected_components_fn.py
---
