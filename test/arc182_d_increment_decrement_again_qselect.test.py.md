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
    from math import inf\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\nimport random\n\ndef partition(A, l, r, pi) -> int:\n    '''Partition\
    \ subarray [l,r)'''\n    r -= 1\n    A[pi], A[r] = A[r], A[pi]\n    pi = l\n \
    \   for j in range(l, r):\n        if A[j] <= A[r]:\n            A[pi], A[j] =\
    \ A[j], A[pi]\n            pi += 1\n    A[pi], A[r] = A[r], A[pi]\n    return\
    \ pi\n\ndef qselect(A, k, l=0, r=None):\n    '''Find kth element in subarray [l,r)'''\n\
    \    if r is None: r = len(A)\n    while True:\n        if l == r-1: return A[k]\n\
    \        pi = partition(A, l, r, random.randint(l, r-1))\n        if k == pi:\n\
    \            return A[k]\n        elif k < pi:\n            r = pi\n        else:\n\
    \            l = pi + 1\n\n\ndef read(shift=0, base=10):\n    return [int(s, base)\
    \ + shift for s in input().split()]\n\ndef main():\n    N, M = read()\n    A =\
    \ read()\n    B = read()\n\n    if M == 2:\n        print(0 if A == B else -1)\n\
    \        exit()\n\n    def rel(x,y):\n        return max(-1,min(x-y,1))\n\n  \
    \  C = [B[0]]\n\n    for i in range(1,N):\n        c = C[-1] - C[-1]%M + B[i]\n\
    \        for Ci in range(c-M,c+2*M,M):\n            if rel(A[i-1],A[i]) == rel(C[-1],Ci)\
    \ and abs(C[-1]-Ci)<M:\n                C.append(Ci)\n                break\n\
    \    median = qselect([c-a for a,c in zip(A,C)], N//2)\n    ans = inf\n    for\
    \ i in range(median//M,median//M+2):\n        now=0\n        for j in range(N):\n\
    \            now+=abs(A[j]+i*M-C[j])\n        ans=min(ans,now)\n    print(ans)\n\
    \    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    from math import inf\nfrom cp_library.alg.divcon.qselect_fn import qselect\nfrom\
    \ cp_library.io.read_int_fn import read\n\ndef main():\n    N, M = read()\n  \
    \  A = read()\n    B = read()\n\n    if M == 2:\n        print(0 if A == B else\
    \ -1)\n        exit()\n\n    def rel(x,y):\n        return max(-1,min(x-y,1))\n\
    \n    C = [B[0]]\n\n    for i in range(1,N):\n        c = C[-1] - C[-1]%M + B[i]\n\
    \        for Ci in range(c-M,c+2*M,M):\n            if rel(A[i-1],A[i]) == rel(C[-1],Ci)\
    \ and abs(C[-1]-Ci)<M:\n                C.append(Ci)\n                break\n\
    \    median = qselect([c-a for a,c in zip(A,C)], N//2)\n    ans = inf\n    for\
    \ i in range(median//M,median//M+2):\n        now=0\n        for j in range(N):\n\
    \            now+=abs(A[j]+i*M-C[j])\n        ans=min(ans,now)\n    print(ans)\n\
    \    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/alg/divcon/qselect_fn.py
  - cp_library/io/read_int_fn.py
  - cp_library/alg/divcon/partition_fn.py
  isVerificationFile: true
  path: test/arc182_d_increment_decrement_again_qselect.test.py
  requiredBy: []
  timestamp: '2024-11-22 04:31:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc182_d_increment_decrement_again_qselect.test.py
layout: document
redirect_from:
- /verify/test/arc182_d_increment_decrement_again_qselect.test.py
- /verify/test/arc182_d_increment_decrement_again_qselect.test.py.html
title: test/arc182_d_increment_decrement_again_qselect.test.py
---
