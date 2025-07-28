import cp_library.__header__
from cp_library.bit.pack.packer_cls import Packer
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapify_fn import heapify
from cp_library.ds.heap.heappop_fn import heappop
from cp_library.ds.heap.heappush_fn import heappush
from cp_library.ds.heap.heappushpop_fn import heappushpop
from cp_library.ds.heap.heapreplace_fn import heapreplace
from cp_library.ds.heap.heap_base_cls import HeapBase

class PriorityQueue(HeapBase[int]):
    def __init__(que, N: int, ids: list[int] = None, priorities: list[int] = None, /):
        que.pkr = Packer(N)
        if ids is None: que.data = elist(N)
        elif priorities is None: heapify(ids); que.data = ids
        else:
            que.data = [0]*(M := len(ids))
            for i in range(M): que.data[i] = que.pkr.enc(priorities[i], ids[i]) 
            heapify(que.data)
    def pop(que): return que.pkr.dec(heappop(que.data))
    def push(que, priority: int, id: int): heappush(que.data, que.pkr.enc(priority, id))
    def pushpop(que, priority: int, id: int): return que.pkr.dec(heappushpop(que.data, que.pkr.enc(priority, id)))
    def replace(que, priority: int, id: int): return que.pkr.dec(heapreplace(que.data, que.pkr.enc(priority, id)))
    def peek(que): return que.pkr.dec(que.data[0])
from cp_library.ds.list.elist_fn import elist