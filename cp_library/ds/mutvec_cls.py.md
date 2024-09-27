---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/ds/vec_op_mixin.py
    title: cp_library/ds/vec_op_mixin.py
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
    \nimport operator\nimport typing\nimport numbers\n\nfrom numbers import Number\n\
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
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \nclass mutvec(list, VecOpMixin):\n    def __init__(self, *args):\n        if\
    \ len(args) == 1 and isinstance(args[0], typing.Iterable):\n            super().__init__(args[0])\n\
    \        else:\n            super().__init__(args)\n\n    def ielm_wise(self,\
    \ other, op):\n        if isinstance(other, numbers.Real):\n            for i\
    \ in range(len(self)):\n                self[i] = op(self[i], other)\n       \
    \ elif isinstance(other, typing.Sequence) and len(self) == len(other):\n     \
    \       for i in range(len(self)):\n                self[i] = op(self[i], other[i])\n\
    \        else:\n            raise ValueError(\"Operand must be a number or a list\
    \ of the same length\")\n        return self\n    \n    def __iadd__(self, other):\
    \ return self.ielm_wise(other, operator.add)\n    def __isub__(self, other): return\
    \ self.ielm_wise(other, operator.sub)\n    def __imul__(self, other): return self.ielm_wise(other,\
    \ operator.mul)\n    def __itruediv__(self, other): return self.ielm_wise(other,\
    \ operator.truediv)\n    def __ifloordiv__(self, other): return self.ielm_wise(other,\
    \ operator.floordiv)\n"
  code: "import cp_library.ds.__header__\n\nimport operator\nimport typing\nimport\
    \ numbers\nfrom cp_library.ds.vec_op_mixin import VecOpMixin\n\nclass mutvec(list,\
    \ VecOpMixin):\n    def __init__(self, *args):\n        if len(args) == 1 and\
    \ isinstance(args[0], typing.Iterable):\n            super().__init__(args[0])\n\
    \        else:\n            super().__init__(args)\n\n    def ielm_wise(self,\
    \ other, op):\n        if isinstance(other, numbers.Real):\n            for i\
    \ in range(len(self)):\n                self[i] = op(self[i], other)\n       \
    \ elif isinstance(other, typing.Sequence) and len(self) == len(other):\n     \
    \       for i in range(len(self)):\n                self[i] = op(self[i], other[i])\n\
    \        else:\n            raise ValueError(\"Operand must be a number or a list\
    \ of the same length\")\n        return self\n    \n    def __iadd__(self, other):\
    \ return self.ielm_wise(other, operator.add)\n    def __isub__(self, other): return\
    \ self.ielm_wise(other, operator.sub)\n    def __imul__(self, other): return self.ielm_wise(other,\
    \ operator.mul)\n    def __itruediv__(self, other): return self.ielm_wise(other,\
    \ operator.truediv)\n    def __ifloordiv__(self, other): return self.ielm_wise(other,\
    \ operator.floordiv)"
  dependsOn:
  - cp_library/ds/vec_op_mixin.py
  isVerificationFile: false
  path: cp_library/ds/mutvec_cls.py
  requiredBy: []
  timestamp: '2024-09-28 04:04:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/mutvec_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/mutvec_cls.py
- /library/cp_library/ds/mutvec_cls.py.html
title: cp_library/ds/mutvec_cls.py
---
