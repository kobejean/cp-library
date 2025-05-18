import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int