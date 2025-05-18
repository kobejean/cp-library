import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u32a(init = None): return array('I') if init is None else array('I', init)  # unsigned int