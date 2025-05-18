import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def f64a(init = None): return array('d') if init is None else array('d', init)  # double