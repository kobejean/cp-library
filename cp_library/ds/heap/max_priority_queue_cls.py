import cp_library.__header__
from cp_library.bit.pack_sm_fn import pack_sm
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.fast_heapq import heapify_max, heappop_max, heappush_max, heappushpop_max, heapreplace_max
from cp_library.ds.heap.heap_proto import HeapProtocol

class MaxPriorityQueue(HeapProtocol[int]):
    def __init__(que, N: int, ids: list[int] = None, priorities: list[int] = None, /):
        que.shift, que.mask = pack_sm(N)
        if ids is None: que.data = elist(N)
        elif priorities is None: heapify_max(ids); que.data = ids
        else:
            que.data = [0]*(M := len(ids))
            for i in range(M): que.data[i] = que.encode(ids[i], priorities[i]) 
            heapify_max(que.data)
    def encode(que, id, priority): return priority << que.shift | id
    def decode(que, encoded): return que.mask & encoded, encoded >> que.shift
    def pop(que): return que.decode(heappop_max(que.data))
    def push(que, id: int, priority: int): heappush_max(que.data, que.encode(id, priority))
    def pushpop(que, id: int, priority: int): return que.decode(heappushpop_max(que.data, que.encode(id, priority)))
    def replace(que, id: int, priority: int): return que.decode(heapreplace_max(que.data, que.encode(id, priority)))
    def peek(que): return que.decode(que.data[0])
from cp_library.ds.elist_fn import elist