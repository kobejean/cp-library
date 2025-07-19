---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer3_cls.py
    title: cp_library/bit/pack/packer3_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n\n\ndef max2(a, b):\n    return a if a > b else b\n\ndef irank(*A: list[int],\
    \ distinct = False):\n    N = mxj = 0\n    for Ai in A: N += len(Ai); mxj = max2(mxj,\
    \ len(Ai))\n    P = Packer3(len(A)-1, mxj); V = P.enumerate(A, N); V.sort()\n\
    \    if distinct:\n        for r,aij in enumerate(V):a,i,j=P.dec(aij);A[i][j],V[r]=r,a\n\
    \    elif V:\n        r, p = -1, V[-1]+1 # set p to unique value to trigger `if\
    \ a != p` on first elm\n        for aij in V:\n            a,i,j=P.dec(aij)\n\
    \            if a!=p:V[r:=r+1]=p=a\n            A[i][j]=r\n        del V[r+1:]\n\
    \    return V\n\n\n\nclass Packer3:\n    def __init__(P, mxb: int, mxc: int):\n\
    \        bb, bc = mxb.bit_length(), mxc.bit_length()\n        P.mc, P.mb, P.sb,\
    \ P.sa = (1<<bc)-1, (1<<bb)-1, bc, bc+bb\n    def enc(P, a: int, b: int, c: int):\
    \ return a << P.sa | b << P.sb | c\n    def dec(P, x: int) -> tuple[int, int,\
    \ int]: return x >> P.sa, (x >> P.sb) & P.mb, x & P.mc\n    def enumerate(P, A,\
    \ N, reverse=False): \n        V, k = [0]*N, 0\n        if reverse:\n        \
    \    for i,Ai in enumerate(A):\n                for j, a in enumerate(Ai):V[k]=P.enc(-a,\
    \ i, j);k+=1\n        else:\n            for i,Ai in enumerate(A):\n         \
    \       for j, a in enumerate(Ai):V[k]=P.enc(a, i, j);k+=1\n        return V\n\
    \ndef rank(*A: list[int], distinct = False): return *(R := tuple(Ai.copy() for\
    \ Ai in A)), irank(*R, distinct)\n"
  code: 'import cp_library.__header__

    import cp_library.alg.__header__

    import cp_library.alg.iter.__header__

    import cp_library.alg.iter.rank.__header__

    from cp_library.alg.iter.rank.irank_multi_fn import irank


    def rank(*A: list[int], distinct = False): return *(R := tuple(Ai.copy() for Ai
    in A)), irank(*R, distinct)'
  dependsOn:
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  isVerificationFile: false
  path: cp_library/alg/iter/rank/rank_multi_fn.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/rank/rank_multi_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/rank/rank_multi_fn.py
- /library/cp_library/alg/iter/rank/rank_multi_fn.py.html
title: cp_library/alg/iter/rank/rank_multi_fn.py
---
