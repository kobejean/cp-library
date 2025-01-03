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
    \ndef find_cycle(G, s: int = 0):\n    state = [0] * G.N\n    depth = [0] * G.N\n\
    \    adj = [None] * G.N\n    stack = [s]\n    \n    while stack:\n        u =\
    \ stack[-1]\n        \n        if not state[u]:\n            state[u] = 1\n  \
    \          adj[u] = iter(G.neighbors(u))\n        \n        if (v := next(adj[u],\
    \ None)) is not None:\n            match state[v]:\n                case 0:  #\
    \ Unvisited\n                    depth[v] = len(stack)\n                    stack.append(v)\n\
    \                case 1:  # In progress\n                    return stack[depth[v]:]\n\
    \        else:\n            stack.pop()\n    return None\n"
  code: "import cp_library.alg.graph.__header__\n\ndef find_cycle(G, s: int = 0):\n\
    \    state = [0] * G.N\n    depth = [0] * G.N\n    adj = [None] * G.N\n    stack\
    \ = [s]\n    \n    while stack:\n        u = stack[-1]\n        \n        if not\
    \ state[u]:\n            state[u] = 1\n            adj[u] = iter(G.neighbors(u))\n\
    \        \n        if (v := next(adj[u], None)) is not None:\n            match\
    \ state[v]:\n                case 0:  # Unvisited\n                    depth[v]\
    \ = len(stack)\n                    stack.append(v)\n                case 1: \
    \ # In progress\n                    return stack[depth[v]:]\n        else:\n\
    \            stack.pop()\n    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/find_cycle_fn.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/find_cycle_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/find_cycle_fn.py
- /library/cp_library/alg/graph/find_cycle_fn.py.html
title: cp_library/alg/graph/find_cycle_fn.py
---
