import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def i32a(init = None): return array('i') if init is None else array('i', init)  # signed int