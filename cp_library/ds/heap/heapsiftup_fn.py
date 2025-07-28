import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

def heapsiftup(heap: list, pos: int):
    n, item, c = len(heap)-1, heap[pos], pos<<1|1
    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos], pos, c = heap[c], c, c<<1|1
    if c == n and heap[c] < item: heap[pos], pos = heap[c], c
    heap[pos] = item