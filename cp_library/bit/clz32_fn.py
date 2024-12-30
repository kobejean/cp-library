import cp_library.bit.__header__
from cp_library.bit.bit_reverse32_fn import bit_reverse32
from cp_library.bit.ctz32_fn import ctz32

def clz32(x): return ctz32(bit_reverse32(x))
