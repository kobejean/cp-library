---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
    title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
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
    \n\n\n\ndef argsort_multi(*A: list[int], reverse=False):\n    s, m = pack_sm((N:=len(A[0]))-1)\n\
    \    I, J = [0]*N, [*range(N)]\n    if reverse:\n        V = [a<<s|m^i for i,a\
    \ in enumerate(A[-1])]; V.sort(reverse=True)\n        for k in range(len(A)-2,-1,-1):\n\
    \            B = A[k]\n            for i,v in enumerate(V):V[i],I[i]=B[j:=J[m^v&m]]<<s|m^i,j\n\
    \            I,J=J,I;V.sort(reverse=True)\n        for i,v in enumerate(V):I[i]=J[m^v&m]\n\
    \    else:\n        V = [a<<s|i for i,a in enumerate(A[-1])]; V.sort()\n     \
    \   for k in range(len(A)-2,-1,-1):\n            B = A[k]\n            for i,v\
    \ in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j\n            I,J=J,I;V.sort()\n\
    \        for i,v in enumerate(V):I[i]=J[v&m]\n    return I\n\n\ndef pack_sm(N:\
    \ int): s=N.bit_length(); return s,(1<<s)-1\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    import cp_library.alg.iter.arg.__header__\n\ndef argsort_multi(*A: list[int],\
    \ reverse=False):\n    s, m = pack_sm((N:=len(A[0]))-1)\n    I, J = [0]*N, [*range(N)]\n\
    \    if reverse:\n        V = [a<<s|m^i for i,a in enumerate(A[-1])]; V.sort(reverse=True)\n\
    \        for k in range(len(A)-2,-1,-1):\n            B = A[k]\n            for\
    \ i,v in enumerate(V):V[i],I[i]=B[j:=J[m^v&m]]<<s|m^i,j\n            I,J=J,I;V.sort(reverse=True)\n\
    \        for i,v in enumerate(V):I[i]=J[m^v&m]\n    else:\n        V = [a<<s|i\
    \ for i,a in enumerate(A[-1])]; V.sort()\n        for k in range(len(A)-2,-1,-1):\n\
    \            B = A[k]\n            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j\n\
    \            I,J=J,I;V.sort()\n        for i,v in enumerate(V):I[i]=J[v&m]\n \
    \   return I\nfrom cp_library.bit.pack.pack_sm_fn import pack_sm"
  dependsOn:
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/alg/iter/arg/argsort_multi_fn.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
documentation_of: cp_library/alg/iter/arg/argsort_multi_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/arg/argsort_multi_fn.py
- /library/cp_library/alg/iter/arg/argsort_multi_fn.py.html
title: cp_library/alg/iter/arg/argsort_multi_fn.py
---
