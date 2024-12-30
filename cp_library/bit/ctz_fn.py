import cp_library.bit.__header__

def ctz(x): return (~x & (x - 1)).bit_count()
