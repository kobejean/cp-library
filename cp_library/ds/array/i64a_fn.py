import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.array.__header__
from array import array
def i64a(init = None): return array('q') if init is None else array('q', init)  # signed long long