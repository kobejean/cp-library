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
  bundledCode: "from typing import Any, List, Union\nfrom typing import Any, Callable,\
    \ List, Union\n\nclass BinaryIndexTree:\n    def __init__(self, e: Any, op: Callable[[Any,\
    \ Any], Any], v: Union[int,List[Any]]):\n        self.e, self.op = e, op\n   \
    \     if isinstance(v, int):\n            self.data, self.size = [e]*v, v\n  \
    \      else:\n            self.build(v)\n\n    def build(self, data):\n      \
    \  self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            r = i|(i+1)\n            if r < self.size: \n                self.data[r]\
    \ = self.op(self.data[i], self.data[r])\n\n    def add(self, i: int, x: Any) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        while i <=\
    \ self.size:\n            self.data[i-1], i = self.op(self.data[i-1], x), i+(i&-i)\n\
    \n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n      \
    \  s = self.e\n        while i > 0:\n            s, i = self.op(s, self.data[i-1]),\
    \ i-(i&-i)\n        return s\n    \n\nclass BinaryIndexTreePURQ(BinaryIndexTree):\n\
    \    def __init__(self, e: Any, op: Callable[[Any, Any], Any],\n             \
    \    inv: Callable[[Any], Any], v: Union[int,List[Any]]):\n        self.inv =\
    \ inv\n        super().__init__(e, op, v)\n\n    def range_sum(self, l: int, r:\
    \ int) -> Any:\n        return self.op(self.pref_sum(r), self.inv(self.pref_sum(l)))\n"
  code: "from typing import Any, List, Union\nfrom typing import Any, Callable, List,\
    \ Union\n\nclass BinaryIndexTree:\n    def __init__(self, e: Any, op: Callable[[Any,\
    \ Any], Any], v: Union[int,List[Any]]):\n        self.e, self.op = e, op\n   \
    \     if isinstance(v, int):\n            self.data, self.size = [e]*v, v\n  \
    \      else:\n            self.build(v)\n\n    def build(self, data):\n      \
    \  self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            r = i|(i+1)\n            if r < self.size: \n                self.data[r]\
    \ = self.op(self.data[i], self.data[r])\n\n    def add(self, i: int, x: Any) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        while i <=\
    \ self.size:\n            self.data[i-1], i = self.op(self.data[i-1], x), i+(i&-i)\n\
    \n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n      \
    \  s = self.e\n        while i > 0:\n            s, i = self.op(s, self.data[i-1]),\
    \ i-(i&-i)\n        return s\n    \n\nclass BinaryIndexTreePURQ(BinaryIndexTree):\n\
    \    def __init__(self, e: Any, op: Callable[[Any, Any], Any],\n             \
    \    inv: Callable[[Any], Any], v: Union[int,List[Any]]):\n        self.inv =\
    \ inv\n        super().__init__(e, op, v)\n\n    def range_sum(self, l: int, r:\
    \ int) -> Any:\n        return self.op(self.pref_sum(r), self.inv(self.pref_sum(l)))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bit_generalized_cls.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bit_generalized_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bit_generalized_cls.py
- /library/cp_library/ds/bit_generalized_cls.py.html
title: cp_library/ds/bit_generalized_cls.py
---
