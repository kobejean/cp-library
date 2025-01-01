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
  bundledCode: "from array import array\nfrom typing import Sequence, SupportsIndex\n\
    \nclass Bounds:\n    def __init__(self, endpoints: array):\n        self.endpoints\
    \ = endpoints\n        view = memoryview(endpoints)\n        self.L = view[:-1]\n\
    \        self.R = view[1:]\n    \n\n    \n    def range(self, key: SupportsIndex):\n\
    \        return range(self.L[key], self.R[key])\n\n# class Partition(Sequence[list[]])\n"
  code: "from array import array\nfrom typing import Sequence, SupportsIndex\n\nclass\
    \ Bounds:\n    def __init__(self, endpoints: array):\n        self.endpoints =\
    \ endpoints\n        view = memoryview(endpoints)\n        self.L = view[:-1]\n\
    \        self.R = view[1:]\n    \n\n    \n    def range(self, key: SupportsIndex):\n\
    \        return range(self.L[key], self.R[key])\n\n# class Partition(Sequence[list[]])"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/partition_cls.py
  requiredBy: []
  timestamp: '2025-01-01 22:39:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/partition_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/partition_cls.py
- /library/cp_library/alg/iter/partition_cls.py.html
title: cp_library/alg/iter/partition_cls.py
---
