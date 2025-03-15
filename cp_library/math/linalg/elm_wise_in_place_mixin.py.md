---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/linalg/mat/mat_cls.py
    title: cp_library/math/linalg/mat/mat_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/mat/mod/mat_cls.py
    title: cp_library/math/linalg/mat/mod/mat_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/vec/mutvec_cls.py
    title: cp_library/math/linalg/vec/mutvec_cls.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "import cp_library.math.vec.__header__\n\nimport operator\nfrom numbers\
    \ import Number\nfrom typing import Sequence\nfrom cp_library.math.vec.elm_wise_mixin\
    \ import ElmWiseMixin\n\nclass ElmWiseInPlaceMixin(ElmWiseMixin):\n    def ielm_wise(self,\
    \ other, op):\n        if isinstance(other, Number):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other)\n        elif isinstance(other,\
    \ Sequence) and len(self) == len(other):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other[i])\n        else:\n            raise\
    \ ValueError(\"Operand must be a number or a list of the same length\")\n    \
    \    return self\n    \n    def __iadd__(self, other): return self.ielm_wise(other,\
    \ operator.add)\n    def __isub__(self, other): return self.ielm_wise(other, operator.sub)\n\
    \    def __imul__(self, other): return self.ielm_wise(other, operator.mul)\n \
    \   def __itruediv__(self, other): return self.ielm_wise(other, operator.truediv)\n\
    \    def __ifloordiv__(self, other): return self.ielm_wise(other, operator.floordiv)\n\
    \    def __imod__(self, other): return self.ielm_wise(other, operator.mod)\n"
  code: "import cp_library.math.vec.__header__\n\nimport operator\nfrom numbers import\
    \ Number\nfrom typing import Sequence\nfrom cp_library.math.vec.elm_wise_mixin\
    \ import ElmWiseMixin\n\nclass ElmWiseInPlaceMixin(ElmWiseMixin):\n    def ielm_wise(self,\
    \ other, op):\n        if isinstance(other, Number):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other)\n        elif isinstance(other,\
    \ Sequence) and len(self) == len(other):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other[i])\n        else:\n            raise\
    \ ValueError(\"Operand must be a number or a list of the same length\")\n    \
    \    return self\n    \n    def __iadd__(self, other): return self.ielm_wise(other,\
    \ operator.add)\n    def __isub__(self, other): return self.ielm_wise(other, operator.sub)\n\
    \    def __imul__(self, other): return self.ielm_wise(other, operator.mul)\n \
    \   def __itruediv__(self, other): return self.ielm_wise(other, operator.truediv)\n\
    \    def __ifloordiv__(self, other): return self.ielm_wise(other, operator.floordiv)\n\
    \    def __imod__(self, other): return self.ielm_wise(other, operator.mod)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/linalg/elm_wise_in_place_mixin.py
  requiredBy:
  - cp_library/math/linalg/mat/mod/mat_cls.py
  - cp_library/math/linalg/mat/mat_cls.py
  - cp_library/math/linalg/vec/mutvec_cls.py
  timestamp: '2025-03-15 12:29:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/linalg/elm_wise_in_place_mixin.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/elm_wise_in_place_mixin.py
- /library/cp_library/math/linalg/elm_wise_in_place_mixin.py.html
title: cp_library/math/linalg/elm_wise_in_place_mixin.py
---
