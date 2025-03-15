import cp_library.__header__
from math import gcd
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.vec.__header__
from cp_library.math.linalg.vec.vec2d_cls import Vec2D

class Slope(Vec2D):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], tuple):
            x,y = args[0]
        else:
            x,y = args
        if x == 0 and y == 0: tup = 0, 0
        elif x == 0: tup = (0,1) if y > 0 else (0,-1)
        elif y == 0: tup = (1,0) if x > 0 else (-1,0)
        else:
            g = gcd(x,y)
            tup = (x//g,y//g)
        return super().__new__(cls, tup)
    
    def __lt__(slope, other):
        q1, q2 = slope.quadrant(), other.quadrant()
        return q1 < q2 or (q1 == q2 and slope.cross(other) > 0)
    
    def quadrant(vec):
        if vec[0] > 0 and vec[1] >= 0: return 1
        elif vec[1] > 0: return 2
        elif vec[0] < 0: return 3
        else: return 4

