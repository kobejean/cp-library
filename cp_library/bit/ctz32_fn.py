import cp_library.bit.__header__
from cp_library.bit.popcnt32_fn import popcnt32

def ctz32(x): return popcnt32(~x & (x - 1))
