
class mint(int):
    mod = None
    def __new__(cls, x): return super().__new__(cls, x % cls.mod)
    def __add__(self, other): return mint(super().__add__(other))
    def __radd__(self, other): return mint(super().__radd__(other))
    def __sub__(self, other): return mint(super().__sub__(other))
    def __rsub__(self, other): return mint(super().__rsub__(other))
    def __mul__(self, other): return mint(super().__mul__(other))
    def __rmul__(self, other): return mint(super().__rmul__(other))
    def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))
    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))
    def __mod__(self, other): return mint(super().__mod__(other))
    def __rmod__(self, other): return mint(super().__rmod__(other))
    def __pow__(self, other): return mint(pow(self,other,self.mod))
    def __rpow__(self, other): return mint(pow(other,other,self.mod))
    def __eq__(self, other): return super().__eq__(mint(other))
    def __req__(self, other): return super().__eq__(mint(other))

