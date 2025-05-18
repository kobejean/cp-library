import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u16a(init = None): return array('H') if init is None else array('H', init)  # unsigned short