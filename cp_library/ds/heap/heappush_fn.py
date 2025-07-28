import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapsiftdown_fn import heapsiftdown

def heappush(heap: list, item):
    heap.append(item)
    heapsiftdown(heap, 0, len(heap)-1)