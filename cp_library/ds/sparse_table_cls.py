import cp_library.__header__
from typing import Generic, Callable
from cp_library.misc.typing import _T
import cp_library.ds.__header__

class SparseTable(Generic[_T]):
    def __init__(st, op: Callable[[_T,_T],_T], arr: list[_T]):
        st.N = N = len(arr)
        st.log, st.op = N.bit_length(), op
        st.data = [0] * (st.log*N)
        st.data[:N] = arr
        for i in range(1,st.log):
            a,b,c=i*N,(i-1)*N,(i-1)*N+(1<<(i-1))
            for j in range(N-(1<<i)+1):
                st.data[a+j] = op(st.data[b+j], st.data[c+j])

    def query(st, l: int, r: int) -> _T:
        k = (r-l).bit_length()-1
        return st.op(st.data[k*st.N+l],st.data[k*st.N+r-(1<<k)])