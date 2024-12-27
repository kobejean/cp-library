import cp_library.bit.__header__
from cp_library.bit.popcnt_fn import popcnt

def ctz(x): return popcnt(~x & (x - 1))
