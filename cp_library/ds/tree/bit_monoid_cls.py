import cp_library.ds.__header__
from typing import Callable, Sized, Union
from cp_library.misc.typing import _T

class BITMonoid(Sized[_T]):
    def __init__(bit, op: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):
        if isinstance(v, int): bit.data, bit.size = [e]*v, v
        else: bit.build(v)
        bit.op, bit.e = op, e

    def __len__(bit) -> int:
        return bit.size

    def build(bit, data: list[_T]) -> None:
        bit.data, bit.size = data, len(data)
        for i in range(bit.size):
            if (r := i|(i+1)) < bit.size: data[r] = bit.op(data[r], data[i])
        
    def add(bit, i: int, x: _T) -> None:
        assert 0 <= i < bit.size
        data, size = bit.data, bit.size
        while i < size:
            data[i], i = bit.op(data[i],x), i|(i+1)

    def sum(bit, n: int) -> _T:
        assert 0 <= n <= bit.size
        s, z, i, data = 0, n.bit_count(), n-1, bit.data
        for _ in range(z): s, i = bit.op(s,data[i]), (i&(i+1))-1
        return s
    
    def presum(bit) -> list[_T]:
        pre = [bit.e]+bit.data
        for i in range(bit.size+1): pre[i] = bit.op(pre[i], pre[i&(i-1)])
        return pre
    
    def bisect_left(bit, v) -> int:
        return bit.bisect_right(v-1)+1
    
    def bisect_right(bit, v: _T) -> int:
        d, i, s, m, n = bit.data, 0, bit.e, bit.lead, bit.size
        while m:
            if (ni:=i|m) <= n and (ns:=bit.op(s,d[ni-1])) <= v: s, i = ns, ni
            m >>= 1
        return i
