import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def f32a(init = None): return array('f') if init is None else array('f', init)  # float