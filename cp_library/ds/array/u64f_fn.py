import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def u64f(N: int, elm: int = 0):     return array('Q', (elm,))*N  # unsigned long long