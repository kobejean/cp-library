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
    \nfrom bisect import bisect_left\n\nclass CHTMonotoneAddMax:\n    def __init__(self):\n\
    \        self.hull = []\n\n    def insert(self, m: int, b: int) -> None:\n   \
    \     # Remove lines with greater or equal slopes (maintaining monotonicity)\n\
    \        while self.hull and self.hull[-1][0] >= m:\n            self.hull.pop()\n\
    \n        def is_obsolete():\n            (m1, b1), (m2, b2) = self.hull[-2],\
    \ self.hull[-1]\n            return (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 -\
    \ m)\n        \n        # Remove lines that are no longer part of the lower envelope\n\
    \        while len(self.hull) >= 2 and is_obsolete():\n            self.hull.pop()\n\
    \        \n        self.hull.append((m, b))\n\n    def max(self, x: int) -> int:\n\
    \        def eval(i):\n            m, b = self.hull[i]\n            return m *\
    \ x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n            m2,\
    \ b2 = self.hull[i+1]\n            return (m1-m2)*x + (b1-b2)\n        return\
    \ eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n"
  code: "import cp_library.ds.__header__\n\nfrom bisect import bisect_left\n\nclass\
    \ CHTMonotoneAddMax:\n    def __init__(self):\n        self.hull = []\n\n    def\
    \ insert(self, m: int, b: int) -> None:\n        # Remove lines with greater or\
    \ equal slopes (maintaining monotonicity)\n        while self.hull and self.hull[-1][0]\
    \ >= m:\n            self.hull.pop()\n\n        def is_obsolete():\n         \
    \   (m1, b1), (m2, b2) = self.hull[-2], self.hull[-1]\n            return (b -\
    \ b1) * (m1 - m2) <= (b2 - b1) * (m1 - m)\n        \n        # Remove lines that\
    \ are no longer part of the lower envelope\n        while len(self.hull) >= 2\
    \ and is_obsolete():\n            self.hull.pop()\n        \n        self.hull.append((m,\
    \ b))\n\n    def max(self, x: int) -> int:\n        def eval(i):\n           \
    \ m, b = self.hull[i]\n            return m * x + b\n        def key(i):\n   \
    \         m1, b1 = self.hull[i]\n            m2, b2 = self.hull[i+1]\n       \
    \     return (m1-m2)*x + (b1-b2)\n        return eval(bisect_left(range(len(self.hull)\
    \ - 1), 0, key=key))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/cht_monotone_add_max_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/cht_monotone_add_max_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/cht_monotone_add_max_cls.py
- /library/cp_library/ds/cht_monotone_add_max_cls.py.html
title: cp_library/ds/cht_monotone_add_max_cls.py
---
