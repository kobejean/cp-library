import cp_library.__header__
from array import array
import cp_library.ds.__header__
import cp_library.ds.array.__header__
def f32f(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float