import cp_library.bit.__header__
from cp_library.bit.popcnt64_fn import popcnt64

def ctz64(x): return popcnt64(~x&(x-1))
