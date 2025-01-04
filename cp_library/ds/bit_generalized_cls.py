import cp_library.ds.__header__
from typing import Union
class BinaryIndexTree:
    def __init__(self, e, op, v: Union[int,list]):
        self.e, self.op = e, op
        if isinstance(v, int):
            self.data, self.size = [e]*v, v
        else:
            self.build(v)

    def build(self, data):
        self.data, self.size = data, len(data)
        for i in range(self.size):
            r = i|(i+1)
            if r < self.size: 
                self.data[r] = self.op(self.data[i], self.data[r])

    def add(self, i: int, x: object) -> None:
        assert 0 <= i <= self.size
        i += 1
        while i <= self.size:
            self.data[i-1], i = self.op(self.data[i-1], x), i+(i&-i)

    def presum(self, i: int):
        assert 0 <= i <= self.size
        s = self.e
        while i > 0:
            s, i = self.op(s, self.data[i-1]), i-(i&-i)
        return s
    

class BinaryIndexTreePURQ(BinaryIndexTree):
    def __init__(self, e, op, inv, v: Union[int,list]):
        self.inv = inv
        super().__init__(e, op, v)

    def range_sum(self, l: int, r: int) -> object:
        return self.op(self.presum(r), self.inv(self.presum(l)))
