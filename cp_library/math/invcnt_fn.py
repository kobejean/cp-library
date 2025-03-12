import cp_library.math.__header__
from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.bit.pack_sm_fn import pack_sm, pack_indices

def invcnt(A: list[int]):
    s, m = pack_sm(N := len(A))
    bit, cnt, I = BIT(N), 0, pack_indices(A, s)
    I.sort(reverse=True)
    for i in I:
        cnt += bit.sum(i&m)
        bit.add(i&m, 1)
    return cnt