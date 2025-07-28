import cp_library.__header__
from cp_library.bit.pack.packer_cls import Packer
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapify_max_fn import heapify_max
from cp_library.ds.heap.heappop_max_fn import heappop_max
from cp_library.ds.heap.heappush_max_fn import heappush_max
from cp_library.ds.heap.heappushpop_max_fn import heappushpop_max
from cp_library.ds.heap.heapreplace_max_fn import heapreplace_max
from cp_library.ds.heap.heap_base_cls import HeapBase

class MaxPriorityQueue(HeapBase[int]):
    def __init__(que, N: int, ids: list[int] = None, priorities: list[int] = None, /):
        que.pkr = Packer(N)
        if ids is None: que.data = elist(N)
        elif priorities is None: heapify_max(ids); que.data = ids
        else:
            que.data = [0]*(M := len(ids))
            for i in range(M): que.data[i] = que.pkr.enc(priorities[i], ids[i])
            heapify_max(que.data)
    def pop(que): return que.pkr.dec(heappop_max(que.data))
    def push(que, priority: int, id: int): heappush_max(que.data, que.pkr.enc(priority, id))
    def pushpop(que, priority: int, id: int): return que.pkr.dec(heappushpop_max(que.data, que.pkr.enc(priority, id)))
    def replace(que, priority: int, id: int): return que.pkr.dec(heapreplace_max(que.data, que.pkr.enc(priority, id)))
    def peek(que): return que.pkr.dec(que.data[0])
from cp_library.ds.list.elist_fn import elist