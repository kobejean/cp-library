import cp_library.math.fps.__header__
from typing import MutableSequence, SupportsIndex
from cp_library.math.table.comb_table_cls import CombTable
from cp_library.math.mod.mint_ntt_cls import mint

class FPS(MutableSequence[int]):
    def __init__(fps, coef: list[int]):
        fps.coef = coef

    def __getitem__(fps, i: SupportsIndex, /):
        return fps.coef[i]
        # return list.__getitem__(fps.coef, i)
    
    def __setitem__(fps, i: SupportsIndex, a: int):
        fps.coef[i] = a
        # list.__setitem__(fps, i, a)
    
    def __len__(fps):
        return len(fps.coef)
    
    def __contains__(self, value):
        return super().__contains__(value)
    
    def tayler_shift(fps, c: int) -> list[int]:
        inv, N, coef = (fact := CombTable.table).inv, len(fps), fps.coef
        res = [int(coef[i]*fact[i]) for i in range(N-1,-1,-1)]
        B = [0]*N
        B[0] = 1
        for i in range(1, N):
            B[i] = int(B[i - 1] * inv[i] * c * fact[i-1])
        res = mint.ntt.conv(res, B, N)
        return FPS([int(x * inv[i]) for i, x in enumerate(reversed(res))])
    
    def conv(fps, other):
        return FPS(mint.ntt.conv(fps.coef[:], other.coef))
    def iconv(fps, other):
        fps.coef = mint.ntt.conv(fps.coef, other.coef)

    def scalar_mul(fps, other):
        return FPS([a*other for a in fps.coef])
    def iscalar_mul(fps, other):
        coef = fps.coef
        for i in range(len(coef)): coef[i] *= other
    
    def __mul__(lhs, rhs):
        if rhs.__class__ is FPS: return lhs.conv(rhs)
        elif rhs.__class__ is list: return lhs.conv(FPS(rhs))
        else: lhs.scalar_mul(rhs)

    __rmul__ = __mul__
    
    def __imul__(lhs, rhs):
        if rhs.__class__ is FPS: lhs.iconv(rhs)
        elif rhs.__class__ is list: lhs.iconv(FPS(rhs))
        else: lhs.iscalar_mul(rhs)
