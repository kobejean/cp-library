---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_a_dijkstra.test.py
    title: test/aoj/grl/grl_1_a_dijkstra.test.py
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
    \n\n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n    heapsiftdown(heap,\
    \ 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item = heap.pop()\n    if heap:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\nfrom typing import Union, overload\n\
    \n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\nfrom math\
    \ import inf\n\n@overload\ndef dijkstra(G, s: int = 0) -> list[int]: ...\n@overload\n\
    def dijkstra(G, s: int, g: int) -> int: ...\ndef dijkstra(G, s = 0, g: Union[int,None]\
    \ = None):\n    N = len(G)\n    D = [inf for _ in range(N)]\n    D[s] = 0\n  \
    \  q = [(0, s)]\n    while q:\n        d, v = heappop(q)\n        if d > D[v]:\
    \ continue\n        if v == g: return d\n        for u, w, *_ in G[v]:\n     \
    \       if chmin(D, u, nd := d + w):\n                heappush(q, (nd, u))\n \
    \   return D if g is None else inf\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.ds.heap.fast_heapq\
    \ import heappop, heappush\nfrom typing import Union, overload\nfrom cp_library.alg.dp.chmin_fn\
    \ import chmin\nfrom math import inf\n\n@overload\ndef dijkstra(G, s: int = 0)\
    \ -> list[int]: ...\n@overload\ndef dijkstra(G, s: int, g: int) -> int: ...\n\
    def dijkstra(G, s = 0, g: Union[int,None] = None):\n    N = len(G)\n    D = [inf\
    \ for _ in range(N)]\n    D[s] = 0\n    q = [(0, s)]\n    while q:\n        d,\
    \ v = heappop(q)\n        if d > D[v]: continue\n        if v == g: return d\n\
    \        for u, w, *_ in G[v]:\n            if chmin(D, u, nd := d + w):\n   \
    \             heappush(q, (nd, u))\n    return D if g is None else inf"
  dependsOn:
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/alg/dp/chmin_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/dijkstra_fn.py
  requiredBy: []
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_1_a_dijkstra.test.py
documentation_of: cp_library/alg/graph/dijkstra_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/dijkstra_fn.py
- /library/cp_library/alg/graph/dijkstra_fn.py.html
title: cp_library/alg/graph/dijkstra_fn.py
---
