---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/auxiliary_tree_cls.py
    title: cp_library/alg/tree/auxiliary_tree_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_fast_cls.py
    title: cp_library/alg/tree/tree_fast_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_set_cls.py
    title: cp_library/alg/tree/tree_set_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
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
    import operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter: Iterable[T], func: Callable[[T,T],T]\
    \ = None, initial: T = None, step = 1) -> list[T]:\n    match step:\n        case\
    \ 1:\n            return list(accumulate(iter, func, initial=initial))\n     \
    \   case step:\n            assert step >= 2\n            if func is None:\n \
    \               func = operator.add\n            A = list(iter)\n            if\
    \ initial is not None:\n                A = [initial] + A\n            for i in\
    \ range(step,len(A)):\n                A[i] = func(A[i], A[i-step])\n        \
    \    return A\n"
  code: "import cp_library.alg.iter.__header__\nimport operator\nfrom itertools import\
    \ accumulate\nfrom typing import Callable, Iterable, TypeVar\n\nT = TypeVar('T')\n\
    def presum(iter: Iterable[T], func: Callable[[T,T],T] = None, initial: T = None,\
    \ step = 1) -> list[T]:\n    match step:\n        case 1:\n            return\
    \ list(accumulate(iter, func, initial=initial))\n        case step:\n        \
    \    assert step >= 2\n            if func is None:\n                func = operator.add\n\
    \            A = list(iter)\n            if initial is not None:\n           \
    \     A = [initial] + A\n            for i in range(step,len(A)):\n          \
    \      A[i] = func(A[i], A[i-step])\n            return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_set_cls.py
  - cp_library/alg/tree/tree_fast_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/presum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum_fn.py
- /library/cp_library/alg/iter/presum_fn.py.html
title: cp_library/alg/iter/presum_fn.py
---
