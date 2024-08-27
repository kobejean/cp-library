---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_pivot.py
    title: cp_library/alg/divcon/partition_pivot.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect.py
    title: cp_library/alg/divcon/qselect.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/median.py
    title: cp_library/math/median.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc122/tasks/arc122_b
    links:
    - https://atcoder.jp/contests/arc122/tasks/arc122_b
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b\n\
    \nfrom fractions import Fraction\nfrom decimal import Decimal, getcontext\nfrom\
    \ statistics import mean\nimport random\n\ndef partition(A, l, r, pi):\n    '''Partition\
    \ subarray [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n \
    \   for j in range(l, r):\n        if A[j] <= A[r]:\n            A[pi], A[j] =\
    \ A[j], A[pi]\n            pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return\
    \ pi\n\ndef kth_element(A, k, l=0, r=None):\n    '''Find kth element in subarray\
    \ [l,r)'''\n    if r is None: r = len(A)\n    while True:\n        if l == r-1:\
    \ return A[k]\n        pi = partition(A, l, r, random.randint(l, r-1))\n     \
    \   if k == pi:\n            return A[k]\n        elif k < pi:\n            r\
    \ = pi\n        else:\n            l = pi + 1\n\ndef median(A):\n    n = len(A)\n\
    \    m = n // 2\n    ret = kth_element(A, m)\n    if n % 2 == 0:\n        return\
    \ (ret + kth_element(A, m-1)) / 2\n    return ret\n\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\ndef ftod(fraction):\n\
    \    getcontext().prec = 50\n    return Decimal(fraction.numerator) / Decimal(fraction.denominator)\n\
    \ndef f(x):\n    x = Fraction(x)\n    return x + mean(max(Fraction(0), a - 2*x)\
    \ for a in A)\n\nN, = rint()\nA = rint()\nx = Fraction(int(median(A)*2), 4)\n\
    ans = f(x)\nprint(f\"{ftod(ans):.20f}\")\n"
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
  - cp_library/alg/divcon/qselect.py
  - cp_library/alg/divcon/partition_pivot.py
  isVerificationFile: true
  path: test/arc122_b_insurance_median.test.py
  requiredBy: []
  timestamp: '2024-08-28 02:08:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc122_b_insurance_median.test.py
layout: document
redirect_from:
- /verify/test/arc122_b_insurance_median.test.py
- /verify/test/arc122_b_insurance_median.test.py.html
title: test/arc122_b_insurance_median.test.py
---
