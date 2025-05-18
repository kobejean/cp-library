import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def i16a(init = None): return array('h') if init is None else array('h', init)  # signed short