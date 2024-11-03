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
  bundledCode: "\nclass BinaryIndexTree:\n    def __init__(self, v: int|list):\n \
    \       if isinstance(v, int):\n            self.data, self.size = [0]*v, v\n\
    \        else:\n            self.build(v)\n\n    def build(self, data):\n    \
    \    self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            if (r := i|(i+1)) < self.size: \n                self.data[r] +=\
    \ self.data[i]\n\n    def get(self, i: int):\n        assert 0 <= i < self.size\n\
    \        s = self.data[i]\n        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ set(self, i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n \
    \   def add(self, i: int, x: object) -> None:\n        assert 0 <= i <= self.size\n\
    \        i += 1\n        while i <= self.size:\n            self.data[i-1], i\
    \ = self.data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert\
    \ 0 <= i <= self.size\n        s = 0\n        for _ in range(i.bit_count()):\n\
    \            s, i = s+self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ range_sum(self, l: int, r: int):\n        return self.pref_sum(r) - self.pref_sum(l)\n\
    \nbit = BinaryIndexTree(list(range(100)))\nl,r = 5,7\na = bit.pref_sum(r) - bit.pref_sum(l)\n\
    b = bit.range_sum(l,r)\nprint(a, b)\nfor i in range(100):\n    assert bit.range_sum(i,i+1)\
    \ == bit.get(i)\n"
  code: "\nclass BinaryIndexTree:\n    def __init__(self, v: int|list):\n        if\
    \ isinstance(v, int):\n            self.data, self.size = [0]*v, v\n        else:\n\
    \            self.build(v)\n\n    def build(self, data):\n        self.data, self.size\
    \ = data, len(data)\n        for i in range(self.size):\n            if (r :=\
    \ i|(i+1)) < self.size: \n                self.data[r] += self.data[i]\n\n   \
    \ def get(self, i: int):\n        assert 0 <= i < self.size\n        s = self.data[i]\n\
    \        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n           \
    \ s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def set(self,\
    \ i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n    def add(self,\
    \ i: int, x: object) -> None:\n        assert 0 <= i <= self.size\n        i +=\
    \ 1\n        while i <= self.size:\n            self.data[i-1], i = self.data[i-1]\
    \ + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n\
    \        s = 0\n        for _ in range(i.bit_count()):\n            s, i = s+self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def range_sum(self, l: int, r: int):\n\
    \        return self.pref_sum(r) - self.pref_sum(l)\n\nbit = BinaryIndexTree(list(range(100)))\n\
    l,r = 5,7\na = bit.pref_sum(r) - bit.pref_sum(l)\nb = bit.range_sum(l,r)\nprint(a,\
    \ b)\nfor i in range(100):\n    assert bit.range_sum(i,i+1) == bit.get(i)"
  dependsOn: []
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2024-11-03 23:06:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
