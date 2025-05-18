import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u64a(init = None): return array('Q') if init is None else array('Q', init)  # unsigned long long