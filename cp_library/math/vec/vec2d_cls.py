import cp_library.math.__header__
from cp_library.io.parser_cls import Parser, TokenStream
from cp_library.math.vec.vec_cls import Vec
from numbers import Number
from typing import Sequence
from math import gcd, sqrt

class Vec2D(Vec):
    def __new__(cls, *args):
        if len(args) == 0:
            return super().__new__(cls, (0,0))
        return super().__new__(cls, *args)

    def elm_wise(self, other, op):
        if isinstance(other, Number):
            return Vec2D(op(self[0], other), op(self[1], other))
        if isinstance(other, Sequence):
            return Vec2D(op(self[0], other[0]), op(self[1], other[1]))
        raise ValueError("Operand must be a number or a tuple of the same length")

    def distance(v1: 'Vec', v2: 'Vec'):
        dx, dy = v2[0]-v1[0], v2[1]-v1[1]
        return sqrt(dx*dx+dy*dy)
    
    def distance2(v1: 'Vec', v2: 'Vec'):
        dx, dy = v2[0]-v1[0], v2[1]-v1[1]
        return dx*dx+dy*dy
    
    def magnitude(vec: 'Vec'):
        x, y = vec
        return sqrt(x*x+y*y)
    
    def magnitude2(vec: 'Vec'):
        x, y = vec
        return x*x+y*y
    
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
    
    def cross(vec, other):
        return vec[0]*other[1] - vec[1]*other[0]
    
    def slope_norm(vec):
        x,y = vec
        if x == 0 and y == 0: return vec
        if x == 0: return Vec2D((0,1)) if y > 0 else Vec2D((0,-1))
        if y == 0: return Vec2D((1,0)) if x > 0 else Vec2D((-1,0))
        g = gcd(x,y)
        return Vec2D((x//g,y//g))
    
    @classmethod
    def compile(cls, T: type = int):
        elm = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls(elm(ts), elm(ts))
        return parse

