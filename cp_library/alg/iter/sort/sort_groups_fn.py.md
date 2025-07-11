---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc203_e_sort_groups.test.py
    title: test/atcoder/abc/abc203_e_sort_groups.test.py
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
    from itertools import groupby\nfrom operator import itemgetter\n\n\n\n\ndef sort_groups(A,\
    \ key=0):\n    if isinstance(key,int):\n        key = itemgetter(key)\n    A.sort(key=key)\n\
    \    return sorted((k,list(g)) for k,g in groupby(A, key=key))\n\n    \n"
  code: "import cp_library.__header__\nfrom itertools import groupby\nfrom operator\
    \ import itemgetter\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.sort.__header__\n\ndef sort_groups(A, key=0):\n   \
    \ if isinstance(key,int):\n        key = itemgetter(key)\n    A.sort(key=key)\n\
    \    return sorted((k,list(g)) for k,g in groupby(A, key=key))\n\n    "
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sort/sort_groups_fn.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc203_e_sort_groups.test.py
documentation_of: cp_library/alg/iter/sort/sort_groups_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort/sort_groups_fn.py
- /library/cp_library/alg/iter/sort/sort_groups_fn.py.html
title: cp_library/alg/iter/sort/sort_groups_fn.py
---
