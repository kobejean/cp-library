import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapsiftup_max_fn import heapsiftup_max

def heappushpop_max(heap: list, item):
    if heap and heap[0] > item: item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item