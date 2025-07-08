import cp_library.__header__
import operator
import cp_library.ds.__header__
import cp_library.ds.list.__header__
class Presum:
    def __init__(P, A: list, op=operator.add, e = 0, diff=operator.sub):
        P.N = len(A); P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)
        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)
    def __getitem__(srs, key): return srs.range_sum(key.start, key.stop) if isinstance(key, slice) else srs.sum(key)
    def sum(srs, r: int): return srs.pre[r]
    def range_sum(srs, l: int, r: int): return srs.diff(srs.pre[r], srs.pre[l])