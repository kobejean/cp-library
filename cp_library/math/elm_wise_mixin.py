import cp_library.math.__header__

import operator
from numbers import Number
from typing import Sequence

class ElmWiseMixin:
    def elm_wise(self, other, op):
        if isinstance(other, Number):
            return type(self)(op(x, other) for x in self)
        if isinstance(other, Sequence):
            return type(self)(op(x, y) for x, y in zip(self, other))
        raise ValueError("Operand must be a number or a tuple of the same length")

    def __add__(self, other): return self.elm_wise(other, operator.add)
    def __radd__(self, other): return self.elm_wise(other, operator.add)
    def __sub__(self, other): return self.elm_wise(other, operator.sub)
    def __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))
    def __mul__(self, other): return self.elm_wise(other, operator.mul)
    def __rmul__(self, other): return self.elm_wise(other, operator.mul)
    def __truediv__(self, other): return self.elm_wise(other, operator.truediv)
    def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))
    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)
    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))
    def __mod__(self, other): return self.elm_wise(other, operator.mod)
