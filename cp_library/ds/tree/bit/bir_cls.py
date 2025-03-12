import cp_library.__header__
from typing import Sequence
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__

class BIR(Sequence[int]):
    def __init__(bir, size: int):
        bir.size, bir.bit1, bir.bit2  = size, BIT(size), BIT(size)
    
    def __len__(bir):
        return bir.size

    def add(bir, l, r, x) -> None:
        """Add x to all elements in range [l, r)"""
        bir.bit1.add(l, x), bir.bit1.add(r, -x)
        bir.bit2.add(l, x * l), bir.bit2.add(r, -x * r)

    def sum(bir, i):
        """Get sum of elements in range [0, i)"""
        return i * bir.bit1.sum(i) - bir.bit2.sum(i)

    def range_sum(bir, l, r):
        """Get sum of elements in range [l, r)"""
        return bir.sum(r) - bir.sum(l)

    def get(bir, i):
        """Get the value at index i"""
        return (i+1) * bir.bit1.sum(i+1) - i*bir.bit1.sum(i) - bir.bit2.get(i)
    __getitem__ = get

    def set(bir, i, x):
        """Set the value at index i to x"""
        bir.add(i, i+1, x - bir.get(i))
    __setitem__ = set
        
from cp_library.ds.tree.bit.bit_cls import BIT
