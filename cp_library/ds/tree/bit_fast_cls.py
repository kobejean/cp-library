
import cp_library.ds.__header__

class BIT:
    def __init__(bit, d):
        bit.d, bit.n = d, len(d)
        for i in range(bit.n):
            if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]

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
        i, ni = s, m = 0, bit.lb
        while m:
            if ni <= bit.n and (ns:=s+bit.d[ni-1]) <= v: s, i = ns, ni
            ni = (m:=m>>1)|i
        return i