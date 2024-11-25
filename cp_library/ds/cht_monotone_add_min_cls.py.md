---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_z_cht_monotone_add_min.test.py
    title: test/dp_z_cht_monotone_add_min.test.py
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
    \nfrom bisect import bisect_left\n\nclass CHTMonotoneAddMin:\n    def __init__(self):\n\
    \        self.hull = []\n\n    def insert(self, m: int, b: int) -> None:\n   \
    \     # Remove lines with greater or equal slopes (maintaining monotonicity)\n\
    \        while self.hull and self.hull[-1][0] <= m:\n            self.hull.pop()\n\
    \n        def is_obsolete():\n            (m1, b1), (m2, b2) = self.hull[-2],\
    \ self.hull[-1]\n            return (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 -\
    \ m)\n        \n        # Remove lines that are no longer part of the lower envelope\n\
    \        while len(self.hull) >= 2 and is_obsolete():\n            self.hull.pop()\n\
    \        \n        self.hull.append((m, b))\n\n    def min(self, x: int) -> int:\n\
    \        def eval(i):\n            m, b = self.hull[i]\n            return m *\
    \ x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n            m2,\
    \ b2 = self.hull[i+1]\n            return (m2-m1)*x + (b2-b1)\n        return\
    \ eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n"
  code: "import cp_library.ds.__header__\n\nfrom bisect import bisect_left\n\nclass\
    \ CHTMonotoneAddMin:\n    def __init__(self):\n        self.hull = []\n\n    def\
    \ insert(self, m: int, b: int) -> None:\n        # Remove lines with greater or\
    \ equal slopes (maintaining monotonicity)\n        while self.hull and self.hull[-1][0]\
    \ <= m:\n            self.hull.pop()\n\n        def is_obsolete():\n         \
    \   (m1, b1), (m2, b2) = self.hull[-2], self.hull[-1]\n            return (b -\
    \ b1) * (m1 - m2) <= (b2 - b1) * (m1 - m)\n        \n        # Remove lines that\
    \ are no longer part of the lower envelope\n        while len(self.hull) >= 2\
    \ and is_obsolete():\n            self.hull.pop()\n        \n        self.hull.append((m,\
    \ b))\n\n    def min(self, x: int) -> int:\n        def eval(i):\n           \
    \ m, b = self.hull[i]\n            return m * x + b\n        def key(i):\n   \
    \         m1, b1 = self.hull[i]\n            m2, b2 = self.hull[i+1]\n       \
    \     return (m2-m1)*x + (b2-b1)\n        return eval(bisect_left(range(len(self.hull)\
    \ - 1), 0, key=key))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/cht_monotone_add_min_cls.py
  requiredBy: []
  timestamp: '2024-11-25 13:28:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dp_z_cht_monotone_add_min.test.py
documentation_of: cp_library/ds/cht_monotone_add_min_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/cht_monotone_add_min_cls.py
- /library/cp_library/ds/cht_monotone_add_min_cls.py.html
title: cp_library/ds/cht_monotone_add_min_cls.py
---
