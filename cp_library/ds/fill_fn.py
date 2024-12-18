import cp_library.ds.__header__
from array import array

def fill_i32(N: int, elm: int = 0):
    return array('i', (elm,)) * N

def fill_u32(N: int, elm: int = 0):
    return array('I', (elm,)) * N

def fill_i64(N: int, elm: int = 0):
    return array('q', (elm,)) * N

def fill_u64(N: int, elm: int = 0):
    return array('Q', (elm,)) * N