---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_events_fn.py
    title: cp_library/alg/graph/dfs_events_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_a_articulation_points_fn.test.py
    title: test/aoj/grl/grl_3_a_articulation_points_fn.test.py
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
    from typing import Union\n\nfrom enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n\
    \    ENTER = auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n\
    \    LEAVE = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS\
    \ = auto()\n    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS\
    \ = auto()\n\n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n\
    \    EULER_TOUR = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN\
    \ | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS\
    \ | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n \
    \   DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS\
    \ \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n\
    \    \n\ndef dfs_events(G, flags: DFSFlags, s: Union[int,list,None] = None, max_depth:\
    \ Union[int,None] = None):\n    if flags == DFSFlags.INTERVAL:\n        if max_depth\
    \ is None:\n            return G.dfs_enter_leave(s)\n    elif flags == DFSFlags.TOPDOWN:\n\
    \        edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)\n        return\
    \ [(DFSEvent.DOWN, p, u) for p,u in edges]\n    elif flags == DFSFlags.BOTTOMUP:\n\
    \        edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n        return\
    \ [(DFSEvent.UP, p, u) for p,u in edges]\n    elif DFSFlags.BACKTRACK in flags:\n\
    \        return G.dfs_backtrack(s)\n    state = [0] * G.N\n    child = [0] * G.N\n\
    \    stack = [0] * G.N\n    if DFSFlags.RETURN_PARENTS in flags:\n        parents\
    \ = [-1] * G.N\n    if DFSFlags.RETURN_DEPTHS in flags:\n        depths = [-1]\
    \ * G.N\n\n    events = []\n    for s in G.starts(s):\n        stack[depth :=\
    \ 0] = s\n        if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:\n        \
    \    events.append((DFSEvent.DOWN,-1,s))\n        while depth != -1:\n       \
    \     u = stack[depth]\n            \n            if not state[u]:\n         \
    \       state[u] = 1\n                if DFSFlags.ENTER in flags:\n          \
    \          events.append((DFSEvent.ENTER, u))\n                if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n                    depths[u] = depth\n            \n           \
    \ if (c := child[u]) < len(G[u]):\n                child[u] += 1\n           \
    \     if (s := state[v := G[u][c]]) == 0: # Unvisited\n                    if\
    \ max_depth is None or depth <= max_depth:\n                        if flags &\
    \ DFSFlags.DOWN:\n                            events.append((DFSEvent.DOWN, u,\
    \ v))\n                        stack[depth := depth+1] = v\n                 \
    \       if flags & DFSFlags.RETURN_PARENTS:\n                            parents[v]\
    \ = u\n                elif s == 1:  # In progress\n                    if flags\
    \ & DFSFlags.BACK:\n                        events.append((DFSEvent.BACK, u, v))\n\
    \                elif s == 2: # Completed\n                    if flags & DFSFlags.CROSS:\n\
    \                        events.append((DFSEvent.CROSS, u, v))\n            else:\n\
    \                depth -= 1\n                state[u] = 0 if DFSFlags.BACKTRACK\
    \ in flags else 2\n                if DFSFlags.LEAVE in flags:\n             \
    \       events.append((DFSEvent.LEAVE, u))\n                if depth != -1 and\
    \ DFSFlags.UP in flags:\n                    events.append((DFSEvent.UP, stack[depth],\
    \ u))\n        if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n            events.append((DFSEvent.UP,-1,s))\n\
    \    ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events\n    if\
    \ DFSFlags.RETURN_PARENTS in flags:\n        ret += (parents,)\n    if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n        ret += (depths,)\n    return ret\nfrom math import inf\n\n\
    def articulation_points(G, s: Union[int,list,None] = None):\n    \"\"\"\n    Find\
    \ articulation points in an undirected graph using DFS events.\n    Returns a\
    \ boolean list that is True for indices where the vertex is an articulation point.\n\
    \    \"\"\"\n    N = G.N\n    if s is None: s = range(N)\n    low, disc, children,\
    \ ap, time = [inf]*N, [-1]*N, [0]*N, [False]*N, 0    \n    flags = DFSFlags.DOWN\
    \ | DFSFlags.BACK | DFSFlags.UP | DFSFlags.RETURN_PARENTS\n    events, parent\
    \ = dfs_events(G, flags, s)\n    for event in events:\n        match event:\n\
    \            case DFSEvent.DOWN, u, v:\n                children[u] += 1\n   \
    \             disc[v] = low[v] = time\n                time += 1\n           \
    \ case DFSEvent.BACK, u, v:\n                if v != parent[u]:\n            \
    \        low[u] = min(low[u], disc[v])\n            case DFSEvent.UP, p, u:\n\
    \                if parent[p] != -1:\n                    low[p] = min(low[p],\
    \ low[u])\n                    ap[p] |= low[u] >= disc[p]\n                else:\n\
    \                    # root case\n                    ap[p] |= children[p] > 1\
    \    \n    return ap\n"
  code: "import cp_library.alg.graph.__header__\nfrom typing import Union\nfrom cp_library.alg.graph.dfs_events_fn\
    \ import DFSEvent, DFSFlags, dfs_events\nfrom math import inf\n\ndef articulation_points(G,\
    \ s: Union[int,list,None] = None):\n    \"\"\"\n    Find articulation points in\
    \ an undirected graph using DFS events.\n    Returns a boolean list that is True\
    \ for indices where the vertex is an articulation point.\n    \"\"\"\n    N =\
    \ G.N\n    if s is None: s = range(N)\n    low, disc, children, ap, time = [inf]*N,\
    \ [-1]*N, [0]*N, [False]*N, 0    \n    flags = DFSFlags.DOWN | DFSFlags.BACK |\
    \ DFSFlags.UP | DFSFlags.RETURN_PARENTS\n    events, parent = dfs_events(G, flags,\
    \ s)\n    for event in events:\n        match event:\n            case DFSEvent.DOWN,\
    \ u, v:\n                children[u] += 1\n                disc[v] = low[v] =\
    \ time\n                time += 1\n            case DFSEvent.BACK, u, v:\n   \
    \             if v != parent[u]:\n                    low[u] = min(low[u], disc[v])\n\
    \            case DFSEvent.UP, p, u:\n                if parent[p] != -1:\n  \
    \                  low[p] = min(low[p], low[u])\n                    ap[p] |=\
    \ low[u] >= disc[p]\n                else:\n                    # root case\n\
    \                    ap[p] |= children[p] > 1    \n    return ap"
  dependsOn:
  - cp_library/alg/graph/dfs_events_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/articulation_points_fn.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_3_a_articulation_points_fn.test.py
documentation_of: cp_library/alg/graph/articulation_points_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/articulation_points_fn.py
- /library/cp_library/alg/graph/articulation_points_fn.py.html
title: cp_library/alg/graph/articulation_points_fn.py
---