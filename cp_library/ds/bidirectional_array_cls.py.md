---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/dp/rerooting_iterative_cls.py
    title: cp_library/alg/dp/rerooting_iterative_cls.py
  - icon: ':warning:'
    path: cp_library/alg/dp/rerooting_recursive_cls.py
    title: cp_library/alg/dp/rerooting_recursive_cls.py
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
    \nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n        self.size\
    \ = len(data)\n        self.prefix = [e] + data.copy()\n        self.suffix =\
    \ data.copy() + [e]\n        self.e = e\n        self.op = op\n        for i in\
    \ range(self.size):\n            self.prefix[i+1] = op(self.prefix[i], self.prefix[i+1])\n\
    \        for i in range(self.size,0,-1):\n            self.suffix[i-1] = op(self.suffix[i-1],\
    \ self.suffix[i])\n    def left(self, l): return self.prefix[l]\n    def right(self,\
    \ r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n    def\
    \ out(self, l, r=None):\n        r = l+1 if r is None else r\n        return self.op(self.prefix[l],\
    \ self.suffix[r])\n"
  code: "import cp_library.ds.__header__\nimport cp_library.__header__\n\nclass BidirectionalArray:\n\
    \    def __init__(self, e, op, data):\n        self.size = len(data)\n       \
    \ self.prefix = [e] + data.copy()\n        self.suffix = data.copy() + [e]\n \
    \       self.e = e\n        self.op = op\n        for i in range(self.size):\n\
    \            self.prefix[i+1] = op(self.prefix[i], self.prefix[i+1])\n       \
    \ for i in range(self.size,0,-1):\n            self.suffix[i-1] = op(self.suffix[i-1],\
    \ self.suffix[i])\n    def left(self, l): return self.prefix[l]\n    def right(self,\
    \ r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n    def\
    \ out(self, l, r=None):\n        r = l+1 if r is None else r\n        return self.op(self.prefix[l],\
    \ self.suffix[r])\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bidirectional_array_cls.py
  requiredBy:
  - cp_library/alg/dp/rerooting_iterative_cls.py
  - cp_library/alg/dp/rerooting_recursive_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bidirectional_array_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bidirectional_array_cls.py
- /library/cp_library/ds/bidirectional_array_cls.py.html
title: cp_library/ds/bidirectional_array_cls.py
---
