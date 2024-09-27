---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_fn.py
    title: cp_library/alg/divcon/partition_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc122_b_insurance_median.test.py
    title: test/arc122_b_insurance_median.test.py
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
    \ndef median(A):\n    n = len(A)\n    m = n // 2\n    ret = qselect(A, m)\n  \
    \  if n % 2 == 0:\n        return (ret + qselect(A, m-1)) / 2\n    return ret\n\
    \n\nimport random\n\ndef partition(A, l, r, pi) -> int:\n    '''Partition subarray\
    \ [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n    for j in\
    \ range(l, r):\n        if A[j] <= A[r]:\n            A[pi], A[j] = A[j], A[pi]\n\
    \            pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return pi\n\ndef qselect(A,\
    \ k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n    if r is\
    \ None: r = len(A)\n    while True:\n        if l == r-1: return A[k]\n      \
    \  pi = partition(A, l, r, random.randint(l, r-1))\n        if k == pi:\n    \
    \        return A[k]\n        elif k < pi:\n            r = pi\n        else:\n\
    \            l = pi + 1\n"
  code: "import cp_library.math.__header__\n\ndef median(A):\n    n = len(A)\n   \
    \ m = n // 2\n    ret = qselect(A, m)\n    if n % 2 == 0:\n        return (ret\
    \ + qselect(A, m-1)) / 2\n    return ret\n\nfrom cp_library.alg.divcon.qselect_fn\
    \ import qselect"
  dependsOn:
  - cp_library/alg/divcon/qselect_fn.py
  - cp_library/alg/divcon/partition_fn.py
  isVerificationFile: false
  path: cp_library/math/median_fn.py
  requiredBy: []
  timestamp: '2024-09-28 04:04:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc122_b_insurance_median.test.py
documentation_of: cp_library/math/median_fn.py
layout: document
redirect_from:
- /library/cp_library/math/median_fn.py
- /library/cp_library/math/median_fn.py.html
title: cp_library/math/median_fn.py
---
