import cp_library.__header__
from typing import Callable, Generic, Union
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__

class BITMonoid(Generic[_T]):
    def __init__(bit, op: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):
        if isinstance(v, int): bit.d, bit.n = [e]*v, v
        else: bit.build(v)
        bit.op, bit.e = op, e

    def __len__(bit) -> int:
        return bit.n

    def build(bit, d: list[_T]) -> None:
        bit.d, bit.n = d, len(d)
        for i in range(bit.n):
            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[i], d[r])

    def add(bit, i: int, x: _T) -> None:
        assert 0 <= i < bit.n
        while i < bit.n:
            bit.d[i] = bit.op(bit.d[i], x)
            i |= i+1

    def sum(bit, r: int) -> _T:
        assert 0 <= r <= bit.n
        s = bit.e
        while r: s, r = bit.op(s,bit.d[r-1]), r&r-1
        return s
       
    def prelist(bit) -> list[_T]:
        pre = [bit.e]+bit.d
        for i in range(bit.n+1): pre[i] = bit.op(pre[i&(i-1)], pre[i])
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