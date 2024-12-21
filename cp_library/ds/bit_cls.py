import cp_library.ds.__header__
from typing import Union

class BinaryIndexTree:
    def __init__(self, v: Union[int,list]):
        if isinstance(v, int):
            self.data, self.size = [0]*v, v
        else:
            self.build(v)

    def build(self, data):
        self.data, self.size = data, len(data)
        for i in range(self.size):
            if (r := i|(i+1)) < self.size: 
                data[r] += data[i]

    def get(self, i: int):
        assert 0 <= i < self.size
        s, z = (data := self.data)[i], i&(i+1)
        for _ in range((i^z).bit_count()):
            s, i = s-data[i-1], i-(i&-i)
        return s
    
    def set(self, i: int, x: int):
        self.add(i, x-self.get(i))
        
    def add(self, i: int, x: int) -> None:
        assert 0 <= i <= self.size
        i += 1
        data, size = self.data, self.size
        while i <= size:
            data[i-1], i = data[i-1] + x, i+(i&-i)

    def pref_sum(self, i: int):
        assert 0 <= i <= self.size
        s = 0
        data = self.data
        for _ in range(i.bit_count()):
            s, i = s+data[i-1], i-(i&-i)
        return s
    
    def range_sum(self, l: int, r: int):
        return self.pref_sum(r) - self.pref_sum(l)
