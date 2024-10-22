import cp_library.math.__header__

import operator
from numbers import Number
from typing import Sequence
from cp_library.math.elm_wise_mixin import ElmWiseMixin

class ElmWiseInPlaceMixin(ElmWiseMixin):
    def ielm_wise(self, other, op):
        if isinstance(other, Number):
            for i in range(len(self)):
                self[i] = op(self[i], other)
        elif isinstance(other, Sequence) and len(self) == len(other):
            for i in range(len(self)):
                self[i] = op(self[i], other[i])
        else:
            raise ValueError("Operand must be a number or a list of the same length")
        return self
    
    def __iadd__(self, other): return self.ielm_wise(other, operator.add)
    def __isub__(self, other): return self.ielm_wise(other, operator.sub)
    def __imul__(self, other): return self.ielm_wise(other, operator.mul)
    def __itruediv__(self, other): return self.ielm_wise(other, operator.truediv)
    def __ifloordiv__(self, other): return self.ielm_wise(other, operator.floordiv)
    def __imod__(self, other): return self.ielm_wise(other, operator.mod)
