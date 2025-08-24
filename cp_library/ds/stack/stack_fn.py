import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.stack.__header__

class stack:
    __slots__ = 'd', 'n'
    def __init__(st, cap): st.d, st.n = [0]*cap, 0
    def push(st, x): st.d[st.n] = x; st.n += 1
    def pop(st): st.n -= 1; return st.d[st.n]
    def peek(st): return st.d[st.n-1]
    def __len__(st): return st.n