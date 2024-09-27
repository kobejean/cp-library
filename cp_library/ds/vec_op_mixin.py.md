---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/mutvec_cls.py
    title: cp_library/ds/mutvec_cls.py
  - icon: ':warning:'
    path: cp_library/ds/vec_cls.py
    title: cp_library/ds/vec_cls.py
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
    \nimport operator\nfrom numbers import Number\nfrom typing import Sequence\n\n\
    class VecOpMixin:\n    def elm_wise(self, other, op):\n        if isinstance(other,\
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
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n"
  code: "import cp_library.ds.__header__\n\nimport operator\nfrom numbers import Number\n\
    from typing import Sequence\n\nclass VecOpMixin:\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number):\n            return type(self)(op(x,\
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
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/vec_op_mixin.py
  requiredBy:
  - cp_library/ds/mutvec_cls.py
  - cp_library/ds/vec_cls.py
  timestamp: '2024-09-28 02:29:45+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/vec_op_mixin.py
layout: document
redirect_from:
- /library/cp_library/ds/vec_op_mixin.py
- /library/cp_library/ds/vec_op_mixin.py.html
title: cp_library/ds/vec_op_mixin.py
---
