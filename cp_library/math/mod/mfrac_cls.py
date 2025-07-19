import cp_library.__header__
from fractions import Fraction
import cp_library.math.__header__
import cp_library.math.mod.__header__

class mfrac(Fraction):
    @classmethod
    def set_mod(cls, mod): cls.mod, cls.zero, cls.one, cls.two = mod, mfrac(0), mfrac(1), mfrac(2)
    @classmethod
    def cast(cls, x): return mfrac(x)
    @classmethod
    def mod_inv(cls, x): return mfrac(1, x)
    def __add__(self, x): return self.cast(super().__add__(x))
    def __radd__(self, x): return self.cast(super().__radd__(x))
    def __sub__(self, x): return self.cast(super().__sub__(x))
    def __rsub__(self, x): return self.cast(super().__rsub__(x))
    def __mul__(self, x): return self.cast(super().__mul__(x))
    def __rmul__(self, x): return self.cast(super().__rmul__(x))
    def __floordiv__(self, x): return self.cast(super().__floordiv__(x))
    def __rfloordiv__(self, x): return self.cast(super().__rfloordiv__(x))
    def __truediv__(self, x): return self.cast(super().__truediv__(x))
    def __rtruediv__(self, x): return self.cast(super().__rtruediv__(x))
    def __pow__(self, x): return self.cast(super().__pow__(x))
    def __neg__(self, x): return self.cast(super().__neg__(x))
    def __pos__(self, x): return self.cast(super().__pos__(x))
    def __abs__(self, x): return self.cast(super().__abs__(x))
    def __repr__(self): return super().__str__()