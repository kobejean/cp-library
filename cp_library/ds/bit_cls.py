import cp_library.ds.__header__
from typing import Union

class BinaryIndexTree:
    def __init__(bit, v: Union[int,list]):
        if isinstance(v, int):
            bit.data, bit.size = [0]*v, v
        else:
            bit.build(v)

    def build(bit, data):
        bit.data, bit.size = data, len(data)
        for i in range(bit.size):
            if (r := i|(i+1)) < bit.size: 
                data[r] += data[i]

    def get(bit, i: int):
        assert 0 <= i < bit.size
        s, z = (data := bit.data)[i], i&(i+1)
        for _ in range((i^z).bit_count()):
            s, i = s-data[i-1], i-(i&-i)
        return s
    __getitem__ = get
    
    def set(bit, i: int, x: int):
        bit.add(i, x-bit.get(i))
    __setitem__ = set
        
    def add(bit, i: int, x: int) -> None:
        assert 0 <= i <= bit.size
        data, size = bit.data, bit.size
        while i < size:
            data[i], i = data[i]+x, i|(i+1)

    def presum(bit, n: int):
        assert 0 <= n <= bit.size
        s, z, i, data = 0, n.bit_count(), n-1, bit.data
        for _ in range(z):
            s, i = s+data[i], (i&(i+1))-1
        return s
    
    def range_sum(bit, l: int, r: int):
        return bit.presum(r) - bit.presum(l)

    def prelist(bit):
        pre = [0]+bit.data
        for i in range(bit.size+1):
            pre[i] += pre[i&(i-1)]
        return pre
    
    def bisect_left(bit, v):
        data, i, s, m = bit.data, 0, 0, 1 << ((N := bit.size).bit_length()-1)
        while m:
            if (ni := i|m) <= N and (ns := s + data[ni-1]) < v:
                s, i = ns, ni
            m >>= 1
        return i
    
    def bisect_right(bit, v):
        data, i, s, m = bit.data, 0, 0, 1 << ((N := bit.size).bit_length()-1)
        while m:
            if (ni := i|m) <= N and (ns := s + data[ni-1]) <= v:
                s, i = ns, ni
            m >>= 1
        return i
