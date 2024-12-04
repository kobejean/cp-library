---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from heapq import heappop, heappush\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom collections import Counter, UserList\nfrom typing\
    \ import Iterable, TypeVar\n\n\nimport sys\ninft: int\n\ninft = sys.maxsize\n\n\
    T = TypeVar('T')\nclass MinMultiset(UserList[T]):\n    \n    def __init__(self,\
    \ iterable: Iterable = None, default = -inft):\n        super().__init__(iterable)\n\
    \        self.default = default\n        self.counter = Counter(self.data)\n\n\
    \    def add(self, x: T):\n        self.counter[x] += 1\n        heappush(self.data,\
    \ x)\n    \n    def remove(self, x: T):\n        cnt, data = self.counter, self.data\n\
    \        cnt[x] -= 1\n        while data and cnt[data[0]] == 0:\n            heappop(data)\n\
    \n    @property\n    def min(self):\n        return self.data[0] if self.data\
    \ else self.default\n"
  code: "from heapq import heappop, heappush\nimport cp_library.ds.heap.__header__\n\
    from collections import Counter, UserList\nfrom typing import Iterable, TypeVar\n\
    \nfrom cp_library.math.inft_cnst import inft\n\nT = TypeVar('T')\nclass MinMultiset(UserList[T]):\n\
    \    \n    def __init__(self, iterable: Iterable = None, default = -inft):\n \
    \       super().__init__(iterable)\n        self.default = default\n        self.counter\
    \ = Counter(self.data)\n\n    def add(self, x: T):\n        self.counter[x] +=\
    \ 1\n        heappush(self.data, x)\n    \n    def remove(self, x: T):\n     \
    \   cnt, data = self.counter, self.data\n        cnt[x] -= 1\n        while data\
    \ and cnt[data[0]] == 0:\n            heappop(data)\n\n    @property\n    def\
    \ min(self):\n        return self.data[0] if self.data else self.default\n"
  dependsOn:
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/ds/heap/min_multiset_cls.py
  requiredBy: []
  timestamp: '2024-12-05 05:25:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/min_multiset_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_multiset_cls.py
- /library/cp_library/ds/heap/min_multiset_cls.py.html
title: cp_library/ds/heap/min_multiset_cls.py
---
