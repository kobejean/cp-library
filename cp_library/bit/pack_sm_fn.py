import cp_library.bit.__header__
def pack_sm(N: int): s=N.bit_length(); return s, (1<<s)-1
def pack_enc(a: int, b: int, s: int): return a<<s|b
def pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m
def pack_indices(A, s): return [a<<s|i for i,a in enumerate(A)]