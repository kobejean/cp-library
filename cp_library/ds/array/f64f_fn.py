import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def f64f(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double