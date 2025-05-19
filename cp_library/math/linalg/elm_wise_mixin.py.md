---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/linalg/elm_wise_in_place_mixin.py
    title: cp_library/math/linalg/elm_wise_in_place_mixin.py
  - icon: ':warning:'
    path: cp_library/math/linalg/mat/mat_cls.py
    title: cp_library/math/linalg/mat/mat_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/mat/mod/mat_cls.py
    title: cp_library/math/linalg/mat/mod/mat_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/vec/mutvec_cls.py
    title: cp_library/math/linalg/vec/mutvec_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/vec/slope_cls.py
    title: cp_library/math/linalg/vec/slope_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/vec/vec2d_cls.py
    title: cp_library/math/linalg/vec/vec2d_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/vec/vec3d_cls.py
    title: cp_library/math/linalg/vec/vec3d_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/vec/vec_cls.py
    title: cp_library/math/linalg/vec/vec_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc151_f_fbisect_left.test.py
    title: test/atcoder/abc/abc151_f_fbisect_left.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc189_e_vec2d.test.py
    title: test/atcoder/abc/abc189_e_vec2d.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc274_e_vec2d.test.py
    title: test/atcoder/abc/abc274_e_vec2d.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from math import hypot\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport operator\nfrom numbers import Number\nfrom typing\
    \ import Sequence\n\nclass ElmWiseMixin:\n    def elm_wise(self, other, op):\n\
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
    \  return vec / vec.magnitude()\n"
  code: "from math import hypot\nimport cp_library.math.__header__\n\nimport operator\n\
    from numbers import Number\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n\
    \    def elm_wise(self, other, op):\n        if isinstance(other, Number):\n \
    \           return type(self)(op(x, other) for x in self)\n        if isinstance(other,\
    \ Sequence):\n            return type(self)(op(x, y) for x, y in zip(self, other))\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n\n    def __add__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __radd__(self, other): return self.elm_wise(other, operator.add)\n  \
    \  def __sub__(self, other): return self.elm_wise(other, operator.sub)\n    def\
    \ __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
    \    def __mul__(self, other): return self.elm_wise(other, operator.mul)\n   \
    \ def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n    def\
    \ __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n  \
    \  def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/linalg/elm_wise_mixin.py
  requiredBy:
  - cp_library/math/linalg/vec/mutvec_cls.py
  - cp_library/math/linalg/vec/vec_cls.py
  - cp_library/math/linalg/vec/vec2d_cls.py
  - cp_library/math/linalg/vec/vec3d_cls.py
  - cp_library/math/linalg/vec/slope_cls.py
  - cp_library/math/linalg/elm_wise_in_place_mixin.py
  - cp_library/math/linalg/mat/mod/mat_cls.py
  - cp_library/math/linalg/mat/mat_cls.py
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc189_e_vec2d.test.py
  - test/atcoder/abc/abc274_e_vec2d.test.py
  - test/atcoder/abc/abc151_f_fbisect_left.test.py
documentation_of: cp_library/math/linalg/elm_wise_mixin.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/elm_wise_mixin.py
- /library/cp_library/math/linalg/elm_wise_mixin.py.html
title: cp_library/math/linalg/elm_wise_mixin.py
---
