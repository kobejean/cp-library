import cp_library.__header__
from cp_library.misc.typing import _T
from typing import Callable, Generic, Union
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.seg.__header__

class SegTree(Generic[_T]):
    _lst = list
    
    def __init__(seg, op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:
        if isinstance(v, int): n = v; v = None
        else: n = len(v)
        seg.op, seg.e, seg.n = op, e, n
        seg.log, seg.sz = (log := (n-1).bit_length()+1), (sz := 1 << log)
        if seg._lst is list: seg.d = [e]*(sz<<1)
        else: seg.d = seg._lst(*([e_]*(sz<<1) for e_ in e))
        if v: seg._build(v)

    def _build(seg, v):
        for i in range(seg.n): seg.d[seg.sz + i] = v[i]
        for i in range(seg.sz-1,0,-1): seg._merge(i, i<<1, i<<1|1)
    
    def _merge(seg, i, j, k): seg.d[i] = seg.op(seg.d[j], seg.d[k])

    def set(seg, p: int, x: _T) -> None:
        p += seg.sz
        seg.d[p] = x
        for _ in range(seg.log):
            p = p^(p&1)
            seg._merge(p>>1, p, p|1)
            p >>= 1
    __setitem__ = set

    def get(seg, p: int) -> _T: return seg.d[p+seg.sz]
    __getitem__ = get

    def prod(seg, l: int, r: int) -> _T:
        sml = smr = seg.e
        l, r = l+seg.sz, r+seg.sz
        while l < r:
            if l&1: sml, l = seg.op(sml, seg.d[l]), l+1
            if r&1: smr = seg.op(seg.d[r:=r-1], smr)
            l, r = l >> 1, r >> 1
        return seg.op(sml, smr)

    def all_prod(seg) -> _T: return seg.d[1]

    def max_right(seg, l: int, f: Callable[[_T], bool]) -> int:
        assert 0 <= l <= seg.n
        assert f(seg.e)
        if l == seg.n: return seg.n
        l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d, seg.e
        while True:
            while l&1 == 0: l >>= 1
            if not f(op(sm, d[l])):
                while l < sz:
                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1
                return l - sz
            sm, l = op(sm, d[l]), l+1
            if l&-l == l: return seg.n

    def min_left(seg, r: int, f: Callable[[_T], bool]) -> int:
        assert 0 <= r <= seg.n
        assert f(seg.e)
        if r == 0: return 0
        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d, seg.e
        while True:
            r -= 1
            while r > 1 and r & 1: r >>= 1
            if not f(op(d[r], sm)):
                while r < sz:
                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm), r-1
                return r + 1 - sz
            sm = op(d[r], sm)
            if (r & -r) == r: return 0