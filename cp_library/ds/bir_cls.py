import cp_library.ds.__header__

class BinaryIndexRange:
    def __init__(self, size: int):
        self.size = size
        self.bit1 = BinaryIndexTree(size)  # For storing a[i] * i
        self.bit2 = BinaryIndexTree(size)  # For storing a[i]

    def add(self, l, r, x) -> None:
        """Add x to all elements in range [l, r)"""
        self.bit1.add(l, x * l)
        self.bit1.add(r, -x * r)
        self.bit2.add(l, x)
        self.bit2.add(r, -x)

    def pref_sum(self, i):
        """Get sum of elements in range [0, i)"""
        return self.bit1.pref_sum(i) - i * self.bit2.pref_sum(i)

    def range_sum(self, l, r):
        """Get sum of elements in range [l, r)"""
        return self.pref_sum(r) - self.pref_sum(l)

    def get(self, i):
        """Get the value at index i"""
        return self.range_sum(i, i+1)

    def set(self, i, x):
        """Set the value at index i to x"""
        current_value = self.get(i)
        self.add(i, i+1, x - current_value)
        
from cp_library.ds.bit_cls import BinaryIndexTree