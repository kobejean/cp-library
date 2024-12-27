import cp_library.ds.__header__
from array import array

def i8a(N: int, elm: int = 0): return array('b', (elm,))*N       # signed char
def u8a(N: int, elm: int = 0): return array('B', (elm,))*N       # unsigned char
def i16a(N: int, elm: int = 0): return array('h', (elm,))*N      # signed short
def u16a(N: int, elm: int = 0): return array('H', (elm,))*N      # unsigned short
def i32a(N: int, elm: int = 0): return array('i', (elm,))*N      # signed int
def u32a(N: int, elm: int = 0): return array('I', (elm,))*N      # unsigned int
def i64a(N: int, elm: int = 0): return array('q', (elm,))*N      # signed long long
def u64a(N: int, elm: int = 0): return array('Q', (elm,))*N      # unsigned long long
def f32a(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float
def f64a(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double