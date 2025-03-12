from cp_library.bit.pack_sm_fn import pack_sm
import cp_library.__header__
from typing import Union
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__
from cp_library.ds.tree.bit import BIT

class SumCountBIT(BIT):
    def __init__(bit, v: Union[int, list[int]]):
        if not isinstance(v, int):
            s, m = pack_sm(len(v))
            for i,d in enumerate(v):
                v[i] = d << s | 1
        else:
            s, m = pack_sm(v)
        super().__init__(v)
        bit.s, bit.m = s, m

    def add(bit, i, x):
        
        while i < bit.n:
            bit.d[i] += x
            i |= i+1

    def sum(bit, n: int) -> int:
        s = 0
        while n: s, n = s+bit.d[n-1], n&n-1
        return s

    def range_sum(bit, l, r):
        s = 0
        while r: s, r = s+bit.d[r-1], r&r-1
        while l: s, l = s-bit.d[l-1], l&l-1
        return s

    def __len__(bit) -> int:
        return bit.n
    
    def __getitem__(bit, i: int) -> int:
        s, l = bit.d[i], i&(i+1)
        while l != i: s, i = s-bit.d[i-1], i-(i&-i)
        return s
    get = __getitem__
    
    def __setitem__(bit, i: int, x: int) -> None:
        bit.add(i, x-bit[i])
    set = __setitem__

    def prelist(bit) -> list[int]:
        pre = [0]+bit.d
        for i in range(bit.n+1): pre[i] += pre[i&i-1]
        return pre

    def bisect_left(bit, v) -> int:
        return bit.bisect_right(v-1) if v>0 else 0
    
    def bisect_right(bit, v) -> int:
        i = s = 0; ni = m = bit.lb
        while m:
            if ni <= bit.n and (ns:=s+bit.d[ni-1]) <= v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i