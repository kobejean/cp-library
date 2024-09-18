import operator
import numbers
import typing

class VecOpMixin:
    def elm_wise(self, other, op):
        if isinstance(other, numbers.Real):
            return type(self)(op(x, other) for x in self)
        if isinstance(other, typing.Sequence):
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
