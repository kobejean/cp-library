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
    from typing import Iterable, Union\n\ndef counter(A: Iterable[int], N: Union[int,list[int],None]\
    \ = None):\n    if isinstance(N, int): cnt = [0]*N\n    elif N is None: cnt =\
    \ [0]*(N := max(A := list(A))+1)\n    else:  N, cnt = len(N), N\n    for a in\
    \ A: cnt[a] += 1\n    return cnt\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import Iterable, Union\n\
    \ndef counter(A: Iterable[int], N: Union[int,list[int],None] = None):\n    if\
    \ isinstance(N, int): cnt = [0]*N\n    elif N is None: cnt = [0]*(N := max(A :=\
    \ list(A))+1)\n    else:  N, cnt = len(N), N\n    for a in A: cnt[a] += 1\n  \
    \  return cnt"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/counter_fn.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/counter_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/counter_fn.py
- /library/cp_library/alg/iter/counter_fn.py.html
title: cp_library/alg/iter/counter_fn.py
---