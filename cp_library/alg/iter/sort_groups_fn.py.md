---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc203_e_sort_groups.test.py
    title: test/abc203_e_sort_groups.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nfrom itertools import groupby\nfrom operator import itemgetter\n\
    \ndef sort_groups(A, key=0):\n    if isinstance(key,int):\n        key = itemgetter(key)\n\
    \    A.sort(key=key)\n    return sorted((k,list(g)) for k,g in groupby(A, key=key))\n\
    \n    \n"
  code: "import cp_library.alg.iter.__header__\nfrom itertools import groupby\nfrom\
    \ operator import itemgetter\n\ndef sort_groups(A, key=0):\n    if isinstance(key,int):\n\
    \        key = itemgetter(key)\n    A.sort(key=key)\n    return sorted((k,list(g))\
    \ for k,g in groupby(A, key=key))\n\n    "
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/sort_groups_fn.py
  requiredBy: []
  timestamp: '2024-12-08 02:40:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc203_e_sort_groups.test.py
documentation_of: cp_library/alg/iter/sort_groups_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/sort_groups_fn.py
- /library/cp_library/alg/iter/sort_groups_fn.py.html
title: cp_library/alg/iter/sort_groups_fn.py
---