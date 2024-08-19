---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_pivot.py
    title: cp_library/alg/divcon/partition_pivot.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect.py
    title: cp_library/alg/divcon/qselect.py
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
    import random\n\ndef partition(A, l, r, pi):\n    '''Partition subarray [l,r)'''\n\
    \    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n    for j in range(l,\
    \ r):\n        if A[j] <= A[r]:\n            A[pi], A[j] = A[j], A[pi]\n     \
    \       pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return pi\n\ndef kth_element(A,\
    \ k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n    if r is\
    \ None: r = len(A)\n    while True:\n        if l == r-1: return A[k]\n      \
    \  pi = partition(A, l, r, random.randint(l, r-1))\n        if k == pi:\n    \
    \        return A[k]\n        elif k < pi:\n            r = pi\n        else:\n\
    \            l = pi + 1\n\ndef rint(shift=0, base=10):\n    return [int(x, base)\
    \ + shift for x in input().split()]\n\nN, M = rint()\nA = rint()\nB = rint()\n\
    \nif M == 2:\n    print(0 if A == B else -1)\n    exit()\n\ndef rel(x,y):\n  \
    \  return max(-1,min(x-y,1))\n\nC = [B[0]]\n\nfor i in range(1,N):\n    c = C[-1]\
    \ - C[-1]%M + B[i]\n    for Ci in range(c-M,c+2*M,M):\n        if rel(A[i-1],A[i])\
    \ == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:\n            C.append(Ci)\n          \
    \  break\nmedian = kth_element([c-a for a,c in zip(A,C)], N//2)\nans = float('inf')\n\
    for i in range(median//M,median//M+2):\n    now=0\n    for j in range(N):\n  \
    \      now+=abs(A[j]+i*M-C[j])\n    ans=min(ans,now)\nprint(ans)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    from cp_library.alg.divcon.qselect import kth_element\n\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\nN, M = rint()\n\
    A = rint()\nB = rint()\n\nif M == 2:\n    print(0 if A == B else -1)\n    exit()\n\
    \ndef rel(x,y):\n    return max(-1,min(x-y,1))\n\nC = [B[0]]\n\nfor i in range(1,N):\n\
    \    c = C[-1] - C[-1]%M + B[i]\n    for Ci in range(c-M,c+2*M,M):\n        if\
    \ rel(A[i-1],A[i]) == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:\n            C.append(Ci)\n\
    \            break\nmedian = kth_element([c-a for a,c in zip(A,C)], N//2)\nans\
    \ = float('inf')\nfor i in range(median//M,median//M+2):\n    now=0\n    for j\
    \ in range(N):\n        now+=abs(A[j]+i*M-C[j])\n    ans=min(ans,now)\nprint(ans)"
  dependsOn:
  - cp_library/alg/divcon/qselect.py
  - cp_library/alg/divcon/partition_pivot.py
  isVerificationFile: true
  path: test/arc182_increment_decrement_again_qselect.test.py
  requiredBy: []
  timestamp: '2024-08-20 00:39:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc182_increment_decrement_again_qselect.test.py
layout: document
redirect_from:
- /verify/test/arc182_increment_decrement_again_qselect.test.py
- /verify/test/arc182_increment_decrement_again_qselect.test.py.html
title: test/arc182_increment_decrement_again_qselect.test.py
---
