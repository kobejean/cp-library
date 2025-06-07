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
    from typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\nfrom typing\
    \ import Iterator, SupportsIndex\n\n\n\nclass SliceIterator(Iterator[_T]):\n \
    \   def __init__(self, A: list[_T], R: list[SupportsIndex]):\n        self.A,\
    \ self.R, self.l, self.i = A, R, 0, 0\n    def __len__(self): return len(self.R)-self.i\n\
    \    def __next__(self):\n        R = self.R\n        if self.i >= len(R): raise\
    \ StopIteration\n        self.l, l = (r := R[self.i]), self.l\n        self.i\
    \ += 1\n        return self.A[l:r]\n"
  code: "import cp_library.__header__\nfrom cp_library.misc.typing import _T\nfrom\
    \ typing import Iterator, SupportsIndex\nimport cp_library.alg.__header__\nimport\
    \ cp_library.alg.iter.__header__\n\nclass SliceIterator(Iterator[_T]):\n    def\
    \ __init__(self, A: list[_T], R: list[SupportsIndex]):\n        self.A, self.R,\
    \ self.l, self.i = A, R, 0, 0\n    def __len__(self): return len(self.R)-self.i\n\
    \    def __next__(self):\n        R = self.R\n        if self.i >= len(R): raise\
    \ StopIteration\n        self.l, l = (r := R[self.i]), self.l\n        self.i\
    \ += 1\n        return self.A[l:r]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/slice_iterator_cls.py
  requiredBy: []
  timestamp: '2025-06-08 03:08:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/slice_iterator_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/slice_iterator_cls.py
- /library/cp_library/alg/iter/slice_iterator_cls.py.html
title: cp_library/alg/iter/slice_iterator_cls.py
---
