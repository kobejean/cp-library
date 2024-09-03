---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/bir_cls.py
    title: cp_library/ds/bir_cls.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from typing import Any, List, Union\n\nclass BinaryIndexTree:\n  \
    \  def __init__(self, v: Union[int,List[Any]]):\n        if isinstance(v, int):\n\
    \            self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            r = i|(i+1)\n            if r\
    \ < self.size: \n                self.data[r] += self.data[i]\n\n    def add(self,\
    \ i: int, x: Any) -> None:\n        assert 0 <= i <= self.size\n        i += 1\n\
    \        while i <= self.size:\n            self.data[i-1], i = self.data[i-1]\
    \ + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n\
    \        s = 0\n        while i > 0:\n            s, i = s+self.data[i-1], i-(i&-i)\n\
    \        return s\n    \n    def range_sum(self, l: int, r: int) -> Any:\n   \
    \     assert 0 <= l <= r <= self.size\n        m = l&r if l.bit_length() == r.bit_length()\
    \ else 0\n        s = 0\n        while l > m:\n            s, l = s-self.data[l-1],\
    \ l-(l&-l)\n        while r > m:\n            s, r = s+self.data[r-1], r-(r&-r)\n\
    \        return s\n"
  code: "from typing import Any, List, Union\n\nclass BinaryIndexTree:\n    def __init__(self,\
    \ v: Union[int,List[Any]]):\n        if isinstance(v, int):\n            self.data,\
    \ self.size = [0]*v, v\n        else:\n            self.build(v)\n\n    def build(self,\
    \ data):\n        self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            r = i|(i+1)\n            if r < self.size: \n                self.data[r]\
    \ += self.data[i]\n\n    def add(self, i: int, x: Any) -> None:\n        assert\
    \ 0 <= i <= self.size\n        i += 1\n        while i <= self.size:\n       \
    \     self.data[i-1], i = self.data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self,\
    \ i: int):\n        assert 0 <= i <= self.size\n        s = 0\n        while i\
    \ > 0:\n            s, i = s+self.data[i-1], i-(i&-i)\n        return s\n    \n\
    \    def range_sum(self, l: int, r: int) -> Any:\n        assert 0 <= l <= r <=\
    \ self.size\n        m = l&r if l.bit_length() == r.bit_length() else 0\n    \
    \    s = 0\n        while l > m:\n            s, l = s-self.data[l-1], l-(l&-l)\n\
    \        while r > m:\n            s, r = s+self.data[r-1], r-(r&-r)\n       \
    \ return s"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bit_cls.py
  requiredBy:
  - cp_library/ds/bir_cls.py
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bit_cls.py
- /library/cp_library/ds/bit_cls.py.html
title: cp_library/ds/bit_cls.py
---
