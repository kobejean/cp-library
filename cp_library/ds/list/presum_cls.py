import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.list.__header__
class Presum:
    def __init__(P, op, e, diff, A: list):
        P.N = len(A); P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)
        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)
    def __getitem__(P,i):return P.pre[i]
    def prod(P,l:int,r:int):return P.diff(P.pre[r],P.pre[l])