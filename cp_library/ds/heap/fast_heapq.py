import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

def heappush(heap: list, item):
    heap.append(item)
    heapsiftdown(heap, 0, len(heap)-1)

def heappop(heap: list):
    item = heap.pop()
    if heap: item, heap[0] = heap[0], item; heapsiftup(heap, 0)
    return item

def heapreplace(heap: list, item):
    item, heap[0] = heap[0], item; heapsiftup(heap, 0)
    return item

def heappushpop(heap: list, item):
    if heap and heap[0] < item: item, heap[0] = heap[0], item; heapsiftup(heap, 0)
    return item

def heapify(x: list):
    for i in reversed(range(len(x)//2)): heapsiftup(x, i)

def heapsiftdown(heap: list, root: int, pos: int):
    item = heap[pos]
    while root < pos and item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p
    heap[pos] = item

def heapsiftup(heap: list, pos: int):
    n, item, c = len(heap)-1, heap[pos], pos<<1|1
    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos], pos, c = heap[c], c, c<<1|1
    if c == n and heap[c] < item: heap[pos], pos = heap[c], c
    heap[pos] = item

def heappop_max(heap: list):
    item = heap.pop()
    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item

def heapreplace_max(heap: list, item):
    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item

def heapify_max(x: list):
    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)

def heappush_max(heap: list, item):
    heap.append(item); heapsiftdown_max(heap, 0, len(heap)-1)

def heapreplace_max(heap: list, item):
    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item

def heappushpop_max(heap: list, item):
    if heap and heap[0] > item: item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)
    return item

def heapsiftdown_max(heap: list, root: int, pos: int):
    item = heap[pos]
    while root < pos and heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p], p
    heap[pos] = item

def heapsiftup_max(heap: list, pos: int):
    n, item, c = len(heap)-1, heap[pos], pos<<1|1
    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos], pos, c = heap[c], c, c<<1|1
    if c == n and item < heap[c]: heap[pos], pos = heap[c], c
    heap[pos] = item