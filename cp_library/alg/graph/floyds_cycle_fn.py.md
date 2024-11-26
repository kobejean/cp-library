---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
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
    \ndef floyds_cycle(F, root):\n    slow = fast = root\n    while F[fast] != -1\
    \ and F[F[fast]] != -1:\n        slow, fast = F[slow], F[F[fast]]\n        if\
    \ slow == fast:\n            cyc = [slow]\n            while F[slow] != cyc[0]:\n\
    \                slow = F[slow]\n                cyc.append(slow)\n          \
    \  return cyc\n    return None\n"
  code: "import cp_library.alg.graph.__header__\n\ndef floyds_cycle(F, root):\n  \
    \  slow = fast = root\n    while F[fast] != -1 and F[F[fast]] != -1:\n       \
    \ slow, fast = F[slow], F[F[fast]]\n        if slow == fast:\n            cyc\
    \ = [slow]\n            while F[slow] != cyc[0]:\n                slow = F[slow]\n\
    \                cyc.append(slow)\n            return cyc\n    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/floyds_cycle_fn.py
  requiredBy:
  - cp_library/alg/graph/edmonds_fn.py
  timestamp: '2024-11-26 21:56:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_b_edmonds_branching.test.py
documentation_of: cp_library/alg/graph/floyds_cycle_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyds_cycle_fn.py
- /library/cp_library/alg/graph/floyds_cycle_fn.py.html
title: cp_library/alg/graph/floyds_cycle_fn.py
---
