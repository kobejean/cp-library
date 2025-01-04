import cp_library.ds.__header__

class BinaryIndexRange:
    def __init__(self, size: int):
        self.size = size
        self.bit1 = BinaryIndexTree(size)
        self.bit2 = BinaryIndexTree(size)

    def add(self, l, r, x) -> None:
        """Add x to all elements in range [l, r)"""
        self.bit1.add(l, x * l)
        self.bit1.add(r, -x * r)
        self.bit2.add(l, x)
        self.bit2.add(r, -x)

    def presum(self, i):
        """Get sum of elements in range [0, i)"""
        return self.bit1.presum(i) - i * self.bit2.presum(i)

    def range_sum(self, l, r):
        """Get sum of elements in range [l, r)"""
        return self.presum(r) - self.presum(l)

    def get(self, i):
        """Get the value at index i"""
        return self.range_sum(i, i+1)

    def set(self, i, x):
        """Set the value at index i to x"""
        self.add(i, i+1, x - self.get(i))
        
from cp_library.ds.bit_cls import BinaryIndexTree