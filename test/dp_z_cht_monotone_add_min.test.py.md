---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/cht_monotone_add_min_cls.py
    title: cp_library/ds/cht_monotone_add_min_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_z
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_z
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
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
    \ eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n\ndef rint(shift=0,\
    \ base=10):\n    return [int(x, base) + shift for x in input().split()]\n\ninf\
    \ = float('inf')\n\nN, C = rint()\nH = rint()\ndp = 0\ncht = CHTMonotoneAddMin()\n\
    \nfor i in range(N-1):\n    m = -2*H[i]\n    b = H[i]**2 + dp\n    cht.insert(m,b)\n\
    \    i+=1\n    dp = cht.min(H[i]) + H[i]**2 + C\n\nprint(dp)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \nfrom cp_library.ds.cht_monotone_add_min_cls import CHTMonotoneAddMin\n\ndef\
    \ rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \ninf = float('inf')\n\nN, C = rint()\nH = rint()\ndp = 0\ncht = CHTMonotoneAddMin()\n\
    \nfor i in range(N-1):\n    m = -2*H[i]\n    b = H[i]**2 + dp\n    cht.insert(m,b)\n\
    \    i+=1\n    dp = cht.min(H[i]) + H[i]**2 + C\n\nprint(dp)"
  dependsOn:
  - cp_library/ds/cht_monotone_add_min_cls.py
  isVerificationFile: true
  path: test/dp_z_cht_monotone_add_min.test.py
  requiredBy: []
  timestamp: '2024-08-30 22:41:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_z_cht_monotone_add_min.test.py
layout: document
redirect_from:
- /verify/test/dp_z_cht_monotone_add_min.test.py
- /verify/test/dp_z_cht_monotone_add_min.test.py.html
title: test/dp_z_cht_monotone_add_min.test.py
---