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
    from collections import deque\nfrom typing import Any, Iterable\n\nclass SlidingMin(deque):\n\
    \    def __init__(self, *, maxlen = None):\n        super().__init__(maxlen=maxlen+1)\n\
    \        self.minq = deque()\n\n    @property\n    def maxlen(self):\n       \
    \ return super().maxlen-1\n\n    def append(self, x: Any) -> None:\n        while\
    \ self.minq and x < self.minq[-1]:\n            self.minq.pop()\n        self.minq.append(x)\n\
    \        super().append(x)\n        if len(self) > self.maxlen:\n            self.popleft()\n\
    \    \n    def appendleft(self, x: Any) -> None:\n        raise NotImplementedError()\n\
    \    \n    def extend(self, iterable: Iterable) -> None:\n        for x in iterable:\n\
    \            self.append(x)\n\n    def extendleft(self, iterable: Iterable) ->\
    \ None:\n        raise NotImplementedError()\n\n    def popleft(self) -> Any:\n\
    \        x = super().popleft()\n        if x == self.minq[0]:\n            self.minq.popleft()\n\
    \        return x\n    \n    def pop(self) -> Any:\n        raise NotImplementedError()\n\
    \n    @property\n    def min(self) -> Any:\n        return self.minq[0]\n"
  code: "import cp_library.ds.__header__\nfrom collections import deque\nfrom typing\
    \ import Any, Iterable\n\nclass SlidingMin(deque):\n    def __init__(self, *,\
    \ maxlen = None):\n        super().__init__(maxlen=maxlen+1)\n        self.minq\
    \ = deque()\n\n    @property\n    def maxlen(self):\n        return super().maxlen-1\n\
    \n    def append(self, x: Any) -> None:\n        while self.minq and x < self.minq[-1]:\n\
    \            self.minq.pop()\n        self.minq.append(x)\n        super().append(x)\n\
    \        if len(self) > self.maxlen:\n            self.popleft()\n    \n    def\
    \ appendleft(self, x: Any) -> None:\n        raise NotImplementedError()\n   \
    \ \n    def extend(self, iterable: Iterable) -> None:\n        for x in iterable:\n\
    \            self.append(x)\n\n    def extendleft(self, iterable: Iterable) ->\
    \ None:\n        raise NotImplementedError()\n\n    def popleft(self) -> Any:\n\
    \        x = super().popleft()\n        if x == self.minq[0]:\n            self.minq.popleft()\n\
    \        return x\n    \n    def pop(self) -> Any:\n        raise NotImplementedError()\n\
    \n    @property\n    def min(self) -> Any:\n        return self.minq[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/slidingmin_cls.py
  requiredBy: []
  timestamp: '2025-02-09 13:23:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/slidingmin_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/slidingmin_cls.py
- /library/cp_library/ds/slidingmin_cls.py.html
title: cp_library/ds/slidingmin_cls.py
---
