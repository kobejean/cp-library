import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

def heapsiftdown_max(heap: list, root: int, pos: int):
    item = heap[pos]
    while root < pos and heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p], p
    heap[pos] = item