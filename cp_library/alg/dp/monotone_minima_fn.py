import cp_library.alg.dp.__header__
from typing import Callable

def monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):
    """
    Finds row minima in a totally monotone N×M matrix using the SMAWK algorithm.
    The matrix is defined implicitly through the comparison function.
    
    A matrix is totally monotone if the minimum in row i occurs at column j,
    then the minimum in row i+1 must occur at column j' where j ≤ j'.
    
    Time: O(N log M), Space: O(N)
    
    Args:
        N: Number of rows
        M: Number of columns
        func(i,j,k): Returns True if element (i,j) < element (i,k)
    
    Returns:
        List of column indices containing the minimum value for each row
    
    Example:
        # Find minima where each element is (i-j)²
        min_indices = monotone_minima(5, 5, lambda i,j,k: (i-j)**2 < (i-k)**2)
    """
    min_j = [0] * N
    st = elist(N+1)
    st.append((0, N, 0, M))

    while st:
        li, ri, lj, rj = st.pop()
        if li == ri: continue
        mi, mj = li + ri >> 1, lj
        for j in range(lj + 1, rj):
            if func(mi, mj, j):
                mj = j
        min_j[mi] = mj
        st.append((li, mi, lj, mj+1))
        st.append((mi+1, ri, mj, rj))

    return min_j

from cp_library.ds.elist_fn import elist