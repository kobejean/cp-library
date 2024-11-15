---
data:
  _extendedDependsOn: []
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
    \nclass BinaryIndexTree:\n    def __init__(self, e, op, v: int|list):\n      \
    \  self.e, self.op = e, op\n        if isinstance(v, int):\n            self.data,\
    \ self.size = [e]*v, v\n        else:\n            self.build(v)\n\n    def build(self,\
    \ data):\n        self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            r = i|(i+1)\n            if r < self.size: \n                self.data[r]\
    \ = self.op(self.data[i], self.data[r])\n\n    def add(self, i: int, x: object)\
    \ -> None:\n        assert 0 <= i <= self.size\n        i += 1\n        while\
    \ i <= self.size:\n            self.data[i-1], i = self.op(self.data[i-1], x),\
    \ i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n\
    \        s = self.e\n        while i > 0:\n            s, i = self.op(s, self.data[i-1]),\
    \ i-(i&-i)\n        return s\n    \n\nclass BinaryIndexTreePURQ(BinaryIndexTree):\n\
    \    def __init__(self, e, op, inv, v: int|list):\n        self.inv = inv\n  \
    \      super().__init__(e, op, v)\n\n    def range_sum(self, l: int, r: int) ->\
    \ object:\n        return self.op(self.pref_sum(r), self.inv(self.pref_sum(l)))\n"
  code: "import cp_library.ds.__header__\n\nclass BinaryIndexTree:\n    def __init__(self,\
    \ e, op, v: int|list):\n        self.e, self.op = e, op\n        if isinstance(v,\
    \ int):\n            self.data, self.size = [e]*v, v\n        else:\n        \
    \    self.build(v)\n\n    def build(self, data):\n        self.data, self.size\
    \ = data, len(data)\n        for i in range(self.size):\n            r = i|(i+1)\n\
    \            if r < self.size: \n                self.data[r] = self.op(self.data[i],\
    \ self.data[r])\n\n    def add(self, i: int, x: object) -> None:\n        assert\
    \ 0 <= i <= self.size\n        i += 1\n        while i <= self.size:\n       \
    \     self.data[i-1], i = self.op(self.data[i-1], x), i+(i&-i)\n\n    def pref_sum(self,\
    \ i: int):\n        assert 0 <= i <= self.size\n        s = self.e\n        while\
    \ i > 0:\n            s, i = self.op(s, self.data[i-1]), i-(i&-i)\n        return\
    \ s\n    \n\nclass BinaryIndexTreePURQ(BinaryIndexTree):\n    def __init__(self,\
    \ e, op, inv, v: int|list):\n        self.inv = inv\n        super().__init__(e,\
    \ op, v)\n\n    def range_sum(self, l: int, r: int) -> object:\n        return\
    \ self.op(self.pref_sum(r), self.inv(self.pref_sum(l)))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bit_generalized_cls.py
  requiredBy: []
  timestamp: '2024-11-16 03:24:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bit_generalized_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bit_generalized_cls.py
- /library/cp_library/ds/bit_generalized_cls.py.html
title: cp_library/ds/bit_generalized_cls.py
---
