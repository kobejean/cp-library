---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
    title: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
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
    \n\n\n\ndef icoord_compress_multi(*A: list[int], distinct = False):\n    N=sum(len(Ai)for\
    \ Ai in A);sj,mj=pack_sm(N-1);si,mi=pack_sm((len(A)-1)<<sj);V,k=[0]*N,0\n    for\
    \ i,Ai in enumerate(A):\n        for j, a in enumerate(Ai):V[k]=a<<si|i<<sj|j;k+=1\n\
    \    V.sort();r=p=-1\n    if distinct:\n        for r,aij in enumerate(V):a,i,j=aij>>si,(aij&mi)>>sj,aij&mj;A[i][j],V[r]=r,a\n\
    \    else:\n        for aij in V:\n            a,i,j=aij>>si,(aij&mi)>>sj,aij&mj\n\
    \            if a!=p:r+=1;V[r]=p=a\n            A[i][j]=r\n    return*A,V\n\n\n\
    def pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.cmpr.__header__\n\ndef icoord_compress_multi(*A: list[int],\
    \ distinct = False):\n    N=sum(len(Ai)for Ai in A);sj,mj=pack_sm(N-1);si,mi=pack_sm((len(A)-1)<<sj);V,k=[0]*N,0\n\
    \    for i,Ai in enumerate(A):\n        for j, a in enumerate(Ai):V[k]=a<<si|i<<sj|j;k+=1\n\
    \    V.sort();r=p=-1\n    if distinct:\n        for r,aij in enumerate(V):a,i,j=aij>>si,(aij&mi)>>sj,aij&mj;A[i][j],V[r]=r,a\n\
    \    else:\n        for aij in V:\n            a,i,j=aij>>si,(aij&mi)>>sj,aij&mj\n\
    \            if a!=p:r+=1;V[r]=p=a\n            A[i][j]=r\n    return*A,V\nfrom\
    \ cp_library.bit.pack.pack_sm_fn import pack_sm"
  dependsOn:
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/cmpr/icoord_compress_multi_fn.py
  requiredBy: []
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_set_range_composite_large_array.test.py
documentation_of: cp_library/alg/iter/cmpr/icoord_compress_multi_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/cmpr/icoord_compress_multi_fn.py
- /library/cp_library/alg/iter/cmpr/icoord_compress_multi_fn.py.html
title: cp_library/alg/iter/cmpr/icoord_compress_multi_fn.py
---
