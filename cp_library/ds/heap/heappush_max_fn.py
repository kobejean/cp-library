import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapsiftdown_max_fn import heapsiftdown_max

def heappush_max(heap: list, item):
    heap.append(item); heapsiftdown_max(heap, 0, len(heap)-1)
