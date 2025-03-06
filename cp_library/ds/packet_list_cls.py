import cp_library.ds.__header__
from typing import Sequence

class PacketList(Sequence[tuple[int,int]]):
    def __init__(lst, A: list[int], max1: int):
        lst.A = A
        lst.mask = (1 << (shift := (max1).bit_length())) - 1
        lst.shift = shift
    def __len__(lst): return lst.A.__len__()
    def __contains__(lst, x: tuple[int,int]): return lst.A.__contains__(x[0] << lst.shift | x[1])
    def __getitem__(lst, key) -> tuple[int,int]:
        x = lst.A[key]
        return x >> lst.shift, x & lst.mask