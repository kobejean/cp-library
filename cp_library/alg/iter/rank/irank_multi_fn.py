import cp_library.__header__
import cp_library.alg.__header__
from cp_library.alg.dp.max2_fn import max2
import cp_library.alg.iter.__header__
import cp_library.alg.iter.rank.__header__

def irank(*A: list[int], distinct = False):
    N = mxj = 0
    for Ai in A: N += len(Ai); mxj = max2(mxj, len(Ai))
    P = Packer3(len(A)-1, mxj); V = P.enumerate(A, N); V.sort()
    if distinct:
        for r,aij in enumerate(V):a,i,j=P.dec(aij);A[i][j],V[r]=r,a
    elif V:
        r, p = -1, V[-1]+1 # set p to unique value to trigger `if a != p` on first elm
        for aij in V:
            a,i,j=P.dec(aij)
            if a!=p:V[r:=r+1]=p=a
            A[i][j]=r
        del V[r+1:]
    return V
from cp_library.bit.pack.packer3_cls import Packer3