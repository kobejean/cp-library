---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
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
    \n\nclass Que01:\n    def __init__(que, hint=None):\n        if hint: que.q0,\
    \ que.q1 = elist(hint), elist(hint)\n        else: que.q0, que.q1 = [], []\n \
    \   def push0(que, item): que.q0.append(item)\n    def push1(que, item): que.q1.append(item)\n\
    \    def pop(que):\n        if que.q0: return que.q0.pop()\n        que.q0, que.q1\
    \ = que.q1, que.q0\n        return que.q0.pop()\n    def __len__(que): return\
    \ len(que.q0) + len(que.q1)\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n\
    \    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n"
  code: "import cp_library.ds.__header__\nimport cp_library.ds.que.__header__\n\n\
    class Que01:\n    def __init__(que, hint=None):\n        if hint: que.q0, que.q1\
    \ = elist(hint), elist(hint)\n        else: que.q0, que.q1 = [], []\n    def push0(que,\
    \ item): que.q0.append(item)\n    def push1(que, item): que.q1.append(item)\n\
    \    def pop(que):\n        if que.q0: return que.q0.pop()\n        que.q0, que.q1\
    \ = que.q1, que.q0\n        return que.q0.pop()\n    def __len__(que): return\
    \ len(que.q0) + len(que.q1)\nfrom cp_library.ds.list.elist_fn import elist"
  dependsOn:
  - cp_library/ds/list/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/que/que01_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/que/que01_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/que/que01_cls.py
- /library/cp_library/ds/que/que01_cls.py.html
title: cp_library/ds/que/que01_cls.py
---
