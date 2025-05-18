from cp_library.bit.pack.pack_sm_fn import pack_sm
import cp_library.__header__
from typing import Union
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__
from cp_library.ds.tree.bit.bit_cls import BIT

class SumCountBIT(BIT):
    def __init__(bit, v: Union[int, list[int]]):
        if not isinstance(v, int):
            bit.s, bit.m = pack_sm(len(v))
            for i,d in enumerate(v): v[i] = d << bit.s | 1
        else:
            bit.s, bit.m = pack_sm(v)
        super().__init__(v)

    def add(bit, i, x):
        while i < bit._n: bit._d[i] += x; i |= i+1

    def sum(bit, n: int) -> int:
        s = 0
        while n: s, n = s+bit._d[n-1], n&n-1
        return s

    def sum_range(bit, l, r):
        s = 0
        while r: s, r = s+bit._d[r-1], r&r-1
        while l: s, l = s-bit._d[l-1], l&l-1
        return s

    def __len__(bit) -> int: return bit.n
    
    def __getitem__(bit, i: int) -> int:
        s, l = bit._d[i], i&(i+1)
        while l != i: s, i = s-bit._d[i-1], i-(i&-i)
        return s
    get = __getitem__
    
    def __setitem__(bit, i: int, x: int) -> None: bit.add(i, x-bit[i])
    set = __setitem__

    def prelist(bit) -> list[int]:
        pre = [0]+bit._d
        for i in range(bit._n+1): pre[i] += pre[i&i-1]
        return pre

    def bisect_left(bit, v) -> int: return bit.bisect_right(v-1) if v>0 else 0
    
    def bisect_right(bit, v) -> int:
        i = s = 0; ni = m = bit._lb
        while m:
            if ni <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i