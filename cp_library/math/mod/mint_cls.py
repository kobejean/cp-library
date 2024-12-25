import cp_library.math.mod.__header__
    
class mint(int):
    mod: int
    zero: 'mint'
    one: 'mint'
    two: 'mint'
    cache: list['mint']

    def __new__(cls, *args, **kwargs):
        if 0<= (x := int(*args, **kwargs)) <= 2:
            return cls.cache[x]
        else:
            return cls.fix(x)

    @classmethod
    def set_mod(cls, mod: int):
        mint.mod = cls.mod = mod
        mint.zero = cls.zero = cls.cast(0)
        mint.one = cls.one = cls.fix(1)
        mint.two = cls.two = cls.fix(2)
        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]

    @classmethod
    def fix(cls, x): return cls.cast(x%cls.mod)

    @classmethod
    def cast(cls, x): return super().__new__(cls,x)

    @classmethod
    def mod_inv(cls, x):
        a,b,s,t = int(x), cls.mod, 1, 0
        while b: a,b,s,t = b,a%b,t,s-a//b*t
        if a == 1: return cls.fix(s)
        raise ValueError(f"{x} is not invertible in mod {cls.mod}")
    
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
    def __neg__(self): return mint.mod-self
    def __pos__(self): return self
    def __abs__(self): return self
