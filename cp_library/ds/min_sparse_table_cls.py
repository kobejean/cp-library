import cp_library.__header__
# from typing import Generic
# from cp_library.misc.typing import _T
from cp_library.alg.dp.min2_fn import min2

import cp_library.ds.__header__

class MinSparseTable:
    def __init__(st, arr: list):
        st.N = N = len(arr)
        st.log = N.bit_length()
        st.data = data = [0] * (st.log*N)
        data[:N] = arr 
        for i in range(1,st.log):
            a, b, c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))
            for j in range(N - (1 << i) + 1):
                data[a+j] = min2(data[b+j], data[c+j])

    def query(st, l: int, r: int):
        k = (r-l).bit_length() - 1
        return min2(st.data[k*st.N + l], st.data[k*st.N + r - (1<<k)])
    