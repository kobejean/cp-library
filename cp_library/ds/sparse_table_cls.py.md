---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
    title: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq_general.test.py
    title: test/library-checker/data-structure/staticrmq_general.test.py
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
    from typing import Generic, Callable\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    _U = TypeVar('U')\n\n\nclass SparseTable(Generic[_T]):\n    def __init__(st, op:\
    \ Callable[[_T,_T],_T], arr: list[_T]):\n        st.N = N = len(arr)\n       \
    \ st.log, st.op = N.bit_length(), op\n        st.data = [0] * (st.log*N)\n   \
    \     st.data[:N] = arr\n        for i in range(1,st.log):\n            a,b,c=i*N,(i-1)*N,(i-1)*N+(1<<(i-1))\n\
    \            for j in range(N-(1<<i)+1):\n                st.data[a+j] = op(st.data[b+j],\
    \ st.data[c+j])\n\n    def query(st, l: int, r: int) -> _T:\n        k = (r-l).bit_length()-1\n\
    \        return st.op(st.data[k*st.N+l],st.data[k*st.N+r-(1<<k)])\n"
  code: "import cp_library.__header__\nfrom typing import Generic, Callable\nfrom\
    \ cp_library.misc.typing import _T\nimport cp_library.ds.__header__\n\nclass SparseTable(Generic[_T]):\n\
    \    def __init__(st, op: Callable[[_T,_T],_T], arr: list[_T]):\n        st.N\
    \ = N = len(arr)\n        st.log, st.op = N.bit_length(), op\n        st.data\
    \ = [0] * (st.log*N)\n        st.data[:N] = arr\n        for i in range(1,st.log):\n\
    \            a,b,c=i*N,(i-1)*N,(i-1)*N+(1<<(i-1))\n            for j in range(N-(1<<i)+1):\n\
    \                st.data[a+j] = op(st.data[b+j], st.data[c+j])\n\n    def query(st,\
    \ l: int, r: int) -> _T:\n        k = (r-l).bit_length()-1\n        return st.op(st.data[k*st.N+l],st.data[k*st.N+r-(1<<k)])"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/sparse_table_cls.py
  requiredBy:
  - cp_library/alg/tree/lca_table_recursive_cls.py
  timestamp: '2025-05-23 09:29:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/staticrmq_general.test.py
  - test/aoj/grl/grl_5_c_lca_table_recursive.test.py
documentation_of: cp_library/ds/sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/sparse_table_cls.py
- /library/cp_library/ds/sparse_table_cls.py.html
title: cp_library/ds/sparse_table_cls.py
---
