import cp_library.math.mod.__init__
from itertools import accumulate

class mint(int):
    mod = zero = one = None

    def __new__(cls, *args, **kwargs):
        match int(*args, **kwargs):
            case 0: return cls.zero
            case 1: return cls.one
            case x: return cls.fix(x)

    @classmethod
    def set_mod(cls, mod):
        cls.mod = mod
        cls.zero, cls.one = cls.cast(0), cls.fix(1)

    @classmethod
    def fix(cls, x): return cls.cast(x%cls.mod)

    @classmethod
    def cast(cls, x): return super().__new__(cls,x)

    @classmethod
    def mod_inv(cls, x):
        a,b,s,t = int(x), cls.mod, 1, 0
        while b: a,b,s,t = b,a%b,t,s-a//b*t
        if a == 1: return cls.fix(s)
        raise ValueError(f"{x} is not invertible")
    
    @property
    def inv(self): return mint.mod_inv(self)

    def __add__(self, x): return mint.fix(super().__add__(x))
    def __radd__(self, x): return mint.fix(super().__radd__(x))
    def __sub__(self, x): return mint.fix(super().__sub__(x))
    def __rsub__(self, x): return mint.fix(super().__rsub__(x))
    def __mul__(self, x): return mint.fix(super().__mul__(x))
    def __rmul__(self, x): return mint.fix(super().__rmul__(x))
    def __floordiv__(self, x): return self * mint.mod_inv(x)
    def __rfloordiv__(self, x): return self.inv * x
    def __truediv__(self, x): return self * mint.mod_inv(x)
    def __rtruediv__(self, x): return self.inv * x
    def __pow__(self, x): 
        return self.cast(super().__pow__(x, self.mod))
    def __eq__(self, x): return super().__eq__(self-x, 0)
    def __neg__(self): return mint.mod-self
    def __pos__(self): return self
    def __abs__(self): return self

    @classmethod
    def precomp(cls,n):
        cls.fac = list(accumulate(
            range(1,n+1), cls.__mul__, initial=cls(1)))
        cls.finv = list(accumulate(
            range(n,0,-1), cls.__mul__, initial=cls.fac[n].inv))[::-1]
        
    @classmethod
    def comb(cls, n, k, /):
        if n < k: return 0
        return cls.fac[n]*cls.finv[k]*cls.finv[n - k]
    
    @classmethod
    def multinom(cls, n, *K):
        res = cls(1)
        for k in K:
            res *= cls.comb(n, k)
            n -= k
        return res
