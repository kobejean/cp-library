---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/divcon/kthelement.py
    title: cp_library/divcon/kthelement.py
  - icon: ':warning:'
    path: cp_library/divcon/partition.py
    title: cp_library/divcon/partition.py
  - icon: ':warning:'
    path: cp_library/math/median.py
    title: cp_library/math/median.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc122/tasks/arc122_b
    links:
    - https://atcoder.jp/contests/arc122/tasks/arc122_b
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b\n\
    \nfrom fractions import Fraction\nfrom decimal import Decimal, getcontext\nfrom\
    \ statistics import mean\n\ndef partition(A, l, r):\n    pivot = A[r]\n    i =\
    \ l - 1\n    \n    for j in range(l, r):\n        if A[j] <= pivot:\n        \
    \    i += 1\n            A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r],\
    \ A[i + 1]\n    return i + 1\n\ndef kth_element(A, k, l=0, r=None):\n    if r\
    \ is None:\n        r = len(A) - 1\n    \n    while True:\n        if l == r:\
    \ return A[k]\n        pi = partition(A, l, r)\n        \n        if k == pi:\n\
    \            return A[k]\n        elif k < pi:\n            r = pi - 1\n     \
    \   else:\n            l = pi + 1\n\ndef median(A):\n    A = list(A)\n    n =\
    \ len(A)\n    m = n // 2\n    ret = kth_element(A, m)\n    if n % 2 == 0:\n  \
    \      return (ret + kth_element(A, m-1)) / 2\n    return ret\n\ndef rint(shift=0,\
    \ base=10):\n    return [int(x, base) + shift for x in input().split()]\n\ndef\
    \ ftod(fraction):\n    getcontext().prec = 50\n    return Decimal(fraction.numerator)\
    \ / Decimal(fraction.denominator)\n\ndef f(x):\n    x = Fraction(x)\n    return\
    \ x + mean(max(Fraction(0), a - 2*x) for a in A)\n\nN, = rint()\nA = rint()\n\
    x = Fraction(int(median(A)*2), 4)\nans = f(x)\nprint(f\"{ftod(ans):.20f}\")\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b\n\
    \nfrom fractions import Fraction\nfrom decimal import Decimal, getcontext\nfrom\
    \ statistics import mean\nfrom cp_library.math.median import median\n\ndef rint(shift=0,\
    \ base=10):\n    return [int(x, base) + shift for x in input().split()]\n\ndef\
    \ ftod(fraction):\n    getcontext().prec = 50\n    return Decimal(fraction.numerator)\
    \ / Decimal(fraction.denominator)\n\ndef f(x):\n    x = Fraction(x)\n    return\
    \ x + mean(max(Fraction(0), a - 2*x) for a in A)\n\nN, = rint()\nA = rint()\n\
    x = Fraction(int(median(A)*2), 4)\nans = f(x)\nprint(f\"{ftod(ans):.20f}\")"
  dependsOn:
  - cp_library/math/median.py
  - cp_library/divcon/kthelement.py
  - cp_library/divcon/partition.py
  isVerificationFile: false
  path: test/arc122_b_insurance_median.text.py
  requiredBy: []
  timestamp: '2024-08-18 15:24:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: test/arc122_b_insurance_median.text.py
layout: document
redirect_from:
- /library/test/arc122_b_insurance_median.text.py
- /library/test/arc122_b_insurance_median.text.py.html
title: test/arc122_b_insurance_median.text.py
---