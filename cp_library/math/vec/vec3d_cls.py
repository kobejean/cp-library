import cp_library.math.__header__
from numbers import Number
from typing import Sequence
from math import sqrt

from cp_library.io.parser_cls import Parser, TokenStream
from cp_library.math.vec.vec_cls import Vec

class Vec3D(Vec):
    def __new__(cls, *args):
        if len(args) == 0:
            return super().__new__(cls, (0,0))
        return super().__new__(cls, *args)
    
    def elm_wise(self, other, op):
        if isinstance(other, Number):
            return Vec3D(op(self[0], other), op(self[1], other), op(self[2], other))
        if isinstance(other, Sequence):
            return Vec3D(op(self[0], other[0]), op(self[1], other[1]), op(self[2], other[2]))
        raise ValueError("Operand must be a number or a tuple of the same length")

    def distance(v1: 'Vec', v2: 'Vec'):
        dx, dy, dz = v2[0]-v1[0], v2[1]-v1[1]
        return sqrt(dx*dx+dy*dy+dz*dz)
    
    def distance2(v1: 'Vec', v2: 'Vec'):
        dx, dy, dz = v2[0]-v1[0], v2[1]-v1[1]
        return dx*dx+dy*dy+dz*dz
    
    def magnitude(vec: 'Vec'):
        x, y, z = vec
        return sqrt(x*x+y*y+z*z)
    
    def magnitude2(vec: 'Vec'):
        x, y, z = vec
        return x*x+y*y+z*z
    
    @classmethod
    def compile(cls, T: type = int):
        elm = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls(elm(ts), elm(ts), elm(ts))
        return parse