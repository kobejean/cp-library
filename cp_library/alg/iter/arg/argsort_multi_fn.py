import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argsort_multi(*A: list[int], reverse=False):
    P = Packer((N:=len(A[0]))-1); I, J, s, m = [0]*N, [*range(N)], P.s, P.m
    V = P.enumerate(A[-1], reverse); V.sort()
    if reverse:
        for B in A[-2::-1]:
            for i,v in enumerate(V):V[i],I[i]=-B[j:=J[v&m]]<<s|i,j
            I,J=J,I;V.sort()
    else:
        for B in A[-2::-1]:
            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j
            I,J=J,I;V.sort()
    for i,v in enumerate(V):I[i]=J[v&m]
    return I
from cp_library.bit.pack.packer_cls import Packer