import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.cmpr.__header__

def icoord_compress_multi(*A: list[int], distinct = False):
    N=sum(len(Ai)for Ai in A);sj,mj=pack_sm(N-1);si,mi=pack_sm((len(A)-1)<<sj);V,k=[0]*N,0
    for i,Ai in enumerate(A):
        for j, a in enumerate(Ai):V[k]=a<<si|i<<sj|j;k+=1
    V.sort();r=p=-1
    if distinct:
        for r,aij in enumerate(V):a,i,j=aij>>si,(aij&mi)>>sj,aij&mj;A[i][j],V[r]=r,a
    else:
        for aij in V:
            a,i,j=aij>>si,(aij&mi)>>sj,aij&mj
            if a!=p:r+=1;V[r]=p=a
            A[i][j]=r
    return*A,V
from cp_library.bit.pack.pack_sm_fn import pack_sm