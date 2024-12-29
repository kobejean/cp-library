import cp_library.ds.__header__
from typing import Sequence

class PacketList(Sequence[tuple[int,int]]):
    def __init__(self, A: list[int], max0: int):
        self.A = A
        self.mask = (1 << (shift := (max0).bit_length())) - 1
        self.shift = shift
    def __len__(self): return self.A.__len__()
    def __contains__(self, x): return self.A.__contains__(x)
    def __getitem__(self, key):
        x = self.A[key]
        return x >> self.shift, x & self.mask