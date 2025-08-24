---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/stack_operations.py
    title: perf/stack_operations.py
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
    \n\n\nclass stack:\n    __slots__ = 'd', 'n'\n    def __init__(st, cap): st.d,\
    \ st.n = [0]*cap, 0\n    def push(st, x): st.d[st.n] = x; st.n += 1\n    def pop(st):\
    \ st.n -= 1; return st.d[st.n]\n    def peek(st): return st.d[st.n-1]\n    def\
    \ __len__(st): return st.n\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.stack.__header__\n\
    \nclass stack:\n    __slots__ = 'd', 'n'\n    def __init__(st, cap): st.d, st.n\
    \ = [0]*cap, 0\n    def push(st, x): st.d[st.n] = x; st.n += 1\n    def pop(st):\
    \ st.n -= 1; return st.d[st.n]\n    def peek(st): return st.d[st.n-1]\n    def\
    \ __len__(st): return st.n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/stack/stack_fn.py
  requiredBy:
  - perf/stack_operations.py
  timestamp: '2025-08-24 20:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/stack/stack_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/stack/stack_fn.py
- /library/cp_library/ds/stack/stack_fn.py.html
title: cp_library/ds/stack/stack_fn.py
---
