import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u8f(N: int, elm: int = 0):      return array('B', (elm,))*N  # unsigned char