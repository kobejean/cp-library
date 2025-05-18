import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def i64f(N: int, elm: int = 0):     return array('q', (elm,))*N  # signed long long