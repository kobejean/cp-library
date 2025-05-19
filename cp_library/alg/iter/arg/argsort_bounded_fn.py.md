---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc.test.py
    title: test/library-checker/graph/incremental_scc.test.py
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
    \n\n\n\ndef argsort_bounded(A, mx):\n    I, cnt, t = [0]*len(A), [0]*(mx+1), 0\n\
    \    for a in A: cnt[a] += 1\n    for a in range(mx+1): cnt[a], t = t, t+cnt[a]\n\
    \    for i,a in enumerate(A): I[cnt[a]] = i; cnt[a] += 1\n    return I\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.arg.__header__\n\ndef argsort_bounded(A, mx):\n   \
    \ I, cnt, t = [0]*len(A), [0]*(mx+1), 0\n    for a in A: cnt[a] += 1\n    for\
    \ a in range(mx+1): cnt[a], t = t, t+cnt[a]\n    for i,a in enumerate(A): I[cnt[a]]\
    \ = i; cnt[a] += 1\n    return I"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/arg/argsort_bounded_fn.py
  requiredBy: []
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/incremental_scc.test.py
documentation_of: cp_library/alg/iter/arg/argsort_bounded_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/arg/argsort_bounded_fn.py
- /library/cp_library/alg/iter/arg/argsort_bounded_fn.py.html
title: cp_library/alg/iter/arg/argsort_bounded_fn.py
---
