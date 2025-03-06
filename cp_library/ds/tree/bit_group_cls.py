import cp_library.ds.__header__
from typing import Callable, Sequence, Union
from cp_library.misc.typing import _T

class BITGroup(Sequence[_T]):
    def __init__(bit, op: Callable[[_T,_T],_T], diff: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):
        if isinstance(v, int): bit.d, bit.n = [e]*v, v
        else: bit.build(v)
        bit.lb = 1<<(bit.n.bit_length()-1)
        bit.op, bit.e, bit.diff = op, e, diff

    def __len__(bit) -> int:
        return bit.n

    def build(bit, d: list[_T]) -> None:
        bit.d, bit.n = d, len(d)
        for i in range(bit.n):
            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[r], d[i])

    def get(bit, i: int) -> _T:
        assert 0 <= i < bit.n
        s, z = (d := bit.d)[i], i&(i+1)
        for _ in range((i^z).bit_count()):
            s, i = bit.diff(s, d[i-1]), i-(i&-i)
        return s
    __getitem__ = get
    
    def set(bit, i: int, x: _T) -> None:
        bit.add(i, bit.diff(x, bit.get(i)))
    __setitem__ = set
        
    def add(bit, i: int, x: _T) -> None:
        assert 0 <= i < bit.n
        d, n = bit.d, bit.n
        while i < n:
            d[i], i = bit.op(d[i],x), i|(i+1)

    def sum(bit, n: int) -> _T:
        assert 0 <= n <= bit.n
        s, z, i, d = 0, n.bit_count(), n-1, bit.d
        for _ in range(z): s, i = bit.op(s,d[i]), (i&(i+1))-1
        return s
    
    def range_sum(bit, l: int, r: int) -> _T:
        return bit.diff(bit.sum(r),bit.sum(l))

    def prelist(bit) -> list[_T]:
        pre = [bit.e]+bit.d
        for i in range(bit.n+1): pre[i] = bit.op(pre[i], pre[i&(i-1)])
        return pre
    
    def bisect_left(bit, v) -> int:
        if v <= bit.e: return 0
        i, s = 0, bit.e
        ni = m = bit.lb
        while m:
            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1])) < v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i
    
    def bisect_right(bit, v) -> int:
        i, s = 0, bit.e
        ni = m = bit.lb
        while m:
            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1])) <= v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i