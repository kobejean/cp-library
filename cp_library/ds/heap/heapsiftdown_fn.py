import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

def heapsiftdown(heap: list, root: int, pos: int):
    item = heap[pos]
    while root < pos and item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p
    heap[pos] = item