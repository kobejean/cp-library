import cp_library.ds.__header__
from typing import Sequence

class BIT(Sequence[int]):
    def __init__(bit, v):
        if isinstance(v, int): bit.d, bit.n = [0]*v, v
        else: bit.build(v)
        bit.lb = 1<<(bit.n.bit_length()-1)

    def build(bit, data):
        bit.d, bit.n = data, len(data)
        for i in range(bit.n):
            if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]

    def add(bit, i, x):
        assert 0 <= i <= bit.n
        while i < bit.n:
            bit.d[i] += x
            i |= i+1

    def sum(bit, r: int) -> int:
        assert 0 <= r <= bit.n
        s = 0
        while r: s, r = s+bit.d[r-1], r&r-1
        return s

    def range_sum(bit, l, r):
        assert 0 <= l <= r <= bit.n
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
        i, ni = s, m = 0, bit.lb
        while m:
            if ni <= bit.n and (ns:=s+bit.d[ni-1]) <= v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i