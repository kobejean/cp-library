import cp_library.math.__header__
from typing import Union
from cp_library.ds.tree.bit_cls import BIT

def invcnt(Z, N: Union[int,None] = None):
    if N is None:
        Zi = { z: i for i, z in enumerate(sorted(set(Z))) }
        Z, N = [Zi[z] for z in Z], len(Z)
    bit, cnt = BIT(N), 0
    for z in reversed(Z):
        cnt += bit.sum(z)
        bit.add(z, 1)
    return cnt