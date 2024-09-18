import operator
import typing
import numbers
from cp_library.ds.vec_op_mixin import VecOpMixin

class mutvec(list, VecOpMixin):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], typing.Iterable):
            super().__init__(args[0])
        else:
            super().__init__(args)

    def ielm_wise(self, other, op):
        if isinstance(other, numbers.Real):
            for i in range(len(self)):
                self[i] = op(self[i], other)
        elif isinstance(other, typing.Sequence) and len(self) == len(other):
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