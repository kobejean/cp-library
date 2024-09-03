from itertools import accumulate

class mint(int):
    mod = None
    def __new__(cls, x=0): return super().__new__(cls, x % cls.mod)
    def __add__(self, other): return mint(super().__add__(other))
    def __radd__(self, other): return mint(super().__radd__(other))
    def __sub__(self, other): return mint(super().__sub__(other))
    def __rsub__(self, other): return mint(super().__rsub__(other))
    def __mul__(self, other): return mint(super().__mul__(other))
    def __rmul__(self, other): return mint(super().__rmul__(other))
    def __truediv__(self, other): return mint(super().__mul__(pow(int(other),-1,self.mod)))
    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(int(self),-1,self.mod)))
    def __mod__(self, other): return mint(super().__mod__(other))
    def __rmod__(self, other): return mint(super().__rmod__(other))
    def __pow__(self, other): return mint(pow(int(self),int(other),self.mod))
    def __rpow__(self, other): return mint(pow(int(other),int(other),self.mod))
    def __eq__(self, other): return super().__eq__(mint(other))
    def __req__(self, other): return super().__eq__(mint(other))
    @classmethod
    def precomp(cls,N):
        cls._fact = list(accumulate(range(1,N+1), cls.__mul__, initial=cls(1)))
        cls._fact_inv = list(accumulate(range(N,0,-1), cls.__mul__, initial=1/cls._fact[N]))[::-1]
    @classmethod
    def comb(cls, N, K):
        if N < K: return 0
        return cls._fact[N]*cls._fact_inv[K]*cls._fact_inv[N - K]
    @classmethod
    def multinom(cls, N, *args):
        res = cls(1)
        for arg in args:
            res *= cls.comb(N, arg)
            N -= arg
        return res