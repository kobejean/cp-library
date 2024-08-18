---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/kthelement.py
    title: cp_library/alg/kthelement.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/partition.py
    title: cp_library/alg/partition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc182/tasks/arc182_d
    links:
    - https://atcoder.jp/contests/arc182/tasks/arc182_d
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    \nimport random\n\ndef partition(A, l, r):\n    pi = random.randint(l, r)\n  \
    \  A[pi], A[r] = A[r], A[pi]\n    pivot = A[r]\n    i = l - 1\n    \n    for j\
    \ in range(l, r):\n        if A[j] <= pivot:\n            i += 1\n           \
    \ A[i], A[j] = A[j], A[i]\n    \n    A[i + 1], A[r] = A[r], A[i + 1]\n    return\
    \ i + 1\n\ndef kth_element(A, k, l=0, r=None):\n    if r is None:\n        r =\
    \ len(A) - 1\n    \n    while True:\n        if l == r: return A[k]\n        pi\
    \ = partition(A, l, r)\n        \n        if k == pi:\n            return A[k]\n\
    \        elif k < pi:\n            r = pi - 1\n        else:\n            l =\
    \ pi + 1\n\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift for\
    \ x in input().split()]\n\nN, M = rint()\nA = rint()\nB = rint()\n\nif M == 2:\n\
    \    print(0 if A == B else -1)\n    exit()\n\ndef rel(x,y):\n    return max(-1,min(x-y,1))\n\
    \nC = [B[0]]\n\nfor i in range(1,N):\n    c = C[-1] - C[-1]%M + B[i]\n    for\
    \ Ci in range(c-M,c+2*M,M):\n        if rel(A[i-1],A[i]) == rel(C[-1],Ci) and\
    \ abs(C[-1]-Ci)<M:\n            C.append(Ci)\n            break\nmedian = kth_element([c-a\
    \ for a,c in zip(A,C)], N//2)\nans = float('inf')\nfor i in range(median//M,median//M+2):\n\
    \    now=0\n    for j in range(N):\n        now+=abs(A[j]+i*M-C[j])\n    ans=min(ans,now)\n\
    print(ans)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    \nfrom cp_library.alg.kthelement import kth_element\n\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\nN, M = rint()\n\
    A = rint()\nB = rint()\n\nif M == 2:\n    print(0 if A == B else -1)\n    exit()\n\
    \ndef rel(x,y):\n    return max(-1,min(x-y,1))\n\nC = [B[0]]\n\nfor i in range(1,N):\n\
    \    c = C[-1] - C[-1]%M + B[i]\n    for Ci in range(c-M,c+2*M,M):\n        if\
    \ rel(A[i-1],A[i]) == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:\n            C.append(Ci)\n\
    \            break\nmedian = kth_element([c-a for a,c in zip(A,C)], N//2)\nans\
    \ = float('inf')\nfor i in range(median//M,median//M+2):\n    now=0\n    for j\
    \ in range(N):\n        now+=abs(A[j]+i*M-C[j])\n    ans=min(ans,now)\nprint(ans)"
  dependsOn:
  - cp_library/alg/kthelement.py
  - cp_library/alg/partition.py
  isVerificationFile: true
  path: test/arc182_increment_decrement_again_kthelement.test.py
  requiredBy: []
  timestamp: '2024-08-18 16:01:16+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc182_increment_decrement_again_kthelement.test.py
layout: document
redirect_from:
- /verify/test/arc182_increment_decrement_again_kthelement.test.py
- /verify/test/arc182_increment_decrement_again_kthelement.test.py.html
title: test/arc182_increment_decrement_again_kthelement.test.py
---
