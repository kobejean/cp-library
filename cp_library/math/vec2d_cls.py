import cp_library.math.__header__

from cp_library.io.parser_cls import Parser, TokenStream
from cp_library.math.vec_cls import Vec
from numbers import Number
from typing import Sequence
from math import sqrt

class Vec2D(Vec):

    def elm_wise(self, other, op):
        if isinstance(other, Number):
            return Vec2D(op(self[0], other), op(self[1], other))
        if isinstance(other, Sequence):
            return Vec2D(op(self[0], other[0]), op(self[1], other[1]))
        raise ValueError("Operand must be a number or a tuple of the same length")

    def dist(v1: 'Vec', v2: 'Vec'):
        dx, dy = v2[0]-v1[0], v2[1]-v1[1]
        return sqrt(dx*dx+dy*dy)
    
    def rot90(vec):
        x,y = vec
        return Vec2D(-y,x)
    
    def rot180(vec):
        x,y = vec
        return Vec2D(-x,-y)
    
    def rot270(vec):
        x,y = vec
        return Vec2D(y,-x)
    
    def flip_x(vec):
        x,y = vec
        return Vec2D(-x,y)
    
    def flip_y(vec):
        x,y = vec
        return Vec2D(x,-y)
    
    @classmethod
    def compile(cls, T: type = int):
        elm = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls(elm(ts), elm(ts))
        return parse

