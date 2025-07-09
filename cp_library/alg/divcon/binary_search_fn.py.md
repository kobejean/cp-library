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
    from typing import Callable\n\n\n\ndef binary_search(ac: int, wa: int, judge:\
    \ Callable[[int],bool]):\n    if ac < wa:\n        while 1<(wa-ac):\n        \
    \    if judge(wj := (ac+wa)>>1): ac = wj\n            else: wa = wj\n    else:\n\
    \        while 1<(ac-wa):\n            if judge(wj := (ac+wa)>>1): ac = wj\n \
    \           else: wa = wj\n    return ac\n"
  code: "import cp_library.__header__\nfrom typing import Callable\nimport cp_library.alg.__header__\n\
    import cp_library.alg.divcon.__header__\n\ndef binary_search(ac: int, wa: int,\
    \ judge: Callable[[int],bool]):\n    if ac < wa:\n        while 1<(wa-ac):\n \
    \           if judge(wj := (ac+wa)>>1): ac = wj\n            else: wa = wj\n \
    \   else:\n        while 1<(ac-wa):\n            if judge(wj := (ac+wa)>>1): ac\
    \ = wj\n            else: wa = wj\n    return ac"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/divcon/binary_search_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/divcon/binary_search_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/divcon/binary_search_fn.py
- /library/cp_library/alg/divcon/binary_search_fn.py.html
title: cp_library/alg/divcon/binary_search_fn.py
---
