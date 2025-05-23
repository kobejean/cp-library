---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    \n\nclass que01:\n    def __init__(self, hint=None):\n        if hint: self.q0,\
    \ self.q1 = elist(hint), elist(hint)\n        else: self.q0, self.q1 = [], []\n\
    \        \n    def push0(self, item):\n        self.q0.append(item)\n\n    def\
    \ push1(self, item):\n        self.q1.append(item)\n    \n    def pop(self):\n\
    \        if self.q0: return self.q0.pop()\n        self.q0, self.q1 = self.q1,\
    \ self.q0\n        return self.q0.pop()\n\n    def __len__(self):\n        return\
    \ len(self.q0) + len(self.q1)\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n\
    \    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n"
  code: "import cp_library.ds.__header__\nimport cp_library.ds.que.__header__\n\n\
    class que01:\n    def __init__(self, hint=None):\n        if hint: self.q0, self.q1\
    \ = elist(hint), elist(hint)\n        else: self.q0, self.q1 = [], []\n      \
    \  \n    def push0(self, item):\n        self.q0.append(item)\n\n    def push1(self,\
    \ item):\n        self.q1.append(item)\n    \n    def pop(self):\n        if self.q0:\
    \ return self.q0.pop()\n        self.q0, self.q1 = self.q1, self.q0\n        return\
    \ self.q0.pop()\n\n    def __len__(self):\n        return len(self.q0) + len(self.q1)\n\
    \nfrom cp_library.ds.elist_fn import elist"
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/que/que01_cls.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/que/que01_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/que/que01_cls.py
- /library/cp_library/ds/que/que01_cls.py.html
title: cp_library/ds/que/que01_cls.py
---
