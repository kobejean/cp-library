---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_fn.py
    title: cp_library/alg/divcon/partition_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/median_fn.py
    title: cp_library/math/median_fn.py
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
    \ statistics import mean\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\ndef median(A):\n    n = len(A)\n    m = n // 2\n    ret\
    \ = qselect(A, m)\n    if n % 2 == 0:\n        return (ret + qselect(A, m-1))\
    \ / 2\n    return ret\n\n\nimport random\n\ndef partition(A, l, r, pi) -> int:\n\
    \    '''Partition subarray [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n\
    \    pi = l\n    for j in range(l, r):\n        if A[j] <= A[r]:\n           \
    \ A[pi], A[j] = A[j], A[pi]\n            pi += 1\n    A[pi], A[r] = A[r], A[pi]\n\
    \    return pi\n\ndef qselect(A, k, l=0, r=None):\n    '''Find kth element in\
    \ subarray [l,r)'''\n    if r is None: r = len(A)\n    while True:\n        if\
    \ l == r-1: return A[k]\n        pi = partition(A, l, r, random.randint(l, r-1))\n\
    \        if k == pi:\n            return A[k]\n        elif k < pi:\n        \
    \    r = pi\n        else:\n            l = pi + 1\n\n\ndef read(shift=0, base=10):\n\
    \    return [int(s, base) + shift for s in input().split()]\n\ndef ftod(fraction):\n\
    \    getcontext().prec = 50\n    return Decimal(fraction.numerator) / Decimal(fraction.denominator)\n\
    \ndef main():\n    N, = read()\n    A = read()\n    x = Fraction(int(median(A)*2),\
    \ 4)\n    ans = x + mean(max(Fraction(0), a - 2*x) for a in A)\n    print(f\"\
    {ftod(ans):.20f}\")\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b\n\
    \nfrom fractions import Fraction\nfrom decimal import Decimal, getcontext\nfrom\
    \ statistics import mean\nfrom cp_library.math.median_fn import median\nfrom cp_library.io.read_int_fn\
    \ import read\n\ndef ftod(fraction):\n    getcontext().prec = 50\n    return Decimal(fraction.numerator)\
    \ / Decimal(fraction.denominator)\n\ndef main():\n    N, = read()\n    A = read()\n\
    \    x = Fraction(int(median(A)*2), 4)\n    ans = x + mean(max(Fraction(0), a\
    \ - 2*x) for a in A)\n    print(f\"{ftod(ans):.20f}\")\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/math/median_fn.py
  - cp_library/io/read_int_fn.py
  - cp_library/alg/divcon/qselect_fn.py
  - cp_library/alg/divcon/partition_fn.py
  isVerificationFile: true
  path: test/arc122_b_insurance_median.test.py
  requiredBy: []
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc122_b_insurance_median.test.py
layout: document
redirect_from:
- /verify/test/arc122_b_insurance_median.test.py
- /verify/test/arc122_b_insurance_median.test.py.html
title: test/arc122_b_insurance_median.test.py
---
