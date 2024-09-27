---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/cht_monotone_add_max_cls.py
    title: cp_library/ds/cht_monotone_add_max_cls.py
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
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
    \ndef main():\n    N, C = read()\n    H = read()\n    dp = 0\n    cht = CHTMonotoneAddMax()\n\
    \n    for i in range(N-1):\n        m = 2*H[i]\n        b = -H[i]**2 + -dp\n \
    \       cht.insert(m,b)\n        i+=1\n        dp = -cht.max(H[i]) + H[i]**2 +\
    \ C\n\n    print(dp)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nfrom bisect import bisect_left\n\nclass CHTMonotoneAddMax:\n\
    \    def __init__(self):\n        self.hull = []\n\n    def insert(self, m: int,\
    \ b: int) -> None:\n        # Remove lines with greater or equal slopes (maintaining\
    \ monotonicity)\n        while self.hull and self.hull[-1][0] >= m:\n        \
    \    self.hull.pop()\n\n        def is_obsolete():\n            (m1, b1), (m2,\
    \ b2) = self.hull[-2], self.hull[-1]\n            return (b - b1) * (m1 - m2)\
    \ <= (b2 - b1) * (m1 - m)\n        \n        # Remove lines that are no longer\
    \ part of the lower envelope\n        while len(self.hull) >= 2 and is_obsolete():\n\
    \            self.hull.pop()\n        \n        self.hull.append((m, b))\n\n \
    \   def max(self, x: int) -> int:\n        def eval(i):\n            m, b = self.hull[i]\n\
    \            return m * x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n\
    \            m2, b2 = self.hull[i+1]\n            return (m1-m2)*x + (b1-b2)\n\
    \        return eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n\n\n\
    def read(shift=0, base=10):\n    return [int(s, base) + shift for s in input().split()]\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \ndef main():\n    N, C = read()\n    H = read()\n    dp = 0\n    cht = CHTMonotoneAddMax()\n\
    \n    for i in range(N-1):\n        m = 2*H[i]\n        b = -H[i]**2 + -dp\n \
    \       cht.insert(m,b)\n        i+=1\n        dp = -cht.max(H[i]) + H[i]**2 +\
    \ C\n\n    print(dp)\n\nfrom cp_library.ds.cht_monotone_add_max_cls import CHTMonotoneAddMax\n\
    from cp_library.io.read_int_fn import read\n\nif __name__ == '__main__':\n   \
    \ main()"
  dependsOn:
  - cp_library/ds/cht_monotone_add_max_cls.py
  - cp_library/io/read_int_fn.py
  isVerificationFile: true
  path: test/dp_z_cht_monotone_add_max.test.py
  requiredBy: []
  timestamp: '2024-09-28 03:27:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_z_cht_monotone_add_max.test.py
layout: document
redirect_from:
- /verify/test/dp_z_cht_monotone_add_max.test.py
- /verify/test/dp_z_cht_monotone_add_max.test.py.html
title: test/dp_z_cht_monotone_add_max.test.py
---
