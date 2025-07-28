import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapsiftup_max_fn import heapsiftup_max

def heappop_max(heap: list):
    item = heap.pop()
    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item