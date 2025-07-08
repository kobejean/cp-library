import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.rank.__header__

def irank(A: list[int], distinct = False):
    P = Packer(len(A)-1); V = P.enumerate(A); V.sort()
    if distinct:
        for r, ai in enumerate(V): a, i = P.dec(ai); A[i], V[r] = r, a
    elif V:
        r, p = -1, V[-1]+1 # set p to unique value to trigger `if a != p` on first elm
        for ai in V:
            a, i = P.dec(ai)
            if a!=p: V[r:=r+1] = p = a
            A[i] = r
        del V[r+1:]
    return V
from cp_library.bit.pack.packer_cls import Packer