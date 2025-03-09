---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec/elm_wise_mixin.py
    title: cp_library/math/vec/elm_wise_mixin.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/vec/mutvec_cls.py
    title: cp_library/math/vec/mutvec_cls.py
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
    \nimport operator\nfrom numbers import Number\nfrom typing import Sequence\nfrom\
    \ math import hypot\n\n\nclass ElmWiseMixin:\n    def elm_wise(self, other, op):\n\
    \        if isinstance(other, Number):\n            return type(self)(op(x, other)\
    \ for x in self)\n        if isinstance(other, Sequence):\n            return\
    \ type(self)(op(x, y) for x, y in zip(self, other))\n        raise ValueError(\"\
    Operand must be a number or a tuple of the same length\")\n\n    def __add__(self,\
    \ other): return self.elm_wise(other, operator.add)\n    def __radd__(self, other):\
    \ return self.elm_wise(other, operator.add)\n    def __sub__(self, other): return\
    \ self.elm_wise(other, operator.sub)\n    def __rsub__(self, other): return self.elm_wise(other,\
    \ lambda x,y: operator.sub(y,x))\n    def __mul__(self, other): return self.elm_wise(other,\
    \ operator.mul)\n    def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n\
    \    def __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n\
    \    def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\n\nclass ElmWiseInPlaceMixin(ElmWiseMixin):\n\
    \    def ielm_wise(self, other, op):\n        if isinstance(other, Number):\n\
    \            for i in range(len(self)):\n                self[i] = op(self[i],\
    \ other)\n        elif isinstance(other, Sequence) and len(self) == len(other):\n\
    \            for i in range(len(self)):\n                self[i] = op(self[i],\
    \ other[i])\n        else:\n            raise ValueError(\"Operand must be a number\
    \ or a list of the same length\")\n        return self\n    \n    def __iadd__(self,\
    \ other): return self.ielm_wise(other, operator.add)\n    def __isub__(self, other):\
    \ return self.ielm_wise(other, operator.sub)\n    def __imul__(self, other): return\
    \ self.ielm_wise(other, operator.mul)\n    def __itruediv__(self, other): return\
    \ self.ielm_wise(other, operator.truediv)\n    def __ifloordiv__(self, other):\
    \ return self.ielm_wise(other, operator.floordiv)\n    def __imod__(self, other):\
    \ return self.ielm_wise(other, operator.mod)\n"
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
  dependsOn:
  - cp_library/math/vec/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/vec/elm_wise_in_place_mixin.py
  requiredBy:
  - cp_library/math/vec/mutvec_cls.py
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/vec/elm_wise_in_place_mixin.py
layout: document
redirect_from:
- /library/cp_library/math/vec/elm_wise_in_place_mixin.py
- /library/cp_library/math/vec/elm_wise_in_place_mixin.py.html
title: cp_library/math/vec/elm_wise_in_place_mixin.py
---
