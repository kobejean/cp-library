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
  bundledCode: "from collections import deque\nfrom typing import Any\n\nclass SlidingMinMax(deque):\n\
    \    def __init__(self):\n        super().__init__()\n        self.minq = deque()\n\
    \        self.maxq = deque()\n\n    def append(self, x: Any) -> None:\n      \
    \  super().append(x)\n        while self.minq and x < self.minq[-1]:\n       \
    \     self.minq.pop()\n        self.minq.append(x)\n        while self.maxq and\
    \ self.maxq[-1] < x:\n            self.maxq.pop()\n        self.maxq.append(x)\n\
    \n    def popleft(self) -> Any:\n        x = super().popleft()\n        if x ==\
    \ self.minq[0]:\n            self.minq.popleft()\n        if x == self.maxq[0]:\n\
    \            self.maxq.popleft()\n        return x\n\n    @property\n    def min(self)\
    \ -> Any:\n        return self.minq[0]\n\n    @property\n    def max(self) ->\
    \ Any:\n        return self.maxq[0]\n"
  code: "from collections import deque\nfrom typing import Any\n\nclass SlidingMinMax(deque):\n\
    \    def __init__(self):\n        super().__init__()\n        self.minq = deque()\n\
    \        self.maxq = deque()\n\n    def append(self, x: Any) -> None:\n      \
    \  super().append(x)\n        while self.minq and x < self.minq[-1]:\n       \
    \     self.minq.pop()\n        self.minq.append(x)\n        while self.maxq and\
    \ self.maxq[-1] < x:\n            self.maxq.pop()\n        self.maxq.append(x)\n\
    \n    def popleft(self) -> Any:\n        x = super().popleft()\n        if x ==\
    \ self.minq[0]:\n            self.minq.popleft()\n        if x == self.maxq[0]:\n\
    \            self.maxq.popleft()\n        return x\n\n    @property\n    def min(self)\
    \ -> Any:\n        return self.minq[0]\n\n    @property\n    def max(self) ->\
    \ Any:\n        return self.maxq[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/slidingminmax_cls.py
  requiredBy: []
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/slidingminmax_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/slidingminmax_cls.py
- /library/cp_library/ds/slidingminmax_cls.py.html
title: cp_library/ds/slidingminmax_cls.py
---
