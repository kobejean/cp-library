---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \ndef matmul(A,B,mod):\n    assert len(A[0]) == len(B)\n    N = len(A)\n    M\
    \ = len(B)\n    ret = [[0]*M for _ in range(N)] \n    for i,reti in enumerate(ret):\n\
    \        for k,a_ik in enumerate(A[i]):\n            for j,b_kj in enumerate(B[k]):\n\
    \                reti[j] = (reti[j] + a_ik*b_kj) % mod  \n\n    return ret \n\n\
    def matpow(A,k,mod):\n    N = len(A)\n    ret = [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n    tmp = A\n    for i in range(k.bit_length()):\n     \
    \   if (k >> i) & 1:\n            ret = matmul(ret,tmp,mod) \n        tmp = matmul(tmp,tmp,mod)\
    \ \n    return ret \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\nN, K = rint()\nA = [rint()\
    \ for _ in range(N)]\nB = matpow(A, K,mod)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \ndef matmul(A,B,mod):\n    assert len(A[0]) == len(B)\n    N = len(A)\n    M\
    \ = len(B)\n    ret = [[0]*M for _ in range(N)] \n    for i,reti in enumerate(ret):\n\
    \        for k,a_ik in enumerate(A[i]):\n            for j,b_kj in enumerate(B[k]):\n\
    \                reti[j] = (reti[j] + a_ik*b_kj) % mod  \n\n    return ret \n\n\
    def matpow(A,k,mod):\n    N = len(A)\n    ret = [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n    tmp = A\n    for i in range(k.bit_length()):\n     \
    \   if (k >> i) & 1:\n            ret = matmul(ret,tmp,mod) \n        tmp = matmul(tmp,tmp,mod)\
    \ \n    return ret \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\nN, K = rint()\nA = [rint()\
    \ for _ in range(N)]\nB = matpow(A, K,mod)\n\nfor row in B:\n    print(*row)\n"
  dependsOn: []
  isVerificationFile: true
  path: pow_of_matrix.test.py
  requiredBy: []
  timestamp: '2024-08-14 03:30:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: pow_of_matrix.test.py
layout: document
redirect_from:
- /verify/pow_of_matrix.test.py
- /verify/pow_of_matrix.test.py.html
title: pow_of_matrix.test.py
---
