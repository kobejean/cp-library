---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting.py
    title: cp_library/alg/dp/rerooting.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting.test.py
    title: test/dp_v_subtree_rerooting.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n\
    \        self.size = len(data)\n        self.prefix = [e] + data.copy()\n    \
    \    self.suffix = data.copy() + [e]\n        self.e = e\n        self.op = op\n\
    \        for i in range(self.size):\n            self.prefix[i+1] = op(self.prefix[i],\
    \ self.prefix[i+1])\n        for i in range(self.size,0,-1):\n            self.suffix[i-1]\
    \ = op(self.suffix[i-1], self.suffix[i])\n    def left(self, l): return self.prefix[l]\n\
    \    def right(self, r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n\
    \    def out(self, l, r=None):\n        r = l+1 if r is None else r\n        return\
    \ self.op(self.prefix[l], self.suffix[r])\n    \n"
  code: "\nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n     \
    \   self.size = len(data)\n        self.prefix = [e] + data.copy()\n        self.suffix\
    \ = data.copy() + [e]\n        self.e = e\n        self.op = op\n        for i\
    \ in range(self.size):\n            self.prefix[i+1] = op(self.prefix[i], self.prefix[i+1])\n\
    \        for i in range(self.size,0,-1):\n            self.suffix[i-1] = op(self.suffix[i-1],\
    \ self.suffix[i])\n    def left(self, l): return self.prefix[l]\n    def right(self,\
    \ r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n    def\
    \ out(self, l, r=None):\n        r = l+1 if r is None else r\n        return self.op(self.prefix[l],\
    \ self.suffix[r])\n    \n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bidirectional_array.py
  requiredBy:
  - cp_library/alg/dp/rerooting.py
  timestamp: '2024-08-29 07:36:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dp_v_subtree_rerooting.test.py
documentation_of: cp_library/ds/bidirectional_array.py
layout: document
redirect_from:
- /library/cp_library/ds/bidirectional_array.py
- /library/cp_library/ds/bidirectional_array.py.html
title: cp_library/ds/bidirectional_array.py
---
