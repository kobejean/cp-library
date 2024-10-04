---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/agc038_b_sliding_min_max.test.py
    title: test/agc038_b_sliding_min_max.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom collections import deque\nfrom typing import Any, Iterable\n\nclass SlidingMinMax(deque):\n\
    \    def __init__(self, *, maxlen = None):\n        super().__init__(maxlen=maxlen)\n\
    \        self.minq = deque(maxlen=maxlen)\n        self.maxq = deque(maxlen=maxlen)\n\
    \n    def append(self, x: Any) -> None:\n        super().append(x)\n        while\
    \ self.minq and x < self.minq[-1]:\n            self.minq.pop()\n        self.minq.append(x)\n\
    \        while self.maxq and self.maxq[-1] < x:\n            self.maxq.pop()\n\
    \        self.maxq.append(x)\n    \n    def appendleft(self, x: Any) -> None:\n\
    \        raise NotImplementedError()\n    \n    def extend(self, iterable: Iterable)\
    \ -> None:\n        super().extend(iterable)\n        for x in iterable:\n   \
    \         while self.minq and x < self.minq[-1]:\n                self.minq.pop()\n\
    \            self.minq.append(x)\n            while self.maxq and self.maxq[-1]\
    \ < x:\n                self.maxq.pop()\n            self.maxq.append(x)\n\n \
    \   def extendleft(self, iterable: Iterable) -> None:\n        raise NotImplementedError()\n\
    \n    def popleft(self) -> Any:\n        x = super().popleft()\n        if x ==\
    \ self.minq[0]:\n            self.minq.popleft()\n        if x == self.maxq[0]:\n\
    \            self.maxq.popleft()\n        return x\n    \n    def pop(self) ->\
    \ Any:\n        raise NotImplementedError()\n\n    @property\n    def min(self)\
    \ -> Any:\n        return self.minq[0]\n\n    @property\n    def max(self) ->\
    \ Any:\n        return self.maxq[0]\n"
  code: "import cp_library.ds.__header__\n\nfrom collections import deque\nfrom typing\
    \ import Any, Iterable\n\nclass SlidingMinMax(deque):\n    def __init__(self,\
    \ *, maxlen = None):\n        super().__init__(maxlen=maxlen)\n        self.minq\
    \ = deque(maxlen=maxlen)\n        self.maxq = deque(maxlen=maxlen)\n\n    def\
    \ append(self, x: Any) -> None:\n        super().append(x)\n        while self.minq\
    \ and x < self.minq[-1]:\n            self.minq.pop()\n        self.minq.append(x)\n\
    \        while self.maxq and self.maxq[-1] < x:\n            self.maxq.pop()\n\
    \        self.maxq.append(x)\n    \n    def appendleft(self, x: Any) -> None:\n\
    \        raise NotImplementedError()\n    \n    def extend(self, iterable: Iterable)\
    \ -> None:\n        super().extend(iterable)\n        for x in iterable:\n   \
    \         while self.minq and x < self.minq[-1]:\n                self.minq.pop()\n\
    \            self.minq.append(x)\n            while self.maxq and self.maxq[-1]\
    \ < x:\n                self.maxq.pop()\n            self.maxq.append(x)\n\n \
    \   def extendleft(self, iterable: Iterable) -> None:\n        raise NotImplementedError()\n\
    \n    def popleft(self) -> Any:\n        x = super().popleft()\n        if x ==\
    \ self.minq[0]:\n            self.minq.popleft()\n        if x == self.maxq[0]:\n\
    \            self.maxq.popleft()\n        return x\n    \n    def pop(self) ->\
    \ Any:\n        raise NotImplementedError()\n\n    @property\n    def min(self)\
    \ -> Any:\n        return self.minq[0]\n\n    @property\n    def max(self) ->\
    \ Any:\n        return self.maxq[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/slidingminmax_cls.py
  requiredBy: []
  timestamp: '2024-10-04 19:59:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/agc038_b_sliding_min_max.test.py
documentation_of: cp_library/ds/slidingminmax_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/slidingminmax_cls.py
- /library/cp_library/ds/slidingminmax_cls.py.html
title: cp_library/ds/slidingminmax_cls.py
---
