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
    from typing import Iterable, TypeVar\n\nfrom math import inf\n\nT = TypeVar('T')\n\
    class MinMultiset(UserList[T]):\n    \n    def __init__(self, iterable: Iterable\
    \ = None, default = -inf):\n        super().__init__(iterable)\n        self.default\
    \ = default\n        self.counter = Counter(self.data)\n\n    def add(self, x:\
    \ T):\n        self.counter[x] += 1\n        heappush(self.data, x)\n    \n  \
    \  def remove(self, x: T):\n        cnt, data = self.counter, self.data\n    \
    \    cnt[x] -= 1\n        while data and cnt[data[0]] == 0:\n            heappop(data)\n\
    \n    @property\n    def min(self):\n        return self.data[0] if self.data\
    \ else self.default\n"
  code: "import cp_library.ds.heap.__header__\nfrom heapq import heappop, heappush\n\
    from collections import Counter, UserList\nfrom typing import Iterable, TypeVar\n\
    \nfrom math import inf\n\nT = TypeVar('T')\nclass MinMultiset(UserList[T]):\n\
    \    \n    def __init__(self, iterable: Iterable = None, default = -inf):\n  \
    \      super().__init__(iterable)\n        self.default = default\n        self.counter\
    \ = Counter(self.data)\n\n    def add(self, x: T):\n        self.counter[x] +=\
    \ 1\n        heappush(self.data, x)\n    \n    def remove(self, x: T):\n     \
    \   cnt, data = self.counter, self.data\n        cnt[x] -= 1\n        while data\
    \ and cnt[data[0]] == 0:\n            heappop(data)\n\n    @property\n    def\
    \ min(self):\n        return self.data[0] if self.data else self.default\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/min_multiset_cls.py
  requiredBy: []
  timestamp: '2025-01-01 22:39:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/min_multiset_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_multiset_cls.py
- /library/cp_library/ds/heap/min_multiset_cls.py.html
title: cp_library/ds/heap/min_multiset_cls.py
---
