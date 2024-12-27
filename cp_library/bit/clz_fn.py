import cp_library.bit.__header__
from cp_library.bit.bit_reverse_fn import bit_reverse
from cp_library.bit.ctz_fn import ctz

def clz(x): return ctz(bit_reverse(x))
