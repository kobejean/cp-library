import cp_library.math.__header__

from cp_library.io.parser_cls import Parser, TokenStream
from cp_library.math.vec_cls import Vec
from numbers import Number
from typing import Sequence
from math import sqrt

class Vec3(Vec):
    
    def elm_wise(self, other, op):
        if isinstance(other, Number):
            return Vec3(op(self[0], other), op(self[1], other), op(self[2], other))
        if isinstance(other, Sequence):
            return Vec3(op(self[0], other[0]), op(self[1], other[1]), op(self[2], other[2]))
        raise ValueError("Operand must be a number or a tuple of the same length")

    def dist(v1: 'Vec', v2: 'Vec'):
        dx, dy, dz = v2[0]-v1[0], v2[1]-v1[1], v2[2]-v1[2]
        return sqrt(dx*dx+dy*dy+dz*dz)
    
    @classmethod
    def compile(cls, T: type = int):
        elm = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls(elm(ts), elm(ts), elm(ts))
        return parse