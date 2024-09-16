from itertools import accumulate

class mint(int):
    mod = None
    def __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)
    @classmethod
    def wrap(cls, x): return super().__new__(cls, x % cls.mod)
    @classmethod
    def cast(cls, x): return super().__new__(cls, x)
    def __add__(self, x): return mint.wrap(super().__add__(x))
    def __radd__(self, x): return mint.wrap(super().__radd__(x))
    def __sub__(self, x): return mint.wrap(super().__sub__(x))
    def __rsub__(self, x): return mint.wrap(super().__rsub__(x))
    def __mul__(self, x): return mint.wrap(super().__mul__(x))
    def __rmul__(self, x): return mint.wrap(super().__rmul__(x))
    def __floordiv__(self, x): return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))
    def __rfloordiv__(self, x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))
    def __pow__(self, x): return mint.cast(pow(int(self),x,self.mod))
    def __eq__(self, x): return super().__eq__(mint.wrap(x))
    def __req__(self, x): return super().__eq__(mint.wrap(x))
    @classmethod
    def precomp(cls,n):
        cls.F = list(accumulate(range(1,n+1), cls.__mul__, initial=cls(1)))
        cls.Finv = list(accumulate(range(n,0,-1), cls.__mul__, initial=1//cls.F[n]))[::-1]
    @classmethod
    def comb(cls, n, k, /):
        if n < k: return 0
        return cls.F[n]*cls.Finv[k]*cls.Finv[n - k]
    @classmethod
    def multinom(cls, n, *K):
        res = cls(1)
        for k in K:
            res *= cls.comb(n, k)
            n -= k
        return res
