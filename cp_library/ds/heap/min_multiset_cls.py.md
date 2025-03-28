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
    from heapq import heappop, heappush\nfrom collections import Counter, UserList\n\
    from typing import Iterable\nfrom math import inf\nfrom typing import TypeVar\n\
    _T = TypeVar('T')\n\nclass MinMultiset(UserList[_T]):\n    def __init__(self,\
    \ iterable: Iterable = None, default = -inf):\n        super().__init__(iterable)\n\
    \        self.default = default\n        self.counter = Counter(self.data)\n\n\
    \    def add(self, x: _T):\n        self.counter[x] += 1\n        heappush(self.data,\
    \ x)\n    \n    def remove(self, x: _T):\n        cnt, data = self.counter, self.data\n\
    \        cnt[x] -= 1\n        while data and cnt[data[0]] == 0: heappop(data)\n\
    \n    @property\n    def min(self): return self.data[0] if self.data else self.default\n"
  code: "import cp_library.ds.heap.__header__\nfrom heapq import heappop, heappush\n\
    from collections import Counter, UserList\nfrom typing import Iterable\nfrom math\
    \ import inf\nfrom cp_library.misc.typing import _T\n\nclass MinMultiset(UserList[_T]):\n\
    \    def __init__(self, iterable: Iterable = None, default = -inf):\n        super().__init__(iterable)\n\
    \        self.default = default\n        self.counter = Counter(self.data)\n\n\
    \    def add(self, x: _T):\n        self.counter[x] += 1\n        heappush(self.data,\
    \ x)\n    \n    def remove(self, x: _T):\n        cnt, data = self.counter, self.data\n\
    \        cnt[x] -= 1\n        while data and cnt[data[0]] == 0: heappop(data)\n\
    \n    @property\n    def min(self): return self.data[0] if self.data else self.default\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/min_multiset_cls.py
  requiredBy: []
  timestamp: '2025-03-28 15:11:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/min_multiset_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_multiset_cls.py
- /library/cp_library/ds/heap/min_multiset_cls.py.html
title: cp_library/ds/heap/min_multiset_cls.py
---
