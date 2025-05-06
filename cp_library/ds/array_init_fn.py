import cp_library.ds.__header__
from array import array

def i8f(N: int, elm: int = 0):      return array('b', (elm,))*N  # signed char
def u8f(N: int, elm: int = 0):      return array('B', (elm,))*N  # unsigned char
def i16f(N: int, elm: int = 0):     return array('h', (elm,))*N  # signed short
def u16f(N: int, elm: int = 0):     return array('H', (elm,))*N  # unsigned short
def i32f(N: int, elm: int = 0):     return array('i', (elm,))*N  # signed int
def u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int
def i64f(N: int, elm: int = 0):     return array('q', (elm,))*N  # signed long long
def u64f(N: int, elm: int = 0):     return array('Q', (elm,))*N  # unsigned long long
def f32f(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float
def f64f(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double

def i8a(init = None):  return array('b') if init is None else array('b', init)  # signed char
def u8a(init = None):  return array('B') if init is None else array('B', init)  # unsigned char
def i16a(init = None): return array('h') if init is None else array('h', init)  # signed short
def u16a(init = None): return array('H') if init is None else array('H', init)  # unsigned short
def i32a(init = None): return array('i') if init is None else array('i', init)  # signed int
def u32a(init = None): return array('I') if init is None else array('I', init)  # unsigned int
def i64a(init = None): return array('q') if init is None else array('q', init)  # signed long long
def u64a(init = None): return array('Q') if init is None else array('Q', init)  # unsigned long long
def f32a(init = None): return array('f') if init is None else array('f', init)  # float
def f64a(init = None): return array('d') if init is None else array('d', init)  # double

i8_max = (1 << 7)-1
u8_max = (1 << 8)-1
i16_max = (1 << 15)-1
u16_max = (1 << 16)-1
i32_max = (1 << 31)-1
u32_max = (1 << 32)-1
i64_max = (1 << 63)-1
u64_max = (1 << 64)-1
