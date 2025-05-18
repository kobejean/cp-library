import cp_library.__header__
import cp_library.bit.__header__
import cp_library.bit.pack.__header__
def pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1