import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argsort_multi(*A: list[int], reverse=False):
    s, m = pack_sm((N:=len(A[0]))-1)
    I, J = [0]*N, [*range(N)]
    if reverse:
        V = [a<<s|m^i for i,a in enumerate(A[-1])]; V.sort(reverse=True)
        for k in range(len(A)-2,-1,-1):
            B = A[k]
            for i,v in enumerate(V):V[i],I[i]=B[j:=J[m^v&m]]<<s|m^i,j
            I,J=J,I;V.sort(reverse=True)
        for i,v in enumerate(V):I[i]=J[m^v&m]
    else:
        V = [a<<s|i for i,a in enumerate(A[-1])]; V.sort()
        for k in range(len(A)-2,-1,-1):
            B = A[k]
            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j
            I,J=J,I;V.sort()
        for i,v in enumerate(V):I[i]=J[v&m]
    return I
from cp_library.bit.pack.pack_sm_fn import pack_sm