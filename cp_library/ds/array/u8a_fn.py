import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u8a(init = None):  return array('B') if init is None else array('B', init)  # unsigned char