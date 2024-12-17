---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/bir_cls.py
    title: cp_library/ds/bir_cls.py
  - icon: ':warning:'
    path: cp_library/math/inversion_cnt_fn.py
    title: cp_library/math/inversion_cnt_fn.py
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
    \nclass BinaryIndexTree:\n    def __init__(self, v: int|list):\n        if isinstance(v,\
    \ int):\n            self.data, self.size = [0]*v, v\n        else:\n        \
    \    self.build(v)\n\n    def build(self, data):\n        self.data, self.size\
    \ = data, len(data)\n        for i in range(self.size):\n            if (r :=\
    \ i|(i+1)) < self.size: \n                self.data[r] += self.data[i]\n\n   \
    \ def get(self, i: int):\n        assert 0 <= i < self.size\n        s = self.data[i]\n\
    \        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n           \
    \ s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def set(self,\
    \ i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n    def add(self,\
    \ i: int, x: int) -> None:\n        assert 0 <= i <= self.size\n        i += 1\n\
    \        data, size = self.data, self.size\n        while i <= size:\n       \
    \     data[i-1], i = data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n\
    \        assert 0 <= i <= self.size\n        s = 0\n        data = self.data\n\
    \        for _ in range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n\
    \        return s\n    \n    def range_sum(self, l: int, r: int):\n        return\
    \ self.pref_sum(r) - self.pref_sum(l)\n"
  code: "import cp_library.ds.__header__\n\nclass BinaryIndexTree:\n    def __init__(self,\
    \ v: int|list):\n        if isinstance(v, int):\n            self.data, self.size\
    \ = [0]*v, v\n        else:\n            self.build(v)\n\n    def build(self,\
    \ data):\n        self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            if (r := i|(i+1)) < self.size: \n                self.data[r] +=\
    \ self.data[i]\n\n    def get(self, i: int):\n        assert 0 <= i < self.size\n\
    \        s = self.data[i]\n        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ set(self, i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n \
    \   def add(self, i: int, x: int) -> None:\n        assert 0 <= i <= self.size\n\
    \        i += 1\n        data, size = self.data, self.size\n        while i <=\
    \ size:\n            data[i-1], i = data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self,\
    \ i: int):\n        assert 0 <= i <= self.size\n        s = 0\n        data =\
    \ self.data\n        for _ in range(i.bit_count()):\n            s, i = s+data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def range_sum(self, l: int, r: int):\n\
    \        return self.pref_sum(r) - self.pref_sum(l)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bit_cls.py
  requiredBy:
  - cp_library/math/inversion_cnt_fn.py
  - cp_library/ds/bir_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bit_cls.py
- /library/cp_library/ds/bit_cls.py.html
title: cp_library/ds/bit_cls.py
---
