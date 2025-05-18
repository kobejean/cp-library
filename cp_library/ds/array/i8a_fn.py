import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def i8a(init = None):  return array('b') if init is None else array('b', init)  # signed char