---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/elm_wise_in_place_mixin.py
    title: cp_library/math/elm_wise_in_place_mixin.py
  - icon: ':warning:'
    path: cp_library/math/mat_cls.py
    title: cp_library/math/mat_cls.py
  - icon: ':warning:'
    path: cp_library/math/mutvec_cls.py
    title: cp_library/math/mutvec_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec2_cls.py
    title: cp_library/math/vec2_cls.py
  - icon: ':warning:'
    path: cp_library/math/vec3_cls.py
    title: cp_library/math/vec3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec_cls.py
    title: cp_library/math/vec_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc274_e_vec2.test.py
    title: test/abc274_e_vec2.test.py
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
    \nimport operator\nfrom numbers import Number\nfrom typing import Sequence\n\n\
    class ElmWiseMixin:\n    def elm_wise(self, other, op):\n        if isinstance(other,\
    \ Number):\n            return type(self)(op(x, other) for x in self)\n      \
    \  if isinstance(other, Sequence):\n            return type(self)(op(x, y) for\
    \ x, y in zip(self, other))\n        raise ValueError(\"Operand must be a number\
    \ or a tuple of the same length\")\n\n    def __add__(self, other): return self.elm_wise(other,\
    \ operator.add)\n    def __radd__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __sub__(self, other): return self.elm_wise(other, operator.sub)\n   \
    \ def __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
    \    def __mul__(self, other): return self.elm_wise(other, operator.mul)\n   \
    \ def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n    def\
    \ __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n  \
    \  def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n"
  code: "import cp_library.math.__header__\n\nimport operator\nfrom numbers import\
    \ Number\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n    def elm_wise(self,\
    \ other, op):\n        if isinstance(other, Number):\n            return type(self)(op(x,\
    \ other) for x in self)\n        if isinstance(other, Sequence):\n           \
    \ return type(self)(op(x, y) for x, y in zip(self, other))\n        raise ValueError(\"\
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
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/elm_wise_mixin.py
  requiredBy:
  - cp_library/math/mutvec_cls.py
  - cp_library/math/mat_cls.py
  - cp_library/math/vec2_cls.py
  - cp_library/math/elm_wise_in_place_mixin.py
  - cp_library/math/vec_cls.py
  - cp_library/math/vec3_cls.py
  timestamp: '2024-10-24 08:20:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc274_e_vec2.test.py
documentation_of: cp_library/math/elm_wise_mixin.py
layout: document
redirect_from:
- /library/cp_library/math/elm_wise_mixin.py
- /library/cp_library/math/elm_wise_mixin.py.html
title: cp_library/math/elm_wise_mixin.py
---
