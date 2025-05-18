import cp_library.__header__
import cp_library.bit.__header__
import cp_library.bit.pack.__header__
def pack_indices(A, s): return [a<<s|i for i,a in enumerate(A)]