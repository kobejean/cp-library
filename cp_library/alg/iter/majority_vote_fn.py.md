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
    \n\n\ndef majority_vote(A: list[int], default = None):\n    T = len(A) >> 1\n\
    \    cnt = val = 0\n    for a in A:\n        if cnt: cnt += 1 if a == val else\
    \ -1\n        else: cnt, val = 1, a\n    return val if cnt and A.count(val) >\
    \ T else default\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \ndef majority_vote(A: list[int], default = None):\n    T = len(A) >> 1\n    cnt\
    \ = val = 0\n    for a in A:\n        if cnt: cnt += 1 if a == val else -1\n \
    \       else: cnt, val = 1, a\n    return val if cnt and A.count(val) > T else\
    \ default"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/majority_vote_fn.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/majority_vote_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/majority_vote_fn.py
- /library/cp_library/alg/iter/majority_vote_fn.py.html
title: cp_library/alg/iter/majority_vote_fn.py
---
