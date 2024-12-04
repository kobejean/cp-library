---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
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
    \nclass BinaryIndexRange:\n    def __init__(self, size: int):\n        self.size\
    \ = size\n        self.bit1 = BinaryIndexTree(size)\n        self.bit2 = BinaryIndexTree(size)\n\
    \n    def add(self, l, r, x) -> None:\n        \"\"\"Add x to all elements in\
    \ range [l, r)\"\"\"\n        self.bit1.add(l, x * l)\n        self.bit1.add(r,\
    \ -x * r)\n        self.bit2.add(l, x)\n        self.bit2.add(r, -x)\n\n    def\
    \ pref_sum(self, i):\n        \"\"\"Get sum of elements in range [0, i)\"\"\"\n\
    \        return self.bit1.pref_sum(i) - i * self.bit2.pref_sum(i)\n\n    def range_sum(self,\
    \ l, r):\n        \"\"\"Get sum of elements in range [l, r)\"\"\"\n        return\
    \ self.pref_sum(r) - self.pref_sum(l)\n\n    def get(self, i):\n        \"\"\"\
    Get the value at index i\"\"\"\n        return self.range_sum(i, i+1)\n\n    def\
    \ set(self, i, x):\n        \"\"\"Set the value at index i to x\"\"\"\n      \
    \  self.add(i, i+1, x - self.get(i))\n        \n\nclass BinaryIndexTree:\n   \
    \ def __init__(self, v: int|list):\n        if isinstance(v, int):\n         \
    \   self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: int) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        data, size\
    \ = self.data, self.size\n        while i <= size:\n            data[i-1], i =\
    \ data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0\
    \ <= i <= self.size\n        s = 0\n        data = self.data\n        for _ in\
    \ range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n        return\
    \ s\n    \n    def range_sum(self, l: int, r: int):\n        return self.pref_sum(r)\
    \ - self.pref_sum(l)\n"
  code: "import cp_library.ds.__header__\n\nclass BinaryIndexRange:\n    def __init__(self,\
    \ size: int):\n        self.size = size\n        self.bit1 = BinaryIndexTree(size)\n\
    \        self.bit2 = BinaryIndexTree(size)\n\n    def add(self, l, r, x) -> None:\n\
    \        \"\"\"Add x to all elements in range [l, r)\"\"\"\n        self.bit1.add(l,\
    \ x * l)\n        self.bit1.add(r, -x * r)\n        self.bit2.add(l, x)\n    \
    \    self.bit2.add(r, -x)\n\n    def pref_sum(self, i):\n        \"\"\"Get sum\
    \ of elements in range [0, i)\"\"\"\n        return self.bit1.pref_sum(i) - i\
    \ * self.bit2.pref_sum(i)\n\n    def range_sum(self, l, r):\n        \"\"\"Get\
    \ sum of elements in range [l, r)\"\"\"\n        return self.pref_sum(r) - self.pref_sum(l)\n\
    \n    def get(self, i):\n        \"\"\"Get the value at index i\"\"\"\n      \
    \  return self.range_sum(i, i+1)\n\n    def set(self, i, x):\n        \"\"\"Set\
    \ the value at index i to x\"\"\"\n        self.add(i, i+1, x - self.get(i))\n\
    \        \nfrom cp_library.ds.bit_cls import BinaryIndexTree"
  dependsOn:
  - cp_library/ds/bit_cls.py
  isVerificationFile: false
  path: cp_library/ds/bir_cls.py
  requiredBy: []
  timestamp: '2024-12-05 01:48:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bir_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bir_cls.py
- /library/cp_library/ds/bir_cls.py.html
title: cp_library/ds/bir_cls.py
---
