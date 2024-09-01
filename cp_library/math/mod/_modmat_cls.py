from typing import Union, List, Tuple
from cp_library.math.mod.mint_cls import mint

import array

class ModMat:
    def __init__(s, r, c, v=0):
        s.r, s.c = r, c
        s.d = array.array('q', [v] * (r * c) if isinstance(v, int) else [x for row in v for x in row])

    def __getitem__(s, k): return mint(s.d[k[0]*s.c + k[1]])
    def __setitem__(s, k, v): s.d[k[0]*s.c + k[1]] = v % mint.mod
    def __str__(s): return '\n'.join(' '.join(map(str, (mint(x) for x in s.d[i*s.c:(i+1)*s.c]))) for i in range(s.r))

    def __add__(s, o):
        d = (a+o for a in s.d) if isinstance(o,int) else (a+b for a,b in zip(s.d, o.d))
        return ModMat(s.r, s.c, d)

    def __matmul__(s, o):
        if s.c != o.r: raise ValueError("Dimension mismatch")
        r = ModMat(s.r, o.c)
        for i in range(s.r):
            i_sc = i * s.c
            for j in range(o.c):
                r[i,j] = sum(s.d[i_sc+k]*o.d[k*o.c+j]%mint.mod for k in range(s.c))
        return r

    @classmethod
    def I(cls, n):
        r = cls(n, n)
        for i in range(n): r[i,i] = 1
        return r

