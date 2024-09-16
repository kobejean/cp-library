
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